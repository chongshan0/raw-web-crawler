import urllib.request
import http.cookiejar

# 在python3.3后urllib2已经不能再用，将urllib2给改为urllib.request即可
# cookielib 模块改名为 http.cookiejar


url = "http://www.baidu.com/"

# basic
response1 = urllib.request.urlopen(url)
print(response1.getcode())
print(response1.read())

# 伪装客户端
request = urllib.request.Request(url)
request.add_header("user-agent", "Mozilla/5.0")
response2 = urllib.request.urlopen(url)
print(response2.getcode())
print(response2.read())

# cookie
cj = http.cookiejar.CookieJar()
opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
urllib.request.install_opener(opener)
response3 = urllib.request.urlopen(url)
print(response3.getcode())
print(response3.read())
print(cj)
