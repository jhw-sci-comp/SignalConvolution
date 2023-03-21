# Exception, which will be raised, if the user tries to perform a convolution with one or two signals
# of type NonZeroWidthSignal with interval length 0
class IntervalSizeException(Exception):
    def __init__(self, str):
        self.str = str