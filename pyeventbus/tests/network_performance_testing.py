from pyeventbus import *
from timeit import default_timer as timer
import numpy
import sys
from os import getcwd
import json
import requests



class Events:
    class NetworkHeavyTestEvent:
        start = 0
        finish = 0
        duration = 0
        def __init__(self):
            pass
        def setStart(self, time):
            self.start = time
        def setFinish(self, time):
            self.finish = time
        def getDuration(self):
            return self.finish - self.start

    class NetworkHeavyTestEventBG:
        start = 0
        finish = 0
        duration = 0
        def __init__(self):
            pass
        def setStart(self, time):
            self.start = time
        def setFinish(self, time):
            self.finish = time
        def getDuration(self):
            return self.finish - self.start

    class NetworkHeavyTestEventGreenlet:
        start = 0
        finish = 0
        duration = 0
        def __init__(self):
            pass
        def setStart(self, time):
            self.start = time
        def setFinish(self, time):
            self.finish = time
        def getDuration(self):
            return self.finish - self.start

    class NetworkHeavyTestEventParallel:
        start = 0
        finish = 0
        duration = 0
        def __init__(self):
            pass
        def setStart(self, time):
            self.start = time
        def setFinish(self, time):
            self.finish = time
        def getDuration(self):
            return self.finish - self.start

    class NetworkHeavyTestEventConcurrent:
        start = 0
        finish = 0
        duration = 0
        def __init__(self):
            pass
        def setStart(self, time):
            self.start = time
        def setFinish(self, time):
            self.finish = time
        def getDuration(self):
            return self.finish - self.start

class PerformanceTester:
    def __init__(self):
        pass

    def register(self, aInstance):
        PyBus.Instance().register(aInstance, self.__class__.__name__)

    def startNetworkHeavyTestInMain(self):
        event = Events.NetworkHeavyTestEvent()
        event.setStart(timer())
        start = timer()
        PyBus.Instance().post(event)
        print("{} got control back in {} seconds.".format('startNetworkHeavyTestInMain: ', timer() - start))

    def startNetworkHeavyTestInBackground(self):
        event = Events.NetworkHeavyTestEventBG()
        event.setStart(timer())
        start = timer()
        PyBus.Instance().post(event)
        print("{} got control back in {} seconds.".format('startNetworkHeavyTestInBackground: ', timer() - start))

    def startNetworkHeavyTestInGreenlet(self):
        event = Events.NetworkHeavyTestEventGreenlet()
        event.setStart(timer())
        start = timer()
        PyBus.Instance().post(event)
        print("{} got control back in {} seconds.".format('startNetworkHeavyTestInGreenlet: ', timer() - start))

    def startNetworkHeavyTestInParallel(self):
        event = Events.NetworkHeavyTestEventParallel()
        event.setStart(timer())
        start = timer()
        PyBus.Instance().post(event)
        print("{} got control back in {} seconds.".format('startNetworkHeavyTestInParallel: ', timer() - start))

    def startNetworkHeavyTestInConcurrent(self):
        event = Events.NetworkHeavyTestEventConcurrent()
        event.setStart(timer())
        start = timer()
        PyBus.Instance().post(event)
        print("{} got control back in {} seconds.".format('startNetworkHeavyTestInConcurrent: ', timer() - start))

