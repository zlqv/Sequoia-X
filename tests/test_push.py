import unittest

import settings
from push import push
from push import push_rich
from push import strategy
from push import strategy
from push import format_stocks
import logging
import datetime


def test_push():
    settings.init()
    push("测试")


def test_strategy():
    settings.init()
    strategy("")
    strategy("1")


def test_format_stocks():
    stocks = [('SH600398', '海澜之家'), ('SZ002851', '麦格米特'), ('SZ000755', '山西高速'), ('SH603615', '茶花股份'), ('SH605100', '华丰股份')]
    format_stocks(stocks)


def test_push_rich():
    settings.init()
    stocks = [('SH600398', '海澜之家'), ('SZ002851', '麦格米特'), ('SZ000755', '山西高速'), ('SH603615', '茶花股份'),
         ('SH605100', '华丰股份')]
    push_rich("8bfca0a4-55fb-495f-87cf-f3c7b410389d", stocks)


current_time = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
log_filename = 'logs/test-push-{}.log'.format(current_time)
logging.basicConfig(format='%(asctime)s %(message)s', filename=log_filename)
logging.getLogger().setLevel(logging.INFO)
