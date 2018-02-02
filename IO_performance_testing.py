from pyeventbus import *
from timeit import default_timer as timer
import numpy
import sys
from os import getcwd
import json

class Events:
    class IOHeavyTestEvent:
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

    class IOHeavyTestEventBG:
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

    class IOHeavyTestEventGreenlet:
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

    class IOHeavyTestEventParallel:
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

    class IOHeavyTestEventConcurrent:
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

    def startIOHeavyTestInMain(self):
        event = Events.IOHeavyTestEvent()
        event.setStart(timer())
        start = timer()
        PyBus.Instance().post(event)
        print("{} got control back in {} seconds.".format('startIOHeavyTestInMain: ', timer() - start))

    def startIOHeavyTestInBackground(self):
        event = Events.IOHeavyTestEventBG()
        event.setStart(timer())
        start = timer()
        PyBus.Instance().post(event)
        print("{} got control back in {} seconds.".format('startIOHeavyTestInBackground: ', timer() - start))

    def startIOHeavyTestInGreenlet(self):
        event = Events.IOHeavyTestEventGreenlet()
        event.setStart(timer())
        start = timer()
        PyBus.Instance().post(event)
        print("{} got control back in {} seconds.".format('startIOHeavyTestInGreenlet: ', timer() - start))

    def startIOHeavyTestInParallel(self):
        event = Events.IOHeavyTestEventParallel()
        event.setStart(timer())
        start = timer()
        PyBus.Instance().post(event)
        print("{} got control back in {} seconds.".format('startIOHeavyTestInParallel: ', timer() - start))

    def startIOHeavyTestInConcurrent(self):
        event = Events.IOHeavyTestEventConcurrent()
        event.setStart(timer())
        start = timer()
        PyBus.Instance().post(event)
        print("{} got control back in {} seconds.".format('startIOHeavyTestInConcurrent: ', timer() - start))

