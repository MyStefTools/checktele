import telebot,requests

bot = telebot.TeleBot('1713857348:AAHL351O-bhrRV-nu-kHCxTatSkp3J1ERCc')

@bot.message_handler(commands=['start'])

def start(message):

    markup = telebot.types.InlineKeyboardMarkup()

    button1 = telebot.types.InlineKeyboardButton(text ='By',url = 'https://t.me/i55i9')

    markup.add(button1)

    bot.send_message(message.chat.id,'Send Email To Rest Instagram',reply_markup=markup)

    @bot.message_handler(func=lambda message:True)

    def rest(message):

        markup1 = telebot.types.InlineKeyboardMarkup()

        button2 = telebot.types.InlineKeyboardButton(text ='كايدن',url = 'https://t.me/mm888xx')

        markup1.add(button2)

        messages=(message.text)

        url = 'https://i.instagram.com/api/v1/accounts/send_password_reset/'

        headers = {

    'authority': 'www.instagram.com',

    'accept': '*/*',

    'accept-language': 'ar',

    'content-type': 'application/x-www-form-urlencoded',

    'cookie': 'csrftoken=vEG96oJnlEsyUWNS53bHLkVTMFYQKCBV; ig_did=5D80D38A-797B-482D-A407-4B51217E09E7; ig_nrcb=1; mid=ZEqtPgALAAE-IVt6zG-ZazKzI4qN; datr=jrJKZGOaV4gHwa-Znj2QCVyB',

    'origin': 'https://www.instagram.com',

    'referer': 'https://www.instagram.com/accounts/password/reset/?next=%2Faccounts%2Flogout%2F',

    'sec-ch-prefers-color-scheme': 'light',

    'sec-ch-ua': '"Chromium";v="112", "Google Chrome";v="112", "Not:A-Brand";v="99"',

    'sec-ch-ua-mobile': '?0',

    'sec-ch-ua-platform': '"Windows"',

    'sec-fetch-dest': 'empty',

    'sec-fetch-mode': 'cors',

    'sec-fetch-site': 'same-origin',

    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36',

    'viewport-width': '1261',

    'x-asbd-id': '198387',

    'x-csrftoken': 'vEG96oJnlEsyUWNS53bHLkVTMFYQKCBV',

    'x-ig-app-id': '936619743392459',

    'x-ig-www-claim': '0',

    'x-instagram-ajax': '1007389883',

    'x-requested-with': 'XMLHttpRequest'}

        data ={

    "user_email": messages

    }

        response = requests.post(url, headers=headers,data=data)

        res = response.text

        if 'no-js not-logged-in' in res:

        	print('Bad Email :'+messages)        if 'minute' in res:

         	bot.send_message(message.chat.id,text=f"Wait ! \nSend /start And Try Again",reply_markup=markup1)

         	print('Wait minute :'+messages)

        else:

        	print(res)

        try:

        	bot.send_message(message.chat.id,text=f"Done Send Rest \nStatus Rest :{res}",reply_markup=markup1)

        except:

        	bot.send_message(message.chat.id,text=f"Bad Email ! \nSend /start And Try Again",reply_markup=markup1)

while True:

        bot.polling(none_stop=True)
