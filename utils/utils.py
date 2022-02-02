from platform import system
from requests import get
from time import sleep
from tqdm import tqdm
from bs4 import BeautifulSoup
from win10toast import ToastNotifier

def notify_user_toast(title, body, duration):
    if system() == "Windows":
        toast = ToastNotifier()
        toast.show_toast(title, body, duration=duration)

def parse_address(address):
    text = ""
    for a in address:
        text += f"{a.text.strip()} "
    return text


def parse_data(item):
    name = item.find("span", class_="black medium").text.strip()
    number = item.find_all("a", class_="no-hover")[1].text.strip()
    add = item.find_all("div", class_="col-12 description truncatePL")
    address = parse_address(add)
    # print([name, number, address])

    return [name, number, address]


def get_html(url):
    response = get(url)
    return response.text


def get_all_items(html):
    soup = BeautifulSoup(html, 'lxml')
    items = soup.find_all("div", { "class": "mb-3 border border-dark px-3"})

    info = []
    for item in items:
        info.append(parse_data(item))

    return info

def remove_duplicates(data):
    new_data = []
    for d in data:
        if not d in new_data:
            new_data.append(d)
    return new_data


def loop_items(initials, postcode, street, format):
    results = []
    if format == "advanced":
        for initial in tqdm(initials):
            for vowel in ['a', 'e', 'i', 'o', 'u']:
                url = f"https://thephonebook.bt.com/Person/PersonSearch/?Surname={initial}{vowel}&Location={postcode}&Street={street}"
                # print(url)
                item = get_all_items(get_html(url))
                if item != []:
                    if isinstance(item, list):
                        for i in item:
                            results.append(i)
                    else:
                        results.append(item)
                sleep(1)
    else:
        for initial in tqdm(initials):
            url = f"https://thephonebook.bt.com/Person/PersonSearch/?Surname={initial}{initial}&Location={postcode}&Street={street}"
            # print(url)
            item = get_all_items(get_html(url))
            if item != []:
                if isinstance(item, list):
                    for i in item:
                        results.append(i)
                else:
                    results.append(item)
            sleep(2)
    
    return remove_duplicates(results)
