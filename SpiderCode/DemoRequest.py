import urllib.request
request = urllib.request.Request("http://www.baidu.com")
response = urllib.request.urlopen(request)
html = response.read()
print(html)
