from pyeventbus import *

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

class A:
    def __init__(self):
        self.bus = PyBus.Instance()
        pass

    def register(self, aInstance):
        self.bus.register(aInstance, self.__class__.__name__)

    def post(self):
        self.bus.post(Events.EventFromA("EventFromA"))
    
    @subscribe(onEvent=Events.EventFromB)
    def readEventFromB(self, event):
        print 'Class A', event.getMessage()

class B:
    def __init__(self):
        self.bus = PyBus.Instance()
        pass
    
    def register(self, bInstance):
        self.bus.register(bInstance, self.__class__.__name__)

    @subscribe(onEvent=Events.EventFromA)
    def readEventFromA(self, event):
        print 'Class B:', event.getMessage()
    
    def post(self):
        self.bus.post(Events.EventFromB("EventFromB"))



a = A()
a.register(a)

b = B()
b.register(b)

a.post()
b.post()
