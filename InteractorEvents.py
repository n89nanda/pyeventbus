class InteractorEvents:
    class ComplexCalculationInMainThreadEvent:
        def __init__(self, msg):
            self.msg = msg
        def getMessage(self):
            return self.msg
    class ComplexCalculationInBackgroundThreadEvent:
        def __init__(self, msg):
            self.msg = msg
        def getMessage(self):
            return self.msg
    
        