from my_agents import myAgent
import chainlit as cl
import asyncio

@cl.on_chat_start
async def start():
    await cl.Message(
       content="👋 Welcome to the Multi-Agent System — specializing in Web Development, App Development & Marketing!"
    ).send()


@cl.on_message
async def main(message: cl.Message):
   user_input = message.content

   await cl.Message(content = "💭 Please wait....").send()
   response = asyncio.run(myAgent(user_input))
   await cl.Message(
       content=f"{response}"
    ).send()
