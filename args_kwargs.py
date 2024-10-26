# строгая типизация
def add(a: int, b: int):
    print(a+b)

# args - возможность передать некий набор параметров - кортеж, и с ним сразу работать
def add_all(*args):
    all_sum = 0
    for num in args:
        all_sum += num
    return all_sum

# kwargs - сюда ждем словарь. Можно вывести отдельно ключ и значение
def authorize(**kwargs):
    print(kwargs)

# в цикле можно перечислять параметры
def authorize2(**kwargs):
    for key, value in kwargs.items():
        print(key)
        print(value)

data = {'name': 'Roman', 'age': '29', 'job': 'AQA'}
values = [1, 2, 3, 4, 5]
more_values = [10, 20, 30, 40, 50, 60]

add(1,2)
print(add_all(*values, *more_values))
authorize(name='Roman', age='29', job='AQA')
authorize2(name='Roman', age='29', job='AQA')
authorize2(**data)