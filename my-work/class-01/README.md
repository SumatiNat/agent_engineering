# Class 1 Assignment

## Student Information
- Name: Sumati Natarajan
- GitHub username: SumatiNat
- Date completed: 2026-08-04

## Workspace Setup
- Forked the repo
- Cloned my fork
- Opened it in Antigravity
- Created my-work/class-01
- Committed and pushed

## What I Learned
Write a short reflection.
- Learnt about the overall course and that this class is a baseline for future classes
- Understood the repository harness structure and its components
- Understanding the repository harness structure means recognizing how these components fit together to form a known-good, reproducible baseline. Instead of starting with unstructured prose or unverified scripts, the harness allows you 
to validate code deterministically at every step of development.













- Learnt how to set up the environment and run the basic checks
   Used  https://test-agent-eng.vercel.app/
## Challenges
Describe what you fixed or learned.
# Initially i was not sure about setting up the .venv and pip install -e .[dev]
# But after reading the BUILD.md and following the steps carefully i was able to set up the environment and run the basic checks

Viewed README.md
Viewed README.md:1-56
Viewed 0003-repository-harness.md:1-30
Listed directory golden-solution
Listed directory scripts
Listed directory .agents

In Agent Engineering, a **Repository Harness** refers to the foundational infrastructure, environment setup, and quality control systems created around a project *before* implementing core agent logic.

Just as a physical harness provides safety and stability, a repository harness establishes the boundary conditions, automated verification tools, and governance rules required for AI agents and human developers to build, test, and run code safely and reproducibly.

---

### Key Components of a Repository Harness

1. **Environment Verification & Dependency Management**
   * **Files**: [pyproject.toml](file:///Users/sumati/agy2-projects/agent_engineering/agent-engineering-book/Gemini/1-Foundations/Classes/class-01/golden-solution/pyproject.toml), [verify_environment.py](file:///Users/sumati/agy2-projects/agent_engineering/agent-engineering-book/Gemini/1-Foundations/Classes/class-01/golden-solution/scripts/verify_environment.py)
   * **Purpose**: Manages project packages, Python versions, and runtime dependencies. `verify_environment.py` ensures the execution environment is properly set up before any code runs.

2. **Deterministic Quality Gate**
   * **Files**: [check.sh](file:///Users/sumati/agy2-projects/agent_engineering/agent-engineering-book/Gemini/1-Foundations/Classes/class-01/golden-solution/scripts/check.sh)
   * **Purpose**: A single, automated command (`./scripts/check.sh`) that executes linting (`ruff`), static type checking (`mypy`), formatting, and unit tests (`pytest`). This gives immediate, objective feedback on code validity.

3. **Agent Rules & Workflows (`.agents/`)**
   * **Directory**: [.agents/](file:///Users/sumati/agy2-projects/agent_engineering/agent-engineering-book/Gemini/1-Foundations/Classes/class-01/golden-solution/.agents)
   * **Purpose**: Contains custom rules and workflow configurations that instruct AI agents (like Antigravity) how to behave within the repository, enforcing coding styles, architectural boundaries, and safety constraints.

4. **Charter & Specification Artifacts**
   * **Files**: [SPEC.md](file:///Users/sumati/agy2-projects/agent_engineering/agent-engineering-book/Gemini/1-Foundations/Classes/class-01/golden-solution/SPEC.md), [KNOWN_FAILURE_CASES.md](file:///Users/sumati/agy2-projects/agent_engineering/agent-engineering-book/Gemini/1-Foundations/Classes/class-01/golden-solution/KNOWN_FAILURE_CASES.md), Architectural Decision Records ([ADRs](file:///Users/sumati/agy2-projects/agent_engineering/agent-engineering-book/Gemini/1-Foundations/Classes/class-01/golden-solution/docs/architecture-decisions))
   * **Purpose**: Defines business context, domain constraints, acceptance criteria, and known edge cases so both human developers and agents work against a clear specification.

---

### Why this is important in Class 01

Understanding the repository harness structure means recognizing how these components fit together to form a **known-good, reproducible baseline**. Instead of starting with unstructured prose or unverified scripts, the harness allows you to validate code deterministically at every step of development.