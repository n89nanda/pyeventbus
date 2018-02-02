pyeventbus
=========================

pyeventbus is a publish/subscribe event bus for Android and Java.

+ simplifies the communication between python classes 
+ decouples event senders and receivers
+ performs well threads, greenlets, queues and concurrent processes
+ avoids complex and error-prone dependencies and life cycle issues
+ makes code simpler
+ has advanced features like delivery threads, workers and spawning different processes, etc.

pyeventbus in 3 steps:

1. Define events::
        
            class MessageEvent:
                # Additional fields and methods if needed
                def __init__(self):
                    pass
                 
2. Prepare subscribers: Declare and annotate your subscribing method, optionally specify a thread mode::

            @subscribe(onEvent=MessageEvent)
            def func(self, event):
                # Do something
                pass
                
   
   Register your subscriber. For example, if you want to register a class in Python::
            
            class MyClass:
                def __init__(self):
                    pass
                
                def register(self, myclass):
                    PyBus.Instance().register(myclass, self.__class__.__name__)
                    
            # then during initilization
            
            myclass = MyClass()
            myclass.register(myclass)
            
3. Post events::
        
            class MyClass:
                def __init__(self):
                    pass
                
                def register(self, myclass):
                    PyBus.Instance().register(myclass, self.__class__.__name__)
                    
                def postingAnEvent(self):
                    PyBus.Instance().post(MessageEvent())
              
             myclass = MyClass()
             myclass.register(myclass)
             myclass.post()
            

Modes: pyeventbus can run the subscribing methods in 5 different modes

1. POSTING:

    + Runs the method in the same thread as posted. For example, if an event is posted from main thread, the subscribing method also runs in the main thread. If an event is posted in a seperate thread, the subscribing method runs in the same seperate method
    
    + This is the default mode::
        
            @subscribe(threadMode = Mode.POSTING, onEvent=MessageEvent)
            def func(self, event):
                # Do something
                pass
    
2. PARALLEL:
    
    + Runs the method in a seperate python thread::
        
            @subscribe(threadMode = Mode.PARALLEL, onEvent=MessageEvent)
            def func(self, event):
                # Do something
                pass
        
3. GREENLET:

    + Runs the method in a greenlet using gevent library::
            
            @subscribe(threadMode = Mode.GREENLET, onEvent=MessageEvent)
            def func(self, event):
                # Do something
                pass
    
4. BACKGROUND:
    
    + Adds the subscribing methods to a queue which is executed by workers.
            
            @subscribe(threadMode = Mode.BACKGROUND, onEvent=MessageEvent)
            def func(self, event):
                # Do something
                pass


3. CONCURRENT:

    + Runs the method in a seperate python process::
            
            @subscribe(threadMode = Mode.CONCURRENT, onEvent=MessageEvent)
            def func(self, event):
                # Do something
                pass
   
   
 
Adding pyeventbus to your project::

    pip install pyeventbus

 
Example::
    
    git clone https://github.com/n89nanda/pyeventbus.git
    
    cd pyeventbus
    
    virtualenv venv
    
    source venv/bin/activate
    
    pip install pyeventbus
    
    python example.py
