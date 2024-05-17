from aiogram import F, types, Router
from aiogram.filters import CommandStart, Command

from keyboard import reply

user_private_router = Router()


@user_private_router.message(CommandStart())
async def start_cmd(message: types.Message):
    await message.answer("Здравствуйте, вас приветствует помощник органов ЗАГС Калининградской области. Чем я могу помочь?", reply_markup=reply.start_kb)

@user_private_router.message(F.text.lower().contains('сети'))
async def menu_cmd(message: types.Message):
    await message.answer('''Телеграм: https://t.me/zagsagentstvo39. 
ВК: https://vk.com/zags039''')


@user_private_router.message(F.text.lower().contains('апостиль'))
async def menu_cmd(message: types.Message):
    await message.answer('''Апостиль - это штамп, определенного формата и содержания, который удостоверяет подлинность подписи и должность лица, подписавшего документ,
а также подлинность печати, которой скреплён документ. На документы, выданные органами ЗАГС Калининградской области, 
апостиль проставляется ЗАГС (Агентством) Калининградской области.''')

@user_private_router.message(F.text.lower().contains('отдел') | (F.text.lower().contains('загс')))
async def menu_cmd(message: types.Message):
    await message.answer("Узнать больше об отделах загс вы можете на сайте https://zags.gov39.ru/otdely-zags/")

@user_private_router.message(F.text.lower().contains('справк') | (F.text.lower().contains('свидетельств')))
async def menu_cmd(message: types.Message):
    await message.answer('''ЗАГС (Агентство) Калининградской области выдаёт следующие виды документов: 
    Об отсутствии записи акта гражданского состояния. 
    Истребование личных документов с территории иностранного государства.
    А также занимается проставлением апостиля на свидетельства выданные в органах ЗАГС
Иные справки или свидетельства вы можете получить в отделе ЗАГС по месту пребывания.''')

@user_private_router.message(F.text.lower().contains('Гос. регистрация актов') | (F.text.lower().contains('регистрация')))
async def menu_cmd(message: types.Message):
    await message.answer("Какой вид регистрации вас интересует?", reply_markup=reply.gosregacts)

@user_private_router.message(F.text.lower().contains('брак'))
async def menu_cmd(message: types.Message):
    await message.answer("Регистрация заключения брака производится любым органом ЗАГС по выбору заявителей. Дата и время выбирается при подаче заявления.",
                         reply_markup=reply.gosregacts)

