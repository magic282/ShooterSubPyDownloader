#!/usr/bin/env python
'''
Created on Jan 20, 2014

@author: magic282
'''

from SVPlayerHash import SVPlayerHash
try:  # Python 3
    from urllib.parse import urlencode
    from urllib.request import Request, urlopen
except ImportError:  # Python 2
    from urllib import urlencode
    from urllib2 import Request, urlopen
import json

class Shooter(object):
    '''
    classdocs
    '''
    
    __SHOOTERURL = "http://shooter.cn/api/subapi.php"
    
    __fileName = ""
    __videoHash = ""
    
    __subInfo = []
    

    def start(self):        
        self.__videoHash = SVPlayerHash.ComputeFileHash(self.__fileName)
        values = dict(filehash = self.__videoHash, pathinfo = self.__fileName, format = "json", lang = "Chn")
        data = urlencode(values).encode('utf-8', 'replace')
        req = Request(self.__SHOOTERURL, data)
        rsp = urlopen(req)
        content = rsp.read().decode('utf-8', 'replace')
        
        jsonContent = json.loads(content)
        for idx_i, i in enumerate(jsonContent):
            print(i)
            
            if i["Delay"] != 0:
                delayFileName = '.'.join((self.__fileName, "chn%s" % ("" if idx_i == 0 else idx_i), "delay"))
                with open(delayFileName, 'w') as output:
                    output.write(str(i["Delay"]))
            for idx_j, j in enumerate(i["Files"]):
                outFileNameList = [self.__fileName, "chn%s" % ("" if idx_i == 0 else idx_i), str(j["Ext"])]
                if len(i["Files"]) != 1:
                    outFileNameList.insert(2, str(idx_j))
                outFileName = '.'.join(outFileNameList)
                dLink = j["Link"]
                print(dLink)
                response = urlopen(dLink)
                backF = response.read()
                with open(outFileName,'wb') as output:
                    output.write(backF)
            
    def __init__(self, params):
        '''
        Constructor
        '''
        self.__fileName = params
        
