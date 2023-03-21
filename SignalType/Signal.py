from abc import ABC, abstractmethod
from NumericalAnalysis import NumericalIntegration


# abstract class for signals
class Signal(ABC):
    @abstractmethod
    def getVal(self, t):             # value of signal in t (overriden in Dirac and subclasses of NonZeroWidthSignal)
        pass

    @abstractmethod
    def convolve(self, signal):     # calculates convolution of two signals (overridden in Dirac and NonZeroWidthSignal)
        pass


class NonZeroWidthSignal(Signal):
    def __init__(self, interval_arg, scale_var):
        super().__init__()
        self.__scale = scale_var                      # scaling of signal
        self.__interval = interval_arg.copy()         # interval of signal
        self.__min_boundary = min(interval_arg)       # lower boundary of interval (t_min)
        self.__max_boundary = max(interval_arg)       # upper boundary of interval (t_max)
        self.__length = self.__max_boundary - self.__min_boundary  # interval length

    @abstractmethod
    def getVal(self, t):      # overridden in Rect, Saw and Tri
        pass

    def setScale(self, scale_var):
        self.__scale = scale_var

    def getScale(self):
        return self.__scale

    def getLength(self):
        return self.__length

    def setLength(self, length_arg):
        self.__length = length_arg

    def getMinBoundary(self):
        return self.__min_boundary

    def setMinBoundary(self, min_boundary_arg):
        self.__min_boundary = min_boundary_arg
        self.setInterval([self.__min_boundary, self.__max_boundary])

    def getMaxBoundary(self):
        return self.__max_boundary

    def setMaxBoundary(self, max_boundary_arg):
        self.__max_boundary = max_boundary_arg
        self.setInterval([self.__min_boundary, self.__max_boundary])

    def getInterval(self):
        return self.__interval

    def setInterval(self, interval_arg):
        self.__interval = interval_arg.copy()

    def convolve(self, signal):
        upper_boundaries_g = []
        next_upper_boundaries_g = []
        integration_intervals = []
        integration_val = []
        t_val = []
        offset = 0.0

        if isinstance(signal, Dirac):
            t_val = [t + signal.getTShift() for t in self.getInterval()]
            integration_val = [self.getVal(round(t - signal.getTShift(), 10)) for t in t_val]
        elif not isinstance(signal, Dirac):
            s2_shift_2 = self.getMinBoundary() + signal.getMinBoundary()
            g = list([round(s2_shift_2 - x, 10) for x in signal.getInterval()]).copy()
            g.sort()

            offset = self.getMinBoundary() + signal.getMinBoundary()

            while g[0] < max(self.getInterval()):
                g_prev = g.copy()
                t_temp = 0.0

                s2_shift = max(self.getLength(), signal.getLength())

                for x in g:
                    upper_boundaries_g.append(min([abs(round(x - y, 10)) if y > x else s2_shift for y in self.getInterval()]))

                s2_shift = min(upper_boundaries_g)

                for j in range(0, len(g)):
                    g[j] = round(g[j] + s2_shift, 10)

                n = 15
                for i in range(0, n):
                    step_g = round(s2_shift / n, 10)

                    t_temp = round(offset + i * step_g, 10)
                    t_val.append(t_temp)

                    g_temp = [round(x + i * step_g, 10) for x in g_prev]

                    g_min = min(g_temp)
                    g_max = max(g_temp)
                    int_intervals_min = max(self.getMinBoundary(), g_min)
                    int_intervals_max = min(self.getMaxBoundary(), g_max)
                    integration_intervals.append(int_intervals_min)
                    integration_intervals.append(int_intervals_max)
                    int_intervals_set = set(integration_intervals)
                    for x in self.getInterval():
                        if x > int_intervals_min and x < int_intervals_max:
                            int_intervals_set.add(x)

                    for k in range(0, len(g_temp)):
                        if g_temp[k] > int_intervals_min and g_temp[k] < int_intervals_max:
                            int_intervals_set.add(g_temp[k])

                    integration_intervals = list(int_intervals_set)
                    integration_intervals.sort()

                    if len(integration_intervals) > 1:
                        int_val_temp = 0.0

                        for j in range(0, len(integration_intervals) - 1):
                            int_val_temp = round(int_val_temp + NumericalIntegration.calculateRombergExtrapolation(lambda tau: self.getVal(tau) * signal.getVal(t_temp - tau), [integration_intervals[j], integration_intervals[j + 1]]), 4)
                        integration_val.append(int_val_temp)
                    else:
                        integration_val.append(0.0)

                    integration_intervals.clear()
                    g_temp.clear()

                offset += s2_shift
                g_prev.clear()
                upper_boundaries_g.clear()

            t_val.append(offset)
            integration_val.append(0.0)
        return [t_val, integration_val]


