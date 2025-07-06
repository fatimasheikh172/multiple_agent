import os
from dotenv import load_dotenv
from agents import Agent , Runner , OpenAIChatCompletionsModel , set_tracing_disabled
from openai import AsyncOpenAI

load_dotenv()
set_tracing_disabled(True)

external_client = AsyncOpenAI(
    api_key=os.getenv("GEMINI_API_KEY"),
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

model = OpenAIChatCompletionsModel(
    model="gemini-2.0-flash", 
    openai_client=external_client
)

# Web developer agent
web_developer = Agent(
    name="Web Developer",
    instructions="A web developer who can build websites and web applications",
    model=model,
    handoff_description="handoff to Web Developer if the task is related to web development"
)

# App developer agent
app_developer = Agent(
    name="App Developer",
    instructions="Develop cross-platform mobile apps for iOS and Android",
    model=model,
    handoff_description="handoff to App Developer if the task is related to app development"
)

# Marketing agent
marketing = Agent(
    name="Marketing Agent",
    instructions="Create and execute marketing strategies for product launches",
    model=model,
    handoff_description="handoff to Marketing Agent if the task is related to marketing"
)

# Manager agent
async def myAgent(user_input):
    manager = Agent(
        name="Manager",
        instructions="""
        You are a helpful assistant that can only help with:

        1. Web Development - Building websites and web applications
        2. Mobile App Development - Creating cross-platform mobile apps for iOS and Android  
        3. Marketing - Creating and executing marketing strategies for product launches

        If the user asks for anything related to these 3 topics, help them appropriately.

        If the user asks for anything else, simply respond with:
        "Sorry, I can't help about this topic."
        """,
        model=model,
        handoff_description=["Web Developer", "App Developer", "Marketing Agent"]
    )

    response = await Runner.run(
        manager,
        input=user_input,
    )

    return response.final_output
