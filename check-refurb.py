from multiprocessing.dummy import Array
import string
import requests
from bs4 import BeautifulSoup


class RefurbItem:
    def __init__(self, link, name) -> None:
        self.link = link
        self.name = name
        pass


def get_apple_refurbished_webpage(url: string) -> BeautifulSoup:
    # Gets the Apple refurb store webpage of the given device string
    # and returns the Respose back
    print(f"[STATUS] Getting page ({url})")
    page = BeautifulSoup(requests.get(url).text, "html.parser")

    return page


def get_refurb_items_links(webpage: string) -> Array:
    # Gets the links of each refurb from the given webpage
    # and returns an Array of links
    print(f"[STATUS] Finding refurbished item links")
    li_links = webpage.find_all("li")

    refurb_items_links = []

    for link in li_links:
        if link.h3 and link.div:
            refurb_items_links.append(
                "https://www.apple.com" + link.a.get("href"))

    return refurb_items_links


def get_refurb_item_details(link: string) -> RefurbItem:
    # TODO
    return RefurbItem(link, "macbook")


def main():
    print("[STATUS] Initialised check-refurb script")

    # Gets refurb webpage
    webpage_soup_parsed = get_apple_refurbished_webpage(
        "https://www.apple.com/sg/shop/refurbished/mac")

    # Get links of refurb items
    refurb_items_links = get_refurb_items_links(webpage_soup_parsed)

    print(f"[INFO] Total of {len(refurb_items_links)} items found")

    # Get reburb items details
    refurb_items = []

    for link in refurb_items_links:
        refurb_items.append(get_refurb_item_details(link))


if __name__ == "__main__":
    main()
