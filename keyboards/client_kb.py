from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

b1= KeyboardButton('/Меню')
b2= KeyboardButton('/Помощь')

kb_client = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)

kb_client.add(b1).add(b2)

k_menu=ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
k_menu.add(KeyboardButton('/Уроки_lightroom')).add(KeyboardButton('/Уроки_по_фотошопу')).add(KeyboardButton('/Тест_по_теме_lightroom')).add(KeyboardButton('/Тест_по_теме_фотошоп')).add(KeyboardButton('/Выход'))


#button_case_admin= ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)