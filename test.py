# 匯入相關套件
from telegram.ext import Updater # 更新者
from telegram.ext import CommandHandler, CallbackQueryHandler # 註冊處理 一般用 回答用
from telegram.ext import MessageHandler, Filters # Filters過濾訊息
from telegram import InlineKeyboardMarkup, InlineKeyboardButton # 互動式按鈕

# 設定 token
token = '1766520232:AAH3mVMifGHjUqPPb38YjdCXn2vLfHXp7aA'

# 初始化bot
updater = Updater(token=token, use_context=False)

# 設定一個dispatcher(調度器)
dispatcher = updater.dispatcher

# 定義收到訊息後的動作(新增handler)
def start(bot, update): # 新增指令/start
    message = update.message
    chat = message['chat']
    update.message.reply_text(text='HI  ' + str("媽媽妳好"))
    print(update)    

dispatcher.add_handler(CommandHandler('start', start))

# 定義收到訊息後的動作(新增handler)
def start(bot, update): # 新增指令/start
    message = update.message
    chat = message['chat']
    update.message.reply_text(text='HI  ' + str(chat['id']))  

# 開始運作bot
updater.start_polling()


# 待命 若要停止按Ctrl-C 就好
#updater.idle()


# 離開
#updater.stop()