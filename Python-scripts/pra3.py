import re

url_details = "google <https://www.google.co.in/>, yahoo <https://in.search.yahoo.com>, okla <https://www.speedtest.net>"
result = re.findall(r"(\w+)\s*<https?://.*?>", url_details)
print(result)

result = re.search(r"(\w+)\s*<https?://.*?>", url_details)
print(result)




