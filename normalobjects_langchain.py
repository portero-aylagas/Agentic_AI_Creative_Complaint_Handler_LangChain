import random

from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain.tools import tool
from langchain_openai import ChatOpenAI
from langchain_core.messages import AIMessage
from openai import APIConnectionError


load_dotenv()


llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.7)


@tool
def consult_demogorgon(complaint: str) -> str:
    """Get the Demogorgon's perspective on a complaint about the Upside Down."""
    responses = [
        (
            "The Demogorgon tilts its head. It seems confused by "
            f"'{complaint}'. Perhaps the issue is that you're thinking in "
            "three dimensions?"
        ),
        (
            "The Demogorgon makes a sound that might be agreement. It suggests "
            "that the problem might be temporal. Things work differently in "
            "the Upside Down's time."
        ),
        (
            "The Demogorgon appears to be eating something. It doesn't seem "
            f"to understand the concept of '{complaint}'. Maybe consistency "
            "isn't a priority there?"
        ),
    ]
    return random.choice(responses)


@tool
def check_hawkins_records(query: str) -> str:
    """Search Hawkins historical records for information."""
    records = {
        "portal": (
            "Records show portals have opened on various dates with no clear "
            "pattern. Weather, electromagnetic activity, and unknown factors "
            "seem involved."
        ),
        "monsters": (
            "Historical records indicate creatures from the Upside Down "
            "behave differently based on environmental factors, time of day, "
            "and proximity to certain individuals."
        ),
        "psychics": (
            "Records show that psychic abilities vary greatly. Some "
            "individuals can move objects but not see the future, while "
            "others can see visions but not move things."
        ),
        "electricity": (
            "Hawkins has a history of electrical anomalies. Records suggest "
            "a connection between the Upside Down and electromagnetic fields."
        ),
    }

    normalized_query = query.lower()
    for key, value in records.items():
        if key in normalized_query:
            return value

    return (
        f"Records don't contain specific information about '{query}', but they "
        "note that many unexplained events have occurred in Hawkins over the years."
    )


@tool
def cast_interdimensional_spell(problem: str, creativity_level: str = "medium") -> str:
    """Suggest a creative interdimensional spell to fix a problem."""
    creativity_multiplier = {"low": 1, "medium": 2, "high": 3}
    selected_count = creativity_multiplier.get(creativity_level, 2)

    spells = [
        (
            "Try chanting 'Bemca Becma Becma' three times while holding a "
            f"Walkman. This might recalibrate the interdimensional frequencies "
            f"related to: {problem}"
        ),
        (
            "Create a salt circle and place a compass in the center. The "
            f"magnetic anomalies might help stabilize: {problem}"
        ),
        (
            "Play 'Running Up That Hill' backwards at the exact location of "
            f"the issue. The temporal resonance could fix: {problem}"
        ),
        (
            "Gather three items: a lighter, a compass, and something personal. "
            f"Arrange them in a triangle while thinking about: {problem}. "
            "The emotional connection might help."
        ),
    ]

    selected_spells = random.sample(spells, min(selected_count, len(spells)))
    return "\n".join(selected_spells)


@tool
def gather_party_wisdom(question: str) -> str:
    """Ask the D&D party for their collective wisdom."""
    party_responses = {
        "portal": (
            "Mike: 'Portals are unpredictable, but they usually open near "
            "strong emotional events or electromagnetic disturbances.' "
            "Dustin: 'They also seem to follow some kind of pattern related "
            "to the Mind Flayer's activity.'"
        ),
        "monsters": (
            "Lucas: 'Demogorgons are territorial but also opportunistic.' "
            "Will: 'They can sense fear and strong emotions. Maybe that's "
            "why they act differently sometimes.'"
        ),
        "psychics": (
            "Mike: 'El's powers seem connected to her emotional state.' "
            "Dustin: 'And they're limited by her physical and mental energy. "
            "That's probably why she can't do everything.'"
        ),
        "electricity": (
            "Lucas: 'The Upside Down seems to interfere with electrical "
            "systems.' Dustin: 'But it also creates strange connections. "
            "It's like a feedback loop.'"
        ),
    }

    normalized_question = question.lower()
    for key, response in party_responses.items():
        if key in normalized_question:
            return response

    return (
        "The party huddles together. Mike: 'This is a tough one.' Dustin: "
        "'We need more information.' Lucas: 'Let's think about what we know.' "
        "Will: 'Maybe we should consult other sources?'"
    )


tools = [
    consult_demogorgon,
    check_hawkins_records,
    cast_interdimensional_spell,
    gather_party_wisdom,
]


agent = create_agent(
    model=llm,
    tools=tools,
    system_prompt=(
        "You are a creative complaint handler for strange happenings in Hawkins "
        "and the Upside Down. Use the available tools when they help, then give "
        "a concise, playful answer that still tries to be coherent."
    ),
)


complaints = [
    "Why do demogorgons sometimes eat people and sometimes don't?",
    "The portal opens on different days—is there a schedule?",
    "Why can some psychics see the Downside Up and others can't?",
    "Why do creatures and power lines react so strangely together?",
]


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
        result = agent.invoke(
            {"messages": [{"role": "user", "content": complaint}]}
        )
    except APIConnectionError as exc:
        raise RuntimeError(
            "The agent could not reach the OpenAI API. Check network access "
            "and verify the current environment can make outbound requests."
        ) from exc

    return extract_final_answer(result)


def main() -> None:
    print(f"Created {len(tools)} creative tools:")
    for current_tool in tools:
        print(f"  - {current_tool.name}: {current_tool.description[:60]}...")

    print("\nTesting agent with sample complaints...\n")
    for complaint in complaints[:2]:
        response = handle_complaint(complaint)
        print(f"\nRESPONSE: {response}\n")


if __name__ == "__main__":
    main()
