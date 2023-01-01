
from pyrogram import Client, filters

bot = Client('Forward bot', api_id= "1543212", api_hash= "d47de4b25ddf79a08127b433de32dc84", bot_token= "1860781460:AAHOUPAWKur2BzMRfmLU1wIBedlm6GGGL8g")

@bot.on_message(filters.command('forward'))
async def start(bot, message):
  try:
    for i in range(4451, 5372):
       await bot.copy_message(chat_id=-1001511163820, from_chat_id=-1001748041723,message_id=i)
  except:
       print("error")

bot.run()
