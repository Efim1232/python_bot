from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram import types, Dispatcher
from create_bot import dp,bot
from aiogram.dispatcher.filters import Text

ID=None
class FSMAdmin(StatesGroup):
	photo = State()
	name = State()

#Получаем ID текущего модератора
async def make_changes_command(message:types.Message):
	global ID 
	ID=message.from_user.id
	await bot.send_message(message.from_user.id,'Что требуется хозяин?'), #reply_markup=button_case_admin),
	await message.delete()


	#Начало диалога с Админом
async def cm_start(message: types.Message):
	if message.from_user.id==ID:
		await FSMAdmin.photo.set()
		await message.reply('Загрузи фото')

		#Выход из состояний
async def cancel_handler(message: types.Message, state :FSMContext):
	if message.from_user.id==ID:
			current_state = await state.get_state()
			if current_state is None:
				return
				await state.finish()
				await message.reply("Ок")

	
	#Ловим первый ответ и пишем в словарь
	
async def load_photo(message: types.Message, state:FSMContext):
		if message.from_user.id==ID:
			async with state.proxy() as data:
			
				data['photo'] = messege.photo[0].file_id
			await FSMAdmin.next()
			await message.reply('Теперь введи название')

		#Ловим второй ответ
async def load_name(message: types.Message, state: FSMContext):
			async with state.proxy() as data:
				data['name'] = messege.text
		




		
		
def register_handlers_admin(dp : Dispatcher):
	dp.register_message_handler(cm_start,commands=['Загрузить'],state=None)
	dp.register_message_handler(cancel_handler,state="*",commands='отмена')
	dp.register_message_handler(cancel_handler,Text(equals='отмена',ignore_case=True), state="*")
	dp.register_message_handler(load_photo,content_types=['photo'], state=FSMAdmin.photo)
	dp.register_message_handler(load_name,state=FSMAdmin.name)
	dp.register_message_handler(make_changes_command,commands=['moderator'],is_chat_admin=True)