import urllib2
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

f = urllib2.urlopen('http://www.douban.com/')
data = f.read()
#print 'Status:', f.status, f.reason
for k, v in f.getheaders():
    print '%s: %s' % (k, v)
print 'Data:', data.decode('utf-8')