from datetime import datetime
from colorama import Fore

def success(message, verbose=True):
    msg = f"{Fore.BLACK}[{datetime.now().strftime('%H:%M:%S')}]{Fore.RESET}	{Fore.GREEN}[+]{Fore.RESET}	{message}"
    if verbose:
        print(msg)
    return msg

def error(message, verbose=True):
    msg = f"{Fore.BLACK}[{datetime.now().strftime('%H:%M:%S')}]{Fore.RESET}	{Fore.RED}[-]{Fore.RESET}	{message}"
    if verbose:
        print(msg)
    return msg

def info(message, verbose=True):
    msg = f"{Fore.BLACK}[{datetime.now().strftime('%H:%M:%S')}]{Fore.RESET}	{Fore.BLUE}[!]{Fore.RESET}	{message}"
    if verbose:
        print(msg)
    return msg

def inpt(message):
    return input( f"{Fore.BLACK}[{datetime.now().strftime('%H:%M:%S')}]{Fore.RESET}	{Fore.BLUE}[?]{Fore.RESET}	{message} : ")