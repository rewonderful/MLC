#!/usr/bin/env python
# _*_ coding:utf-8 _*_
from datetime import timedelta
import datetime
if __name__ == '__main__':
    t = datetime.datetime.strptime("201908081147", "%Y%m%d%H%M")
    tt = t - timedelta(minutes=t.minute % 15)
    print(t,tt)
    print(t.strftime("%Y%m%d"))