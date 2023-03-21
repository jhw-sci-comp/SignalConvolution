from SignalType.Signal import Rect, Saw, Tri, Dirac


class IOData:
    def __init__(self):
        self.__signal1_type = "Rectangular"
        self.__signal1_t_min = -1.0
        self.__signal1_t_max = 1.0
        self.__signal1_t_shift = 0.0
        self.__signal1_scale = 1.0
        self.__signal1_val = None

        self.__signal1 = None

        self.__signal2_type = "Rectangular"
        self.__signal2_t_min = -1.0
        self.__signal2_t_max = 1.0
        self.__signal2_t_shift = 0.0
        self.__signal2_scale = 1.0
        self.__signal2_val = None

        self.__signal2 = None

        self.__t_convolution = []
        self.__val_convolution = []

    def createSignal1(self, signal_type_arg, interval_arg, scale_arg):
        if signal_type_arg == "Rectangular":
            self.__signal1 = Rect(interval_arg, scale_arg)
            self.__signal1_t_min = min(interval_arg)
            self.__signal1_t_max = max(interval_arg)
        elif signal_type_arg == "Sawtooth":
            self.__signal1 = Saw(interval_arg, scale_arg)
            self.__signal1_t_min = min(interval_arg)
            self.__signal1_t_max = max(interval_arg)
        elif signal_type_arg == "Triangular":
            self.__signal1 = Tri(interval_arg, scale_arg)
            self.__signal1_t_min = min(interval_arg)
            self.__signal1_t_max = max(interval_arg)
        elif signal_type_arg == "Dirac":
            if len(interval_arg) == 1:
                self.__signal1 = Dirac(interval_arg[0])
                self.__signal1_t_min = min(interval_arg)

        self.__signal1_type = signal_type_arg
        self.__signal1_scale = scale_arg
        self.__signal1_val = self.__signal1.getVal

    def getSignal1Type(self):
        return self.__signal1_type

    def getSignal1TMin(self):
        return self.__signal1_t_min

    def setSignal1TMin(self, signal_t_min):
        self.__signal1_t_min = signal_t_min

        if self.__signal1_type == "Dirac":
            self.__signal1.setTShift(self.__signal1_t_min)
        else:
            self.__signal1.setMinBoundary(self.__signal1_t_min)

    def getSignal1TMax(self):
        return self.__signal1_t_max

    def setSignal1TMax(self, signal_t_max):
        self.__signal1_t_max = signal_t_max

        if self.__signal1_type != "Dirac":
            self.__signal1.setMaxBoundary(self.__signal1_t_max)

    def getSignal1TShift(self):
        return self.__signal1_t_shift

    def setSignal1TShift(self, signal_t_shift_var):
        self.__signal1_t_shift = signal_t_shift_var

    def getSignal1Val(self):
        return self.__signal1_val

    def getSignal1Scale(self):
        return self.__signal1_scale

    def setSignal1Scale(self, signal_scale_var):
        self.__signal1_scale = signal_scale_var

    def createSignal2(self, signal_type_arg, interval_arg, scale_arg):
        if signal_type_arg == "Rectangular":
            self.__signal2 = Rect(interval_arg, scale_arg)
            self.__signal2_t_min = min(interval_arg)
            self.__signal2_t_max = max(interval_arg)
        elif signal_type_arg == "Sawtooth":
            self.__signal2 = Saw(interval_arg, scale_arg)
            self.__signal2_t_min = min(interval_arg)
            self.__signal2_t_max = max(interval_arg)
        elif signal_type_arg == "Triangular":
            self.__signal2 = Tri(interval_arg, scale_arg)
            self.__signal2_t_min = min(interval_arg)
            self.__signal2_t_max = max(interval_arg)
        elif signal_type_arg == "Dirac":
            if len(interval_arg) == 1:
                self.__signal2 = Dirac(interval_arg[0])
                self.__signal2_t_min = min(interval_arg)

        self.__signal2_type = signal_type_arg
        self.__signal2_scale = scale_arg
        self.__signal2_val = self.__signal2.getVal

    def getSignal2Type(self):
        return self.__signal2_type

    def getSignal2TMin(self):
        return self.__signal2_t_min

    def setSignal2TMin(self, signal_t_min):
        self.__signal2_t_min = signal_t_min

        if self.__signal2_type == "Dirac":
            self.__signal2.setTShift(self.__signal2_t_min)
        else:
            self.__signal2.setMinBoundary(self.__signal2_t_min)

    def getSignal2TMax(self):
        return self.__signal2_t_max

    def setSignal2TMax(self, signal_t_max):
        self.__signal2_t_max = signal_t_max

        if self.__signal2_type != "Dirac":
            self.__signal2.setMaxBoundary(self.__signal2_t_max)

    def getSignal2TShift(self):
        return self.__signal2_t_shift

    def setSignal2TShift(self, signal_t_shift_var):
        self.__signal2_t_shift = signal_t_shift_var

    def getSignal2Val(self):
        return self.__signal2_val

    def getSignal2Scale(self):
        return self.__signal2_scale

    def setSignal2Scale(self, signal_scale_var):
        self.__signal2_scale = signal_scale_var

    def calculateConvolution(self):
        [self.__t_convolution, self.__val_convolution] = self.__signal1.convolve(self.__signal2)
        return [self.__t_convolution, self.__val_convolution]