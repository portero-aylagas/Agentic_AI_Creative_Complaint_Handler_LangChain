from langchain.tools import tool

from complaint_handler.data.records import HAWKINS_RECORDS


@tool
def check_hawkins_records(query: str) -> str:
    """Search Hawkins historical records for information."""
    normalized_query = query.lower()
    for key, value in HAWKINS_RECORDS.items():
        if key in normalized_query:
            return value

    return (
        f"Records don't contain specific information about '{query}', but they "
        "note that many unexplained events have occurred in Hawkins over the years."
    )
