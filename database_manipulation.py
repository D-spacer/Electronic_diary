from datacenter.models import Schoolkid
from datacenter.models import Mark
from datacenter.models import Chastisement
from datacenter.models import Commendation
from datacenter.models import Lesson
from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned
import random


def fix_marks(schoolkid):
    bad_marks = Mark.objects.filter(schoolkid=schoolkid, points__in=[2, 3])
    for mark in bad_marks:
        mark.points = 5
        mark.save()


def remove_chastisements(schoolkid):
    remarks = Chastisement.objects.filter(schoolkid=schoolkid)
    for remark in remarks:
        remark.delete()


def create_commendation(name, subject):

    commendations = ['Молодец!', 'Отлично!', 'Хорошо!', 'Гораздо лучше, чем я ожидал!', 'Приятно удивил!',
                     'Великолепно!', 'Прекрасно!', 'Сегодня очень обрадовал!' , 'Именно этого я давно ждал от тебя!',
                     'Сказано здорово – просто и ясно!', 'Как всегда, точен!', 'Очень хороший ответ!',
                     'Талантливо!', 'Cегодня прыгнул выше головы!', 'Я поражен!', 'Уже существенно лучше!', 'Потрясающе!',
                     'Замечательно!', 'Прекрасное начало!', 'Так держать!', 'Идет на верном пути!', 'Здорово!',
                     'Это как раз то, что нужно!', 'Я тобой горжусь!', 'С каждым разом у тебя получается всё лучше!',
                     'Мы с тобой не зря поработали!', 'Я вижу, как ты стараешься!', 'Ты растешь над собой!',
                     'Ты многое сделал, я это вижу!', 'Теперь у тебя точно все получится!']

    lessons = Lesson.objects.filter(year_of_study=6, group_letter='А', subject__title=subject)
    lesson = random.choice(lessons)
    student = Schoolkid.objects.filter(full_name__contains=name)[0]
    Commendation.objects.create(text=random.choice(commendations), created=lesson[0].timeslot, schoolkid=student,
                                subject=lesson[0].subject, teacher=lesson[0].teacher)


def main():
    student = Schoolkid.objects.filter(full_name__contains='Фролов Иван')[0]
    try:
        Schoolkid.objects.get(full_name=student)
    except ObjectDoesNotExist:
        print("Такой ученик не существует")
    except MultipleObjectsReturned:
        print('Найдено несколько учеников, уточните запрос')
    fix_marks(student)
    remove_chastisements(student)
    create_commendation(student, 'Математика')
