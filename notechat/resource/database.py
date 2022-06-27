import os

from notedrive.sqlalchemy.base import BaseTable, create_engines, meta
from notetool.secret import read_secret
from sqlalchemy import BIGINT, Column, String, Table

uri = read_secret(cate1='notechat', cate2='dataset', cate3='db_path')
uri = uri or f'sqlite:///{os.path.abspath(os.path.dirname(__file__))}/data/notechat.db'

engine = create_engines(uri)


class AuthorDetail(BaseTable):
    def __init__(self, table_name="author_detail", *args, **kwargs):
        super(AuthorDetail, self).__init__(table_name=table_name, engine=engine, *args, **kwargs)
        self.table = Table(self.table_name, meta,
                           Column('author_id', BIGINT, comment='用户ID', primary_key=True),
                           Column('name', String, comment='名称', default=0),
                           Column('source', String, comment='来源', default=0),
                           )
        self.create()


class ResourceDetail(BaseTable):
    def __init__(self, table_name="resource_detail", *args, **kwargs):
        super(ResourceDetail, self).__init__(table_name=table_name, engine=engine, *args, **kwargs)
        self.table = Table(self.table_name, meta,
                           Column('resource_id', BIGINT, comment='资源ID', primary_key=True),
                           Column('resource_type', String(30), comment='资源类型'),
                           Column('author', String, comment='作者ID', default=0),
                           Column('title', String, comment='标题', default=0),
                           Column('sub_title', String, comment='子标题', default=0),
                           Column('content', String, comment='内容', default=0),
                           Column('url', String, comment='资源地址', default=0),
                           Column('source_url', String, comment='资源原地址', default=0),
                           )
        self.create()
