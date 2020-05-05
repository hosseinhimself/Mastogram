'''
This work is licensed under a Creative Commons Attribution-ShareAlike 4.0 International License.
Link: https://creativecommons.org/licenses/by-sa/4.0/

You are free to:
        Share: copy and redistribute the material in any medium or format
        Adapt: remix, transform, and build upon the material for any purpose, even commercially.
        The licensor cannot revoke these freedoms as long as you follow the license terms.

Under the following terms:
        Attribution: You must give appropriate credit, provide a link to the license, and indicate if changes were made. You may do so in any reasonable manner, but not in any way that suggests the licensor endorses you or your use.
        ShareAlike: If you remix, transform, or build upon the material, you must distribute your contributions under the same license as the original.
        No additional restrictions: You may not apply legal terms or technological measures that legally restrict others from doing anything the license permits.

Notices:
        You do not have to comply with the license for elements of the material in the public domain or where your use is permitted by an applicable exception or limitation.
        No warranties are given. The license may not give you all of the permissions necessary for your intended use. For example, other rights such as publicity, privacy, or moral rights may limit how you use the material.
'''


import config as cfg
import logging
import telegram
from telegram import ReplyKeyboardMarkup
from telegram.error import NetworkError, Unauthorized
from time import sleep
from mastodon import Mastodon

update_id = None

def createmastodonapp(appname , baseurl , email , password ):
    Mastodon.create_app(
        appname,
        api_base_url=baseurl,
        to_file='pytooter_clientcred.secret'
    )
    # Then login. This can be done every time, or use persisted.
    mastodon = Mastodon(
        client_id='pytooter_clientcred.secret',
        api_base_url=baseurl
    )
    mastodon.log_in(
        email,
        password,
        to_file='pytooter_usercred.secret'
    )

def sendtoot(text):
    mastodon = Mastodon(
        access_token='pytooter_usercred.secret',
        api_base_url=cfg.instance
    )

def notifications():
    notiflist=[]
    mastodon = Mastodon(
        access_token='pytooter_usercred.secret',
        api_base_url=cfg.instance
    )
    for i in range(0, 10):
        p = mastodon.notifications()[i]
        numberid = str(p['account']['id'])
        id = str(p['account']['url'])
        name = str(p['account']['display_name'])
        if ':verified:' in name:
            name = name.replace(":verified:", "✅")
        type = str(p['type'])
        if type == 'mention':
            inreplytoid = str(p['status']['in_reply_to_id'])
            content = str(p['status']['content'])
        else:
            inreplytoid = 'None'
            content = 'None'
        sendittouser = 'type of notifcation: ' + type + '\n' + 'id: ' + id + '\n' + 'numberid: ' + numberid + '\n' + 'name: ' + name + '\n' + 'replyid: ' + inreplytoid + '\n' + 'content: ' + content
        notiflist.append(sendittouser)
    return notiflist

def main():
    a=0
    createmastodonapp(cfg.Appname , cfg.instance , cfg.Youremail , cfg.Password)
    global update_id
    bot = telegram.Bot(cfg.Bottoken)
    try:
        update_id = bot.get_updates()[0].update_id
    except IndexError:
        update_id = None
    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    while True:
        try:
            if a==1 :
                a=BOT(bot , 1)
            else:
                a = BOT(bot, 0)
        except NetworkError:
            sleep(1)
        except Unauthorized:
            update_id += 1


def BOT(bot , sendtootflag):
    global update_id
    update_dict = bot.get_updates(offset=update_id, timeout=10)
    for update in update_dict:
        update_id = update.update_id + 1
        if update.message:
            chatid = update.message.chat.id
            print(chatid)
            if chatid == cfg.yourchatid:
                if update.message.text == '/start':
                    WelcomeText = []
                    reply_keyboard = [['Send Toot'],
                                      ['Notifications'],
                                      ['About ArakLUG', 'License']]
                    markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)
                    update.message.reply_text('Welcome To Mastodon, Choose your Command',reply_markup = markup)
                    sendtootflag = 0

                elif update.message.text == 'License':
                    License='This work is licensed under a Creative Commons Attribution-ShareAlike 4.0 International License.\n\nLink: https://creativecommons.org/licenses/by-sa/4.0/'
                    update.message.reply_text(License)
                    sendtootflag = 0

                elif update.message.text == 'About ArakLUG':
                    aboutlug='🐧ArakLUG:\n🌐Website: araklug.ir\n🔘Telegram Channel: @arak_lug\n🔘Mastodon: @araklug@mastodon.social\n🔘Twitter and Instagram: @arak_lug\n\n🔵Developed By : Hossein Mohseni ( @hosseinhimself )'
                    update.message.reply_text(aboutlug)
                    sendtootflag = 0

                elif update.message.text=='Notifications':
                    notifs=notifications()
                    for flag in range(len(notifs)):
                       update.message.reply_text(notifs[flag])
                    sendtootflag = 0
                elif update.message.text=='Send Toot':
                    update.message.reply_text("What's on your mind?")
                    sendtootflag = 1
                else:
                    if sendtootflag == 1:
                        toot = update.message.text
                        sendtoot(toot)
                        sendtootflag = 0
    return sendtootflag

if __name__ == '__main__':
    main()