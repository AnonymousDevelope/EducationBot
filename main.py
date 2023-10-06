import logging
from aiogram import Bot, Dispatcher, executor, types
from config import API_TOKEN
from buttans import natija, natija2 ,result_4,result_5
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardRemove,ContentType
from data import Dars,videos
from pathlib import Path

download_path = Path().joinpath("fayllar")
download_path.mkdir(parents=True,exist_ok=True)

logging.basicConfig(level=logging.INFO)

bot = Bot(API_TOKEN)
xotira = MemoryStorage()

dp = Dispatcher(bot,storage=xotira)


def save_info(info):
    with open("info.txt", "a") as file:
        file.write(info + "\n")

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    return await message.answer("Assalom aleykum😊 \nBotimizga xush kelibsiz", reply_markup=natija)


@dp.message_handler()
async def natija_handler(message: types.Message):
    if message.text == "Lessons📖":
        await message.answer("Pastdagi link orqali darslarni ko'rishingiz mumkin ⬇️")
        for video in videos:
            await message.answer(video)
        # await message.answer_video(video="https://youtu.be/tzWggCnYVWU?si=iyDvSf9VpiRKvhIC")    
    elif message.text == "Test📊":
        return await message.answer("Tayyorlanmoqda⏱")
    elif message.text == "Topshiriq📝":
        await Dars.tanishtiring.set()
        return await message.answer("boshlash uchun 'tayyor' deb yozing !",reply_markup=ReplyKeyboardRemove())
    elif message.text == "Fikrlar📨":
        return await message.answer("Fikrlaringizni qoldiring!", reply_markup=natija2)
    elif message.text == "Hammasi A'lo Darajada👍":
        return await message.answer("menyuga qaytish", reply_markup=natija)
    elif message.text == "Menga yoqmadi👎":
        return await message.answer("menyuga qaytish", reply_markup=natija)
    elif message.text == "Registration✅":
        return await message.answer("ism , familya , telefon raqamingizni qoldiring📱",reply_markup=natija)
    elif message.text == "Ortga⬅️":
        return await message.answer("menyuga qaytish", reply_markup=natija)
    elif message.text == "ha":
        return await message.answer("menyuga qaytish", reply_markup=natija)
    elif message.text == "yo'q":
        return await message.answer("menyuga qaytish", reply_markup=natija)



@dp.message_handler(commands=['help'])
async def help(message: types.Message):
    return await message.answer("Qanday yordam 📱")

@dp.message_handler(state=Dars.tanishtiring)
async def start(message: types.Message ,state:FSMContext):
    async with state.proxy() as info:
        info['tanishtiring'] = message.text
    
    await Dars.next()
    await message.answer("1-savol-->: O'zingiz haqingizda")

@dp.message_handler(state=Dars.savol1)
async def name(message: types.Message ,state:FSMContext):
    async with state.proxy() as info:
        info['savol1'] = message.text
    
    await Dars.next()
    await message.answer("2-savol-->: Bu fanga qanday kirdingiz ?")

@dp.message_handler(state=Dars.savol2)
async def bir(message: types.Message ,state:FSMContext):
    async with state.proxy() as info:
        info['savol2'] = message.text
    
    await Dars.next()
    await message.answer("3-savol-->: Astronomiya haqida nimlar bilasiz ?")

@dp.message_handler(state=Dars.savol3)
async def son(message: types.Message ,state:FSMContext):
    async with state.proxy() as info:
        info['savol3'] = message.text
    
    await Dars.next()
    await message.answer("4-savol-->: Astronomiya so'zini manosi ?")

@dp.message_handler(state=Dars.savol4)
async def harf(message: types.Message ,state:FSMContext):
    async with state.proxy() as info:
        info['savol4'] = message.text
    
    await Dars.next()
    await message.answer("5-savol-->: Astronomiyaga qiziqasizmi , nima uchun ?")


    global msg

    await state.finish()
    await message.answer('',reply_markup=result_5)

if __name__ == '__main__':
    open("info.txt", "w").close()
    executor.start_polling(dp, skip_updates=True)




