# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from twisted.enterprise import adbapi
import pandas as pd
import os
class MyprojectPipeline:

    def process_item(self, item, spider):
        file_path = r'website_info.csv'
        df = pd.DataFrame(
            {
            'title':item['title'],
            'url':item['url'],
            'introduction':item['introduction']
        },index = [0])
        file_exists = os.path.exists(file_path)
        if file_exists:
            df.to_csv(file_path, encoding='utf_8_sig',header=None,index=False,mode = 'a')
        else:
            df.to_csv(file_path,encoding='utf_8_sig',index=False,mode = 'a' )

