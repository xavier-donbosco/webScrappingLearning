# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

import sqlite3
class QuotetutorialPipeline:
    def __init__(self):
        self.create_connection()
        self.create_table()


    def create_connection(self):
        self.conn=sqlite3.connect("quote_db.db")
        self.cur=self.conn.cursor()

    def create_table(self):
        self.cur.execute("""drop table if exists quote_tb""")
        self.cur.execute("""create table quote_tb(
            title text,
            author text,
            tag text
        )""")
    def process_item(self, item, spider):
        self.store(item)
        return item

    def store(self,item):
        self.cur.execute("""insert into quote_tb values (?,?,?)""",(
                        item["title"][0],
                        item["author"][0],
                        item["tag"][0]
                         ))
        self.conn.commit()