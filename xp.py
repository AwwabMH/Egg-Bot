import discord
import mongo_db as mongo
import titles_and_ranks as tar
import time
import datetime

def xp_gain_message(message):
    user_egg_id = message.author.id
    if bool(mongo.users.find_one({'user_id':user_egg_id})) == False:
        mongo.users.insert_one({'user_id':user_egg_id, 'balance':0, 'net_worth':0, 'xp':10, 'level':1, 'last_message':message.created_at, 'employment':"unemployed", 'title':tar.titles[0], 'rank':tar.ranks[0]})
        return False
    else:
        user = mongo.users.find_one({'user_id':user_egg_id})
        user_level = user['level']
        message_time = user['last_message']
        delta_time = message.created_at.replace(tzinfo=None) - message_time
        print(delta_time.total_seconds())
        if abs(delta_time.total_seconds()) >= 2:
            mongo.users.update_one({'user_id':user_egg_id}, {'$set':{'last_message':message.created_at}})
            user_xp = user['xp']
            new_xp = int(user_xp) + len(message.content)
            level_threshold = round(pow(int(user_level), 0.5)*50)
            if int(user_xp) >= level_threshold:
                new_level = int(user_level) + 1
                mongo.users.update_one({'user_id':user_egg_id}, {'$set':{'xp':0, 'level':new_level}})
                send_message = "Congratulations! you just leveled up to level " + str(new_level) + "!"
                return send_message
            else:
                mongo.users.update_one({'user_id':user_egg_id}, {'$set':{'xp':new_xp}})
                return False
        else:
            return False

def xp_gain_command(ctx):
    user_egg_id = ctx.author.id
    if bool(mongo.users.find_one({'user_id':user_egg_id})) == False:
        mongo.users.insert_one({'user_id':user_egg_id, 'balance':0, 'net_worth':0, 'xp':10, 'level':1, 'last_message':datetime.datetime.now(tz=None), 'employment':"unemployed", 'title':tar.titles[0], 'rank':tar.ranks[0]})
        return False
    else:
        user = mongo.users.find_one({'user_id':user_egg_id})
        user_level = user['level']
        user_xp = user['xp']
        new_xp = int(user_xp) + 8
        level_threshold = round(pow(int(user_level), 0.5)*50)
        if int(user_xp) >= level_threshold:
            new_level = int(user_level) + 1
            mongo.users.update_one({'user_id':user_egg_id}, {'$set':{'xp':0, 'level':new_level}})
            send_message = "Congratulations! you just leveled up to level " + str(new_level) + "!"
            return send_message
        else:
            mongo.users.update_one({'user_id':user_egg_id}, {'$set':{'xp':new_xp}})
            return False