import requests

response = requests.get("https://www.doh.gov.ph/doh-press-release/DOH-SENDS-OFF-NCC-REPATS%3B-UPDATES-ON-COVID-19-CASES?fbclid=IwAR0QEAE_92K8mVs4mhRfawXOAmGltHlIInJZQyPD9E9OMNBB16elKBVI3do")
content = response.text
covid19list_html = open("covid19list_html", "w+",  encoding="utf-8")
covid19list_html.write(content)
covid19list_html.close()

print("covid19list html saved")
