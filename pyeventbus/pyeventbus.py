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
    
    subscribers = {}
    pending_events = []
    event_method = {}
    method_mode = {}

    def __init__(self):
        self.common_background_thread = PyBusThread(0, "PyBusBackgroundThread", 1)
        self.queue = Queue(maxsize=0)
        self.num_threads = 2000
        for worker in [lambda: self.startWorkers() for i in range(self.num_threads)]: worker()
        

    def startWorkers(self):
        worker =Thread (target=self.monitorQueue, args=(self.queue,))
        worker.setDaemon(True)
        worker.start()

    def monitorQueue(self, q):
        while True:
            q.get()
            q.task_done()

    def register(self, subscriber=None, subscriber_key=None):
        self.subscribers[subscriber_key] = subscriber
    
    def post(self, event):
        self.pending_events.append(event)
        self.execute()
        
    def DoesSubscribersContainThisMethod(self, method, subscriber):
        return True if method.__name__ in dir(subscriber) else False


    def call(self, method, withEvent, inMode, subscriber):
        from random import randint
        if inMode == 0: method(subscriber, withEvent) 
        else:
            try:
                threadName = "thread-" + method.__name__
                if inMode == 4: PyBusThread(randint(1,100), threadName, 1, method, withEvent, subscriber).start()
                elif inMode == 1: self.queue.put(PyBusThread(randint(1,100), threadName, 1, method, withEvent, subscriber).start())
                elif inMode == 5: multiprocessing.Process(target=method, args=(subscriber, withEvent,)).start()
                elif inMode == 3: gevent.spawn(method(subscriber, withEvent))                    
            except:
                raise Exception('Unable to start thread for method: ', method, ' with event: ', withEvent)

    def execute(self):
        for event in self.pending_events:
            self.pending_events.remove(event)
            if event.__class__ in self.event_method:
                for method in self.event_method[event.__class__]:
                    subscribersContainingThisMethod = filter(lambda subscriber: self.DoesSubscribersContainThisMethod(method, subscriber), self.subscribers.values())
                    for subscriber in subscribersContainingThisMethod:
                        self.call(method=method, withEvent=event, inMode=self.method_mode.get(method), subscriber=subscriber)
            else:
                raise Exception('Could not find subscriber for posted event', event)

    def addEventsWithMethods(self, event, method, threadMode):
        self.method_mode[method] = threadMode
        if event in self.event_method: 
            subscribedMethodsForEvent = self.event_method.get(event)
            subscribedMethodsForEvent.append(method)
            for method in self.event_method.get(event):
                self.event_method[event] = subscribedMethodsForEvent
        else:
            self.event_method[event] = [method]
            
        
       


if __name__ == '__main__':
    pass


class Mode:
        POSTING = 0 
        BACKGROUND = 1 
        GREENLET = 3
        PARALLEL = 4 
        CONCURRENT = 5

        def __init__(self):
            pass


class PyBusThread (threading.Thread):
    def __init__(self, threadID, name=None, counter=None, method=None, event=None, subscriber=None):
       threading.Thread.__init__(self)
       self.threadID = threadID
       self.name = name
       self.counter = counter
       self.method = method
       self.event = event
       self.subscriber = subscriber

    def run(self):
        self.method(self.subscriber, self.event)

from pyeventbus import Mode
def subscribe(threadMode = Mode.POSTING, onEvent = None):
    bus = PyBus.Instance()
    def real_decorator(function):
        bus.addEventsWithMethods(onEvent, function, threadMode)
        def wrapper(*args, **kwargs):
            return function(*args, **kwargs)    
        return wrapper
    return real_decorator

