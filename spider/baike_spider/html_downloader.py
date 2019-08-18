from urllib import request
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

class HtmlDownloader(object):
    def download(self, url):
        if url is None:
            print('url is None')
            return None

        try:
            response=request.urlopen(url,timeout=100)
            if response.getcode()!=200:
                print('download fail')
                return None
        except:
            print('download timeout')
        return response.read()