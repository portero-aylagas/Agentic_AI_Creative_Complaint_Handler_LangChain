import random

from langchain.tools import tool


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
