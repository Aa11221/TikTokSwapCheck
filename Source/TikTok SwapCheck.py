try:
    import requests
    import os
    import time
    from os import system, path

    system("title " + "Soud Was Here - @_agf - Soud#0737")
    import colorama
    from colorama import Fore

    colorama.init(autoreset=True)
except Exception as m:
    print("Something Went Wrong\n")
    print(m)
    input()
    exit()

print("""
    ░██████╗░█████╗░██╗░░░██╗██████╗░░█████╗░░█████╗░  ██╗░░██╗███████╗██████╗░███████╗
    ██╔════╝██╔══██╗██║░░░██║██╔══██╗██╔═══╝░██╔══██╗  ██║░░██║██╔════╝██╔══██╗██╔════╝
    ╚█████╗░██║░░██║██║░░░██║██║░░██║██████╗░╚██████║  ███████║█████╗░░██████╔╝█████╗░░
    ░╚═══██╗██║░░██║██║░░░██║██║░░██║██╔══██╗░╚═══██║  ██╔══██║██╔══╝░░██╔══██╗██╔══╝░░
    ██████╔╝╚█████╔╝╚██████╔╝██████╔╝╚█████╔╝░█████╔╝  ██║░░██║███████╗██║░░██║███████╗
    ╚═════╝░░╚════╝░░╚═════╝░╚═════╝░░╚════╝░░╚════╝░  ╚═╝░░╚═╝╚══════╝╚═╝░░╚═╝╚══════╝
                              """, Fore.GREEN + "Credit @_agf - Soud#0737")
print(Fore.GREEN + "TikTok Checker + Swap By Soud Beta Version,", Fore.RED+"Free And Not For Sell")

noe = int(input("[Choose Mode]\n1) Any\n2) 2L Only\n3) 3L Only\n4) 4L Only\n>> "))
if noe >= 5:
    print(Fore.RED+"Wrong Number, Stupid")
    time.sleep(3)
    exit()
sessionid = str(input("Enter SessionID: "))
input("Press any Key to start Checking\n")


