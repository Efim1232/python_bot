from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

button_case_admin=ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)

button_case_admin.add(KeyboardButton('/Загрузить_новый_урок'))
 
button_case_admin1=ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
button_case_admin1.add(KeyboardButton('/lightroom')).add(KeyboardButton('/Photoshop')).add(KeyboardButton('/Выход'))