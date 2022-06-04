import discord
from discord.ext import bridge
from discord.ext import commands
import mongo_db as mongo
import work_cmd as work
import joke_cmd as jokecmd
import balance_cmd
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


@bot.bridge_command(name = 'work', description="Start working to get some 🥚s")
async def workcmd(ctx):
    await work.work(ctx)
# Work command. Gives the user a random amount of eggs


@bot.bridge_command(name = 'bal', description="Checks your current 🥚 balance")
async def bal(ctx):
    await ctx.respond(embed=balance_cmd.get_bal(ctx))
@bot.bridge_command(name = 'balance', description="Checks your current 🥚 balance")
async def balance(ctx):
    await ctx.respond(embed=balance_cmd.get_bal(ctx))
# Balance command. If user exists it will read off his balance and if the user doesn't exist it will create a new document in the databse


@bot.bridge_command(description='Gets you a funny dad joke!')
async def joke(ctx):
    await ctx.respond(embed=jokecmd.get_joke())
# Requests a joke from an API and sends it



@bot.listen()
async def on_message(message):
    if message.author != bot.user:
        user_egg_id = message.author.id
        if bool(mongo.users.find_one({'user_id':user_egg_id})) == False:
            mongo.users.insert_one({'user_id':user_egg_id, 'balance':0, 'xp':10, 'level':1, 'last_message':message.created_at.second, 'employment':"unemployed"})
        else:
            user_database_entry = mongo.users.find_one({'user_id':user_egg_id})
            message_time = user_database_entry['last_message']
            delta_time = abs(int(message_time) - int(message.created_at.second))
            if delta_time > 3:
                mongo.users.update_one({'user_id':user_egg_id}, {'$set':{'last_message':message.created_at.second}})
                user_xp = user_database_entry['xp']
                user_level = user_database_entry['level']
                new_xp = int(user_xp) + len(message.content)/4
                level_threshold = round(pow(int(user_level), 0.5)*100)
                if int(user_xp) >= level_threshold:
                    new_level = int(user_level) + 1
                    mongo.users.update_one({'user_id':user_egg_id}, {'$set':{'xp':0, 'level':new_level}})
                    await message.channel.send("Congratulations! you just leveled up to level " + str(new_level) + "!", reference=message)
                else:
                    mongo.users.update_one({'user_id':user_egg_id}, {'$set':{'xp':new_xp}})

@bot.listen()
async def on_application_command(ctx):
    if ctx.author != bot.user:
        user_egg_id = ctx.author.id
        if bool(mongo.users.find_one({'user_id':user_egg_id})) == False:
            mongo.users.insert_one({'user_id':user_egg_id, 'balance':0, 'xp':10, 'level':1, 'last_message':0, 'employment':"unemployed"})

# XP event listener that adds xp for every message a user sends if the user already exists. It will create a new database entry for the user if it's his first message
# Has an anti-spam threshold of 3 seconds between messages and bases xp gained of the length of each message
# Has a level checker that automaticlaly levels up the user and resets his xp back to 0 if a certain xp_threshold has been met





bot.run("OTc2ODY3NDU0NDQ3OTMxNDQy.GC958J.VvN1emiLDzjbte74eudV5pg0l1Z_CefkiC4ud8")