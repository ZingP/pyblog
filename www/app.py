#! /usr/bin/env python
#  -*- coding: utf-8 -*-
# Author: "liuyouyuan"
# Date: 2018/3/8

import logging; logging.basicConfig(level=logging.INFO)
import asyncio, os, json, time
from datetime import datetime

from aiohttp import web

def index(request):
    print("hello")
    print(request)
    body = '<h1> Hello pyblog </h1>'
    resp = web.Response(body=body.encode("utf-8"))
    # 如果不添加content_type，某些严谨的浏览器会把网页当成文件下载，而不是直接显示
    resp.content_type = 'text/html;charset=utf-8'
    return resp

@asyncio.coroutine
def init(loop):
    app = web.Application(loop=loop)
    app.router.add_route('GET', '/', index)
    srv = yield from loop.create_server(app.make_handler(), '127.0.0.1', 9000)
    logging.info("server started at http://127.0.0.1:9000")
    return srv


loop = asyncio.get_event_loop()
loop.run_until_complete(init(loop))
loop.run_forever()