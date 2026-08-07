"""Context builder module for WidgetWare SDR context package."""

import copy
from pathlib import Path
from typing import Any

import yaml

from widgetware_sdr.instructions import get_system_instructions


def _get_default_config_dir() -> Path:
    """Return the default config directory path."""
    # Assuming config/ is located at project root relative to src/
    return Path(__file__).resolve().parent.parent.parent / "config"


def load_yaml_config(file_path: Path) -> dict[str, Any]:
    """Load a YAML configuration file safely.

    Raises:
        FileNotFoundError: If the configuration file does not exist.
        ValueError: If the YAML content is invalid or empty.
    """
    if not file_path.is_file():
        raise FileNotFoundError(
            f"Required configuration file is missing: {file_path.name} at {file_path}"
        )

    with open(file_path, "r", encoding="utf-8") as f:
        data = yaml.safe_load(f)

    if data is None:
        raise ValueError(f"Configuration file is empty: {file_path.name}")

    if not isinstance(data, dict):
        raise ValueError(
            f"Invalid configuration format in {file_path.name}: expected dict, got {type(data).__name__}"
        )

    return data


def build_context(
    account: dict[str, Any],
    objective: str,
    evidence: list[dict[str, Any]],
    state: dict[str, Any] | None = None,
    config_dir: str | Path | None = None,
) -> dict[str, Any]:
    """Assemble the 5-layer WidgetWare SDR context package.

    Args:
        account: Target account information (task data).
        objective: SDR research or analysis objective.
        evidence: List of evidence dictionaries containing provenance.
        state: Optional current workflow state. Defaults to empty dict if None.
        config_dir: Path to configuration directory containing YAML files.

    Returns:
        Structured context dictionary with 5 separate layers.
    """
    if config_dir is None:
        cfg_path = _get_default_config_dir()
    else:
        cfg_path = Path(config_dir)

    products_data = load_yaml_config(cfg_path / "products.yaml")
    icp_data = load_yaml_config(cfg_path / "icp.yaml")
    policies_data = load_yaml_config(cfg_path / "policies.yaml")

    # Deep copy input data to guarantee input immutability
    account_copy = copy.deepcopy(account)
    objective_copy = str(objective)
    evidence_copy = copy.deepcopy(evidence)
    state_copy = copy.deepcopy(state) if state is not None else {}

    return {
        "system_instructions": get_system_instructions(),
        "business_context": {
            "products": products_data,
            "icp": icp_data,
            "policies": policies_data,
        },
        "task_context": {
            "account": account_copy,
            "objective": objective_copy,
        },
        "retrieved_evidence": evidence_copy,
        "state": state_copy,
    }
