import string
from urllib import request
from urllib.parse import quote


class HtmlDownloader(object):

    # 下载指定url的页面
    def download(self, url):
        if url is None:
            return None

        url_ = quote(url, safe=string.printable)  # python特有的函数参数传递方式，指定传给safe这个形参
        response = request.urlopen(url_)

        if response.getcode() != 200:
            return None

        return response.read()  # 读取页面，返回
