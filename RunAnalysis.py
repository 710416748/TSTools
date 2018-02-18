# -*- coding: utf-8 -*-
#
# @Time       : 18-2-15
# @Author     : YeChen
# @Email      : a710416748@hotmail.com
# @File       : RunAnalysis.py
# @Software   : PyCharm
# @Description: Just run the all analysis.py in ylog

import os
import sys
import TSLogging

def dealFile(pyFile):
    mLogger.debug("get file:" + pyFile)
    if os.path.isfile(pyFile) and os.path.split(pyFile)[1] == "analyzer.py":
        os.system("python " + pyFile)


def dealDir(dirFile):
    global mLogger
    mLogger = TSLogging.getLogger(__file__)
    mLogger.debug("get dir: " + dirFile)
    
    fileList = os.listdir(dirFile)
    mLogger.debug('files are: ')
    mLogger.debug(fileList)

    for item in fileList:
        wholePath = os.path.join(dirFile,item)
        if (os.path.isdir(wholePath)):
            dealDir(wholePath)
        else:
            dealFile(wholePath)

'''
@useless
def analyzer_log():

    fileList = os.listdir(os.getcwd())
    print(fileList)

    for item in fileList:
        if (os.path.isdir(item)):
            deal_dir(os.getcwd() + "/" + item)
        else:
            run_py(item)
'''
if __name__ == '__main__':
    dealDir(os.getcwd())
