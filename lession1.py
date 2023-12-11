from jinja2 import Template


# name = "Фёдор"
#
#
# tm = Template("Привет {{ name }}")
# msg = tm.render(name=name)
#
# # print(msg)
#
# name = "Антон"
# age = 28


# tm2 = Template("Привет, мне {{ a }} лет и зовут меня {{ n }}")
# msg2 = tm2.render(n=name, a=age)
#
# print(msg2)

# name = "Антон"
# age = 28
#
# tm2 = Template("Привет, мне {{ a*2 }} лет и зовут меня {{ n.upper() }}")
# msg2 = tm2.render(n=name, a=age)
#
# print(msg2)

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def getAge(self):
        return self.age

    def getName(self):
        return self.name


per = Person("Егор", 22)

tm = Template("Мне {{ p.age }} лет и зовут меня {{ p.name }}.")
tm2 = Template("Мне {{ p.getAge() }} лет и зовут меня {{ p.getName() }}.")
msg = tm.render(p=per)
msg2 = tm2.render(p=per)

print(msg)
print(msg2)

# per = {'name': 'Петя', 'age': 30}
#
# tm = Template("Мне {{ p.age }} лет и зовут меня {{ p.name }}.")
# tm2 = Template("Мне {{ p['age'] }} лет и зовут меня {{ p['name'] }}.")
# msg = tm.render(p=per)
# msg2 = tm2.render(p=per)
# print(msg)
# print(msg2)
