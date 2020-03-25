#! /usr/bin/python3
# -*- coding:utf-8 -*-


from __future__ import unicode_literals
from .ad_views import (
    TbkGoodsHandle
)

urls = [
    #从 /users/regist 过来的请求，将调用 users_views 里面的 TbkGoodsHandle 类
    (r'tbkgoods', TbkGoodsHandle)
]
