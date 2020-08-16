**What exactly does this project do?**
This script was written to connect a telegram bot to a Mastodon account. In this bot, you must enter the login information of your Mastodon account.

(But now there is only the ability to receive notifications and send toots. Other features will be added ASAP.)

You must run this script on a personal server or host with the Telegram bot that you defined.

**Requirements**
* Mastodon.py
* python-telegram-bot

**How to run**
* pip install -r requirements.txt
* Enter Your informations to "config.py"

**Get your Telegram chat ID**

Paste the following link in your browser. Replace "API-access-token" with the API access token:

    https://api.telegram.org/botAPI-access-token/getUpdates?offset=0
    
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
