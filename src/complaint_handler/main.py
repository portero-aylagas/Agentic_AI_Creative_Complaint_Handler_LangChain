from complaint_handler.agent import handle_complaint
from complaint_handler.data.complaints import COMPLAINTS
from complaint_handler.tools import TOOLS


def main() -> None:
    print(f"Created {len(TOOLS)} creative tools:")
    for current_tool in TOOLS:
        print(f"  - {current_tool.name}: {current_tool.description[:60]}...")

    print("\nTesting agent with sample complaints...\n")
    for complaint in COMPLAINTS[:2]:
        response = handle_complaint(complaint)
        print(f"\nRESPONSE: {response}\n")


if __name__ == "__main__":
    main()
