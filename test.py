import sys
import os
import re
import gc
import json
import logging
import telnetlib
import socket
from testbase import logger

from websocket import create_connection

global ws

try:
    ws = create_connection("ws://192.168.116.89:8080/clockck/websocket")
    # ws = create_connection("ws://10.22.115.88:8080/clockck/websocket") 
    result = ws.recv()
    print("Received '%s'" % result)
except socket.error as error:
    print("==== websocket error")


def close_socket():
    try:
        ws.close()  # 需关闭连接
        logger.debug("finish the test success")
    except:
        # ws = None
        logger.debug(" try except finish the test ")


def switchCases(caseType, res):
    try:
        ws.send(
            json.dumps({"one": 1231}))  # 通知服务器，执行用例开始

    except:
        ws.send(json.dumps(dict))  # 统一封装成json格式给服务器      
