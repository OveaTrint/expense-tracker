from termcolor import colored

def print_info(msg: str):
    print(colored(msg, "yellow"))


def print_warning(msg: str):
    print(colored(msg, "light_yellow"))


def print_error(msg: str):
    print(colored(msg, "red"))
