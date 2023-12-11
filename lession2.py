from jinja2 import Template
from markupsafe import escape

# data = '''Модуль Jinja вместо определения {{ name }} подставляет соответствующее значение'''
#
#
# tm = Template(data)
# msg = tm.render(name='Фёдор')
#
# print(msg)
#
# data2 = '''{% raw %}Модуль Jinja вместо определения {{ name }} подставляет соответствующее значение{% endraw %}'''
#
# tm2 = Template(data2)
# msg2 = tm2.render(name='Фёдор')
# print(msg2)
#в первом случае работает как в лекции 1, но во втором raw и endraw экранируют строку с нём и не дают подставить переменную в name
#
# link = '''В HTML-документе ссылки опреляются так:
# <a href="#">Ссылка</a>'''
#
# tm = Template(link)
# msg = tm.render()
#
# print(msg)
# # если открыть этот текст в браузере он отобразит его как ссылку, а не дословно <a href="#">Ссылка</a>, для того чтобы
# # этот текст дословно вывести в браузере есть экранирование символов, такое как e:
# tm2 = Template("{{ link | e}}") # указать е вот так
# msg2 = tm2.render(link=link)
# print(msg2)
# # теперь это браузер дословно и досимвольно выведет <a href="#">Ссылка</a>
# # или проще записать:
# msg3 = escape(link) #escape это тоже самое что и е, но проще записать (даже без рендера)
# print(msg3)

# cities = [
#     {'id': 1, 'city': 'Москва'},
#     {'id': 3, 'city': 'Тверь'},
#     {'id': 5, 'city': 'Калуга'},
#     {'id': 7, 'city': 'Ростов'},
#     {'id': 9, 'city': 'Санкт-Петербург'}
# ]
#
# link = '''<select name="cities">
# {% for c in cities -%}
#     <option value="{{c['id']}}">{{c['city']}}</option>
# {% endfor -%}
# </select>'''
# # минус нужен чтобы построчно вывести значения и без пустых переносов строки
# tm = Template(link)
# msg = tm.render(cities=cities)
#
# print(msg)

cities = [
    {'id': 1, 'city': 'Москва'},
    {'id': 3, 'city': 'Тверь'},
    {'id': 6, 'city': 'Калуга'},
    {'id': 7, 'city': 'Ростов'},
    {'id': 9, 'city': 'Санкт-Петербург'}
]

link = '''<select name="cities">
{% for c in cities -%} 
{% if c.id > 6 -%}
    <option value="{{c['id']}}">{{c['city']}}</option>
{% elif c.city == "Москва" -%}
    <option>{{c['city']}}</option>
{% else -%}
ID {{ c.id }} меньше 7
{% endif -%}
{% endfor -%}
</select>'''
# минус нужен чтобы построчно вывести значения и без пустых переносов строки
tm = Template(link)
msg = tm.render(cities=cities)

print(msg)