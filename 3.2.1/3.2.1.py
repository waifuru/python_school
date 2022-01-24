import logging


def get_logger():
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.ERROR)
    formatter = logging.Formatter('%(asctime)s %(name)-12s %(levelname)-8s %(message)s')

    file_handler = logging.FileHandler('found_errors.log')
    file_handler.setLevel(logging.ERROR)
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    console = logging.StreamHandler()
    console.setLevel(logging.CRITICAL)
    console.setFormatter(formatter)
    logger.addHandler(console)

    return logger


def process_log(log_filename):
    with open("found_errors.log", 'r+') as f:
        f.truncate(0)

    log_lines = open(log_filename).readlines()
    logger = get_logger()
    error_string = ' error '
    critical_string = ' critical error '
    count_errors = 0

    for line in log_lines:
        try:
            if critical_string in line.lower():
                count_errors += 1
                raise CriticalErrorException(line)
            elif error_string in line.lower():
                logger.error(line)
                count_errors += 1
        except CriticalErrorException as e:
            logger.critical(e.value)

    try:
        return len(log_lines) / count_errors
    except ZeroDivisionError:
        print("There were zero errors for " + len(log_lines).__str__() + " lines of logs.")


class CriticalErrorException(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)


if __name__ == '__main__':
    print("Task 3.2.1")
    print(process_log("yupdate.log"))