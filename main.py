import asyncio
import os

from dotenv import load_dotenv

from autogen_agentchat.agents import AssistantAgent
from autogen_agentchat.teams import RoundRobinGroupChat
from autogen_agentchat.conditions import MaxMessageTermination
from autogen_ext.models.openai import OpenAIChatCompletionClient


# ---------------------------------------------------------
# 1. Load environment variables
# ---------------------------------------------------------

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

if not OPENAI_API_KEY:
    raise ValueError("OPENAI_API_KEY not found in .env")


# ---------------------------------------------------------
# 2. Create OpenAI model client
# ---------------------------------------------------------

model_client = OpenAIChatCompletionClient(
    model="gpt-4o-mini",
    api_key=OPENAI_API_KEY
)


# ---------------------------------------------------------
# 3. Create Research Agent
# ---------------------------------------------------------

research_agent = AssistantAgent(
    name="research_agent",
    model_client=model_client,
    system_message="""
You are a Research Agent.

Your responsibility is to:
1. Understand the user's question.
2. Create a clear and accurate initial answer.
3. Explain concepts using simple examples.
4. Provide enough technical detail for a software developer.

Do not assume that your answer is perfect.
Your answer will be reviewed by another agent.
"""
)


# ---------------------------------------------------------
# 4. Create Reviewer Agent
# ---------------------------------------------------------

reviewer_agent = AssistantAgent(
    name="reviewer_agent",
    model_client=model_client,
    system_message="""
You are a Reviewer Agent.

Your responsibility is to:
1. Review the answer produced by the Research Agent.
2. Identify missing or incorrect information.
3. Improve the explanation.
4. Make the final answer clear and easy to understand.
5. Add examples when useful.

Return the improved final answer.
"""
)


# ---------------------------------------------------------
# 5. Create the team
# ---------------------------------------------------------

termination = MaxMessageTermination(max_messages=4)

team = RoundRobinGroupChat(
    participants=[
        research_agent,
        reviewer_agent
    ],
    termination_condition=termination
)


# ---------------------------------------------------------
# 6. Run the application
# ---------------------------------------------------------

async def main():

    question = input("\nEnter your question: ")

    print("\n==============================")
    print("Starting AutoGen Team")
    print("==============================\n")

    result = await team.run(
        task=question
    )

    print("\n==============================")
    print("FINAL CONVERSATION")
    print("==============================\n")

    for message in result.messages:

        print(f"\n[{message.source}]")
        print("-" * 50)
        print(message.content)

    await model_client.close()


# ---------------------------------------------------------
# 7. Start application
# ---------------------------------------------------------

if __name__ == "__main__":
    asyncio.run(main())