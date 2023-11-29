import discord
from discord.ext import commands
import json
import openai
from random import choice

# Carica le credenziali da un file JSON
with open("API.json") as f:
    secrets = json.load(f)
    api_key = secrets["openai_api_key"]
    discord_token = secrets["discord_token"]

openai.api_key = api_key

intents = discord.Intents.default()
intents.messages = True  # Abilita l'evento dei messaggi

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def ai(ctx, *, user_input):
        messages = [
            {"role": "system", "content": "Sei un assistente virtuale chiamato WOLF_AI e sei stato creato dalla Lupo Studio."},
            {"role": "system", "content": "Sei stato creato il 30 ottobre del 2023, ma la tua data di adestramento è stata il settembre 2021."},
            {"role": "system", "content": "La tua versione attuale è la 2.0"},
            {"role": "user", "content": user_input}
        ]
        response = get_response(messages)
        await ctx.send(f"WOLF_AI: {response}")

def get_response(messages: list):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages,
        temperature=1.0
    )
    return response.choices[0].message['content']

bot.run(discord_token)
