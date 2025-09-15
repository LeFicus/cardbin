# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import sqlite3
import os
import pandas as pd
from pymongo import MongoClient,errors

# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


# class CardbinPipeline:
#     def process_item(self, item, spider):
#         return item

class SqlitePipeline:
    def __init__(self,db_path='identifier.sqlite',batch_size=1000):
        self.db_path = db_path
        self.batch_size = batch_size
        self.buffer = []

    @classmethod
    def from_crawler(cls,crawler):
        return cls(db_path=crawler.settings.get('SQLITE_DB','identifier.sqlite'),batch_size=crawler.settings.get('SQLITE_BATCH',1000))

    def open_spider(self,spider):
        self.conn = sqlite3.connect(self.db_path,check_same_thread=False)
        self.cursor = self.conn.cursor()
        self.cursor.execute(
            '''
                create table if not exists cardbin (
                id integer primary key autoincrement,
                url text unique,
                bin_iin text,
                brand text,
                card_type text,
                category text,
                bank text,
                bank_url text,
                country text,
                country_short text,
                latitude text,
                longitude text      
                )
            '''
        )
        self.conn.commit()

    def process_item(self, item, spider):
        self.buffer.append((
            item.get('url'),
            item.get('bin_iin'),
            item.get('brand'),
            item.get('card_type'),
            item.get('category'),
            item.get('bank'),
            item.get('bank_url'),
            item.get('country'),
            item.get('country_short'),
            item.get('latitude'),
            item.get('longitude')
            )
        )
        if len(self.buffer) >= self.batch_size:
            self._flush()
        return item

    def _flush(self):
        try:
            self.cursor.executemany("insert or ignore into cardbin (url,bin_iin,brand,card_type,category,bank,bank_url,country,country_short,latitude,longitude) values (?,?,?,?,?,?,?,?,?,?,?)",self.buffer)
            self.conn.commit()
        finally:
            self.buffer = []

    def close_spider(self,spider):
        if self.buffer:
            self._flush()
        self.conn.close()