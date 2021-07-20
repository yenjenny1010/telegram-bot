from telegram.ext import Updater  # 更新者
from telegram.ext import CommandHandler, CallbackQueryHandler  # 註冊處理器 一般用 回答用
from telegram.ext import MessageHandler, Filters  # Filters過濾訊息
from telegram import InlineKeyboardMarkup, InlineKeyboardButton  # 互動式按鈕
from random import randint
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler
from telegram import InlineKeyboardMarkup, InlineKeyboardButton
# 設定 token
token = '1834735572:AAHKCT_-Jv6XNKMt704guggO2fkqbvFQaco'

# 初始化bot
updater = Updater(token=token, use_context=False)
dispatcher = updater.dispatcher


def start(bot, update):
    a, b = randint(1, 100), randint(1, 100)
    update.message.reply_text('{} + {} = ?'.format(a, b),
                              reply_markup=InlineKeyboardMarkup([[
                                  InlineKeyboardButton(str(s), callback_data='{} {} {}'.format(a, b, s)) for s in range(a + b - randint(1, 3), a + b + randint(1, 3))
                              ]]))


def answer(bot, update):
    a, b, s = [int(x) for x in update.callback_query.data.split()]
    if a + b == s:
        update.callback_query.edit_message_text('你答對了！')
    else:
        update.callback_query.edit_message_text('你答錯囉！')


updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CallbackQueryHandler(answer))

updater.start_polling()
updater.idle()
