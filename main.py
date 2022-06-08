import discord
from discord.ext import bridge
from discord.ext import commands
from os import environ
import mongo_db as mongo
import work_cmd as work
import joke_cmd as jokecmd
import balance_cmd
import titles_and_ranks as tar
import xp
import rl_check as rl
# Imports




intents = discord.Intents.all()
intents.members = True
intents.message_content = True
bot = bridge.Bot(command_prefix='?', intents=intents)
# logging into the bot




@bot.event
async def on_ready():
    print("Logged in as: " + str(bot.user) + "!")
    await bot.change_presence(activity = discord.Game('Egg'))
# Check to make sure bot has logged in + change the bot's activity




@bot.slash_command(name = 'work', description="Start working to get some 🥚s")
@commands.cooldown(1, 5, commands.BucketType.user)
async def workcmd(ctx):
    await work.work(ctx)
# Work command. Gives the user a random amount of eggs




@bot.slash_command(name = 'bal', description="Checks your current 🥚 balance")
@commands.cooldown(1, 5, commands.BucketType.user)
async def bal(ctx):
    await ctx.respond(embed=balance_cmd.get_bal(ctx))
@bot.slash_command(name = 'balance', description="Checks your current 🥚 balance")
@commands.cooldown(1, 5, commands.BucketType.user)
async def balance(ctx):
    await ctx.respond(embed=balance_cmd.get_bal(ctx))
# Balance command. If user exists it will read off his balance and if the user doesn't exist it will create a new document in the databse




@bot.slash_command(description='Gets you a funny dad joke!')
@commands.cooldown(1, 5, commands.BucketType.user)
async def joke(ctx):
    await ctx.respond(embed=jokecmd.get_joke())
# Requests a joke from an API and sends it




@bot.listen()
async def on_message(message):
    if message.author != bot.user:
        var = xp.xp_gain_message(message)
        if var != False:
            print(var)
            await message.channel.send(var, reference = message)
@bot.listen()
async def on_application_command(ctx):
    if ctx.author != bot.user:
        var = xp.xp_gain_command(ctx)
        if var != False:
            await ctx.respond(var)
# XP event listener that adds xp for every message a user sends if the user already exists. It will create a new database entry for the user if it's his first message
# Has an anti-spam threshold of 3 seconds between messages and bases xp gained of the length of each message
# Has a level checker that automaticlaly levels up the user and resets his xp back to 0 if a certain xp_threshold has been met




@bot.listen('on_message')
async def on_message2(message):
    if message.author != bot.user:
        rl.tarcheck(message)

@bot.listen('on_application_command')
async def on_application_command2(ctx):
    if ctx.author != bot.user:
        rl.tarcheck_command(ctx)
# After the XP listener there is a script that checks for titles and ranks based on the user's level and net_worth
# Net worth is different from balance as it includes all wealth collected in the user's life rather than what the user has in balance right now




@bot.event
async def on_application_command_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        embedvar = discord.Embed(
            description = error,
            color = discord.Color.gold()
        )
        await ctx.respond(embed=embedvar)
    else:
        raise error
# Error checker for command cooldown






bot.run(environ['Token'])