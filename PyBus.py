from Singleton import *
import thread
import threading
import time
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
        pass

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
                            try:
                                threadName = "thread-" + str(i)
                                mode = self.method_mode.get(method)
                                print 'executing ', method.__name__, ' in mode: ', mode
                                if mode == 2:
                                    method(self, event)
                                elif mode == 4:
                                    PyBusAsyncThread(i, threadName, 1, method, event).start()
                                else:
                                    method(self, event)
                            except:
                                print 'Error: unable to start thread'
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
        MAIN = 0 # ONLY IN PYTHON 2.7
        BACKGROUND = 1 
        POSTING = 2 #DEFAULT
        CONCURRENT = 3
        ASYNC = 4 #SPAWN NEW THREAD
        #THREADPOOL = 5

        def __init__(self):
            pass


class PyBusAsyncThread (threading.Thread):
   def __init__(self, threadID, name, counter, method, event):
       threading.Thread.__init__(self)
       self.threadID = threadID
       self.name = name
       self.counter = counter
       self.method = method
       self.event = event
   def run(self):
      print "Starting " + self.name
      self.method(self, self.event)
      print "Exiting " + self.name


from PyBus import Mode
def subscribe(threadMode = Mode.POSTING, onEvent = None):
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

