import discord
import mongo_db as mongo
import titles_and_ranks as tar

def tarcheck(message):
    user_egg_id = message.author.id
    if bool(mongo.users.find_one({'user_id':user_egg_id})) == True:
        user = mongo.users.find_one({'user_id':user_egg_id})
        user_net_worth = user['net_worth']
        user_level = user['level']
        i = 0
        for x in tar.titles:
            if user_net_worth >= tar.titles_net_worth[i] and user['title'] != tar.titles[i] and tar.titles.index((user['title'])) < i:
                mongo.users.update_one({'user_id':user_egg_id}, {'$set':{'title':tar.titles[i]}})
                break
            else:  
                i = i + 1
        i = 0
        for x in tar.ranks:
            if user_level >= tar.ranks_level[i] and user['rank'] != tar.ranks[i] and tar.ranks.index((user['rank'])) < i:
                mongo.users.update_one({'user_id':user_egg_id}, {'$set':{'rank':tar.ranks[i]}})
                break
            else:
                i = i + 1

def tarcheck_command(ctx):
    user_egg_id = ctx.author.id
    if bool(mongo.users.find_one({'user_id':user_egg_id})) == True:
        user = mongo.users.find_one({'user_id':user_egg_id})
        user_net_worth = user['net_worth']
        user_level = user['level']
        i = 0
        for x in tar.titles:
            if user_net_worth >= tar.titles_net_worth[i] and user['title'] != tar.titles[i] and tar.titles.index((user['title'])) < i:
                mongo.users.update_one({'user_id':user_egg_id}, {'$set':{'title':tar.titles[i]}})
                break
            else:  
                i = i + 1
        i = 0
        for x in tar.ranks:
            if user_level >= tar.ranks_level[i] and user['rank'] != tar.ranks[i] and tar.ranks.index((user['rank'])) < i:
                mongo.users.update_one({'user_id':user_egg_id}, {'$set':{'rank':tar.ranks[i]}})
                break
            else:
                i = i + 1

