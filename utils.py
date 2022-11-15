import json


def load_students(filename):
    """
    Загружает список студентов из файла
    """
    # список студентов
    list_students = []
    with open(filename, 'r', encoding='utf-8') as file:
        data = json.load(file)
    for student in data:
        list_students.append(student['pk'])
    return list_students


def get_student_by_pk(filename, pk):
    """
    Получает словарь с данными студента по его pk
    """
    with open(filename, 'r', encoding='utf-8') as file:
        data = json.load(file)
    for student in data:
        if student['pk'] == pk:
            return student


def load_professions(filename):
    """
    Загружает список профессий из файла
    """
    # список профессий
    professions_list = []

    with open(filename, 'r', encoding='utf-8') as file:
        professions = json.load(file)
    for skil in professions:
        # временная переменная для перевода слов списка в нижний регистр
        lower_skil = skil["title"].lower()
        professions_list.append(lower_skil)
    return professions_list


def get_profession_by_title(filename, title):
    """
    Получает словарь с инфо о профе по названию
    """
    with open(filename, 'r', encoding='utf-8') as file:
        data = json.load(file)
    for professions in data:
        if professions["title"] == title.title():
            return set(professions["skills"])


def check_fitness(student, profession):
    """
    состовляет чек лист соответствия студента профессии
    """

    # словарь соответствия студента
    check_list = {}
    # множество того что умеет
    has = student.intersection(profession)
    # множество того что не умеет
    lacks = profession.difference(student)
    # записываем в словарь то что умеет
    check_list['has'] = list(has)
    # записываем в словарь то что не умеет
    check_list['lacks'] = list(lacks)
    # записываем в словарь процент соответствия
    check_list['fit_percent'] = round(len(has) / len(lacks) * 100, 2)
    return check_list
