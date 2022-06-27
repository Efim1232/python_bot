from aiogram import  types, Dispatcher
from create_bot import dp, bot
from keyboards import kb_client, k_menu
from aiogram.types import ReplyKeyboardRemove
from data_base import sqlite_db



async def command_start(message: types.Message):
	
	await bot.send_message(message.from_user.id,'Добрый день! Я бот созданный помочь тебе в освоении навыков видеомантожа.',reply_markup=kb_client)
	await message.delete()
	

async def command_menu(message: types.Message):
	
	await bot.send_message(message.from_user.id,'Меню',reply_markup=k_menu)
	await message.delete()


async def command_lesson1(message: types.Message):
	await sqlite_db.sql_read1(message)
	await  bot.send_message(message.from_user.id,'Возврат в меню',reply_markup=k_menu)



async def command_lesson2(message: types.Message):
	await sqlite_db.sql_read2(message)
	await  bot.send_message(message.from_user.id,'Возврат в меню',reply_markup=k_menu)


async def command_test1(message: types.Message):

	await  bot.send_message(message.from_user.id,'t.me/QuizBot?start=d127798Z',reply_markup=k_menu)
	await message.delete()



async def command_test2(message: types.Message):

	await  bot.send_message(message.from_user.id,'t.me/QuizBot?start=ZobSPJO1',reply_markup=k_menu)
	await message.delete()




async def command_help(message: types.Message):
	
	await bot.send_message(message.from_user.id,'Для использования бота используйте интерактивные кнопочки.',reply_markup=kb_client)
	await message.delete()

def register_handlers_client(dp : Dispatcher):

	dp.register_message_handler(command_start, commands=['start','Выход'])
	dp.register_message_handler(command_menu, commands=['Меню'])
	dp.register_message_handler(command_help, commands=['Помощь'])
	dp.register_message_handler(command_lesson1, commands=['Уроки_lightroom'])
	dp.register_message_handler(command_lesson2, commands=['Уроки_по_фотошопу'])
	dp.register_message_handler(command_test1, commands=['Тест_по_теме_lightroom'])
	dp.register_message_handler(command_test2, commands=['Тест_по_теме_фотошоп'])
