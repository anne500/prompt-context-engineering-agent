from time import perf_counter

from langchain.agents import create_agent
from langchain_ollama import ChatOllama


MODEL = "qwen3.5:4b"

QUESTION = "Why are automated tests useful?"

FORMAT_RULES = (
    "Use exactly three bullet points and fewer than 80 words. "
    "Explain this to someone learning software engineering."
)

REFERENCE = """
Project Cedar runs its automated tests whenever a pull request is opened.
Its regression tests check that existing behavior still works after a change.
A failed test blocks the release workflow until the problem is reviewed.
The tests cover selected scenarios; passing them does not prove the absence
of all defects.
""".strip()


def main():
    model = ChatOllama(
        model=MODEL,
        temperature=0,
        reasoning=False,
    )

    agent = create_agent(
        model=model,
        tools=[],
        system_prompt="You help people understand software engineering.",
    )

    experiments = [
        ("Baseline", QUESTION),
        ("Prompt engineered", f"{QUESTION}\n\n{FORMAT_RULES}"),
        (
            "Context engineered",
            f"{QUESTION}\n\n{FORMAT_RULES}\n\n"
            f"Reference information:\n{REFERENCE}",
        ),
    ]

    print(f"Model: {MODEL}", flush=True)

    for label, user_input in experiments:
        print(f"\n=== {label} ===", flush=True)
        started = perf_counter()

        response = agent.invoke(
            {"messages": [{"role": "user", "content": user_input}]}
        )

        elapsed = perf_counter() - started
        print(response["messages"][-1].content, flush=True)
        print(f"\nElapsed: {elapsed:.2f} seconds", flush=True)


if __name__ == "__main__":
    main()
