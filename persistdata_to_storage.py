from bs4 import BeautifulSoup

#with open(r"covid19_file.html", "r", encoding="utf-8") as f:
#    page = f.read()
#tree = html.fromstring(page)

#tree = html.parse("covid19_file.html")

f = open(file="covid19_file.html",encoding="utf-8")
soup = BeautifulSoup(f,features="lxml")

table = soup.find("table")
rows = table.find_all("tr")
#print(rows)
data = [[td.findChildren(text=True) for td in tr.findAll("td")] for tr in rows]
print(data)

f.close()




