import main
import telebot
from random import randint
from telebot.types import Message

token = '5321872607:AAHlVsZ1cCQvuSGQMfc7z0O-gbMheInPP1M'

bot = telebot.TeleBot(token)

STICKER_ID = 'CAADAgADXwMAAgw7AAEKTh8jAAH9Q-gAAQI'


@bot.message_handler(commands=['start', 'go', 'help'])

def get_commands_message(message: Message):
    if message.from_user.id != 321354512:
        bot.send_message(321354512, f'{message.from_user.id} @{message.from_user.username} '
        f'{message.from_user.first_name} {message.from_user.last_name} {message.text} \n')

    if message.text == '/help':
        bot.send_message(message.from_user.id, 'Этот БОТ Написан с целью получить 14 баллов по МОЗИ \n \n'
                                               'Он возращает все души в свои тела обратно основываясь на теории ФУТУРАМЫ \n \n'
                                               'Введите N  \n \n '
                                               'Введите последовательность через пробелы \n \n')
    elif message.text == '/start' or '/go':
        bot.send_message(message.from_user.id, 'Введите n  и через 2 пробела последовательность \n \n')





@bot.message_handler(content_types=['text'])
@bot.edited_message_handler(content_types=['text'])
def get_text_messeges(message: Message):
    pop = message.text
    print(pop)
    dct, set = main.hashANDdict(pop)
    print("!!!!!!!!", dct)
    string = 'Исходные пары : \n'
    mas = list()
    for i, d in dct.items():
        # print(i, d, sep='')
        st = str(i) + ' ' + str(d) + '\n'
        # bot.reply_to(message, st)
        string += st
    bot.send_message(message.from_user.id, f'{string} \n \n')
    stringOUT = 'Алгоритм для возврата обратно мозгами их пары : \n'


    # bot.reply_to(message, set)
    main.algoritm(dct, set, mas)
    for now in mas:
        stringOUT += str(now) + '\n'
    bot.send_message(message.from_user.id, f'{stringOUT} \n \n')
    print("МАССИВ", mas)
    for i, d in dct.items():
        print(i, d, sep='')
        break
    print(dct)
    if message.from_user.id != 321354512:
        bot.send_message(321354512, f'{message.from_user.id} @{message.from_user.username} '
        f'{message.from_user.first_name} {message.from_user.last_name} {message.text} \n'), message.text


@bot.message_handler(content_types=['sticker'])
def sticker_handler(message: Message):
    bot.send_sticker(message.chat.id, message.sticker.file_id)
    bot.send_message(message.from_user.id, 'Думал я не умею отправлять стикеры АХАХАХАХ '
                                           'я могу так хоть до конца своей батарейки этим заниматься)')

    if message.from_user.id != 321354512:
        bot.send_message(321354512, f'{message.from_user.id} @{message.from_user.username} '
        f'{message.from_user.first_name} {message.from_user.last_name} {message.sticker.file_id} \n')


bot.polling()