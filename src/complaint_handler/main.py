from complaint_handler.agent import ToolUsageTracker, build_agent, handle_complaint
from complaint_handler.data.complaints import COMPLAINTS
from complaint_handler.tools import TOOLS


def print_tool_usage_analysis(tracker: ToolUsageTracker) -> None:
    stats = tracker.get_statistics()

    print("\n=== Tool Usage Analysis ===")
    print(f"Total tool calls: {stats['total_tool_calls']}")
    print(f"Tool usage counts: {stats['tool_counts']}")
    print(f"Most used tool: {stats['most_used']}")
    print("\nTool sequence examples:")

    for index, sequence in enumerate(stats["tool_sequences"], start=1):
        sequence_text = " -> ".join(sequence) if sequence else "No tools used"
        print(f"  Complaint {index}: {sequence_text}")


def main() -> None:
    print(f"Created {len(TOOLS)} creative tools:")
    for current_tool in TOOLS:
        print(f"  - {current_tool.name}: {current_tool.description[:60]}...")

    agent = build_agent()
    tracker = ToolUsageTracker()

    print("\nTesting agent with sample complaints...\n")
    for complaint in COMPLAINTS[:3]:
        response = handle_complaint(complaint, agent=agent, tracker=tracker)
        print(f"\nRESPONSE: {response}\n")

    print_tool_usage_analysis(tracker)


if __name__ == "__main__":
    main()
