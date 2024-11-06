"""
Создайте класс, который будет считывать файл.
Напишите декоратор, который будет замерять время выполнения.
Напишите декоратор, который будет вызывать функцию n-раз.
Воспользуйтесь декоратором для замера времени и примените его ко всем функциям в вашем модуле.
"""
import time


def measure_time(func):
    """
Decorator for measuring function execution time
    """

    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Время выполнения функции '{func.__name__}': {end_time - start_time:.4f} секунд")
        return result

    return wrapper


def repeat(n):
    """
    Decorator for calling a function multiple times

    """

    def decorator(func):
        def wrapper(*args, **kwargs):
            result = None
            for i in range(n):
                print(f"Выполнение {i + 1}-й раз функции '{func.__name__}'")
                result = func(*args, **kwargs)
            return result

        return wrapper

    return decorator


class FileReader:
    """
        Reads the contents of a file and returns it as a string
    """

    def __init__(self, filename):
        self.filename = filename

    @measure_time
    @repeat(5)
    def read_file(self):
        try:
            with open(self.filename, 'r', encoding='utf-8') as file:
                content = file.read()
                return content
        except FileNotFoundError:
            print("File Not Found")
            return None


file_reader = FileReader('home_work14.txt')
content = file_reader.read_file()
