from pyeventbus import *
from timeit import default_timer as timer
import numpy
import sys

class Events:
    class EventFromA:
        def __init__(self, msg):
            self.msg = msg
        def getMessage(self):
            return self.msg
    class EventFromB:
        def __init__(self, msg):
            self.msg = msg
        def getMessage(self):
            return self.msg
    class CPUHeavyTestEvent:
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

    class CPUHeavyTestEventBG:
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

    class CPUHeavyTestEventGreenlet:
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

    class CPUHeavyTestEventParallel:
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

    class CPUHeavyTestEventConcurrent:
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

    def startCPUHeavyTestInMain(self):
        event = Events.CPUHeavyTestEvent()
        event.setStart(timer())
        start = timer()
        PyBus.Instance().post(event)
        print("{} got control back in {} seconds.".format('startCPUHeavyTestInMain: ', timer() - start))

    def startCPUHeavyTestInBackground(self):
        event = Events.CPUHeavyTestEventBG()
        event.setStart(timer())
        start = timer()
        PyBus.Instance().post(event)
        print("{} got control back in {} seconds.".format('startCPUHeavyTestInBackground: ', timer() - start))

    def startCPUHeavyTestInGreenlet(self):
        event = Events.CPUHeavyTestEventGreenlet()
        event.setStart(timer())
        start = timer()
        PyBus.Instance().post(event)
        print("{} got control back in {} seconds.".format('startCPUHeavyTestInGreenlet: ', timer() - start))

    def startCPUHeavyTestInParallel(self):
        event = Events.CPUHeavyTestEventParallel()
        event.setStart(timer())
        start = timer()
        PyBus.Instance().post(event)
        print("{} got control back in {} seconds.".format('startCPUHeavyTestInParallel: ', timer() - start))

    def startCPUHeavyTestInConcurrent(self):
        event = Events.CPUHeavyTestEventConcurrent()
        event.setStart(timer())
        start = timer()
        PyBus.Instance().post(event)
        print("{} got control back in {} seconds.".format('startCPUHeavyTestInConcurrent: ', timer() - start))

