# import logging
# from aiogram import Bot, Dispatcher, executor, types
# from config import API_TOKEN
# from buttans import natija, natija2 ,result_4,result_5
# from aiogram.contrib.fsm_storage.memory import MemoryStorage
# from aiogram.dispatcher import FSMContext
# from aiogram.types import ReplyKeyboardRemove,ContentType
# from data import Dars
# from pathlib import Path

# download_path = Path().joinpath("fayllar")
# download_path.mkdir(parents=True,exist_ok=True)

# logging.basicConfig(level=logging.INFO)

# bot = Bot(API_TOKEN)
# xotira = MemoryStorage()

# dp = Dispatcher(bot,storage=xotira)


# def save_info(info):
#     with open("info.txt", "a") as file:
#         file.write(info + "\n")

# @dp.message_handler(commands=['start'])
# async def start(message: types.Message):
#     return await message.answer("Hello 😊 \nWelcome to our bot", reply_markup=natija)


# @dp.message_handler()
# async def natija_handler(message: types.Message):
#     if message.text == "Lessons📖":
#         await message.answer("You can see the lessons through the link below ⬇️")
#         await message.answer("https://www.youtube.com/results?search_query=dasturlashni+o%27rganish+1+dars")
#     elif message.text == "Test📊":
#         return await message.answer("Proccess . . .⏱")
#     elif message.text == "Assignment📝":
#         await Dars.tanishtiring.set()
#         return await message.answer("type 'ready' to start !",reply_markup=ReplyKeyboardRemove())
#     elif message.text == "Thoughts📨":
#         return await message.answer("Leave your comment!", reply_markup=natija2)
#     elif message.text == "Everything is excellent👍":
#         return await message.answer("Back to menu", reply_markup=natija)
#     elif message.text == "I didn't like👎":
#         return await message.answer("Back to menu", reply_markup=natija)
#     elif message.text == "Registration✅":
#         return await message.answer("Write your name , surename and phone please📱",reply_markup=natija)
#     elif message.text == "Back⬅️":
#         return await message.answer("Back to menu", reply_markup=natija)
#     elif message.text == "Yes":
#         return await message.answer("Back to menu", reply_markup=natija)
#     elif message.text == "No":
#         return await message.answer("Back to menu", reply_markup=natija)



# @dp.message_handler(commands=['help'])
# async def help(message: types.Message):
#     return await message.answer("What a help 📱")

# @dp.message_handler(state=Dars.tanishtiring)
# async def start(message: types.Message ,state:FSMContext):
#     async with state.proxy() as info:
#         info['tanishtiring'] = message.text
#     await Dars.next()
#     await message.answer("Question 1-->: About yourself")
# @dp.message_handler(state=Dars.savol1)
# async def name(message: types.Message ,state:FSMContext):
#     async with state.proxy() as info:
#         info['savol1'] = message.text
#     await Dars.next()
#     await message.answer("Question 2-->: How did you get into this subject?")

# @dp.message_handler(state=Dars.savol2)
# async def bir(message: types.Message ,state:FSMContext):
#     async with state.proxy() as info:
#         info['savol2'] = message.text
#     await Dars.next()
#     await message.answer("Question 3-->: What do you know about astronomy?")

# @dp.message_handler(state=Dars.savol3)
# async def son(message: types.Message ,state:FSMContext):
#     async with state.proxy() as info:
#         info['savol3'] = message.text
    
#     await Dars.next()
#     await message.answer("Question 4-->: What is the meaning of the word astronomy?")

# @dp.message_handler(state=Dars.savol4)
# async def harf(message: types.Message ,state:FSMContext):
#     async with state.proxy() as info:
#         info['savol4'] = message.text
#     await Dars.next()
#     await message.answer("Question 5-->: Are you interested in astronomy, why?")


#     global msg

#     await state.finish()
#     await message.answer('your answer to the question',reply_markup=result_5)

