import requests
import datetime

SOURCE_URL = "https://raw.githubusercontent.com/metowolf/iplist/master/data/special/china.txt"
LIST_NAME = "China_Cidr"
OUTPUT_FILE = "china_cidr.rsc"

def fetch_and_convert():
    try:
        response = requests.get(SOURCE_URL, timeout=30)
        response.raise_for_status()
        cidrs = [line.strip() for line in response.text.splitlines() if line.strip()]
        
        with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
            f.write(f"/ip firewall address-list remove [find list=\"{LIST_NAME}\"]\n")
            f.write("/ip firewall address-list\n")
            for cidr in cidrs:
                f.write(f"add list=\"{LIST_NAME}\" address={cidr}\n")
    except Exception:
        exit(1)

if __name__ == "__main__":
    fetch_and_convert()
