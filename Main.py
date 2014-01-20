'''
Created on Jan 20, 2014

@author: magic282
'''
import sys
from Shooter import Shooter

if __name__ == '__main__':
    print("Welcome to ShooterSubPyDownloader")
    
    fileNames = sys.argv[1:];
    
    for f in fileNames:
        shooter = Shooter(f)
        shooter.start()
    