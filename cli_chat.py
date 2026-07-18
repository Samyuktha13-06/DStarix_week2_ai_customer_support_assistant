# pyrefly: ignore [missing-import]
from chains.support_chains import support_chain

def main():
    print("=" * 60)
    print("🤖 AI Customer Support Assistant")
    print("Type 'exit' or 'quit' to end the conversation.")
    print("=" * 60)

    while True:
        user_input = input("\nYou: ").strip()

        if not user_input:
            print("Assistant: Please enter a question.")
            continue

        if user_input.lower() in ["exit", "quit"]:
            print("\nAssistant: Thank you for contacting.")
            print("Have a great day! 👋")
            break

        try:
            response = support_chain.invoke(
                {
                    "question": user_input
                }
            )

            print(f"\nAssistant: {response}")

        except Exception as e:
            print(f"\nError: {e}")

if __name__ == "__main__":
    main()