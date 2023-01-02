from pyrogram import Client, filters
import pyromod.listen
bot = Client('Forward bot', api_id= "1695333", api_hash= "acfb6f602239fc52a93d1847a3d850d1", bot_token= "5527448498:AAGXvarac-1CXLl-7b1EtjvKDyvsdD0RSYA")
import time

@bot.on_message(filters.command('forward'))
async def start(bot, message):
 # start_msg = await bot.ask(text = "Send The Start Message ID", chat_id = message.from_user.id, filters=filters.text, timeout=30)
 # end_msg = await bot.ask(text = "Send The End Message ID", chat_id = message.from_user.id, filters=filters.text, timeout=30)
 # bot.send_message(f'{start_msg} ,{end_msg}')
  await bot.send_message(message.from_user.id,f"Forwading Started")

  try:
    for i in range(0, 5372):
      await bot.copy_message(chat_id=-1001525314409, from_chat_id=-1001665685493,message_id=i)
      time.sleep(5)
  except:
       pass
    else:
       await bot.send_message(message.from_user.id,f"Forwading Stopped\n\nERROR : {e}")
       
bot.run()
