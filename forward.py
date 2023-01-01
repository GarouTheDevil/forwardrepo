
from pyrogram import Client, filters

bot = Client('Forward bot', api_id= "1695333", api_hash= "acfb6f602239fc52a93d1847a3d850d1", bot_token= "5527448498:AAECjLx626Z5AaGOUZUIvIlq7rtWFQh6kDQ")

async def start(bot, message):
  try:
    for i in range(0, 5372):
       await bot.copy_message(chat_id=-1001525314409, from_chat_id=-1001665685493,message_id=i)
  except:
       pass

bot.run()
