from aiogram import  types, Dispatcher
from create_bot import dp





async def echo_send(messange : types.Message):
	
	await message.answer(message.text)
#	await message.reply(message.text)
#	await message.answer(message.text)

def register_handlers_other(dp : Dispatcher):
	dp.register_message_handler(echo_send)