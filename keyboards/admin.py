from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram import types, Dispatcher
from create_bot import dp,bot
from aiogram.dispatcher.filters import Text
from data_base import sqlite_db
from keyboards import button_case_admin,button_case_admin1
ID=None
class FSMAdmin(StatesGroup):
	link1=State()
	name1 = State()
	link2=State()
	name2 = State()
#Получаем ID текущего модератора
async def make_changes_command(message:types.Message):
	global ID 
	ID=message.from_user.id
	await bot.send_message(message.from_user.id,'Что мне сделать?', reply_markup=button_case_admin)
	await message.delete()


	#Начало диалога с Админом
async def cm_start(message: types.Message):
	if message.from_user.id==ID:
		await message.reply('Выбери тему',reply_markup=button_case_admin1)

#Вход в машину состояний в зависимости от темы

async def cm_start2(message: types.Message):
	
		await FSMAdmin.link1.set()
		await message.reply('Загрузи ссылку на урок')

async def load_link1(message: types.Message, state:FSMContext):
	
		async with state.proxy() as data:
			data['link1'] = message.text
		await FSMAdmin.next()
		await message.reply('Теперь введи название')



async def load_name1(message: types.Message, state: FSMContext):
	
		async with state.proxy() as data:
			data['name1'] = message.text
		await sqlite_db.sql_add_command1(state)
		await state.finish()
		await message.reply('Загрузка данных успешно прошла. Возврат в меню',reply_markup=button_case_admin)
			



	
	

async def cm_start3(message: types.Message):

		await FSMAdmin.link2.set()
		await message.reply('Загрузи ссылку на урок')

async def load_link2(message: types.Message, state:FSMContext):
	
		async with state.proxy() as data:
			data['link2'] = message.text
		await FSMAdmin.next()
		await message.reply('Теперь введи название')



async def load_name2(message: types.Message, state: FSMContext):
	
		async with state.proxy() as data:
			data['name2'] = message.text
		await sqlite_db.sql_add_command2(state)
		await state.finish()
		await message.reply('Загрузка данных успешно прошла. Возврат в меню',reply_markup=button_case_admin)
			



		#Выход из состояний
async def cancel_handler(message: types.Message, state :FSMContext):
		
			current_state = await state.get_state()
			if current_state is None:
					return
			await state.finish()
			await message.reply("Вы вышли из панели админа")
			
			

	
	#Ловим первый ответ и пишем в словарь
	

		

#После ловим последний ответ/



	




		
		
def register_handlers_admin(dp : Dispatcher):
	dp.register_message_handler(cm_start,commands=['Загрузить_новый_урок'],state=None)
	dp.register_message_handler(cm_start2,commands=['lightroom'],state=None)
	dp.register_message_handler(cm_start3,commands=['Photoshop'],state=None)
	dp.register_message_handler(cancel_handler,commands=['Выход'],state="*")
	dp.register_message_handler(load_link1,state=FSMAdmin.link1)
	dp.register_message_handler(load_link2,state=FSMAdmin.link2)
	dp.register_message_handler(load_name2,state=FSMAdmin.name2)
	dp.register_message_handler(load_name1,state=FSMAdmin.name1)
	dp.register_message_handler(make_changes_command,commands=['moderator'],is_chat_admin=True)