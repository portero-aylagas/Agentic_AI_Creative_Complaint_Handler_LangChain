from typing import Any

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


class ToolUsageTracker:
    """Track tool calls found in LangChain agent message history."""

    def __init__(self) -> None:
        self.usage_count = {tool.name: 0 for tool in TOOLS}
        self.tool_sequences: list[list[str]] = []

    def track_result(self, result: dict[str, Any]) -> list[str]:
        sequence: list[str] = []

        for message in result.get("messages", []):
            for tool_call in getattr(message, "tool_calls", []) or []:
                tool_name = tool_call.get("name")
                if tool_name in self.usage_count:
                    self.usage_count[tool_name] += 1
                    sequence.append(tool_name)

        self.tool_sequences.append(sequence)
        return sequence

    def get_statistics(self) -> dict[str, Any]:
        total_tool_calls = sum(self.usage_count.values())
        most_used = None
        if total_tool_calls:
            most_used = max(self.usage_count.items(), key=lambda item: item[1])[0]

        return {
            "total_tool_calls": total_tool_calls,
            "tool_counts": self.usage_count,
            "most_used": most_used,
            "tool_sequences": self.tool_sequences,
        }


def extract_final_answer(result: dict) -> str:
    """Return the last AI message content from a LangChain v1 agent result."""
    messages = result.get("messages", [])
    for message in reversed(messages):
        if isinstance(message, AIMessage):
            return str(message.content)
    raise ValueError("Agent did not return an AI message.")


def handle_complaint(
    complaint: str,
    agent=None,
    tracker: ToolUsageTracker | None = None,
) -> str:
    """Handle a single complaint with the LangChain v1 agent."""
    print(f"\n{'=' * 60}")
    print(f"COMPLAINT: {complaint}")
    print(f"{'=' * 60}\n")

    active_agent = agent or build_agent()

    try:
        result = active_agent.invoke(
            {"messages": [{"role": "user", "content": complaint}]}
        )
    except APIConnectionError as exc:
        raise RuntimeError(
            "The agent could not reach the OpenAI API. Check network access "
            "and verify the current environment can make outbound requests."
        ) from exc

    if tracker is not None:
        tracker.track_result(result)

    return extract_final_answer(result)
