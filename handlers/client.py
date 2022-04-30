from aiogram import  types, Dispatcher
from create_bot import dp, bot
from keyboards import kb_client


async def command_start(message: types.Message):
	#try:
		await bot.send_message(message.from_user.id,'Добрый день! Я бот созданный помочь тебе в освоении навыков видеомантожа.',reply_markup=kb_client)
		await message.delete()
	

async def command_menu(message: types.Message):
	#try:
		await bot.send_message(message.from_user.id,'меню',reply_markup=kb_client)
		await message.delete()

async def command_help(message: types.Message):
	#try:
		await bot.send_message(message.from_user.id,'краткое руковдство по использованию бота.',reply_markup=kb_client)
		await message.delete()

def register_handlers_client(dp : Dispatcher):

	dp.register_message_handler(command_start, commands=['start'])
	dp.register_message_handler(command_menu, commands=['Меню'])
	dp.register_message_handler(command_help, commands=['Помощь'])