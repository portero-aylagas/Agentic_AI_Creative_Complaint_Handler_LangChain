# Creative Complaint Handler with LangChain

Small demo project that uses LangChain plus a few themed tools to answer strange complaints about Hawkins and the Upside Down.

## Structure

```text
.
├─ normalobjects_langchain.py
├─ requirements.txt
├─ .env.example
└─ src/
   └─ complaint_handler/
      ├─ config.py
      ├─ agent.py
      ├─ prompts.py
      ├─ main.py
      ├─ tools/
      └─ data/
```

## Modules

- `normalobjects_langchain.py`: compatibility entrypoint that runs the packaged app
- `src/complaint_handler/config.py`: environment loading and model settings
- `src/complaint_handler/agent.py`: LangChain model and agent creation plus complaint handling
- `src/complaint_handler/prompts.py`: system prompt text
- `src/complaint_handler/main.py`: demo runtime flow
- `src/complaint_handler/tools/`: tool definitions
- `src/complaint_handler/data/`: hardcoded demo data

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

You can also place it in a local `.env` file because the app uses `python-dotenv`.

## Run

```bash
python normalobjects_langchain.py
```

You can also run the package entrypoint directly:

```bash
PYTHONPATH=src python -m complaint_handler.main
```

## Notes

- This is still a small demo project, but the original script has been separated into agent, prompt, tool, data, and runtime modules.
- The tools and sample complaint data are still hardcoded in the repository.
- The model is currently configured as `gpt-4o-mini`.
