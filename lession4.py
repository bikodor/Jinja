from jinja2 import Environment, FileSystemLoader, FunctionLoader
# про Environment подробнее на https://jinja.palletsprojects.com/en/2.11.x/api/#jinja2.Environment
# про Загрузчики подробнее на https://jinja.palletsprojects.com/en/2.11.x/api/#jinja2.FileSystemLoader

persons = [
    {'name': 'Алексей', 'old': 18, 'balance': 5000},
    {'name': 'Михаил', 'old': 32, 'balance': 12400},
    {'name': 'Пётр', 'old': 44, 'balance': 4000},
    {'name': 'Евгений', 'old': 24, 'balance': 3900}
]

# file_loader = FileSystemLoader('templates')
# env = Environment(loader=file_loader)
#
# tm = env.get_template('main.html') #Template
# msg = tm.render(users=persons)
#
# print(msg)

def loadTpl(path):
    if path == "index":
        return '''Имя {{u.name}}, возраст {{u.old}}'''
    else:
        return '''Данные: {{u}}'''

file_loader2 = FunctionLoader(loadTpl)
env2 = Environment(loader=file_loader2)

tm2 = env2.get_template('index') #Template
msg2 = tm2.render(u=persons[0])

print(msg2)