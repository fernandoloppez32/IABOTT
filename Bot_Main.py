import requests,os,time
from aiogram import *
from aiogram.types import ParseMode

tk = Bot('6277337687:AAHaYOU-6hPVn7UctOGbtOPwYNGQK0wUBS0')
rex = Dispatcher(tk)

@rex.message_handler(commands='start')
async def start(msg):
    h1 = await msg.reply('<b>¡ IA ! - Online Server...</b>',ParseMode.HTML)
    time.sleep(2)
    h2 = await h1.edit_text('<b>Ia configurarda correctamente. ✅</b>',ParseMode.HTML)
    time.sleep(2)
    name = msg['from']['first_name']
    await h2.edit_text(f'<b>Wellcome mr <code>{name}</code>.</b>',ParseMode.HTML)


@rex.message_handler(lambda message:True)
async def iaB(msg):
    h1 = await msg.reply('<b>Okey, Buscando respuestas..</b>',ParseMode.HTML)
    reqS = requests.get(f'https://gptzaid.zaidbot.repl.co/1/text={msg.text}').text
    await h1.edit_text(reqS, ParseMode.MARKDOWN)


if __name__ == '__main__':
    os.system('cls')
    print('Starting: _Onli')
    executor.start_polling(rex)

