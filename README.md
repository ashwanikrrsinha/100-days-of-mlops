# 100-days-of-mlops
A journey to mastery: learning MLOps from scratch to production.

# 100 Days of MLOps Challenge

## 🎯 Goal
To go from basic scripts to building, deploying, and monitoring scalable ML pipelines.

## 📚 Logbook

| Day | Topic | Status | Link |
| :---: | :--- | :---: | :---: |
| 01 | Git, Repo Setup & Project Structure | ✅ | [Log](./logs/day-001.md) |
| 02 | ... | ⬜ | ... |
| 03 | ... | ⬜ | ... |

---

# Day 1: The Journey Begins

## What I Learned
Today I set up the foundation for my MLOps journey.
- **Version Control:** Learned how to initialize a repo and why .gitignore is essential for Python projects.
- **Structure:** Set up the `logs` and `projects` directories to keep documentation separate from code.

## Challenges
- [Mention any small issue you faced, e.g., configuring git email, or "None today!"]

## Next Steps
- Dive into Python virtual environments and dependency management.

---

# Day 2: Virtual Environments

## Key Concepts
- **Isolation:** Using `venv` prevents dependency conflicts between projects.
- **Reproducibility:** `requirements.txt` acts as the "recipe" for recreating the environment on any machine.
- **Git Hygiene:** Never commit the virtual environment folder (`.venv`); only commit the recipe (`requirements.txt`).

## Commands Learned
- `python -m venv .venv`: Creates the environment.
- `source .venv/bin/activate`: Enters the environment.
- `pip freeze > requirements.txt`: Saves the current libraries to a file.
- `deactivate`: Exits the environment.

---

# Day 3: Production-Ready Python Scripts

## Key Concepts
- **Scripts vs. Notebooks:** Notebooks are for exploration; Scripts (`.py`) are for automation and production.
- **Type Hinting:** Using `variable: type` to ensure code clarity and reduce bugs.
- **`if __name__ == "__main__":`**: Ensures code only runs when executed directly, not when imported.
- **`argparse`**: The library that allows us to pass parameters into the script from the terminal, making the code reusable without editing it.

## Code Snippet
```bash
# Example of running the script with arguments
python projects/01-python-refresher/model.py --n_estimators 200