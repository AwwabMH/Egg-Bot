import random
import discord
from discord.ext import commands
from discord.ext import bridge
from discord.ui import Button, View
import mongo_db as mongo
import companies_and_jobs as comps



async def new_work(ctx):
    user_egg_id = ctx.author.id

    embedvar = discord.Embed(
        title = "Current Listings 📜:",
        description = str(comps.av_conts[0]) + " is looking for a " + str(comps.av_jobs[0]) + ".\n\n" + str(comps.av_conts[1]) + " is looking for a  " + str(comps.av_jobs[1] + ".\n\n" + str(comps.av_conts[2]) + " is looking for a " + str(comps.av_jobs[2])),
        color = discord.Color.gold()
    )
    btn1 = discord.ui.Button(
        label = str(comps.av_jobs[0]),
        style = discord.ButtonStyle.primary
    )
    btn2 = discord.ui.Button(
        label = str(comps.av_jobs[1]),
        style = discord.ButtonStyle.primary
    )
    btn3 = discord.ui.Button(
        label = str(comps.av_jobs[2]),
        style = discord.ButtonStyle.primary
    )

    view = View()
    view.add_item(btn1)
    view.add_item(btn2)
    view.add_item(btn3)

    async def btn1call(interaction: discord.Interaction):
        mongo.users.update_one({'user_id':user_egg_id}, {'$set':{'employment':str(comps.av_jobs[0])}})
        embedvar1 = discord.Embed(
            description = "Your Interview went great! You've been hired by " + str(comps.av_conts[0]),
            color = discord.Color.brand_green()
        )
        btn1.disabled = True
        btn2.disabled = True
        btn3.disabled = True
        await interaction.response.edit_message(embed=embedvar, view=view)
        await interaction.followup.send(embed=embedvar1)

    async def btn2call(interaction: discord.Interaction):
        mongo.users.update_one({'user_id':user_egg_id}, {'$set':{'employment':str(comps.av_jobs[1])}})
        embedvar1 = discord.Embed(
            description = "Your Interview went great! You've been hired by " + str(comps.av_conts[1]),
            color = discord.Color.brand_green()
        )
        btn1.disabled = True
        btn2.disabled = True
        btn3.disabled = True
        await interaction.response.edit_message(embed=embedvar, view=view)
        await interaction.followup.send(embed=embedvar1)

    async def btn3call(interaction: discord.Interaction):
        mongo.users.update_one({'user_id':user_egg_id}, {'$set':{'employment':str(comps.av_jobs[2])}})
        embedvar1 = discord.Embed(
            description = "Your Interview went great! You've been hired by " + str(comps.av_conts[2]),
            color = discord.Color.brand_green()
        )
        btn1.disabled = True
        btn2.disabled = True
        btn3.disabled = True
        await interaction.response.edit_message(embed=embedvar, view=view)
        await interaction.followup.send(embed=embedvar1)
    
    btn1.callback = btn1call
    btn2.callback = btn2call
    btn3.callback = btn3call

    await ctx.respond(embed = embedvar, view=view)





def work(ctx):
    user_egg_id = ctx.author.id
    try:
        if mongo.users.find_one({'user_id':user_egg_id})['employment'] == "unemployed":
            return new_work(ctx)
        else:
            user_database_entry = mongo.users.find_one({'user_id':user_egg_id})
            eggs_gained = random.randint(2,10)
            balance = int(user_database_entry['balance']) + eggs_gained
            mongo.users.update_one({'user_id':user_egg_id}, {'$set':{'balance':balance}})
            embedvar = discord.Embed(
                description = "You worked as a Chicken farmer and recieved " + str(eggs_gained) + " 🥚s!",
                color = discord.Color.gold()
            )
            embedvar.set_footer(text = "Requested By " + ctx.author.name, icon_url=ctx.author.avatar.url)
            return ctx.respond(embed = embedvar)
    except:
           return new_work(ctx)