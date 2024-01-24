import time
import requests
from colorama import Fore, Style
import os

os.system('cls')
def main():
    banner = fr"""{Fore.RED + Style.BRIGHT}
██████╗ ██╗███████╗ ██████╗ ██████╗ ██████╗ ██████╗     ██╗    ██╗███████╗██████╗ ██╗  ██╗ ██████╗  ██████╗ ██╗  ██╗
██╔══██╗██║██╔════╝██╔════╝██╔═══██╗██╔══██╗██╔══██╗    ██║    ██║██╔════╝██╔══██╗██║  ██║██╔═══██╗██╔═══██╗██║ ██╔╝
██║  ██║██║███████╗██║     ██║   ██║██████╔╝██║  ██║    ██║ █╗ ██║█████╗  ██████╔╝███████║██║   ██║██║   ██║█████╔╝ 
██║  ██║██║╚════██║██║     ██║   ██║██╔══██╗██║  ██║    ██║███╗██║██╔══╝  ██╔══██╗██╔══██║██║   ██║██║   ██║██╔═██╗ 
██████╔╝██║███████║╚██████╗╚██████╔╝██║  ██║██████╔╝    ╚███╔███╔╝███████╗██████╔╝██║  ██║╚██████╔╝╚██████╔╝██║  ██╗
╚═════╝ ╚═╝╚══════╝ ╚═════╝ ╚═════╝ ╚═╝  ╚═╝╚═════╝      ╚══╝╚══╝ ╚══════╝╚═════╝ ╚═╝  ╚═╝ ╚═════╝  ╚═════╝ ╚═╝  ╚═╝
                                                                                                                    
 ██████╗██╗     ██╗███████╗███╗   ██╗████████╗                                                                      
██╔════╝██║     ██║██╔════╝████╗  ██║╚══██╔══╝                                                                      
██║     ██║     ██║█████╗  ██╔██╗ ██║   ██║                                                                         
██║     ██║     ██║██╔══╝  ██║╚██╗██║   ██║                                                                         
╚██████╗███████╗██║███████╗██║ ╚████║   ██║                                                                         
 ╚═════╝╚══════╝╚═╝╚══════╝╚═╝  ╚═══╝   ╚═╝     

 ~by a5hx
    """
    print(banner)

    webhook = input(fr"{Fore.RED + Style.BRIGHT}Input webhook: ")

    def messages():

        message = input(fr"{Fore.RED + Style.BRIGHT}Message : ")
        data = {
      "content" : f"{message}",
        }

        sendmessage = requests.post(webhook, json = data)
        try:
            sendmessage.raise_for_status()
        except requests.exceptions.HTTPError as e:
            print(fr"{Fore.RED}Webhook is invalid.")
            time.sleep(1)
            exit()
        else:
            print(fr'{Fore.RED + Style.BRIGHT}Successfully sent message "{message}" to "{webhook}"')
        messages()

    messages()

main()
