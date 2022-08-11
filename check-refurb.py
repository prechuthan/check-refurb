import requests

# Constants
APPLE_REFURB_STORE_URL = "https://www.apple.com/sg/shop/refurbished"


def get_apple_refurbished_website(device):
    page = requests.get(f"{APPLE_REFURB_STORE_URL}/{device}")
    return page


def main():
    print("[INFO] Initialised check-refurb script")
    webpage_text = get_apple_refurbished_website("mac").text
    print(f"[OUTPUT]\n {webpage_text}")


if __name__ == "__main__":
    main()
