from PyBus import *
import time
import threading
import numpy.random
from datetime import datetime
import os

from InteractorEvents import *
class Interactor:
    'Interactor class always on Background Thread'

    def __init__(self):
        self.bus = PyBus.Instance()
    

    def register(self, interactorInstance):
        self.bus.register(interactorInstance, self.__class__.__name__)

    def bigFunc(self):
        test_arr_1 = numpy.random.randint(0,high=1000,size=1000000)
        test_arr_2 = numpy.random.randint(0,high=1000,size=1000000)
        self.sort_arrays(test_arr_1, test_arr_2)

    def sort_arrays(self, a1, a2):
        sorted(a1)
        sorted(a2)

    @subscribe(threadMode=Mode.CONCURRENT, onEvent = InteractorEvents.ComplexCalculationInBackgroundThreadEvent)
    def performComplexCalculationInMainThread(self, event):
        # print 'current thread: for performComplexCalculationInMainThread', threading.currentThread().getName()
        # print 'PID:', os.getpid()
        # for line in open("/proc/%d/status" % pid).readlines():
        #     if line.startswith("State:"):
        #         print line.split(":",1)[1].strip().split(' ')[0]
        # print 'starting long task at:', str(datetime.now())
        test_arr_1 = numpy.random.randint(0,high=1000,size=10000000)
        test_arr_2 = numpy.random.randint(0,high=1000,size=10000000)
        sorted(test_arr_1)
        sorted(test_arr_2)
        # print 'finished long task at:', str(datetime.now())
        
        PyBus.Instance().post(InteractorEvents.PresentInformation("present this from performComplexCalculationInMainThread"))
        # for line in open("/proc/%d/status" % pid).readlines():
        #     if line.startswith("State:"):
        #         print line.split(":",1)[1].strip().split(' ')[0]
        

    @subscribe(threadMode=Mode.CONCURRENT, onEvent = InteractorEvents.ComplexCalculationInBackgroundThreadEvent)
    def performComplexCalculationInBackgroundThread(self, event):
        # print 'current thread for performComplexCalculationInBackgroundThread:', threading.currentThread().getName()
        # print 'PID:', os.getpid()
        # for line in open("/proc/%d/status" % pid).readlines():
        #     if line.startswith("State:"):
        #         print line.split(":",1)[1].strip().split(' ')[0]
        # print 'starting long task at:', str(datetime.now())
        test_arr_1 = numpy.random.randint(0,high=1000,size=10000000)
        test_arr_2 = numpy.random.randint(0,high=1000,size=10000000)
        sorted(test_arr_1)
        sorted(test_arr_2)
        # print 'finished long task at:', str(datetime.now())
        PyBus.Instance().post(InteractorEvents.PresentInformation("present this from performComplexCalculationInBackgroundThread"))
        # for line in open("/proc/%d/status" % pid).readlines():
        #     if line.startswith("State:"):
        #         print line.split(":",1)[1].strip().split(' ')[0]

    # @subscribe(threadMode=Mode.ASYNC, onEvent = InteractorEvents.ComplexCalculationInBackgroundThreadEvent)
    # def performComplexCalculationInDefaultThread(self, event):
    #     for i in range(0,10):
    #         print 'current thread for default:', threading.currentThread().getName()
    #         print event.getMessage(), " index: ", i
        
    # @subscribe(threadMode=Mode.ASYNC, onEvent = InteractorEvents.ComplexCalculationInBackgroundThreadEvent)
    # def performComplexCalculationInDefaultThread2(self, event):
    #     for i in range(0,10):
    #         print 'current thread for default2:', threading.currentThread().getName()
    #         print event.getMessage(), " index: ", i


    # @subscribe(threadMode="Main", onEvent = InteractorEvents.ComplexCalculationInMainThreadEvent)
    # def performComplexCalculationInPostingThread(self, event):
    #     print 'inside performComplexCalculationInPostingThread', event.getMessage()
    #     return 'inside performComplexCalculationInPostingThread'
    # @tags("p")
    # def get_text(name):
    #     return "Hello "+name

if __name__ == "__main__":
    pass