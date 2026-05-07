# Creative Complaint Handler with LangChain

Small demo project that uses LangChain plus a few themed tools to answer strange complaints about Hawkins and the Upside Down.

## Files

- `normalobjects_langchain.py`: single-file demo with tools, agent setup, sample complaints, and runtime logic
- `requirements.txt`: Python dependencies
- `.gitignore`: local ignore rules for this workspace

## Requirements

- Python 3.12 or compatible
- An OpenAI API key available in your environment or in a local `.env` file

## Install

```bash
pip install -r requirements.txt
```

## Environment

Set your API key before running:

```bash
OPENAI_API_KEY=your_key_here
```

You can also place it in a local `.env` file because the script uses `python-dotenv`.

## Run

```bash
python normalobjects_langchain.py
```

## Notes

- This is intentionally a single-file demo project.
- The tools and sample complaint data are hardcoded in the script.
- The model is currently configured as `gpt-4o-mini`.
