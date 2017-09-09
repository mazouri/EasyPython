import urllib.request

from bs4 import BeautifulSoup

url = 'http://www.wal-martchina.com/walmart/store/14_hubei.htm'

user_agent = "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.134 Safari/537.36"

request = urllib.request.Request(url)

request.add_header('User-Agent', user_agent)

content = urllib.request.urlopen(request)

# print(content)

soup = BeautifulSoup(content, from_encoding="gb18030")

# Shop name.
shop_name = soup.find_all('td', {"class", "xl714445"})

# print(shop_name)

address = soup.find_all('td', {'class', 'xl684445'})

phones = soup.find_all('td', {'class', 'xl744445'})

for shop in shop_name:
    print("Shop name is " + shop.text.lstrip().rstrip())

print('-------------------------')

for address in address:
    print("Shop address is " + address.text.lstrip().rstrip())

sum = 0

for phone in phones:
    if sum % 2 == 0:
        print("Phone is " + phone.text.lstrip().rstrip())
    else:
        print("Route is " + phone.text.lstrip().rstrip())
        print('----------------------------------')
    sum += 1

