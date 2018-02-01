from View import *
from Interactor import *

view = View()
view.register(view)

interactor = Interactor()
interactor.register(interactor)

# Complex calculation in main thread
view.complex_calculation_in_main_thread()



