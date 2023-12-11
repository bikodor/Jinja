from jinja2 import Template

# cars = [
#     {'model': 'Audi', 'price': 23000},
#     {'model': 'BMW', 'price': 25050},
#     {'model': 'Volvo', 'price': 15200},
#     {'model': 'Mercedes', 'price': 28400}
# ]
#
# tpl = "Суммарная цена автомобилей = {{ c | sum(attribute='price') }}"
# tm = Template(tpl)
# msg = tm.render(c=cars)
#
# print(msg)

# cost = [4, 10, 30, 5, 8, 22]
# tpl = "Суммарная цена = {{ c | sum }}"
# tm = Template(tpl)
# msg = tm.render(c=cost)
#
# print(msg)


# tpl = "Самая дорогая машина = {{ (c | max(attribute='price')).model }}" # и min може самое только минимальное
# tm = Template(tpl)
# msg = tm.render(c=cars)
#
# print(msg)
# # tpl2 = "Рандомная машина = {{ c | random }}"
# tpl2 = "Рандомная машина = {{ (c | random).model }}"
# tm2 = Template(tpl2)
# msg2 = tm2.render(c=cars)
# print(msg2)

persons = [
    {'name': 'Алексей', 'old': 18, 'balance': 5000},
    {'name': 'Михаил', 'old': 32, 'balance': 12400},
    {'name': 'Пётр', 'old': 44, 'balance': 4000},
    {'name': 'Евгений', 'old': 24, 'balance': 3900}
]
#
# tpl = '''
# {%- for u in users -%}
# {% filter upper %}{{u.name}}{% endfilter %}
# {% endfor -%}
# '''
# # или lower вместо upper
# tm = Template(tpl)
# msg = tm.render(users=persons)
#
# print(msg)

# МАКРООПРЕДЕЛЕНИЕ
# html = '''
# {% macro input(name, value='', type='text', size=20) -%}
#     <input type="{{ type }}" name="{{ name }}" value="{{ value | e }}" size="{{ size }}">
# {%- endmacro %}
#
# <p>{{ input('username', 45,'text', 36) }}
# <p>{{ input('email', 'Валя@mail.ru') }}
# <p>{{ input('password', '', 'number', 36) }}
# '''
#
# tm = Template(html)
# msg = tm.render()
#
# print(msg)

#Вложенный макрос

html = '''
{% macro list_users(list_of_user) -%}
<ul>
{% for u in list_of_user -%}
    <li>{{u.name}} {{caller(u)}}
{%- endfor %}
</ul>
{%- endmacro %}

{% call(user) list_users(users) %}
    <ul>
    <li>age: {{user.old}}
    <li>balance: {{user.balance}}
    </ul>
{% endcall -%}
'''
# вместо блока call после endmacro можно юзать {{list_users(users)}}, но тогда блок call не заработает (просто вызываем list_users с persons нашими сверху)
tm = Template(html)
msg = tm.render(users=persons)
print(msg)



# https://jinja.palletsprojects.com/en/2.11.x/templates/ - список всех фильтров