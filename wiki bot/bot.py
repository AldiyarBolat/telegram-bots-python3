import telebot
import requests
import html2text

bot = telebot.TeleBot('926676977:AAEXr4VQxLIaGfA1pBOdtSL0aB70iWlfX8Y')


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Hello i am an Wikipedia bot, you can ask me for anything you want, type a word...')


@bot.message_handler(content_types=['text'])
def send_text(message):
    title = message.text.lower()
    msg = find_article_in_wiki(title)
    bot.send_message(message.chat.id, msg[:3000] + '\n\n' + 'see more in wikipedia.org')


def find_article_in_wiki(title):
    URL = "https://en.wikipedia.org/w/api.php"
    PARAMS = {'format': 'json', 'action': 'query', 'prop': 'extracts', 'redirects': 1, 'titles': title}

    r = requests.get(url=URL, params=PARAMS)
    data = r.json()

    tmp = data['query']
    a = (tmp['pages'])
    for key in a:
        t = a[key]
        html = (t['extract'])

        return html2text.html2text(html)


bot.polling()
