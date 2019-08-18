# coding=utf8
# !/usr/bin/python
# -*- coding: ascii -*-

from baike_spider import url_manager, html_downloader, html_parser, html_outputer
from

class SpiderMain(object):
    def __init__(self):
        # 初始化url管理器
        self.urls = url_manager.UrlManager()
        # 初始化下载器
        self.downloader = html_downloader.HtmlDownloader()
        # 初始化解析器
        self.parser = html_parser.HtmlParser()
        # 初始化输出器
        self.outputer = html_outputer.HtmlOutputer()

    def craw(self, root_url):

        count = 1

        # 将入口url加入url管理器
        self.urls.add_new_url(root_url)
        # 管理器中有新的url时，需获得新的url
        while self.urls.has_new_url():

            try:
                # 获取新的url
                new_url = self.urls.get_new_url()

                print 'craw %d : %s' % (count, new_url)

                # 用下载器下载页面
                html_cout = self.downloader.download(new_url)
                # 页面下载完成后，使用解析器解析页面数据，得到新的url及url数据
                new_urls, new_data = self.parser.parse(new_url, html_cout)
                # 批量添加解析出的url
                self.urls.add_new_urls(new_urls)
                # 收集数据
                self.outputer.collect_data(new_data)

                # 加入计数器
                if count == 10:
                    print 'done!'
                    break

                count = count + 1

            # 加入爬取失败处理方法
            except:
                print 'craw failed'

        # 输出收集好的数据
        self.outputer.output_html()


if __name__ == "__main__":
    print 'main 执行'
    # 设置要爬取的入口url
    root_url = "https://baike.baidu.com/item/Python/407313?fr=aladdin"
    obj_spider = SpiderMain()
    # 用spider的craw方法启动爬虫
    obj_spider.craw(root_url)
