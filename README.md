**What exactly does this project do?**

این اسکریپت برای اتصال یک بات تلگرام به اکانت ماستودون نوشته شده. شما در این بات میتونین اطلاعات ورود مربوط به اکانت ماستودون خودتون رو وارد کنید و اکانت خودتونو مدیریت کنید 

(البته فعلا فقط قابلیت دریافت نوتیفیکیشن ها و ارسال بوق وجود داره. بقیه قابلیت ها به زودی اضافه خواهد شد.)

لازم به ذکره که باید این اسکریپت رو روی سرور یا هاست شخصی و با بات تلگرامی که خودتون تعریف کردید پیاده کنید.

**Requirements**
* Mastodon.py
* python-telegram-bot

**How to run**
* pip install -r requirements.txt
* Enter Your informations to "config.py"

**Get your Telegram chat ID**

Paste the following link in your browser. Replace "<API-access-token>" with the API access token:

    https://api.telegram.org/bot<API-access-token>/getUpdates?offset=0
    
Send a message to your bot in the Telegram application. The message text can be anything. Your chat history must include at least one message to get your chat ID.
Refresh your browser.
Identify the numerical chat ID by finding the id inside the chat JSON object.

In the example below, the chat ID is 123456789..

```
{  
   "ok":true,
   "result":[  
      {  
         "update_id":XXXXXXXXX,
         "message":{  
            "message_id":2,
            "from":{  
               "id":123456789,
               "first_name":"Mushroom",
               "last_name":"Kap"
            },
            "chat":{  
               "id":123456789,
               "first_name":"Mushroom",
               "last_name":"Kap",
               "type":"private"
            },
            "date":1487183963,
            "text":"hi"
         }
      }
   ]
}
```
