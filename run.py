import datetime

from scrapy.cmdline import execute
import os
import sys

if __name__ == '__main__':
    print('start:%s'%datetime.datetime.now())
    sys.path.append(os.path.dirname(os.path.abspath(__file__)))
    execute(['scrapy', 'crawl', 'spider'])