class PerformanceExecuter:
    def __init__(self):
        pass
    
    def register(self, bInstance):
        PyBus.Instance().register(bInstance, self.__class__.__name__)

    @subscribe(onEvent=Events.CPUHeavyTestEvent)
    def cpuHeavyTest1(self, event):
        test_arr_1 = numpy.random.randint(0,high=1000,size=10000000)
        test_arr_2 = numpy.random.randint(0,high=1000,size=10000000)
        sorted(test_arr_1)
        sorted(test_arr_2)
        event.setFinish(timer())
        print("{} ran the code in {} seconds.".format('cpuHeavyTest1: Main-thread', event.getDuration()))
    
    @subscribe(threadMode = Mode.BACKGROUND, onEvent=Events.CPUHeavyTestEventBG)
    def cpuHeavyTest2(self, event):
        test_arr_1 = numpy.random.randint(0,high=1000,size=10000000)
        test_arr_2 = numpy.random.randint(0,high=1000,size=10000000)
        sorted(test_arr_1)
        sorted(test_arr_2)
        event.setFinish(timer())
        print("{} ran the code in {} seconds.".format('cpuHeavyTest2: Background-thread', event.getDuration()))

    @subscribe(threadMode = Mode.GREENLET, onEvent=Events.CPUHeavyTestEventGreenlet)
    def cpuHeavyTest3(self, event):
        test_arr_1 = numpy.random.randint(0,high=1000,size=10000000)
        test_arr_2 = numpy.random.randint(0,high=1000,size=10000000)
        sorted(test_arr_1)
        sorted(test_arr_2)
        event.setFinish(timer())
        print("{} ran the code in {} seconds.".format('cpuHeavyTest3: Greenlet', event.getDuration()))

    @subscribe(threadMode = Mode.PARALLEL, onEvent=Events.CPUHeavyTestEventParallel)
    def cpuHeavyTest4(self, event):
        test_arr_1 = numpy.random.randint(0,high=1000,size=10000000)
        test_arr_2 = numpy.random.randint(0,high=1000,size=10000000)
        sorted(test_arr_1)
        sorted(test_arr_2)
        event.setFinish(timer())
        print("{} ran the code in {} seconds.".format('cpuHeavyTest4: parallel', event.getDuration()))

    @subscribe(threadMode = Mode.CONCURRENT, onEvent=Events.CPUHeavyTestEventConcurrent)
    def cpuHeavyTest5(self, event):
        test_arr_1 = numpy.random.randint(0,high=1000,size=10000000)
        test_arr_2 = numpy.random.randint(0,high=1000,size=10000000)
        sorted(test_arr_1)
        sorted(test_arr_2)
        event.setFinish(timer())
        print("{} ran the code in {} seconds.".format('cpuHeavyTest5: Concurrent', event.getDuration()))

    @subscribe(onEvent=Events.CPUHeavyTestEvent)
    def cpuHeavyTest6(self, event):
        test_arr_1 = numpy.random.randint(0,high=1000,size=10000000)
        test_arr_2 = numpy.random.randint(0,high=1000,size=10000000)
        sorted(test_arr_1)
        sorted(test_arr_2)
        event.setFinish(timer())
        print("{} ran the code in {} seconds.".format('cpuHeavyTest6: Main-thread', event.getDuration()))
    
    @subscribe(threadMode = Mode.BACKGROUND, onEvent=Events.CPUHeavyTestEventBG)
    def cpuHeavyTest7(self, event):
        test_arr_1 = numpy.random.randint(0,high=1000,size=10000000)
        test_arr_2 = numpy.random.randint(0,high=1000,size=10000000)
        sorted(test_arr_1)
        sorted(test_arr_2)
        event.setFinish(timer())
        print("{} ran the code in {} seconds.".format('cpuHeavyTest7: Background-thread', event.getDuration()))

    @subscribe(threadMode = Mode.GREENLET, onEvent=Events.CPUHeavyTestEventGreenlet)
    def cpuHeavyTest8(self, event):
        test_arr_1 = numpy.random.randint(0,high=1000,size=10000000)
        test_arr_2 = numpy.random.randint(0,high=1000,size=10000000)
        sorted(test_arr_1)
        sorted(test_arr_2)
        event.setFinish(timer())
        print("{} ran the code in {} seconds.".format('cpuHeavyTest8: Greenlet', event.getDuration()))

    @subscribe(threadMode = Mode.PARALLEL, onEvent=Events.CPUHeavyTestEventParallel)
    def cpuHeavyTest9(self, event):
        test_arr_1 = numpy.random.randint(0,high=1000,size=10000000)
        test_arr_2 = numpy.random.randint(0,high=1000,size=10000000)
        sorted(test_arr_1)
        sorted(test_arr_2)
        event.setFinish(timer())
        print("{} ran the code in {} seconds.".format('cpuHeavyTest9: parallel', event.getDuration()))

    @subscribe(threadMode = Mode.CONCURRENT, onEvent=Events.CPUHeavyTestEventConcurrent)
    def cpuHeavyTest10(self, event):
        test_arr_1 = numpy.random.randint(0,high=1000,size=10000000)
        test_arr_2 = numpy.random.randint(0,high=1000,size=10000000)
        sorted(test_arr_1)
        sorted(test_arr_2)
        event.setFinish(timer())
        print("{} ran the code in {} seconds.".format('cpuHeavyTest10: Concurrent', event.getDuration()))

    @subscribe(onEvent=Events.CPUHeavyTestEvent)
    def cpuHeavyTest11(self, event):
        test_arr_1 = numpy.random.randint(0,high=1000,size=10000000)
        test_arr_2 = numpy.random.randint(0,high=1000,size=10000000)
        sorted(test_arr_1)
        sorted(test_arr_2)
        event.setFinish(timer())
        print("{} ran the code in {} seconds.".format('cpuHeavyTest11: Main-thread', event.getDuration()))
    
    @subscribe(threadMode = Mode.BACKGROUND, onEvent=Events.CPUHeavyTestEventBG)
    def cpuHeavyTest12(self, event):
        test_arr_1 = numpy.random.randint(0,high=1000,size=10000000)
        test_arr_2 = numpy.random.randint(0,high=1000,size=10000000)
        sorted(test_arr_1)
        sorted(test_arr_2)
        event.setFinish(timer())
        print("{} ran the code in {} seconds.".format('cpuHeavyTest12: Background-thread', event.getDuration()))

    @subscribe(threadMode = Mode.GREENLET, onEvent=Events.CPUHeavyTestEventGreenlet)
    def cpuHeavyTest13(self, event):
        test_arr_1 = numpy.random.randint(0,high=1000,size=10000000)
        test_arr_2 = numpy.random.randint(0,high=1000,size=10000000)
        sorted(test_arr_1)
        sorted(test_arr_2)
        event.setFinish(timer())
        print("{} ran the code in {} seconds.".format('cpuHeavyTest13: Greenlet', event.getDuration()))

    @subscribe(threadMode = Mode.PARALLEL, onEvent=Events.CPUHeavyTestEventParallel)
    def cpuHeavyTest14(self, event):
        test_arr_1 = numpy.random.randint(0,high=1000,size=10000000)
        test_arr_2 = numpy.random.randint(0,high=1000,size=10000000)
        sorted(test_arr_1)
        sorted(test_arr_2)
        event.setFinish(timer())
        print("{} ran the code in {} seconds.".format('cpuHeavyTest14: parallel', event.getDuration()))

    @subscribe(threadMode = Mode.CONCURRENT, onEvent=Events.CPUHeavyTestEventConcurrent)
    def cpuHeavyTest15(self, event):
        test_arr_1 = numpy.random.randint(0,high=1000,size=10000000)
        test_arr_2 = numpy.random.randint(0,high=1000,size=10000000)
        sorted(test_arr_1)
        sorted(test_arr_2)
        event.setFinish(timer())
        print("{} ran the code in {} seconds.".format('cpuHeavyTest15: Concurrent', event.getDuration()))


if __name__ == '__main__':

    tester = PerformanceTester()
    tester.register(tester)

    executer = PerformanceExecuter()
    executer.register(executer)

    print sys.argv[1:][0]
    arg = sys.argv[1:][0]
    if arg == 'startCPUHeavyTestInMain': tester.startCPUHeavyTestInMain()
    elif arg == 'startCPUHeavyTestInBackground': tester.startCPUHeavyTestInBackground()
    elif arg == 'startCPUHeavyTestInGreenlet': tester.startCPUHeavyTestInGreenlet()
    elif arg == 'startCPUHeavyTestInParallel': tester.startCPUHeavyTestInParallel()
    elif arg == 'startCPUHeavyTestInConcurrent': tester.startCPUHeavyTestInConcurrent()
    


# tester.startCPUHeavyTestInMain()
# tester.startCPUHeavyTestInBackground()
# tester.startCPUHeavyTestInGreenlet()
# tester.startCPUHeavyTestInParallel()
# tester.startCPUHeavyTestInConcurrent()
