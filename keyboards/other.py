from aiogram import  types, Dispatcher
from create_bot import dp




async def command_start(message: types.Message):
		await bot.send_message(message.from_user.id,'Добрый день! Я бот созданный помочь тебе в освоении навыков видеомантожа.',reply_markup=kb_client)
		await message.delete()
	



def register_handlers_other(dp : Dispatcher):

	dp.register_message_handler(command_start, commands=['start'])