# if __name__ == '__main__':
#     open("info.txt", "w").close()
#     executor.start_polling(dp, skip_updates=True)



import logging
from aiogram import Bot, Dispatcher, executor, types
from config import API_TOKEN
from buttans import natija, natija2, result_4, result_5
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardRemove
from data import Dars
from pathlib import Path

download_path = Path().joinpath("fayllar")
download_path.mkdir(parents=True, exist_ok=True)

logging.basicConfig(level=logging.INFO)

bot = Bot(API_TOKEN)
xotira = MemoryStorage()

dp = Dispatcher(bot, storage=xotira)


def save_info(info):
    with open("info.txt", "a") as file:
        file.write(info + "\n")

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    return await message.answer("Hello 😊\nWelcome to our bot", reply_markup=natija)

@dp.message_handler()
async def natija_handler(message: types.Message):
    if message.text == "Lessons📖":
        await message.answer("You can see the lessons through the link below ⬇️")
        await message.answer("https://www.youtube.com/results?search_query=dasturlashni+o%27rganish+1+dars")
    elif message.text == "Test📊":
        return await message.answer("Proccess . . .⏱")
    elif message.text == "Assignment📝":
        await Dars.tanishtiring.set()
        return await message.answer("type 'ready' to start !", reply_markup=ReplyKeyboardRemove())
    elif message.text == "Thoughts📨":
        return await message.answer("Leave your comment!", reply_markup=natija2)
    elif message.text == "Everything is excellent👍":
        return await message.answer("Back to menu", reply_markup=natija)
    elif message.text == "I didn't like👎":
        return await message.answer("Back to menu", reply_markup=natija)
    elif message.text == "Registration✅":
        return await message.answer("Write your name, surname, and phone please📱", reply_markup=natija)
    elif message.text == "Back⬅️":
        return await message.answer("Back to menu", reply_markup=natija)
    elif message.text == "Yes":
        return await message.answer("Back to menu", reply_markup=natija)
    elif message.text == "No":
        return await message.answer("Back to menu", reply_markup=natija)

@dp.message_handler(commands=['help'])
async def help(message: types.Message):
    return await message.answer("What a help 📱")

@dp.message_handler(state=Dars.tanishtiring)
async def start_assignment(message: types.Message, state: FSMContext):
    async with state.proxy() as info:
        info['tanishtiring'] = message.text
    await Dars.next()
    await message.answer("Question 1-->: About yourself")

@dp.message_handler(state=Dars.savol1)
async def name(message: types.Message, state: FSMContext):
    async with state.proxy() as info:
        info['savol1'] = message.text
    await Dars.next()
    await message.answer("Question 2-->: How did you get into this subject?")

@dp.message_handler(state=Dars.savol2)
async def bir(message: types.Message, state: FSMContext):
    async with state.proxy() as info:
        info['savol2'] = message.text
    await Dars.next()
    await message.answer("Question 3-->: What do you know about astronomy?")

@dp.message_handler(state=Dars.savol3)
async def son(message: types.Message, state: FSMContext):
    async with state.proxy() as info:
        info['savol3'] = message.text
    await Dars.next()
    await message.answer("Question 4-->: What is the meaning of the word astronomy?")

@dp.message_handler(state=Dars.savol4)
async def harf(message: types.Message, state: FSMContext):
    async with state.proxy() as info:
        info['savol4'] = message.text
    await Dars.next()
    await message.answer("Question 5-->: Are you interested in astronomy, why?")

@dp.message_handler(state=Dars.savol5)
async def process_answers(message: types.Message, state: FSMContext):
    async with state.proxy() as info:
        info['savol5'] = message.text

    # Process user answers here
    # You can save the answers or perform any necessary actions
    
    await state.finish()
    await message.answer('Thank you for answering the questions!', reply_markup=result_5)

if __name__ == '__main__':
    open("info.txt", "w").close()
    executor.start_polling(dp, skip_updates=True)