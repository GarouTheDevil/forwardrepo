from pyrogram import Client, filters
import pyromod.listen
bot = Client('Forward bot', api_id= "1543212", api_hash= "d47de4b25ddf79a08127b433de32dc84", session_string= "BAAXjCwATVa3sVVvl3k-DW0pPjAyuTw8oH0hrHeu7ZA_x6yIhcynBUR87BHq3TQClack4i8dw4DuOkm2TDQFI5XaKgAd6kQ1_6ypNEdkm-3xEHMsotWEJhkUhzoja8V8990b7HMgucAj0H8nd689LT9lTrUvS7De5CCEy1Au3hDtiO-yUhrWjhid4SlGLVFTfy9PP_Wb7c8z5WMVbux2ep6VMxccvASXnFjJ2zTnuWY7Ma6URyzgKUkD43Aqy0d7KIpL_5kDGDTO2lUs_wRrrdKa8mj9y3-JttMY5-cc3DPbQF3OPHWIUJsgRFxamNan4fTPPg0kxr2aHnM8819HLbuqGlIxBQAAAABYHfJiAA")
import time

@bot.on_message(filters.command('forward'))
async def start(bot, message):
 # start_msg = await bot.ask(text = "Send The Start Message ID", chat_id = message.from_user.id, filters=filters.text, timeout=30)
 # end_msg = await bot.ask(text = "Send The End Message ID", chat_id = message.from_user.id, filters=filters.text, timeout=30)
 # bot.send_message(f'{start_msg} ,{end_msg}')
  await bot.send_message(message.from_user.id,f"Forwading Started")

  try:
    for i in range(1783, 4166):
      await bot.copy_message(chat_id=-1001525314409, from_chat_id= -1001260881403,message_id=i)
      time.sleep(5)
  except:
       pass
bot.run()
