from pyrogram import Client, filters
import pyromod.listen
bot = Client('Forward bot', api_id= "1543212", api_hash= "d47de4b25ddf79a08127b433de32dc84", session_string= "BAAXjCwAEXawe2BfRCJvUc5m1oUz3p-yUzdxpBZtVU_C2OurynoMQwzgjSJZNv8WXoUJg-fpkupC27LV0RTKELZr5talUKO3W8hm_1eqQcSCd_c_ZHwCxl3gVVzTCeiufJzcnHxtsXFwNdFxovANu6jOZrJdmLBElZWdHDcCdlx43iEFCmC51d1wKNZ0_K_uagRHQPyBkf68xZuo2olvpc2OxA41WwHgXv0Se6tU6VQPQIsUkWnsNl9v_wdMaTMusfy_OqO5kxx_ocWHKpD-46_of5Q6XkIbyn9iOvlkSZmdIWlIt1GB0JMo8tA9fVsLUZaZmPGWXUhs_-aw5jpKnjramYuRkQAAAABYHfJiAA")
import time

@bot.on_message(filters.command('forward'))
async def start(bot, message):
 # start_msg = await bot.ask(text = "Send The Start Message ID", chat_id = message.from_user.id, filters=filters.text, timeout=30)
 # end_msg = await bot.ask(text = "Send The End Message ID", chat_id = message.from_user.id, filters=filters.text, timeout=30)
 # bot.send_message(f'{start_msg} ,{end_msg}')
  await bot.send_message(message.from_user.id,f"Forwading Started")

  try:
    for i in range(0, 4166):
      await bot.copy_message(chat_id=-1001525314409, from_chat_id= -1001260881403,message_id=i)
      time.sleep(5)
  except:
       pass
bot.run()
