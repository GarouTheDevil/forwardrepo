from pyrogram import Client, filters
import pyromod.listen
bot = Client('Forward bot', api_id= "1543212", api_hash= "d47de4b25ddf79a08127b433de32dc84", session_string= "BAAXjCwAlWCr9f1bzYZIga9DYYXc8Ule75YT0zeHt9B7rLCmv5USIUBGEhryNJN_CcBbRUEcDzlhI3wLBi5EElAVJAYx1h08IjdZwftEIa5KTRa08R2BPWLksIyf_ZEogwvcGO_Ty8wa5E7OCHklle10KSJVT1Dqan11KGLal0x4WPKmMI4PVzXKIhuhWM6HsOPSovN9TPugqS_2w3SEGQY5b6o9_rSb9t1mOfyH67TyJrA0ZdnQcedqMlZ-teu4kCwoI9N15AOxSvMbbqyiRKGaadbJITOHs1h78cR4qhmQru5J9MrnrlTCGeFnErNoZYTrSn1BGXC51m0Sf-SQODXpmveowQAAAABYHfJiAA")
import time

@bot.on_message(filters.command('forward'))
async def start(bot, message):
 # start_msg = await bot.ask(text = "Send The Start Message ID", chat_id = message.from_user.id, filters=filters.text, timeout=30)
 # end_msg = await bot.ask(text = "Send The End Message ID", chat_id = message.from_user.id, filters=filters.text, timeout=30)
 # bot.send_message(f'{start_msg} ,{end_msg}')
  await bot.send_message(message.from_user.id,f"Forwading Started")

  try:
    for i in range(2054, 4166):
      await bot.copy_message(chat_id=-1001525314409, from_chat_id= -1001260881403,message_id=i)
      time.sleep(5)
  except:
       pass
bot.run()
