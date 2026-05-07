from langchain.tools import tool

from complaint_handler.data.party_responses import PARTY_RESPONSES


@tool
def gather_party_wisdom(question: str) -> str:
    """Ask the D&D party for their collective wisdom."""
    normalized_question = question.lower()
    for key, response in PARTY_RESPONSES.items():
        if key in normalized_question:
            return response

    return (
        "The party huddles together. Mike: 'This is a tough one.' Dustin: "
        "'We need more information.' Lucas: 'Let's think about what we know.' "
        "Will: 'Maybe we should consult other sources?'"
    )
