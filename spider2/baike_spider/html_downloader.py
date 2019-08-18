# !/usr/bin/python
# -*- coding: ascii -*-

import urllib2
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

class HtmlDownloader(object):
    def download(self, url):
        if url is None:
            print 'url is None'
            return None

        try:
            reponse = urllib2.urlopen(url,timeout=1000)
            if reponse.getcode() != 200:
                print 'download false'
                return None
            print 'download success'
        except:
            print 'download timeout'
        return reponse.read()
