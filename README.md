# AgenticExample

Minimal example that demonstrates using the OpenAI Python client to send system/user prompts, compare responses (baseline, role, constraints, reasoning), and display results in both Jupyter and plain terminal.

## Quick setup

1. Create and activate your virtualenv (macOS):
```bash
python3 -m venv venv
source venv/bin/activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
# or at minimum:
pip install openai python-dotenv ipython
```

3. Set your OpenAI API key (do NOT commit this):
```bash
export OPENAI_API_KEY="sk-REDACTED"
```
Or create a local `.env` (gitignored) and use python-dotenv (example in `prompt.py`).

## Files of interest
- `prompt.py` — main script: loads OPENAI_API_KEY, initializes client, defines `get_completion`, runs several prompts (baseline, role, constraints, reasoning), and uses `display_responses` which falls back to plain printing when not in IPython.
- `.env` — local environment file (must be added to `.gitignore`).
- `.gitignore` — configured to ignore `.env`, `venv/`, `__pycache__/`, `.ipynb_checkpoints/`.

## Run
- Terminal:
```bash
export OPENAI_API_KEY="sk-..."
python prompt.py
```
- Jupyter Notebook: open the notebook and run cells to get HTML/Markdown rendering.

## Notes & troubleshooting
- If script raises an OpenAI client error, ensure `OPENAI_API_KEY` is set in the environment or loaded via `python-dotenv`.
- `display_responses` will render Markdown in Jupyter; in plain Python it prints responses. Add `print()` after `get_completion()` calls to debug returned text.

## Security
- Never commit API keys. `.env` is ignored by default — keep it that way or use a secret manager.
