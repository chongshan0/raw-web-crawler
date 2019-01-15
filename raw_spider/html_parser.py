import re
import urllib.parse

from bs4 import BeautifulSoup


class HtmlParser(object):

    # 找到本页面上新的url
    def _get_new_urls(self, page_url, soup):
        new_urls = set()
        links = soup.find_all('a', href=re.compile(r"/item/"))  # 查找<a>标签，并且匹配特定的href值
        for link in links:
            new_url = link['href']  # 不完整的url
            new_full_url = urllib.parse.urljoin(page_url, new_url)  # 拼接url
            new_urls.add(new_full_url)
        return new_urls

    # 解析得到html中需要的数据（这里有3个）
    def _get_new_data(self, page_url, soup):
        res_data = {}  # python字典（键值对）

        # url
        res_data['url'] = page_url

        # 解析下面这个元素
        # <dd class="lemmaWgt-lemmaTitle-title"> <h1>Python</h1>
        title_node = soup.find('dd', class_='lemmaWgt-lemmaTitle-title').find('h1')
        res_data['title'] = title_node.get_text()

        # 解析下面这个元素
        # <div class="lemma-summary" label-module="lemmaSummary">
        summary_node = soup.find('div', class_='lemma-summary')
        if summary_node is None:
            return
        res_data['summary'] = summary_node.get_text()

        return res_data

    # 解析页面（通过BeautifulSoup）
    def parse(self, page_url, html_cont):
        if page_url is None or html_cont is None:
            return

        soup = BeautifulSoup(html_cont, 'html.parser', from_encoding='utf-8')

        new_urls = self._get_new_urls(page_url, soup)  # 自定义函数，见上面
        new_data = self._get_new_data(page_url, soup)  # 自定义函数，见上面

        return new_urls, new_data
