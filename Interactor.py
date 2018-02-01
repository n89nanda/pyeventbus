from PyBus import *
import time

from InteractorEvents import *
class Interactor:
    'Interactor class always on Background Thread'

    def __init__(self):
        self.bus = PyBus.Instance()
    

    def register(self, interactorInstance):
        self.bus.register(interactorInstance, self.__class__.__name__)


    @subscribe(threadMode=Mode.MAIN, onEvent = InteractorEvents.ComplexCalculationInMainThreadEvent)
    def performComplexCalculationInMainThread(self, event):
        for i in range(0,10):
            print  event.getMessage(), " index: ", i

    

    @subscribe(threadMode=Mode.ASYNC, onEvent = InteractorEvents.ComplexCalculationInBackgroundThreadEvent)
    def performComplexCalculationInBackgroundThread(self, event):
        for i in range(0,10):
            print event.getMessage() , " index: ", i
        

    # @subscribe(threadMode=Mode.ASYNC, onEvent = InteractorEvents.ComplexCalculationInBackgroundThreadEvent)
    # def performComplexCalculationInDefaultThread(self, event):
    #     for i in range(0,10):
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