class PerformanceExecuter:
    def __init__(self):
        pass
    
    def register(self, bInstance):
        PyBus.Instance().register(bInstance, self.__class__.__name__)

    @subscribe(onEvent=Events.IOHeavyTestEvent)
    def IOHeavyTest1(self, event):
        for i in range(3000):
            with open('{}/generated.json'.format(getcwd())) as f:
                data = json.load(f)

        event.setFinish(timer())
        print("{} ran the code in {} seconds.".format('IOHeavyTest1: Main-thread', event.getDuration()))
    
    @subscribe(threadMode = Mode.BACKGROUND, onEvent=Events.IOHeavyTestEventBG)
    def IOHeavyTest2(self, event):
        for i in range(3000):
            with open('{}/generated.json'.format(getcwd())) as f:
                data = json.load(f)
        event.setFinish(timer())
        print("{} ran the code in {} seconds.".format('IOHeavyTest2: Background-thread', event.getDuration()))

    @subscribe(threadMode = Mode.GREENLET, onEvent=Events.IOHeavyTestEventGreenlet)
    def IOHeavyTest3(self, event):
        for i in range(3000):
            with open('{}/generated.json'.format(getcwd())) as f:
                data = json.load(f)
        event.setFinish(timer())
        print("{} ran the code in {} seconds.".format('IOHeavyTest3: Greenlet', event.getDuration()))

    @subscribe(threadMode = Mode.PARALLEL, onEvent=Events.IOHeavyTestEventParallel)
    def IOHeavyTest4(self, event):
        for i in range(3000):
            with open('{}/generated.json'.format(getcwd())) as f:
                data = json.load(f)
        event.setFinish(timer())
        print("{} ran the code in {} seconds.".format('IOHeavyTest4: parallel', event.getDuration()))

    @subscribe(threadMode = Mode.CONCURRENT, onEvent=Events.IOHeavyTestEventConcurrent)
    def IOHeavyTest5(self, event):
        for i in range(3000):
            with open('{}/generated.json'.format(getcwd())) as f:
                data = json.load(f)
        event.setFinish(timer())
        print("{} ran the code in {} seconds.".format('IOHeavyTest5: Concurrent', event.getDuration()))

    @subscribe(onEvent=Events.IOHeavyTestEvent)
    def IOHeavyTest6(self, event):
        for i in range(3000):
            with open('{}/generated.json'.format(getcwd())) as f:
                data = json.load(f)
        event.setFinish(timer())
        print("{} ran the code in {} seconds.".format('IOHeavyTest6: Main-thread', event.getDuration()))
    
    @subscribe(threadMode = Mode.BACKGROUND, onEvent=Events.IOHeavyTestEventBG)
    def IOHeavyTest7(self, event):
        for i in range(3000):
            with open('{}/generated.json'.format(getcwd())) as f:
                data = json.load(f)
        event.setFinish(timer())
        print("{} ran the code in {} seconds.".format('IOHeavyTest7: Background-thread', event.getDuration()))

    @subscribe(threadMode = Mode.GREENLET, onEvent=Events.IOHeavyTestEventGreenlet)
    def IOHeavyTest8(self, event):
        for i in range(3000):
            with open('{}/generated.json'.format(getcwd())) as f:
                data = json.load(f)
        event.setFinish(timer())
        print("{} ran the code in {} seconds.".format('IOHeavyTest8: Greenlet', event.getDuration()))

    @subscribe(threadMode = Mode.PARALLEL, onEvent=Events.IOHeavyTestEventParallel)
    def IOHeavyTest9(self, event):
        for i in range(3000):
            with open('{}/generated.json'.format(getcwd())) as f:
                data = json.load(f)
        event.setFinish(timer())
        print("{} ran the code in {} seconds.".format('IOHeavyTest9: parallel', event.getDuration()))

    @subscribe(threadMode = Mode.CONCURRENT, onEvent=Events.IOHeavyTestEventConcurrent)
    def IOHeavyTest10(self, event):
        for i in range(3000):
            with open('{}/generated.json'.format(getcwd())) as f:
                data = json.load(f)
        event.setFinish(timer())
        print("{} ran the code in {} seconds.".format('IOHeavyTest10: Concurrent', event.getDuration()))

    @subscribe(onEvent=Events.IOHeavyTestEvent)
    def IOHeavyTest11(self, event):
        for i in range(3000):
            with open('{}/generated.json'.format(getcwd())) as f:
                data = json.load(f)
        event.setFinish(timer())
        print("{} ran the code in {} seconds.".format('IOHeavyTest11: Main-thread', event.getDuration()))
    
    @subscribe(threadMode = Mode.BACKGROUND, onEvent=Events.IOHeavyTestEventBG)
    def IOHeavyTest12(self, event):
        for i in range(3000):
            with open('{}/generated.json'.format(getcwd())) as f:
                data = json.load(f)
        event.setFinish(timer())
        print("{} ran the code in {} seconds.".format('IOHeavyTest12: Background-thread', event.getDuration()))

    @subscribe(threadMode = Mode.GREENLET, onEvent=Events.IOHeavyTestEventGreenlet)
    def IOHeavyTest13(self, event):
        for i in range(3000):
            with open('{}/generated.json'.format(getcwd())) as f:
                data = json.load(f)
        event.setFinish(timer())
        print("{} ran the code in {} seconds.".format('IOHeavyTest13: Greenlet', event.getDuration()))

    @subscribe(threadMode = Mode.PARALLEL, onEvent=Events.IOHeavyTestEventParallel)
    def IOHeavyTest14(self, event):
        for i in range(3000):
            with open('{}/generated.json'.format(getcwd())) as f:
                data = json.load(f)
        event.setFinish(timer())
        print("{} ran the code in {} seconds.".format('IOHeavyTest14: parallel', event.getDuration()))

    @subscribe(threadMode = Mode.CONCURRENT, onEvent=Events.IOHeavyTestEventConcurrent)
    def IOHeavyTest15(self, event):
        for i in range(3000):
            with open('{}/generated.json'.format(getcwd())) as f:
                data = json.load(f)
        event.setFinish(timer())
        print("{} ran the code in {} seconds.".format('IOHeavyTest15: Concurrent', event.getDuration()))


if __name__ == '__main__':

    tester = PerformanceTester()
    tester.register(tester)

    executer = PerformanceExecuter()
    executer.register(executer)

    print sys.argv[1:][0]
    arg = sys.argv[1:][0]
    if arg == 'startIOHeavyTestInMain': tester.startIOHeavyTestInMain()
    elif arg == 'startIOHeavyTestInBackground': tester.startIOHeavyTestInBackground()
    elif arg == 'startIOHeavyTestInGreenlet': tester.startIOHeavyTestInGreenlet()
    elif arg == 'startIOHeavyTestInParallel': tester.startIOHeavyTestInParallel()
    elif arg == 'startIOHeavyTestInConcurrent': tester.startIOHeavyTestInConcurrent()
    


# tester.startIOHeavyTestInMain()
# tester.startIOHeavyTestInBackground()
# tester.startIOHeavyTestInGreenlet()
# tester.startIOHeavyTestInParallel()
# tester.startIOHeavyTestInConcurrent()
