# telegram bot
[資料來源](https://pixnashpython.pixnet.net/blog/post/32391757-%E3%80%90telegram-api%E3%80%91python%E6%89%93%E9%80%A0telegrame%E6%A9%9F%E5%99%A8%E4%BA%BA%E6%89%8B%E6%8A%8A%E6%89%8B%E6%95%99)


## 設定TOKEN及初始化BOT
> Updater更新者可以依照你給的TOKEN取得Telegram上的所有事件，包含誰對你的機器人發訊息、訊息內容等等所有事件，如果把機器人丟進群組一樣會取得群組內的事件狀況。
:::warning
* token
API Token 由組織中的使用者核發，並與使用者的帳戶以及從中產生 API Token 的組織相關聯。OAuth 應用程式由組織中的使用者建立後，便充當伺服器與伺服器互動中的實體，並且可以在多個組織中使用。只有建立 API Token 的使用者才可以管理這些 Token。OAuth 應用程式的擁有者是建立該應用程式所在的組織，作為組織擁有者或具有開發人員角色的組織成員的使用者可管理該應用程式。 
[來源](https://ithelp.ithome.com.tw/articles/10237588)
:::

```py=
# 匯入相關套件
from telegram.ext import Updater # 更新者
from telegram.ext import CommandHandler, CallbackQueryHandler # 註冊處理 一般用 回答用
from telegram.ext import MessageHandler, Filters # Filters過濾訊息
from telegram import InlineKeyboardMarkup, InlineKeyboardButton # 互動式按鈕

# 設定 token
token = '填入你剛取得的TOKEN'

# 初始化bot
updater = Updater(token=token, use_context=False)
```
## 設定一個dispatcher(調度器)
>dispatcher(調度器)像是一個調度者，它的功用就是處理你有定義的handler，handler是你等等要定義的對事件的處理方式。
```py=
#設定一個dispatcher(調度器)
dispatcher = updater.dispatcher
```
## 新增handler並加入dispatcher
>定義一個handler叫做start，當機器人收到 /start 指定時，就要去進行start方法裡面的動作。
我們先定義出start方法而後藉由CommandHandler跟指令/start做綁定。
而後使用dispatcher.add_handler把一個handler加入我們的dispatcher(調度器)。
如此一來我們只要輸入/start 機器人就會回答HI + 發送訊息群組或個人的ID

```py=
# 定義收到訊息後的動作(新增handler)
def start(bot, update): # 新增指令/start
    message = update.message
    chat = message['chat']
    update.message.reply_text(text='HI  ' + str(chat['id']))    

dispatcher.add_handler(CommandHandler('start', start))
```
:::warning
```py=
print(update)
```
>最後來看一下我們可以藉由update中的可以取得哪些訊息，你可以在start的函數中加上print(update)看一下，這樣才知道我們的回覆需要用到那些資訊。

>chat與from最大的差別在，一個是指取得對方是從何個群組發動訊息給機器人，也就是說如果是以直接對機器人發訊息chat與from會是一樣的，但如果機器人在某群組，則chat取得群組資料，from取得群組裡發送訊息的人資訊。
:::
>在我們的範例中，我先對update取得message取得訊息後，在繼續往下找我所需要的訊息。
最後找到message下chat下的id大家可以跟我用一樣的方法，比較好理解。
update.message.reply_text則用這個方法把我們的訊息回覆出去。
```py=
# 定義收到訊息後的動作(新增handler)
def start(bot, update): # 新增指令/start
    message = update.message
    chat = message['chat']
    update.message.reply_text(text='HI  ' + str(chat['id'])) 
```
## 開始運作Telegram Bot
>讓Telegram Bot運轉起來，updater.start_polling()就可以使機器人運作。
updater.idle()這行帶入的話，則在開始運作後你無法對機器人做任何動作，例如對指定人發訊，但其實updater.start_polling()已經讓你的機器人開始上線瞜。
```py=
# 開始運作bot
updater.start_polling()


# 待命 若要停止按Ctrl-C 就好
#updater.idle()


# 離開
#updater.stop()
```
## 對指定對象發話
# 發指定對象訊息
>使用dispatcher.bot.send_message方法就可以把訊息藉由機器人送到某人、或聊天室。
這個id是chat的id可以藉由上面update中取得。
```py=
who = '對象ID, '
text = '我是機器人可以問我問題喔!'
dispatcher.bot.send_message(chat_id=who, text=text) # 發送訊息
```
## 回答非指定或其他種問題(回答不是/ 指令 問題)
>使用from telegram.ext import MessageHandler,Filters，
Filters.text意思是如果聊天端發送的訊息是文字就是True，而後藉由MessageHandler來與我們定義的echo連結，最後使用dispatcher.add_handler加入調度器。
```py=
from telegram.ext import MessageHandler, Filters # Filters過濾訊息

def echo(bot, update): # 其他訊息
    message = update.message
    text = message.text + '  <<< 這個部份我就不太懂了~'
    update.message.reply_text(text=text)

dispatcher.add_handler(MessageHandler(Filters.text, echo)) # Filters如果是文字就呼叫echo
```
## 回答選單
>使用InlineKeyboardMarkup, InlineKeyboardButton來建立回答的是按鈕，使用方式如程式碼所述。
```py=
from telegram import InlineKeyboardMarkup, InlineKeyboardButton # 互動式按鈕

def blog(bot, update): # /btc 互動式按鈕
    update.message.reply_text('量化交易中心',
                              reply_markup = InlineKeyboardMarkup([[
                                  InlineKeyboardButton('恩哥Python量化教室', 
                                                       url = 'https://pixnashpython.pixnet.net/blog'),
                                  InlineKeyboardButton('你的網路生活教授Nash', 
                                                       url = 'https://pixnashlife.pixnet.net/blog')
                                  ]])
                              )
dispatcher.add_handler(CommandHandler('blog', blog))
```
## 與機器人選單問與答
>先建立問題及回答問題的方式如下面定義的question及answer方法，最後question使用CommandHandler綁定 /question，answer使用CallbackQueryHandler綁定，就可以取得對方按下按鈕後的資訊，並且去做處理。
callback_query取得對方按下的資訊，哪個按鈕、按鈕內容等，用callback_query.edit_message_text把資訊回覆出去。

```py=
from telegram.ext import CommandHandler, CallbackQueryHandler # 註冊處理 一般用 回答用
from telegram import InlineKeyboardMarkup, InlineKeyboardButton # 互動式按鈕

# 定義問題
qt = {
    'Q1': '你是誰?',
    'Q2': '有新文章嗎?',
    'Q3': '今天會下雨嗎?'
        } 

# 問題以選單方式提出
def question(bot, update):
    update.message.reply_text('你問我答',
        reply_markup = InlineKeyboardMarkup([[
                InlineKeyboardButton(qt, callback_data = name) for name, qt in qt.items()
            ]]))

# 回答問題  
def answer(bot, update):
    yours = update.callback_query.data # 一樣從update中抽取資料
    update.callback_query.edit_message_text(text=yours)


dispatcher.add_handler(CommandHandler('question', question)) # 問題
dispatcher.add_handler(CallbackQueryHandler(answer)) # 回答問題
```

## 完整程式碼
```py=
# pip install python-telegram-bot
# telegram.__version__ = 13.3
from telegram.ext import Updater # 更新者
from telegram.ext import CommandHandler, CallbackQueryHandler # 註冊處理器 一般用 回答用
from telegram.ext import MessageHandler, Filters # Filters過濾訊息
from telegram import InlineKeyboardMarkup, InlineKeyboardButton # 互動式按鈕
#import telegram


# 設定 token
token = '你的機器人TOKEN'

# 初始化bot
updater = Updater(token=token, use_context=False)


# 設定一個dispatcher(調度器)
dispatcher = updater.dispatcher


# 定義收到訊息後的動作(新增handler)
def start(bot, update): # 新增指令/start
    message = update.message
    chat = message['chat']
    update.message.reply_text(text='HI  ' + str(chat['id']))    
    

def blog(bot, update): # /btc 互動式按鈕
    update.message.reply_text('量化交易中心',
                              reply_markup = InlineKeyboardMarkup([[
                                  InlineKeyboardButton('恩哥Python量化教室', 
                                                       url = 'https://pixnashpython.pixnet.net/blog'),
                                  InlineKeyboardButton('你的網路生活教授Nash', 
                                                       url = 'https://pixnashlife.pixnet.net/blog')
                                  ]])
                              )
qt = {
    'Q1': '你是誰?',
    'Q2': '有新文章嗎?',
    'Q3': '今天會下雨嗎?'
        } 

def question(bot, update):
    update.message.reply_text('你問我答',
        reply_markup = InlineKeyboardMarkup([[
                InlineKeyboardButton(qt, callback_data = name) for name, qt in qt.items()
            ]]))
    
def answer(bot, update):
    yours = update.callback_query.data # 一樣從update中抽取資料
    update.callback_query.edit_message_text(text=yours)


def echo(bot, update): # 其他訊息
    message = update.message
    text = message.text + '  <<< 這個部份我就不太懂了~'
    update.message.reply_text(text=text)
    

# 把handler加入dispatcher()
dispatcher.add_handler(CommandHandler('start', start))
dispatcher.add_handler(CommandHandler('blog', blog))
dispatcher.add_handler(CommandHandler('question', question)) # 問題
dispatcher.add_handler(CallbackQueryHandler(answer)) # 回答問題
dispatcher.add_handler(MessageHandler(Filters.text, echo)) # Filters如果是文字就呼叫start


# 發指定對象訊息
who = '對象ID, '
text = '我是機器人可以問我問題喔!'
dispatcher.bot.send_message(chat_id=who, text=text) # 發送訊息


# 開始運作bot
updater.start_polling()


# 待命 若要停止按Ctrl-C 就好
#updater.idle()


# 離開
#updater.stop()
```


