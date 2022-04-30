from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

b1= KeyboardButton('/Меню')
b2= KeyboardButton('/Помощь')
b3= KeyboardButton('/start')
#b4= KeyboardButton('/отмена')
#b5= KeyboardButton('/photo')



kb_client = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)

kb_client.add(b3).add(b1).add(b2)


#button_case_admin= ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)