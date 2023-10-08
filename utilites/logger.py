import datetime
import os


# str_datetime = str(datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S"))
# file_name = f"logs\\log_{str_datetime}.log"


# class Decorator:

#     @staticmethod
#     def write_log_to_file(data: str):
#         with open(file_name, 'a', encoding='utf=8') as logger_file:
#             logger_file.write(data)

#     @staticmethod
#     def __call__(func):
#         test_name = os.environ.get('PYTEST_CURRENT_TEST')

#         data_to_add = f"\n-----\n"
#         data_to_add += f"Test: {test_name}\n"
#         data_to_add += f"Start time: {str(datetime.datetime.now())}\n"
#         data_to_add += f"Start name method: {func.__name__}\n"
#         data_to_add += "\n"
#         func()
#         write_log_to_file(data_to_add)
#         data_to_add = f"End time: {str(datetime.datetime.now())}\n"
#         data_to_add += f"End name method: {func.__name__}\n"
#         data_to_add += f"\n-----\n"

#         write_log_to_file(data_to_add)


class Logger():
    str_datetime = str(datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S"))
    file_name = f"logs\\log_{str_datetime}.log"

    @classmethod
    def write_log_to_file(cls, data: str):
        with open(cls.file_name, 'a', encoding='utf=8') as logger_file:
            logger_file.write(data)

    @classmethod
    def add_start_step(cls, method: str):
        test_name = os.environ.get('PYTEST_CURRENT_TEST')

        data_to_add = f"\n-----\n"
        data_to_add += f"Test: {test_name}\n"
        data_to_add += f"Start time: {str(datetime.datetime.now())}\n"
        data_to_add += f"Start name method: {method}\n"
        data_to_add += "\n"

        cls.write_log_to_file(data_to_add)

    @classmethod
    def add_end_step(cls, url: str, method: str):

        data_to_add = f"End time: {str(datetime.datetime.now())}\n"
        data_to_add += f"End name method: {method}\n"
        data_to_add += f"URL: {url}\n"
        data_to_add += f"\n-----\n"

        cls.write_log_to_file(data_to_add)