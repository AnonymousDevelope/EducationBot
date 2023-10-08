import json
from aiogram.types import KeyboardButton,ReplyKeyboardMarkup
natija = json.dumps({
    "keyboard": [["Lessons📖", "Test📊"], ["Assignment📝", "Thoughts📨"], ["Registration✅", "Back⬅️"]],
    "resize_keyboard": True,
    "one_time_keyboard": True
})

natija2 = json.dumps({
    "keyboard": [["Everything is excellent👍", "I didn't like👎"]],
    "resize_keyboard": True,
    "one_time_keyboard": True
})

son = KeyboardButton(text="Back⬅️")

result_4 = ReplyKeyboardMarkup(resize_keyboard=True).add(son)

son1 = KeyboardButton(text="Yes")
son2 = KeyboardButton(text="No")

result_5 = ReplyKeyboardMarkup(resize_keyboard=True).add(son1,son2)