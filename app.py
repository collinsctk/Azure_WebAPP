#!/usr/bin/env python3

from flask import Flask
import socket

node = Flask(__name__)


# 静态路由,最简单页面
@node.route('/', methods=['GET'])
def index():
    return f"APPService:{socket.gethostname()}, My IP is {socket.gethostbyname(socket.gethostname())}"


if __name__ == "__main__":
    node.run(host='0.0.0.0', port=80)
