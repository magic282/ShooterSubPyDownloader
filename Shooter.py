'''
Created on Jan 20, 2014

@author: magic282
'''

from SVPlayerHash import SVPlayerHash
import urllib, urllib2
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
        self.__videoHash = SVPlayerHash.ComputerFileHash(self.__fileName)
        values = dict(filehash = self.__videoHash, pathinfo = self.__fileName, format = "json", lang = "Chn")
        data = urllib.urlencode(values)
        req = urllib2.Request(self.__SHOOTERURL, data)
        rsp = urllib2.urlopen(req)
        content = rsp.read()
        
        jsonContent = json.loads(content)
        for i in range(len(jsonContent)):
            print(jsonContent[i])
            
            if jsonContent[i]["Delay"] != 0:
                delayFileName = self.__fileName + ".chn" +"" if i==0 else str(i) + ".delay"
                output = open(delayFileName, 'w');
                output.write(str(jsonContent[i]["Delay"]))
                output.close()
            for j in range(len(jsonContent[i]["Files"])):
                outFileName = self.__fileName + ".chn" + ("" if i==0 else str(i)) + ("" if (len(jsonContent[i]["Files"]) == 1) else ("." + str(j))) + (".") + (jsonContent[i]["Files"][j]["Ext"])
                dLink = jsonContent[i]["Files"][j]["Link"]
                print(dLink)
                response = urllib2.urlopen(dLink)
                backF = response.read()
                output = open(outFileName,'wb')
                output.write(backF)
                output.close()
            
    def __init__(self, params):
        '''
        Constructor
        '''
        self.__fileName = params
        
