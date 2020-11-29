# Написать свой cache декоратор c максимальным размером кеша и его очисткой при необходимости. Декоратор должен
# перехватывать аргументы оборачиваемой функции Декоратор должен иметь хранилище, где будут сохраняться все
# перехваченные аргументы и результаты выполнения декорируемой функции Декоратор должен проверять наличие
# перехваченных аргументов в хранилище. Если декорируемая функция уже вызывалась с такими аргументами, она не будет
# вызываться снова, вместо этого декоратор вернет сохраненное значение. Декоратор должен принимать один аргумент -
# максимальный размер хранилища. Если хранилище заполнено, нужно удалить 1 любой элемент, чтобы освободить место под
# новый.

from collections import deque


def do_cache(maxsize):
    memory = dict()

    def decorator_cache(func):
        def wrapper(*args):
            key = [*args]
            for key in args:
                if key not in memory:
                    if len(memory) == maxsize:
                        memory.popitem()
                    temp = func(*args)
                    memory.update({args: temp})
            return memory.get(args)

        return wrapper

    return decorator_cache


@do_cache(maxsize=3)
def get_value(a, b):
    return a + b


print(get_value(10, 11))
print(get_value(12, 13))
print(get_value(12, 13))
print(get_value(12, 13))
print(get_value(16, 17))
print(get_value(16, 18))
