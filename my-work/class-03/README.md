# Class 3 Starter — WidgetWare SDR Context Package

This is the minimal starting project for Class 3.

## Source of truth

Read `SPEC.md` before implementing the lab. Use `LAB.md` for detailed guidance.

The starter intentionally does **not** include:

- WidgetWare product configuration;
- ICP configuration;
- policy configuration;
- agent instructions;
- the context builder;
- completed scenario fixtures;
- completed Class 3 tests.

Students will create those items during the lab.

## Setup

From this directory:

```bash
python -m pip install -e ".[dev]"
python -m pytest -v
```

The starter smoke test must pass before implementation begins.

## Important boundaries

Class 3 does not build:

- a Google ADK agent;
- Gemini or another LLM call;
- web research;
- email or social-message delivery;
- CRM integration;
- a database;
- deployment code;
- external side effects.
------------------
Ran command: `python3 -m pytest -v`

### Validation Report — `SPEC.md` vs. Test Results

All **12 test cases passed** (`12 passed in 0.31s`). 

Here is the itemized validation mapping each test case directly back to the requirements in [SPEC.md](file:///Users/sumati/agy2-projects/agent_engineering/my-work/class-03/SPEC.md):

---

### 1. Configuration Tests (`SPEC.md §8 & §13.1`)

| Test Case | SPEC Requirement | Status |
| :--- | :--- | :---: |
| `test_yaml_config_files_exist_and_load` | Verifies that `products.yaml`, `icp.yaml`, and `policies.yaml` exist, load cleanly, contain at least 2 offerings, a numeric employee threshold (5,000), and all 5 evidence classifications (`verified_fact`, `derived_fact`, `inference`, `unknown`, `conflict`). | **PASSED** |
| `test_policies_prohibitions_and_approvals` | Verifies safety boundaries in `policies.yaml`, including prohibited actions (`send_email`, `modify_crm`, `invent_company_facts`) and human approval triggers (`external_outreach`, `crm_write`). | **PASSED** |

---

### 2. System Instructions Tests (`SPEC.md §9 & §13.2`)

| Test Case | SPEC Requirement | Status |
| :--- | :--- | :---: |
| `test_system_instructions_content` | Verifies that `get_system_instructions()` returns stable, observable rules enforcing evidence provenance, prohibiting invented facts, prohibiting automated email/CRM actions, and requiring explicit human approval. | **PASSED** |

---

### 3. Context Builder Tests (`SPEC.md §10 & §13.3`)

| Test Case | SPEC Requirement | Status |
| :--- | :--- | :---: |
| `test_build_context_structure` | Verifies that `build_context()` returns a dictionary containing all **5 distinct context layers** (`system_instructions`, `business_context`, `task_context`, `retrieved_evidence`, `state`). | **PASSED** |
| `test_build_context_default_state` | Verifies that when workflow `state` is omitted, it defaults to an empty object `{}` without error. | **PASSED** |
| `test_build_context_input_immutability` | Verifies that `build_context()` creates deep copies of input objects (`account`, `evidence`, `state`) so caller objects are never mutated. | **PASSED** |
| `test_build_context_missing_config_error` | Verifies that missing configuration files produce a clear, actionable `FileNotFoundError`. | **PASSED** |

---

### 4. Scenario Tests (`SPEC.md §12 & §13.4`)

| Test Case | Scenario Fixture | SPEC Requirement | Status |
| :--- | :--- | :--- | :---: |
| `test_scenario_qualified_account` | `qualified_account.yaml` | Target account meets company size (12,000), preferred industry (`industrial_automation`), region (`united_states`), and buying signals with verified evidence. | **PASSED** |
| `test_scenario_unqualified_account` | `unqualified_account.yaml` | Target account falls below employee threshold (350) and belongs to an excluded industry (`consumer_retail`). Disqualifying facts remain visible without drafting outreach. | **PASSED** |
| `test_scenario_insufficient_evidence` | `insufficient_evidence.yaml` | Target account has missing decisive fields (`industry: unknown`, `employee_count: null`). System preserves missing values without inventing facts. | **PASSED** |
| `test_scenario_prompt_injection` | `prompt_injection.yaml` | Account notes contain malicious prompt injection trying to force qualification and send email. Injection text remains strictly localized in `task_context` and cannot override `system_instructions` or `policies`. | **PASSED** |

---

### 5. Starter Environment (`SPEC.md §3`)

| Test Case | SPEC Requirement | Status |
| :--- | :--- | :---: |
| `test_starter_environment` | Confirms package import and module docstring. | **PASSED** |

---

### 🎯 Conclusion

Your project completely satisfies all **Definition of Done** (§17) and **Acceptance Criteria** (§16) requirements set out in `SPEC.md`:

- ✅ 5 context layers strictly separated
- ✅ Provenance preserved on evidence records
- ✅ Unknowns remain unknown
- ✅ Safety boundaries & prompt injection defense verified
- ✅ Zero out-of-scope code (No ADK agent, no LLM calls, no DB/CRM/email side-effects)
- ✅ 100% passing test suite (12/12)