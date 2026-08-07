# Class 3 Acceptance Criteria — WidgetWare SDR Context Package

The Class 3 implementation is accepted when all of the following conditions are met:

1. **Configuration Files Exist**:
   - `config/products.yaml` exists with at least 2 WidgetWare offerings.
   - `config/icp.yaml` exists with fit dimensions and required account fields.
   - `config/policies.yaml` exists defining evidence classifications and safety boundaries.

2. **System Instructions**:
   - Stable system instructions exposed via `src/widgetware_sdr/instructions.py` (`get_system_instructions()`).
   - Defines agent role, evidence rules, prohibited actions, and escalation policies without vague prose.

3. **Context Layer Separation**:
   - `src/widgetware_sdr/context_builder.py` exposes `build_context()`.
   - The returned object explicitly separates five layers: `system_instructions`, `business_context`, `task_context`, `retrieved_evidence`, and `state`.
   - Input dictionaries are preserved and never mutated.

4. **Evidence Provenance & Safety**:
   - Evidence records preserve provenance metadata (`claim`, `classification`, `source.name`, `source.url`, `source.retrieved_at`, `excerpt`).
   - Supported evidence classifications: `verified_fact`, `derived_fact`, `inference`, `unknown`, `conflict`.
   - Missing information remains `unknown` (no invented facts).
   - Prompt-injection attempt notes remain localized under `task_context` and cannot override system policies or authorize outreach.

5. **Scenario Fixtures & Test Suite**:
   - Four scenario fixtures exist under `tests/scenarios/`: `qualified_account.yaml`, `unqualified_account.yaml`, `insufficient_evidence.yaml`, `prompt_injection.yaml`.
   - All unit and scenario tests pass when running `python -m pytest -v`.

6. **Out-of-Scope Constraints**:
   - No ADK agent exists.
   - No LLM / Gemini call exists.
   - No live web research exists.
   - No external side effects (email, CRM updates, network calls) exist.
