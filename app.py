import os
import requests

EBAY_ACCESS_TOKEN = os.environ.get("EBAY_ACCESS_TOKEN")

BASE_URL = "https://api.ebay.com"

def ebay_headers():
    if not EBAY_ACCESS_TOKEN:
        raise RuntimeError("EBAY_ACCESS_TOKEN is not configured.")

    return {
        "Authorization": f"Bearer {EBAY_ACCESS_TOKEN}",
        "Content-Type": "application/json",
        "Content-Language": "en-GB",
    }


def get_selling_policies():
    url = f"{BASE_URL}/sell/account/v1/fulfillment_policy"
    response = requests.get(
        url,
        headers=ebay_headers(),
        params={"marketplace_id": "EBAY_GB"},
        timeout=30,
    )

    response.raise_for_status()
    return response.json()


if __name__ == "__main__":
    print(get_selling_policies())