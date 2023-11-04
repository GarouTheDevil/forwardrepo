from pyrogram import Client, filters
import pyromod.listen
bot = Client('Forward bot', api_id= "1543212", api_hash= "d47de4b25ddf79a08127b433de32dc84", session_string= "BAAXjCwAqmujgFonUZOifEtLsTIR4QESZY0GeJmoKGWs0M6NawmIcm8pSxQ2uLpStMdGLTq4PvuWKCDq_IgCDEqLaL0clAVCUzGZ5JmM19GrVCmLJJ_g61Cfr411l0zI_JczD0QleJ5kXkSk_UOKdfY2p0rcpaYhc3pdErJySzGuyDgTBX4jIBS8yjQGmSZ6Nhh1d9pg2HbVy2AjxRyB-wSxeRba00GdL4yycxE8TuvBO3ueaXDwk8WK8DMcUdNjcIC6jc2Oqhp1wlt0lGAetsbW6K9cMhAos_V4aM7XYv3jhg4Zj-zZy0BYbUQOuMlWU3K5YrIS_WKTgDd2r_X3_XJG2oP5wgAAAABYHfJiAA")
import time

@bot.on_message(filters.command('forward'))
async def start(bot, message):
 # start_msg = await bot.ask(text = "Send The Start Message ID", chat_id = message.from_user.id, filters=filters.text, timeout=30)
 # end_msg = await bot.ask(text = "Send The End Message ID", chat_id = message.from_user.id, filters=filters.text, timeout=30)
 # bot.send_message(f'{start_msg} ,{end_msg}')
  await bot.send_message(message.from_user.id,f"Forwading Started")

  try:
    for i in range(5, 5688):
      await bot.copy_message(chat_id=-1001959628938, from_chat_id= -1001260881403,message_id=i)
      time.sleep(5)
  except:
       pass
bot.run()