class Rect(NonZeroWidthSignal):
    def __init__(self, interval_arg, scale_arg):
        super().__init__(interval_arg, scale_arg)

    def getVal(self, t_arg):
        if t_arg >= self.getMinBoundary() and t_arg <= self.getMaxBoundary():
            return self.getScale()
        else:
            return 0.0

    def setInterval(self, interval_arg):
        min_boundary = min(interval_arg)
        max_boundary = max(interval_arg)
        self.setLength(max_boundary - min_boundary)
        super().setInterval([min_boundary, max_boundary])


class Saw(NonZeroWidthSignal):
    def __init__(self, interval_arg, scale_arg):
        super().__init__(interval_arg, scale_arg)

    def getVal(self, t):
        alpha_temp = self.getScale() / self.getLength()
        beta_temp = -alpha_temp * self.getMinBoundary()
        if t >= self.getMinBoundary() and t <= self.getMaxBoundary():
            return round(alpha_temp * t + beta_temp, 10)
        else:
            return 0.0

    def setInterval(self, interval_arg):
        min_boundary = min(interval_arg)
        max_boundary = max(interval_arg)
        self.setLength(round(max_boundary - min_boundary, 10))
        super().setInterval([min_boundary, max_boundary])


class Tri(NonZeroWidthSignal):
    def __init__(self, interval_arg, scale_var):
        super().__init__(interval_arg, scale_var)
        self.__center = (round(self.getMaxBoundary() + self.getMinBoundary(), 10)) / 2
        interval_temp = interval_arg.copy()
        interval_temp.append(self.__center)
        interval_temp.sort()
        self.setInterval(interval_temp)

    def getVal(self, t):
        alpha1_temp = self.getScale() / (round(self.__center - self.getMinBoundary(), 10))
        beta1_temp = - alpha1_temp * self.getMinBoundary()
        alpha2_temp = -self.getScale() / (round(self.getMaxBoundary() - self.__center, 10))
        beta2_temp = -alpha2_temp * self.getMaxBoundary()
        if t >= self.getMinBoundary() and t <= self.__center:
            return round(alpha1_temp * t + beta1_temp, 10)
        elif t > self.__center and t <= self.getMaxBoundary():
            return round(alpha2_temp * t + beta2_temp, 10)
        else:
            return 0.0

    def setCenter(self, center_arg):
        self.__center = center_arg

    def setInterval(self, interval_arg):
        min_boundary = min(interval_arg)
        max_boundary = max(interval_arg)
        self.setLength(round(max_boundary - min_boundary, 10))
        self.__center = (round(max_boundary + min_boundary, 10)) / 2
        super().setInterval([min_boundary, self.__center, max_boundary])


class Dirac(Signal):
    def __init__(self, t_shift_var):
        super().__init__()
        self.__t_shift = t_shift_var

    def getVal(self, t):
        if t == self.__t_shift:
            return 1.0
        else:
            return 0.0

    def getTShift(self):
        return self.__t_shift

    def setTShift(self, t_shift_var):
        self.__t_shift = t_shift_var

    def convolve(self, signal):
        integration_val = []
        t_val = []
        if not isinstance(signal, Dirac):
            t_val = [t + self.getTShift() for t in signal.getInterval()]
            integration_val = [signal.getVal(round(t - self.getTShift(), 10)) for t in t_val]
        elif isinstance(signal, Dirac):
            t_val = [self.getTShift() + signal.getTShift()]
            integration_val = [1.0]
        return [t_val, integration_val]