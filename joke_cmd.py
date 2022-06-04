import discord
import requests

def get_joke():
    joke = requests.get('https://icanhazdadjoke.com/', headers={'Accept': 'application/json'})
    embedvar = discord.Embed(
        description = joke.json()['joke'],
        color = discord.Color.gold()
    )
    return embedvar