import requests
from bs4 import BeautifulSoup
from time import sleep

slack_webhook = open("slack_webhook_url.txt", 'r')


def in_stock():
    url = slack_webhook.read()
    requests.post(url, json={"text":"There's ice cream!!  Go to https://www.undergroundcreamery.com/shop now!"})

def main():
    print("[-] Checking For Ice Cream...")
    res = requests.get("https://www.undergroundcreamery.com/shop")
    soup = BeautifulSoup(res.text, 'html.parser')
    status_list = soup.find_all("div", {"class": "grid-meta-status"})
    for status in status_list:
        is_sold_out = status.find_all("div", {"class":"product-mark"})
        if "sold out" not in is_sold_out[0].contents[0]:
            in_stock()
    print("[!] No luck this time... :(\n[!] Checking again in 1 hour...")

if __name__ == "__main__":
    while True:
        main()
        sleep(3600)