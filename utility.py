''' Creation Date: 09/11/2022 '''

from colorama import Fore, Style
import traceback


class Log:
    ''' Purpose: Correctly format print messages given purpose. '''
    PREFIX_STATUS = f'[{Fore.GREEN}-{Style.RESET_ALL}]'
    PREFIX_WARN = f'{Fore.LIGHTBLACK_EX}[{Fore.CYAN}*{Style.RESET_ALL}{Fore.LIGHTBLACK_EX}] {Fore.CYAN}Warning:{Style.RESET_ALL}'
    PREFIX_ALERT = f'{Fore.LIGHTBLACK_EX}[{Fore.RED}!{Style.RESET_ALL}{Fore.LIGHTBLACK_EX}] {Fore.RED}ERROR:{Style.RESET_ALL}'
    PREFIX_INFO = f'[{Fore.BLUE}i{Style.RESET_ALL}{Fore.LIGHTBLACK_EX}]'
    PREFIX_TRACE = f'{Fore.LIGHTBLACK_EX}[{Fore.RED}!{Style.RESET_ALL}{Fore.LIGHTBLACK_EX}] {Fore.RED}TRACE:{Style.RESET_ALL}'
    @staticmethod
    def status(message: str):
        ''' Format: [-] message '''
        print(f'{Log.PREFIX_STATUS} {message}')
    @staticmethod
    def warn(message: str):
        ''' Format: [*] Warning: message '''
        print(f'{Log.PREFIX_WARN} {Fore.LIGHTBLACK_EX}{message}{Style.RESET_ALL}')
    @staticmethod
    def alert(message: str):
        ''' Format: [!] ERROR: message '''
        print(f'{Log.PREFIX_ALERT} {Fore.LIGHTBLACK_EX}{message}{Style.RESET_ALL}')
    @staticmethod
    def info(message: str):
        ''' Formats: [i] message '''
        print(f'{Log.PREFIX_INFO} {message}{Style.RESET_ALL}')
    @staticmethod
    def trace(error_traceback):
        ''' Formats: [!] trace '''
        formatted_traceback = ''.join(traceback.format_tb(error_traceback))
        print(f'{Log.PREFIX_TRACE}\n{Fore.LIGHTBLACK_EX}{formatted_traceback}{Style.RESET_ALL}')