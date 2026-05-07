from langchain.agents import create_agent
from langchain_core.messages import AIMessage
from langchain_openai import ChatOpenAI
from openai import APIConnectionError

from complaint_handler.config import MODEL_NAME, TEMPERATURE
from complaint_handler.prompts import SYSTEM_PROMPT
from complaint_handler.tools import TOOLS


def build_model() -> ChatOpenAI:
    return ChatOpenAI(model=MODEL_NAME, temperature=TEMPERATURE)


def build_agent():
    return create_agent(
        model=build_model(),
        tools=TOOLS,
        system_prompt=SYSTEM_PROMPT,
    )


def extract_final_answer(result: dict) -> str:
    """Return the last AI message content from a LangChain v1 agent result."""
    messages = result.get("messages", [])
    for message in reversed(messages):
        if isinstance(message, AIMessage):
            return str(message.content)
    raise ValueError("Agent did not return an AI message.")


def handle_complaint(complaint: str) -> str:
    """Handle a single complaint with the LangChain v1 agent."""
    print(f"\n{'=' * 60}")
    print(f"COMPLAINT: {complaint}")
    print(f"{'=' * 60}\n")

    try:
        result = build_agent().invoke(
            {"messages": [{"role": "user", "content": complaint}]}
        )
    except APIConnectionError as exc:
        raise RuntimeError(
            "The agent could not reach the OpenAI API. Check network access "
            "and verify the current environment can make outbound requests."
        ) from exc

    return extract_final_answer(result)
