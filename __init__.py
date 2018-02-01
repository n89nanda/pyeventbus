from View import *
from Interactor import *
import threading
import timeit
from functools import partial

print 'current thread: ', threading.currentThread().getName()
view = View()
view.register(view)

interactor = Interactor()
interactor.register(interactor)

# import numpy.random
# def sort_arrays(a1, a2):
#   sorted(a1)
#   sorted(a2)
# test_arr_1 = numpy.random.randint(0,high=1000,size=1000000)
# test_arr_2 = numpy.random.randint(0,high=1000,size=1000000)
# from timeit import Timer
# t = Timer(lambda: sort_arrays(test_arr_1, test_arr_2))
# print t.timeit(number=5)







# Complex calculation in main thread
print 'starting view task at:', str(datetime.now())
view.complex_calculation_in_main_thread()
print 'ending view task at:', str(datetime.now())

# from Queue import Queue
# from threading import Thread

# def do_stuff(q):
#   while True:
#     print 'doing//'
#     print q.get()
#     q.task_done()

# q = Queue(maxsize=0)
# num_threads = 10

# for i in range(num_threads):
#   print 'executing'
#   worker = Thread(target=do_stuff, args=(q,))
#   worker.setDaemon(True)
#   worker.start()

# for x in range(5):
#     print 'putting: ',x
#     q.put(x)