def chkswp():
    if path.exists("User.txt"):
        ggg = open("User.txt", "r")
    else:
        print(Fore.RED + "Pls Make User.txt file and try again")
        time.sleep(3)
        exit()
    a = requests.Session()
    co = 0
    do = 0
    bann = 0
    fa = 0
    while 1:
        user = ggg.readline().split("\n")[0]
        if user == "":
            print(Fore.GREEN + f"Found: {do} | Taken: {fa} | Banned: {bann} | Checked: {co}\nChecker By Soud @_agf Soud#0737\nSaved All in Tiktok-Found.txt <3\n")
        url = f"https://m.tiktok.com/node/share/user/@{user}"
        re = a.get(url)
        if 'statusCode":10202,' in re.text:
            co += 1
            do += 1
            print(Fore.GREEN + f"[+] Found >> @{user} | Checked: {co}")
            with open("Tiktok-Found.txt", "a") as result:
                result.write(f"{user}\n")
                result.close()
                if noe == 1:
                    while 1:
                        url = "https://api16-normal-c-alisg.tiktokv.com/passport/login_name/update/?residence=KW&device_id=6926456821994505733&iid=6933716544179652353&app_name=musical_ly"
                        headers = {
                            "Host": "api16-normal-c-alisg.tiktokv.com",
                            "Connection": "keep-alive",
                            "sdk-version": 1,
                            "x-Tt-Token": "",
                            "Content-Type": "application/x-www-form-urlencoded",
                            "x-tt-passport-csrf-token": sessionid,
                            "Accept-Encoding": "gzip, deflate",
                            "Cookie": f"sessionid={sessionid}"
                        }
                        data = {
                            "login_name": f"{user}"
                        }

                        swapp = requests.post(url, data=data, headers=headers)
                        if "login name can only be updated once within one month" in swapp.text:
                            print(Fore.RED + "[-] Cannot Change Username, Wait 30Days")
                            input()
                            exit()
                        elif "The conversation has expired, please log in again" in swapp.text:
                            print(Fore.RED + "[-] Expired/Bad SessionID")
                            input()
                            exit()
                        elif "You are visiting our service too frequently." in swapp.text:
                            print(Fore.RED + "[-] IP Banned, Turn VPN Or Use Proxy")
                            input()
                            exit()
                        elif 'message":"success' in swapp.text:
                            print(Fore.GREEN + f"""
                            [+] Swapped Done @{user} By Soud69
                            Instagram: https://instagram.com/_agf
                            Github: https://github.com/Soud69
                            Telegram: https://t.me/Soud69
                            Discord: Soud#0737""")
                            input()
                            exit()
                        elif "This username is taken, but you can try a different one" in swapp.text:
                            print(Fore.RED + "[-] User Is Taken, Checking Again")
                            input()
                        else:
                            print(Fore.RED + f"[?] Error with @{user}")
                            print(swapp.status_code)
                            print(swapp.text)
                            input()
                            exit()
                elif noe == 2:
                    if len(user) == 2:
                        while 1:
                            url = "https://api16-normal-c-alisg.tiktokv.com/passport/login_name/update/?residence=KW&device_id=6926456821994505733&iid=6933716544179652353&app_name=musical_ly"
                            headers = {
                                "Host": "api16-normal-c-alisg.tiktokv.com",
                                "Connection": "keep-alive",
                                "sdk-version": 1,
                                "x-Tt-Token": "",
                                "Content-Type": "application/x-www-form-urlencoded",
                                "x-tt-passport-csrf-token": sessionid,
                                "Accept-Encoding": "gzip, deflate",
                                "Cookie": f"sessionid={sessionid}"
                            }
                            data = {
                                "login_name": f"{user}"
                            }

                            swapp = requests.post(url, data=data, headers=headers)
                            if "login name can only be updated once within one month" in swapp.text:
                                print(Fore.RED + "[-] Cannot Change Username, Wait 30Days")
                                input()
                                exit()
                            elif "The conversation has expired, please log in again" in swapp.text:
                                print(Fore.RED + "[-] Expired/Bad SessionID")
                                input()
                                exit()
                            elif "You are visiting our service too frequently." in swapp.text:
                                print(Fore.RED + "[-] IP Banned, Turn VPN Or Use Proxy")
                                input()
                                exit()
                            elif 'message":"success' in swapp.text:
                                print(Fore.GREEN + f"""
                                [+] Swapped Done @{user} By Soud69
                                Instagram: https://instagram.com/_agf
                                Github: https://github.com/Soud69
                                Telegram: https://t.me/Soud69
                                Discord: Soud#0737""")
                                input()
                                exit()
                            elif "This username is taken, but you can try a different one" in swapp.text:
                                print(Fore.RED + "[-] User Is Taken, Checking Again")
                                input()
                            else:
                                print(Fore.RED + f"[?] Error with @{user}")
                                print(swapp.status_code)
                                print(swapp.text)
                                input()
                                exit()
                elif noe == 3:
                    if len(user) == 3:
                        while 1:
                            url = "https://api16-normal-c-alisg.tiktokv.com/passport/login_name/update/?residence=KW&device_id=6926456821994505733&iid=6933716544179652353&app_name=musical_ly"
                            headers = {
                                "Host": "api16-normal-c-alisg.tiktokv.com",
                                "Connection": "keep-alive",
                                "sdk-version": 1,
                                "x-Tt-Token": "",
                                "Content-Type": "application/x-www-form-urlencoded",
                                "x-tt-passport-csrf-token": sessionid,
                                "Accept-Encoding": "gzip, deflate",
                                "Cookie": f"sessionid={sessionid}"
                            }
                            data = {
                                "login_name": f"{user}"
                            }

                            swapp = requests.post(url, data=data, headers=headers)
                            if "login name can only be updated once within one month" in swapp.text:
                                print(Fore.RED + "[-] Cannot Change Username, Wait 30Days")
                                input()
                                exit()
                            elif "The conversation has expired, please log in again" in swapp.text:
                                print(Fore.RED + "[-] Expired/Bad SessionID")
                                input()
                                exit()
                            elif "You are visiting our service too frequently." in swapp.text:
                                print(Fore.RED + "[-] IP Banned, Turn VPN Or Use Proxy")
                                input()
                                exit()
                            elif 'message":"success' in swapp.text:
                                print(Fore.GREEN + f"""
                                [+] Swapped Done @{user} By Soud69
                                Instagram: https://instagram.com/_agf
                                Github: https://github.com/Soud69
                                Telegram: https://t.me/Soud69
                                Discord: Soud#0737""")
                                input()
                                exit()
                            elif "This username is taken, but you can try a different one" in swapp.text:
                                print(Fore.RED + "[-] User Is Taken, Checking Again")
                                input()
                            else:
                                print(Fore.RED + f"[?] Error with @{user}")
                                print(swapp.status_code)
                                print(swapp.text)
                                input()
                                exit()
                elif noe == 4:
                    if len(user) == 4:
                        while 1:
                            url = "https://api16-normal-c-alisg.tiktokv.com/passport/login_name/update/?residence=KW&device_id=6926456821994505733&iid=6933716544179652353&app_name=musical_ly"
                            headers = {
                                "Host": "api16-normal-c-alisg.tiktokv.com",
                                "Connection": "keep-alive",
                                "sdk-version": 1,
                                "x-Tt-Token": "",
                                "Content-Type": "application/x-www-form-urlencoded",
                                "x-tt-passport-csrf-token": sessionid,
                                "Accept-Encoding": "gzip, deflate",
                                "Cookie": f"sessionid={sessionid}"
                            }
                            data = {
                                "login_name": f"{user}"
                            }

                            swapp = requests.post(url, data=data, headers=headers)
                            if "login name can only be updated once within one month" in swapp.text:
                                print(Fore.RED + "[-] Cannot Change Username, Wait 30Days")
                                input()
                                exit()
                            elif "The conversation has expired, please log in again" in swapp.text:
                                print(Fore.RED + "[-] Expired/Bad SessionID")
                                input()
                                exit()
                            elif "You are visiting our service too frequently." in swapp.text:
                                print(Fore.RED + "[-] IP Banned, Turn VPN Or Use Proxy")
                                input()
                                exit()
                            elif 'message":"success' in swapp.text:
                                print(Fore.GREEN + f"""
                                [+] Swapped Done @{user} By Soud69
                                Instagram: https://instagram.com/_agf
                                Github: https://github.com/Soud69
                                Telegram: https://t.me/Soud69
                                Discord: Soud#0737""")
                                input()
                                exit()
                            elif "This username is taken, but you can try a different one" in swapp.text:
                                print(Fore.RED + "[-] User Is Taken, Checking Again")
                                input()
                            else:
                                print(Fore.RED + f"[?] Error with @{user}")
                                print(swapp.status_code)
                                print(swapp.text)
                                input()
                                exit()
        elif 'statusCode":10222,' or 'statusCode":0,' in re.text:
            co += 1
            fa += 1
            print(Fore.RED + f"[-] Taken >> @{user} | Checked: {co}")
        elif 'statusCode":10221,' or 'statusCode":10223' in re.text:
            co += 1
            bann += 1
            print(Fore.RED + f"[!] Banned >> @{user} | Checked: {co}")
        else:
            print(Fore.RED + f"[?] Error >> @{user} | Checked: {co}")


chkswp()
