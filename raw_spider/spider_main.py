from raw_spider import url_manager, html_downloader, html_parser, html_outputer


class SpiderMain(object):
    # 初始化
    def __init__(self):
        self.urls = url_manager.UrlManager()  # url管理器
        self.downloader = html_downloader.HtmlDownloader()  # 下载器
        self.parser = html_parser.HtmlParser()  # 解析器
        self.outputer = html_outputer.HtmlOutputer()  # 输出器

    # 入口
    def craw(self, root_url):
        count = 1
        self.urls.add_new_url(root_url)  # 添加第一个url
        while self.urls.has_new_url():
            try:
                new_url = self.urls.get_new_url()  # 随机取一个url
                print('craw %d : %s' % (count, new_url))

                html_cont = self.downloader.download(new_url)  # 下载页面

                new_urls, new_data = self.parser.parse(new_url, html_cont)  # 解析，得到内容和新的url

                self.urls.add_new_urls(new_urls)  # 新url给url管理器

                self.outputer.collect_data(new_data)  # 数据传给输出器

                if count >= 100:  # 就爬100条
                    break
                count += 1

            except Exception as e:
                print(str(e))

            self.outputer.output_html()


# 入口
if __name__ == '__main__':
    root_url = 'https://baike.baidu.com/item/Python/407313?fr=aladdin'
    obj_spider = SpiderMain()  # 初始化
    obj_spider.craw(root_url)
