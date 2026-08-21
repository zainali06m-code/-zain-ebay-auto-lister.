import os
import requests

EBAY_TOKEN = os.environ.get("EBAY_AUTH_TOKEN")

if not EBAY_TOKEN:
    raise RuntimeError("EBAY_AUTH_TOKEN is not configured")

url = "https://api.ebay.com/ws/api.dll"

headers = {
    "X-EBAY-API-COMPATIBILITY-LEVEL": "1455",
    "X-EBAY-API-CALL-NAME": "GeteBayOfficialTime",
    "X-EBAY-API-SITEID": "3",
    "Content-Type": "text/xml",
}

xml = f"""<?xml version="1.0" encoding="utf-8"?>
<GeteBayOfficialTimeRequest xmlns="urn:ebay:apis:eBLBaseComponents">
    <RequesterCredentials>
        <eBayAuthToken>{EBAY_TOKEN}</eBayAuthToken>
    </RequesterCredentials>
</GeteBayOfficialTimeRequest>
"""

response = requests.post(url, headers=headers, data=xml, timeout=30)

print("HTTP:", response.status_code)
print(response.text)