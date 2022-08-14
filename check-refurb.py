import string
import requests
from bs4 import BeautifulSoup

# Constants
APPLE_REFURB_STORE_URL = "https://www.apple.com/sg/shop/refurbished"


def get_apple_refurbished_webpage(device: string):
    # Gets the Apple refurb store webpage of the given device string
    # and returns the Respose back
    page = requests.get(f"{APPLE_REFURB_STORE_URL}/{device}").text

    return page


def get_refurb_items_links(webpage: BeautifulSoup):
    # Gets the links of each refurb from the given webpage
    # and returns an Array of links
    APPLE_URL = "https://www.apple.com"

    li_links = webpage.find_all("li")

    refurb_items_links = []

    for link in li_links:
        if link.h3 and link.div:
            refurb_items_links.append(APPLE_URL + link.a.get("href"))

    return refurb_items_links


def main():
    print("[INFO] Initialised check-refurb script")

    webpage_soup_parsed = BeautifulSoup(
        get_apple_refurbished_webpage("mac"), "html.parser")

    refurb_items_links = get_refurb_items_links(webpage_soup_parsed)

    for link in refurb_items_links:
        print(f"[OUTPUT] Item {refurb_items_links.index(link) + 1}:\n{link}")


if __name__ == "__main__":
    main()
