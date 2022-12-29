from HW_10.logger import log
from HW_10 import model
from telegram import Update
from telegram.ext import ContextTypes


async def output_book(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    for my_dict in model.get_data():
        await update.message.reply_text(f'Имя: {my_dict["first_name"]}\n'
                                        f'Фамилия: {my_dict["last_name"]}\n'
                                        f'Телефон: {my_dict["phone_number"]}\n'
                                        f'Дата рождения: {my_dict["birthday"]}\n'
                                        f'Место работы: {my_dict["workplace"]}\n'
                                        f'Id: {my_dict["id"]}')


async def add_data(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    my_dict = {}
    tel_list = []
    my_dict['first_name'] = update.message.text.split()[1]
    my_dict['last_name'] = update.message.text.split()[2]
    my_dict['phone_number'] = update.message.text.split()[3]
    my_dict['birthday'] = update.message.text.split()[4]
    my_dict['workplace'] = update.message.text.split()[5]

    model.add_data(my_dict)
    await update.message.reply_text('Данные записаны в справочник')


@log
def print_book(data: list):
    """Вывод в консоль данных содержимого справочника"""
    for my_dict in data:
        print(f'Имя: {my_dict["first_name"]} | Фамилия: {my_dict["last_name"]}'
              '| Телефон: ', *my_dict["phone_number"], f' | Дата рождения: {my_dict["birthday"]}'
                                                       f' | Место работы: {my_dict["workplace"]} | Id: {my_dict["id"]}')
    if not data:
        print("<-Нет данных для отображения->")
        print()


@log
def add_record() -> dict:
    """Диалог добавления записи.
    :return Cловарь с данными записи.:"""
    my_dict = {}
    tel_list = []

    my_dict['first_name'] = input('Введите имя : ')
    my_dict['last_name'] = input('Введите фамилию : ')
    while True:
        data = input('Введите номер телефона (для выхода нажмите Enter) : ')
        if data:
            tel_list.append(data)
        else:
            break
    my_dict['phone_number'] = tel_list
    my_dict['birthday'] = input('Дата рождения: ')
    my_dict['workplace'] = input('Место работы: ')
    return my_dict


@log
def request_id() -> int:
    """Запрос id от пользователя
    :return id:"""
    return int(input('Введите id: '))


@log
def editor(data: dict) -> dict:
    """:param data: Выбранная запись
    :return отредактированная запись:"""
    new_dict = {}
    data['first_name'] = input(f"Имя: {data['first_name']}. Введите новое имя: ")

    data['last_name'] = input(f"Фамилия: {data['last_name']} Введите новую фамилию: ")
    print("Телефон:", *data['phone_number'])
    tel_list = []
    while True:
        tel = input('Введите номер телефона (для выхода нажмите Enter) : ')
        if tel:
            tel_list.append(tel)
        else:
            break
    data['phone_number'] = tel_list
    data['birthday'] = input(f"Дата рождения: {data['birthday']} Введите новую дату: ")
    data['workplace'] = input(f"Место работы: {data['workplace']} Введите новое место работы: ")

    return data


@log
def request_last_name() -> str:
    """Запрос фамилии от пользователя
    :return фамилия:"""
    return input('Введите Фамилию: ')
