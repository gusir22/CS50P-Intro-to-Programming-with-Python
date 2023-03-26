import re


url = input("URL: ").strip()

if matches := re.search(r"^(?:https?://)?(?:www\.)?twitter\.com/([a-z0-9_]+)", url, flags=re.IGNORECASE):
    print(f"Username: {matches.group(1)}")
