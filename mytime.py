# encoding: utf-8


import time,datetime

def timeToStr(timestamp=1462451334):
	time_local = time.localtime(timestamp)
	dt = time.strftime("%Y-%m-%d %H:%M:%S",time_local)
	return dt

def timeformat_to_timestamp(timeformat=None, format='%Y-%m-%d %H:%M:%S'):
    # try:
    if timeformat:
        time_tuple = time.strptime(timeformat,format)
        res = time.mktime(time_tuple) #转成时间戳
    else:
        res = time.time()        #获取当前时间戳
    return int(res) * 1000


if __name__ == '__main__':
	