# -*- coding: utf-8 -*-
from django.shortcuts import render
# ----ччч - я тут самый прокаченный дать номер пйдра----
# kill me this is mac - drop the base!!!
# Для "basic_one"
# Чтобы мы могли возвратить response - Нам нужно из django импортировать HttpResponse
from django.http.response import HttpResponse

# Импортируем несколько важных для нас классов
from django.template.loader import get_template 
from django.template import Context 
# Мы импортировали два класса: get_template и Context
# get_template - отвечает за получение шаблона
# Context отвечает за хранение тех переменных, которые будут потом отправлены в шаблон


# Это для третей функции импорты
# render в ответ сразу
from django.shortcuts  import render_to_response 


#  Функция 'basic_one'.
# В качестве параметра функция должна получать request (некий запрос), 
# делает некие действия и должна вернуть response - ответ.
def basic_one(request):
    view = "basic_one"
# Здесь мы имитируем html-code
# % - знак означает что мы должны его заменить строковым значением описанным после кавычек
    html = "<html><body>This is %s view fuckyeah!!! lol</html></body>" % view
    return HttpResponse(html)


def template_two(request):
# 1. Создали переменную	
    view = "template_two"
# 2. Получили файл шаблона. Кладем в переменную t наш шаблон.
    t = get_template('myview.html')

# У нас в представлении есть переменная "name" 

###### !!! Context отвечает за хранение переменных,
###### которые будут потом отображаться в представлении. 

# 3. Создали контекст представления внутри которого отправили нашу переменную name со значением view 
# Context({'name':view})

###### Вставляем нашу переменную в виде словаря как ключ словаря
###### Как значение словаря мы добавляем view - template_two


# ===========Мы формируем html-code. Для этого мы используем "render"==========
# 4. t.render(...) - объединили текст шаблона с переменной т.е. создали полнеценнй html-код
   
    html = t.render(Context({'name':view})) 
# Эта строка сгенерирует наш финальный html-код.
# Но теперь его надо отправить обратно в браузер 
# 5. Вернули этот html код внутри нашего HttpResponse объекта
    return HttpResponse(html)

# Второй вариант несколько сложен, нам нужно написать целых 4 строки для простейшего действия.
# Разработчики Django создали упращенный вариант

# самый простой и эффективный способ отправки информации пользователю:
def template_three_simple(request):
    view = "template_thee"
# В какой view отправляем данные 
# Потом какие именно мы собираемся отправлять данные
    return render_to_response('myview.html', {'name': view})

