import json
from aiogram.types import KeyboardButton,ReplyKeyboardMarkup
natija = json.dumps({
    "keyboard": [["Lessons📖", "Test📊"], ["Topshiriq📝", "Fikrlar📨"], ["Registration✅", "Ortga⬅️"]],
    "resize_keyboard": True,
    "one_time_keyboard": True
})

natija2 = json.dumps({
    "keyboard": [["Hammasi A'lo Darajada👍", "Menga yoqmadi👎"]],
    "resize_keyboard": True,
    "one_time_keyboard": True
})

son = KeyboardButton(text="Ortga⬅️")

result_4 = ReplyKeyboardMarkup(resize_keyboard=True).add(son)

son1 = KeyboardButton(text="ha")
son2 = KeyboardButton(text="yo'q")

result_5 = ReplyKeyboardMarkup(resize_keyboard=True).add(son1,son2)