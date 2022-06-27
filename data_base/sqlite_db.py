import sqlite3 as sq
from create_bot import bot

def sql_start():
	global base, cur
	base = sq.connect('bot_cool.db')
	cur = base.cursor()
	if base:
		print('База данных успешно подключена')
	base.execute('CREATE TABLE IF NOT EXISTS menu1(link TEXT , name TEXT PRIMARY KEY)')
	base.execute('CREATE TABLE IF NOT EXISTS menu2(link TEXT , name TEXT PRIMARY KEY)')
	base.commit()
	

async def sql_add_command1(state):
	async with state.proxy() as data:
		cur.execute('INSERT INTO menu1 VALUES (?,?)', tuple(data.values() ) )
		base.commit()

async def sql_add_command2(state):
	async with state.proxy() as data:
		cur.execute('INSERT INTO menu2 VALUES (?,?)', tuple(data.values() ) )
		base.commit()

async def sql_read1(message):
	for ret in cur.execute('SELECT  * FROM menu1').fetchall():
		await bot.send_message(message.from_user.id,f' {ret[1]} \n , {ret[0]} \n ')

async def sql_read2(message):
	for ret in cur.execute('SELECT  * FROM menu2').fetchall():
		await bot.send_message(message.from_user.id, f'{ret[1]} \n , {ret[0]} \n ')
