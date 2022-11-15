from utils import load_students, load_professions, get_student_by_pk, get_profession_by_title, check_fitness

from config import FILENAME_STUDENTS, FILENAME_PROFESSION


def checking_availability_of_student():
    """
    функция получения номера студента
    проверки правельности ввода и наличия студента
    """
    # ввод номера студента
    pk = input('Введите номер студента:\n')
    if pk.isdigit():
        int_pk = int(pk)
        # список студентов
        list_students = load_students(FILENAME_STUDENTS)

        # проверка наличия студента
        if int_pk in list_students:
            data_list_students = get_student_by_pk(FILENAME_STUDENTS, int_pk)

            # переменная имени студента
            name_student = data_list_students["full_name"]

            # переменная скилов студента
            skil_student = ", ".join(data_list_students["skills"])

            # noinspection PyUnboundLocalVariable
            print(f'Студент: {name_student}\nЗнает: {skil_student}')

            # множество скилов студента
            lots_of_skills = set(data_list_students["skills"])
            checking_availability_profession(name_student, lots_of_skills)
        else:
            print('У нас нет такого студента')
    else:
        print('Вы использовали не верный формат ввода номера ученика')


def checking_availability_profession(name_student, lots_of_skills):
    """
    функция ввода профессии
    проверки наличия профессии в перечне
    вывод соответствия студента профессии
    """

    # ввод профессии
    title = input(f'Выберите специальность для оценки студента {name_student}\n')

    # список профессий
    professions_list = load_professions(FILENAME_PROFESSION)

    # проверка наличия профессии
    if title.lower() in professions_list:
        skills_for_profession = get_profession_by_title(FILENAME_PROFESSION, title)
        check_list = check_fitness(lots_of_skills, skills_for_profession)
        print(f"Пригодность {check_list['fit_percent']}%")
        print(f"{name_student} знает: {', '.join(check_list['has'])}")
        print(f"{name_student} не знает: {', '.join(check_list['lacks'])}")
    else:
        print('У нас нет такой специальности')


if __name__ == "__main__":
    checking_availability_of_student()
