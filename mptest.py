# -*- coding: utf-8 -*-
"""
Created on Wed Jun 14 16:12:35 2017

@author: sheila
"""

import multiprocessing
import time
import numpy as np

def funSquare(num):
    return num ** 2

if __name__ == '__main__':
    nums=range(30000)
    tic0 = time.clock()
    poola = multiprocessing.Pool(1) #initializes N workers, where N = # of CPU cores
    poolb = multiprocessing.Pool(3) #initializes N workers, where N = # of CPU cores
    toc0 = time.clock()
    tic1 = time.clock()
    results1 = poola.map(funSquare, nums)
    toc1 = time.clock()
    tic2 = time.clock()
    results12 = poolb.map(funSquare, nums)
    toc2 = time.clock()
    tic3 = time.clock()
    resultsseq = map(funSquare, nums)
    toc3 = time.clock()
    tic4 = time.clock()
    resultsman = funSquare(np.array(nums))
    toc4 = time.clock()
    print('Pool setup time: %r' % (toc0 - tic0))
    print('Parallel processing time (1, 3 proc): %r %r\nSerial processing time (map, manual): %r %r'
          % (toc1 - tic1, toc2 - tic2, toc3 - tic3, toc4 - tic4))