import discord
import openai
from io import StringIO
import pandas as pd

openai.api_key = "OPEN-AI-KEY"

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents = intents)
@client.event
async def on_ready():
    print("We have logged in as {0.user}".format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    if message.content.startswith("!gpt"):
        message.content = message.content[3:]
        resp  = chatgpt_response(message)
        await message.channel.send(resp)
    

def chatgpt_response(msg):
        response = openai.Completion.create(
        model="text-davinci-003",
        prompt = msg,
        temperature = 0,
        max_tokens = 60,
        frequency_penalty = 0.0,
        presence_penalty = 0.0)
        
        resp_dict = response.get("choices")
        if resp_dict and len(resp_dict) > 0:
            prompt_response = resp_dict[0]["text"]
        return prompt_response
        

client.run("DISCORD-BOT-KEY")