class PerformanceExecuter:
    def __init__(self):
        pass
    
    def register(self, bInstance):
        PyBus.Instance().register(bInstance, self.__class__.__name__)

    @subscribe(onEvent=Events.NetworkHeavyTestEvent)
    def NetworkHeavyTest1(self, event):
        for i in range(100): response = requests.get('http://marvel.wikia.com/wiki/Marvel_Database')
        event.setFinish(timer())
        print("{} ran the code in {} seconds.".format('NetworkHeavyTest1: Main-thread', event.getDuration()))
    
    @subscribe(threadMode = Mode.BACKGROUND, onEvent=Events.NetworkHeavyTestEventBG)
    def NetworkHeavyTest2(self, event):
        for i in range(100): response = requests.get('http://marvel.wikia.com/wiki/Marvel_Database')
        event.setFinish(timer())
        print("{} ran the code in {} seconds.".format('NetworkHeavyTest2: Background-thread', event.getDuration()))

    @subscribe(threadMode = Mode.GREENLET, onEvent=Events.NetworkHeavyTestEventGreenlet)
    def NetworkHeavyTest3(self, event):
        for i in range(100): response = requests.get('http://marvel.wikia.com/wiki/Marvel_Database')
        event.setFinish(timer())
        print("{} ran the code in {} seconds.".format('NetworkHeavyTest3: Greenlet', event.getDuration()))

    @subscribe(threadMode = Mode.PARALLEL, onEvent=Events.NetworkHeavyTestEventParallel)
    def NetworkHeavyTest4(self, event):
        for i in range(100): response = requests.get('http://marvel.wikia.com/wiki/Marvel_Database')
        event.setFinish(timer())
        print("{} ran the code in {} seconds.".format('NetworkHeavyTest4: parallel', event.getDuration()))

    @subscribe(threadMode = Mode.CONCURRENT, onEvent=Events.NetworkHeavyTestEventConcurrent)
    def NetworkHeavyTest5(self, event):
        for i in range(100): response = requests.get('http://marvel.wikia.com/wiki/Marvel_Database')
        event.setFinish(timer())
        print("{} ran the code in {} seconds.".format('NetworkHeavyTest5: Concurrent', event.getDuration()))

    @subscribe(onEvent=Events.NetworkHeavyTestEvent)
    def NetworkHeavyTest6(self, event):
        for i in range(100): response = requests.get('http://marvel.wikia.com/wiki/Marvel_Database')
        event.setFinish(timer())
        print("{} ran the code in {} seconds.".format('NetworkHeavyTest6: Main-thread', event.getDuration()))
    
    @subscribe(threadMode = Mode.BACKGROUND, onEvent=Events.NetworkHeavyTestEventBG)
    def NetworkHeavyTest7(self, event):
        for i in range(100): response = requests.get('http://marvel.wikia.com/wiki/Marvel_Database')
        event.setFinish(timer())
        print("{} ran the code in {} seconds.".format('NetworkHeavyTest7: Background-thread', event.getDuration()))

    @subscribe(threadMode = Mode.GREENLET, onEvent=Events.NetworkHeavyTestEventGreenlet)
    def NetworkHeavyTest8(self, event):
        for i in range(100): response = requests.get('http://marvel.wikia.com/wiki/Marvel_Database')
        event.setFinish(timer())
        print("{} ran the code in {} seconds.".format('NetworkHeavyTest8: Greenlet', event.getDuration()))

    @subscribe(threadMode = Mode.PARALLEL, onEvent=Events.NetworkHeavyTestEventParallel)
    def NetworkHeavyTest9(self, event):
        for i in range(100): response = requests.get('http://marvel.wikia.com/wiki/Marvel_Database')
        event.setFinish(timer())
        print("{} ran the code in {} seconds.".format('NetworkHeavyTest9: parallel', event.getDuration()))

    @subscribe(threadMode = Mode.CONCURRENT, onEvent=Events.NetworkHeavyTestEventConcurrent)
    def NetworkHeavyTest10(self, event):
        for i in range(100): response = requests.get('http://marvel.wikia.com/wiki/Marvel_Database')
        event.setFinish(timer())
        print("{} ran the code in {} seconds.".format('NetworkHeavyTest10: Concurrent', event.getDuration()))

    @subscribe(onEvent=Events.NetworkHeavyTestEvent)
    def NetworkHeavyTest11(self, event):
        for i in range(100): response = requests.get('http://marvel.wikia.com/wiki/Marvel_Database')
        event.setFinish(timer())
        print("{} ran the code in {} seconds.".format('NetworkHeavyTest11: Main-thread', event.getDuration()))
    
    @subscribe(threadMode = Mode.BACKGROUND, onEvent=Events.NetworkHeavyTestEventBG)
    def NetworkHeavyTest12(self, event):
        for i in range(100): response = requests.get('http://marvel.wikia.com/wiki/Marvel_Database')
        event.setFinish(timer())
        print("{} ran the code in {} seconds.".format('NetworkHeavyTest12: Background-thread', event.getDuration()))

    @subscribe(threadMode = Mode.GREENLET, onEvent=Events.NetworkHeavyTestEventGreenlet)
    def NetworkHeavyTest13(self, event):
        for i in range(100): response = requests.get('http://marvel.wikia.com/wiki/Marvel_Database')
        event.setFinish(timer())
        print("{} ran the code in {} seconds.".format('NetworkHeavyTest13: Greenlet', event.getDuration()))

    @subscribe(threadMode = Mode.PARALLEL, onEvent=Events.NetworkHeavyTestEventParallel)
    def NetworkHeavyTest14(self, event):
        for i in range(100): response = requests.get('http://marvel.wikia.com/wiki/Marvel_Database')
        event.setFinish(timer())
        print("{} ran the code in {} seconds.".format('NetworkHeavyTest14: parallel', event.getDuration()))

    @subscribe(threadMode = Mode.CONCURRENT, onEvent=Events.NetworkHeavyTestEventConcurrent)
    def NetworkHeavyTest15(self, event):
        for i in range(100): response = requests.get('http://marvel.wikia.com/wiki/Marvel_Database')
        event.setFinish(timer())
        print("{} ran the code in {} seconds.".format('NetworkHeavyTest15: Concurrent', event.getDuration()))


if __name__ == '__main__':

    tester = PerformanceTester()
    tester.register(tester)

    executer = PerformanceExecuter()
    executer.register(executer)

    print sys.argv[1:][0]
    arg = sys.argv[1:][0]
    if arg == 'startNetworkHeavyTestInMain': tester.startNetworkHeavyTestInMain()
    elif arg == 'startNetworkHeavyTestInBackground': tester.startNetworkHeavyTestInBackground()
    elif arg == 'startNetworkHeavyTestInGreenlet': tester.startNetworkHeavyTestInGreenlet()
    elif arg == 'startNetworkHeavyTestInParallel': tester.startNetworkHeavyTestInParallel()
    elif arg == 'startNetworkHeavyTestInConcurrent': tester.startNetworkHeavyTestInConcurrent()
    


# tester.startNetworkHeavyTestInMain()
# tester.startNetworkHeavyTestInBackground()
# tester.startNetworkHeavyTestInGreenlet()
# tester.startNetworkHeavyTestInParallel()
# tester.startNetworkHeavyTestInConcurrent()
