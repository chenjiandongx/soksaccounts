import json
import re

import requests
from bs4 import BeautifulSoup

HEADERS = {
    "X-Requested-With": "XMLHttpRequest",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36"
    "(KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36",
}

# PATH = r"C:\software\Shadowsocks-4.0\gui-config.json"  # gui-config.json path
PATH = r"D:\gui-config.json"  # gui-config.json path


def parse_iso369():
    """
    parse website：http://2s.iso369.com
    """
    try:
        url = "http://2s.iso369.com"
        req = requests.get(url, headers=HEADERS).text.encode(
            "ISO-8859-1"
        ).decode(
            "utf-8"
        )
        bs = BeautifulSoup(req, "lxml").find(
            "aside", id="free"
        ).get_text().strip()
    except Exception as e:
        print(e)

    else:
        server = re.findall(r"\d+\.\d+\.\d+\.\d+", bs)
        server_port = re.findall(r"(?<=端口：)\d+", bs)
        password = re.findall(r"(?<=密码：)[a-zA-Z0-9.]+", bs)

        accounts = []
        for i, value in enumerate(server):
            account = {
                "server": value,
                "server_port": server_port[len(server) - i - 1],
                "password": password[i],
                "method": "aes-256-cfb",
                "remarks": "",
                "timeout": 5,
            }
            accounts.append(account)
        configs.extend(accounts)


def parse_ishadow():
    """
    parse website：http://xyz.ishadow.online/
    """
    try:
        url = "http://xyz.ishadow.online/"
        req = requests.get(url, headers=HEADERS).text.encode(
            "ISO-8859-1"
        ).decode(
            "utf-8"
        )
        bs = BeautifulSoup(req, "lxml").find(
            "div", class_="portfolio-items"
        ).get_text().strip()
    except Exception as e:
        print(e)

    else:
        server = re.findall(r"(?<=IP Address:)\S+", bs)
        server_port = re.findall(r"(?<=Port：)\d+", bs)
        password = re.findall(r"(?<=Password:) *\S*", bs)
        method = re.findall(r"(?<=Method:)\S+", bs)

        accounts = []
        # some account without password
        for i, value in enumerate(password):
            if value != " ":
                account = {
                    "server": server[i],
                    "server_port": server_port[i],
                    "password": value,
                    "method": method[i],
                    "remarks": "",
                    "timeout": 5,
                }
                accounts.append(account)
        configs.extend(accounts)


def parse_kejiss():
    """
    parse website：https://www.kejiss.com
    """
    try:
        url = "https://www.kejiss.com/page/testss.html"
        req = requests.get(url, headers=HEADERS).text
        bs = BeautifulSoup(req, "lxml").find(
            "div", class_="pagecontent"
        ).get_text().strip()
    except Exception as e:
        print(e)

    else:
        server = re.findall(r"(?<=服务器IP：)\S+", bs)
        server_port = re.findall(r"(?<=端口：)\d+", bs)
        password = re.findall(r"(?<=密码：)\S+", bs)
        method = re.findall(r"(?<=加密方式：)\S+", bs)

        accounts = []
        for i, value in enumerate(server):
            account = {
                "server": value,
                "server_port": server_port[i],
                "password": password[i],
                "method": method[i],
                "remarks": "",
                "timeout": 5,
            }
            accounts.append(account)
        configs.extend(accounts)


def main():
    """
    程序入口
    """
    parse_iso369()
    parse_ishadow()
    # parse_kejiss()      # 这个网站挂了

    gui_config = {
        "configs": configs,
        "strategy": "com.shadowsocks.strategy.ha",
        "index": -1,
        "global": "false",
        "enabled": "true",
        "shareOverLan": "false",
        "isDefault": "false",
        "localPort": 1080,
        "pacUrl": "null",
        "useOnlinePac": "false",
        "secureLocalPac": "true",
        "availabilityStatistics": "false",
        "autoCheckUpdate": "false",
        "checkPreRelease": "false",
        "isVerboseLogging": "false",
        "logViewer": {
            "topMost": "false",
            "wrapText": "false",
            "toolbarShown": "false",
            "Font": "Consolas, 9.75pt",
            "BackgroundColor": "Black",
            "TextColor": "White",
        },
        "proxy": {
            "useProxy": "false",
            "proxyType": 0,
            "proxyServer": "",
            "proxyPort": 0,
            "proxyTimeout": 3,
        },
        "hotkey": {
            "SwitchSystemProxy": "",
            "SwitchSystemProxyMode": "",
            "SwitchAllowLan": "",
            "ShowLogs": "",
            "ServerMoveUp": "",
            "ServerMoveDown": "",
        },
    }

    try:
        result = json.dumps(gui_config)
        with open(PATH, "w+", encoding="utf-8") as f:
            f.write(result)
    except Exception:
        print(">>  Generate gui-config.json failed")
    else:
        print(">>  Generate gui-config.json successful")


if __name__ == "__main__":
    configs = []
    main()
