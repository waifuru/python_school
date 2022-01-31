import functools
import logging


def get_file_logger(path_to_file):
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)
    formatter = logging.Formatter('%(levelname)-8s %(asctime)s: %(message)s')

    file_handler = logging.FileHandler(path_to_file)
    file_handler.setLevel(logging.INFO)
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    return logger


def log_to_file(path_to_file):
    def log(func, ):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            logger = get_file_logger(path_to_file)
            result = func(*args, **kwargs)

            args_str = ""
            for arg in args:
                args_str += str(arg) + " "

            name = func.__name__
            module = func.__module__

            logger.info(module + ": " + name + ": " + args_str + ": " + str(result))
            return func(*args, **kwargs)

        return wrapper

    return log


@log_to_file("4_1_2.log")
def sum(a, b):
    return a + b


if __name__ == '__main__':
    print("Task 4.1.2")
    print(sum(5, 10))
    print('function {}, from module {}'.format(sum.__name__,  sum.__module__))


