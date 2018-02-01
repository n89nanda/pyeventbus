from Singleton import *
import thread
import threading
import time, sys
from Queue import Queue
from threading import Thread
from multiprocessing.dummy import Pool as ThreadPool
import multiprocessing
import gevent, os
exitFlag = 0

@Singleton
class PyBus:
    'PyBus class'

    subscribers = {}
    pending_events = []
    threadModes = []
    events = []
    methods = []

    evnts_method = {}
    method_mode = {}




    def __init__(self):
        self.common_background_thread = PyBusAsyncThread(0, "PyBusBackgroundThread", 1)
        self.queue = Queue(maxsize=0)
        self.num_threads = 2000
        for i in range(self.num_threads):
            worker =Thread (target=self.do_stuff, args=(self.queue,))
            worker.setDaemon(True)
            worker.start()

    def do_stuff(self, q):
        while True:
            print q.get()
            q.task_done()

    def register(self, subscriber=None, subscriber_key=None):
        self.subscribers[subscriber_key] = subscriber
    
    def post(self, event):
        self.pending_events.append(event)
        self.execute()
        

    def execute(self):
        i = 0
        for event in self.pending_events:
            self.pending_events.remove(event)
            if event.__class__ in self.evnts_method:
                for method in self.evnts_method[event.__class__]:
                    i += 1
                    for subscriber in self.subscribers.values():
                        if method.__name__ in dir(subscriber):
                            mode = self.method_mode.get(method)
                            print 'executing ', method.__name__, ' in mode: ', mode
                            print 'PID:', os.getpid()
                            if mode == 0:
                                method(self, event)
                            else:
                                try:
                                    threadName = "thread-" + method.__name__
                                    if mode == 4:
                                        PyBusAsyncThread(i, threadName, 1, method, event).start()
                                    elif mode == 1:
                                        self.queue.put(PyBusAsyncThread(i, threadName, 1, method, event).start())
                                    elif mode == 5:
                                        p = multiprocessing.Process(target=method, args=(self, event,))
                                        p.start()
                                    elif mode == 3:
                                        print 'spawning'
                                        gevent.spawn(method(self, event))
    
                                        # gevent.joinall([gevent.spawn(method(self, event))])
                                        
                                except:
                                    print 'Error: unable to start thread: ', sys.exc_info()[0]
                            #method(self, event)
            else:
                print 'No Subscribers for posted event'
                raise Exception('Could not find subscriber for posted event', event)
    
        # # Create new threads
        # thread1 = myThread(1, "Thread-1", 1)
        # thread2 = myThread(2, "Thread-2", 2)

        # # Start new Threads
        # thread1.start()
        # thread2.start()

    def subscriber(self, decorator):
        pass

    def addThread(self, threadMode):
        self.threadModes.append(threadMode)

    def addEvents(self, events):
        self.events.append(events)

    def addsubscribeMethods(self, methods):
        self.methods.append(methods)

    def addEventsWithMethods(self, event, method, threadMode):
        self.method_mode[method] = threadMode
        if event in self.evnts_method:
            print 'subscribers exist for event', event
            print 'number of subscribers=', len(self.evnts_method.get(event))
            subscribedMethodsForEvent = self.evnts_method.get(event)
            subscribedMethodsForEvent.append(method)
            for method in self.evnts_method.get(event):
                self.evnts_method[event] = subscribedMethodsForEvent
        else:
            self.evnts_method[event] = [method]
            
        
       


if __name__ == '__main__':
    pass


class Mode:
        MAIN = 0 
        BACKGROUNDQUEUE = 1 
        GREENLET = 3
        ASYNC = 4 
        CONCURRENT = 5

        def __init__(self):
            pass


class PyBusAsyncThread (threading.Thread):
    def __init__(self, threadID, name, counter, method=None, event=None):
       threading.Thread.__init__(self)
       self.threadID = threadID
       self.name = name
       self.counter = counter
       self.method = method
       self.event = event
    
    def add(self, method, event):
        self.method = method
        self.event = event
        print 'added'
    

    def run(self):
        print "Starting " + self.name
        self.method(self, self.event)
        print "Exiting " + self.name


from PyBus import Mode
def subscribe(threadMode = Mode.MAIN, onEvent = None):
    bus = PyBus.Instance()
    def real_decorator(function):
        bus.addsubscribeMethods(function)
        bus.addEvents(onEvent)
        bus.addThread(threadMode)
        bus.addEventsWithMethods(onEvent, function, threadMode)
        def wrapper(*args, **kwargs):
            return function(*args, **kwargs)    
        return wrapper
    return real_decorator

