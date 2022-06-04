import discord
import mongo_db as mongo

async def get_bal(ctx):
    user_egg_id = ctx.author.id
    if bool(mongo.users.find_one({'user_id':user_egg_id})) == True:
        user_database_entry = mongo.users.find_one({'user_id':user_egg_id})
        balance = user_database_entry['balance']
        if balance > 0  :
            embedvar = discord.Embed(
                title = ctx.author.name + "'s " + "Balance",
                description = "You have " + str(balance) + " 🥚s!",
               color = discord.Color.gold()
            )
            embedvar.set_footer(text = "Requested By " + ctx.author.name, icon_url=ctx.author.avatar.url)
            await embedvar
        else:
            embedvar = discord.Embed(
            description = "You got 0 🥚s!\n\nUse ?work to get some 🥚s",
            color = discord.Color.gold()
        )
            await embedvar
    else:
        embedvar = discord.Embed(
            description = "Your unemployed ass has 0 🥚s!\n\nUse ?work to get some 🥚s",
            color = discord.Color.gold()
        )
        await embedvar