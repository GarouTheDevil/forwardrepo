from pyrogram import Client, filters
import pyromod.listen
bot = Client('Forward bot', api_id= "1543212", api_hash= "d47de4b25ddf79a08127b433de32dc84", session_string= "BAAXjCwAb8M8WpFE8HpRFoCrU_fuMxxwJqAWggvr0oMIfbmAD30Wh2H91lbjz_I7eU0ULltGD2X4X0nrP2qCfQINuoTT6vOZX3aYAA6cZuKAwyN9dfBcjw8rMl8Nukn3dgbO97AG7bB2vQs17Xv5bVChyHOP9BsiyVHZd3wIIUcVwkrs3byXKAQNsHQeYgDNBiNWrgVEcYqICymfxRlExsyf6dqFmRWHDF-yJ-4lNn28JziGDm3mbyP3uwTKlBPGI0ME3I_tx94Pd5iejsCMFdd5q_1TLUG9y8jsMvbBSK3Orm0VWgAyM4gRXEwt6a8J0i3a_JI1J1OxykLlvRQlx3rvWCCsjQAAAABYHfJiAA")
import time

@bot.on_message(filters.command('forward'))
async def start(bot, message):
 # start_msg = await bot.ask(text = "Send The Start Message ID", chat_id = message.from_user.id, filters=filters.text, timeout=30)
 # end_msg = await bot.ask(text = "Send The End Message ID", chat_id = message.from_user.id, filters=filters.text, timeout=30)
 # bot.send_message(f'{start_msg} ,{end_msg}')
  await bot.send_message(message.from_user.id,f"Forwading Started")

  try:
    for i in range(2052, 4166):
      await bot.copy_message(chat_id=-1001525314409, from_chat_id= -1001260881403,message_id=i)
      time.sleep(5)
  except:
       pass
bot.run()
