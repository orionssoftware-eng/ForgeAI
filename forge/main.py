import anyio

from forge.agent.agent import Agent


async def main():

    print("=" * 50)
    print(" ForgeAI")
    print("=" * 50)

    agent = Agent()

    await agent.initialize()

    while True:

        prompt = input("\n>>> ")

        if prompt.lower() in ("exit", "quit"):

            break

        result = await agent.execute(prompt)

        print()

        print(result)


if __name__ == "__main__":

    anyio.run(main)