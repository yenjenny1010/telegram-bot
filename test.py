# pip install python-telegram-bot
# telegram.__version__ = 13.3
from telegram.ext import Updater # 更新者
from telegram.ext import CommandHandler, CallbackQueryHandler # 註冊處理器 一般用 回答用
from telegram.ext import MessageHandler, Filters # Filters過濾訊息
from telegram import InlineKeyboardMarkup, InlineKeyboardButton # 互動式按鈕
import time
#import telegram


# 設定 token
token = '1834735572:AAHKCT_-Jv6XNKMt704guggO2fkqbvFQaco'

# 初始化bot
updater = Updater(token=token, use_context=False)


# 設定一個dispatcher(調度器)
dispatcher = updater.dispatcher


# 定義收到訊息後的動作(新增handler)
def start(bot, update): # 新增指令/start
    message = update.message
    chat = message['chat']
    update.message.reply_text(text='HI  ' + "阿嬤你好")    
    update.message.reply_text(text="輸入這次全部的電費 第一間的度數 第二間的度數 第三間的度數")
    time.sleep(5)
    message = update.message
    totla_cost = message.text 




def echo(bot, update): # 其他訊息
    
    message = update.message.text
    text =message 
    text = text.split(' ')
    totalcost=text[0]
    onedegree=text[1]
    twodegree=text[2]
    threedegree=text[3]
    totalcost=eval(totalcost)
    onedegree=eval(onedegree)
    twodegree=eval(twodegree)
    threedegree=eval(threedegree)
    totaldegree=onedegree+twodegree+threedegree
    onecost=totalcost*(onedegree/totaldegree)
    twocost=totalcost*(twodegree/totaldegree)
    threecost=totalcost*(threedegree/totaldegree)
    text="第一間"+str(onecost)+"第二間"+str(twocost)+"第三間"+str(threecost)
    update.message.reply_text(text=text)
    print(update)

# 把handler加入dispatcher()
dispatcher.add_handler(CommandHandler('start', start))
dispatcher.add_handler(MessageHandler(Filters.text, echo)) # Filters如果是文字就呼叫start





# 開始運作bot
updater.start_polling()


# 待命 若要停止按Ctrl-C 就好
#updater.idle()


# 離開
#updater.stop()