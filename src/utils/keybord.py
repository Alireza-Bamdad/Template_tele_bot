from telebot import types


def creat_buttens(*keys,row_width=2, resize_keyboard=True):
    markup = types.ReplyKeyboardMarkup(
        row_width=row_width,
        resize_keyboard=resize_keyboard
    )
    
    buttens = map(types.KeyboardButton, keys)
    markup.add(*buttens)
    return markup


