from datacenter.models import Schoolkid
from datacenter.models import Mark
from datacenter.models import Chastisement
from datacenter.models import Commendation
from datacenter.models import Lesson
from django.core.exceptions import MultipleObjectsReturned
import random

COMMENDATIONS = ['Молодец!', 'Отлично!', 'Хорошо!', 'Гораздо лучше, чем я ожидал!', 'Приятно удивил!',
                 'Великолепно!', 'Прекрасно!', 'Сегодня очень обрадовал!' , 'Именно этого я давно ждал от тебя!',
                 'Сказано здорово – просто и ясно!', 'Как всегда, точен!', 'Очень хороший ответ!',
                 'Талантливо!', 'Cегодня прыгнул выше головы!', 'Я поражен!', 'Уже существенно лучше!', 'Потрясающе!',
                 'Замечательно!', 'Прекрасное начало!', 'Так держать!', 'Идет на верном пути!', 'Здорово!',
                 'Это как раз то, что нужно!', 'Я тобой горжусь!', 'С каждым разом у тебя получается всё лучше!',
                 'Мы с тобой не зря поработали!', 'Я вижу, как ты стараешься!', 'Ты растешь над собой!',
                 'Ты многое сделал, я это вижу!', 'Теперь у тебя точно все получится!']


def fix_marks(schoolkid):
    bad_marks = Mark.objects.filter(schoolkid=schoolkid, points__in=[2, 3]).update(points=5)


def remove_chastisements(schoolkid):
    remarks = Chastisement.objects.filter(schoolkid=schoolkid).delete()


def create_commendation(name, subject):
    lessons = Lesson.objects.filter(year_of_study=name.year_of_study, group_letter=name.group_letter, subject__title=subject)
    lesson = random.choice(lessons..first())
    Commendation.objects.create(text=random.choice(COMMENDATIONS), created=lesson.timeslot, schoolkid=name,
                                subject=lesson.subject, teacher=lesson.teacher)


def main():
    try:
        student = Schoolkid.objects.filter(full_name__contains='Фролов Иван').first()
    except Schoolkid.MultipleObjectsReturned:
        raise MultipleObjectsReturned('Найдено несколько учеников, уточните ФИО')
    subject = input('Укажите предмет, где вы хотите оставить положительный комментарий')
    fix_marks(student)
    remove_chastisements(student)
    create_commendation(student, subject)

    
if __name__ == "__main__":
    main()
