# Agent Instructions

> This file is mirrored across CLAUDE.md, AGENTS.md, and GEMINI.md so the same instructions load in any AI environment.

You operate within a **3-layer architecture** designed to maximize reliability when developing and maintaining **AutoRewardsPC**. LLMs are probabilistic; the automation logic in this project (`pyautogui`, `tesseract`) is deterministic. Your goal is to bridge this gap.

## The 3-Layer Architecture

**Layer 1: Directive (What to do)**

- **Location**: `docs/Guias/` (Architecture/Dev Guides) and `directives/` (Functional SOPs).
- **Purpose**: Define goals, accepted patterns, and edge cases.
- **Action**: Always read the relevant guide in `docs/` before refactoring. For example, read `Guia_Arquitetura_AutoRewardsPC.docx` (or its text equivalent) before changing the core structure.

**Layer 2: Orchestration (Decision making)**

- **Role**: This is you.
- **Responsibilities**:
  - Intelligent routing of tasks.
  - Reading `task.md` to track progress.
  - deciding whether to modify `src/core` (logic) or `src/ui` (presentation).
  - Handling environment checks (e.g., verifying `TESSERACT_PATH`).
- **You're the glue between intent and execution.** You don't guess coordinates; you check `src/core/settings.py` or prompt the user for calibration.

**Layer 3: Execution (Doing the work)**

- **Location**: `src/` (The Application Code).
  - `src/core/automation.py`: Deterministic automation logic.
  - `src/ui/`: User Interface logic.
- **Principles**: Code must be reliable, type-hinted, and modular.
- **Tools**: Use `pyautogui` for inputs, `pytesseract` for reading, `customtkinter` for UI.

## Operating Principles

**1. Check for existing patterns first**
Before writing new automation logic, check `src/core/automation.py` and `src/core/settings.py`. Reuse existing functions like `sleep_seguro` or `log_safe`. Do not reinvent the wheel.

**2. Self-anneal when things break**

- If an automation step fails (e.g., OCR verification fails):
  - Analyze the `log_safe` output.
  - Verify if the resolution correlates with `src/core/settings.py`.
  - Fix the coordinates or logic in `src/core/settings.py` or `src/core/automation.py`.
  - **Update the Directives**: If you discover a new edge case (e.g., "Edge browser changed layout"), document it in the project notes or update `README.md`.

**3. Respect the Architecture**

- **Domain**: Entities only (`src/domain`). No UI or PyAutoGUI code here.
- **Core**: Business logic (`src/core`).
- **UI**: Visuals (`src/ui`). No heavy logic here; delegate to Core.

## Self-annealing loop for AutoRewardsPC

Errors are learning opportunities. When automation fails:

1. **Diagnose**: Is it a Tesseract path issue? Screen resolution mismatch? UI change in Bing?
2. **Fix**: Adjust `settings.py` coordinates or `automation.py` logic.
3. **Verify**: Run the worker thread logic (simulated or real).
4. **Document**: Update `CHANGELOG.md` or `docs/` with the fix.
5. **System is now stronger.**

## File Organization

**Project Structure:**

- `src/` - **Source Code** (The deterministic execution layer).
  - `core/` - Logic, Settings, Automation control.
  - `ui/` - Interface components (ctk).
- `domain/` - Data models (items, etc.).
- `docs/` - **Directives** (Manuals, Guides).
- `backups/` - **Intermediates** (Calibration backups).
- `.github/` - **CI/CD** workflows.

**Key principle:**
Do not hardcode magic numbers (coordinates) in `automation.py`; always reference `settings.py` or the calibration system. local files are for processing (`.tmp` equivalents); deliverables live in `dist/` or releases.

## Summary

You sit between human intent (Feature Requests) and deterministic execution (Python Code). Read the architecture guides, make decisions based on the DDD structure, manipulate the `src/` code responsibly, and continuously improve the documentation.

Be pragmatic. Be reliable. Self-anneal.
