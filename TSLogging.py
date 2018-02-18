# -*- coding: utf-8 -*-
#
# @Time       : 18-2-15
# @Author     : YeChen
# @Email      : a710416748@hotmail.com
# @File       : TSLogging.py
# @Software   : PyCharm
# @Description: manage the log format and log files


import os
import sys
import logging
import time

LOG_PATH = '/home/coder/LOG/'
LOG_FILE_MAX = 10

# log level table
# DEBUG < INFO < WARNING < ERROR < FATAL < CRITICAL
LOG_LEVEL = logging.DEBUG

TAG = 'TSLogging'

mNameList = []
mLogFile = ""

def initLogger(logger):

    formatter = logging.Formatter('%(asctime)s [%(levelname)s] %(process)d %(message)s')

    fileHandler = logging.FileHandler(mLogFile)
    fileHandler.setFormatter(formatter)

    consoleHandler = logging.StreamHandler(sys.stdout)
    consoleHandler.setFormatter(formatter)

    logger.addHandler(fileHandler)
    logger.addHandler(consoleHandler)
    logger.setLevel(LOG_LEVEL)

    return logger

def getLogFile(filename = LOG_PATH + time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())) + '.log'):
    fileList = os.listdir(LOG_PATH)
    for file in fileList:
        if os.path.isdir(LOG_PATH + file) or os.path.isfile(LOG_PATH + file) and not file.endswith(".log"):
            fileList.remove(file)
            print(file + " isn't log files")

    if len(fileList) >= LOG_FILE_MAX:
        fileList.sort()
        os.remove(LOG_PATH + fileList[0])
        print('LOG FILES is too many, delete ' + LOG_PATH + fileList[0])
        fileList.remove(fileList[0])

    return filename

def getLogger(name = 'TSLogDefault'):
    if not isinstance(name,str):
        raise TypeError('we need a string! please check it')
    global mLogFile
    global mNameList
    global mLogger

    if mLogFile == "":
        mLogFile = getLogFile()


    if TAG not in mNameList:
        mLogger = initLogger(logging.getLogger(TAG))
        mNameList.append(TAG)

    if name in mNameList:
        return logging.getLogger(name)
    else:
        mNameList.append(name)
        logger = logging.getLogger(name)
        return initLogger(logger)


if __name__ == '__main__':
    logger = getLogger('test')
    logger.info('just test')