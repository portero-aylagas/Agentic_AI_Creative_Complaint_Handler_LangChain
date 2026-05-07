import random

from langchain.tools import tool


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
