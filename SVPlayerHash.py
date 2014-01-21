#!/usr/bin/env python
'''
Created on Jan 20, 2014

@author: magic282

https://docs.google.com/document/d/1w5MCBO61rKQ6hI5m9laJLWse__yTYdRugpVyz4RzrmM/preview
'''

import os
import hashlib


class SVPlayerHash(object):
    '''
    classdocs
    '''

    @staticmethod
    def ComputeFileHash(fileName):
        ret = ""
        try:
            vfile = open(fileName, "rb")
        except IOError:
            print("Cannot read file %s" % fileName)

        statinfo = os.stat(fileName)
        fLength = statinfo.st_size

        ret = []
        for i in (4096, int(fLength/3)*2, int(fLength/3), fLength-8192):
            vfile.seek(i, 0)
            bBuf = vfile.read(4096)
            ret.append(hashlib.md5(bBuf).hexdigest())
        vfile.close()
        return ';'.join(ret)

    def __init__(self, params):
        '''
        Constructor
        '''
