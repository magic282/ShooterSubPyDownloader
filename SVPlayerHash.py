'''
Created on Jan 20, 2014

@author: magic282

https://docs.google.com/document/d/1w5MCBO61rKQ6hI5m9laJLWse__yTYdRugpVyz4RzrmM/preview
'''

import os
import md5

class SVPlayerHash(object):
    '''
    classdocs
    '''

    @staticmethod
    def  ComputerFileHash(fileName):
        ret = ""
        try:
            vfile = open(fileName, "rb")
        except IOError:
            print("Cannot read file " + fileName)
        
        statinfo = os.stat(fileName)
        fLength = statinfo.st_size
                
        offset = [0] * 4
        offset[3] = fLength - 8 * 1024
        offset[2] = fLength / 3
        offset[1] = fLength / 3 * 2
        offset[0] = 4 * 1024
        
        for i in range(4):
            vfile.seek(offset[i], 0)
            bBuf = vfile.read(1024 * 4)
            m = md5.new()
            m.update(bBuf)
            if i != 0 :
                ret += ";"
            ret += m.hexdigest()
        vfile.close()
        return ret

    def __init__(self, params):
        '''
        Constructor
        '''
        