from SignalGUI.SignalDisplayControl import *


class MainWindow(tk.Tk):
    def __init__(self, iodata_arg):
        super().__init__()
        self.geometry("1100x600")
        self.minsize(1100, 600)
        self.title("Signal Convolution")
        self.__iodata = iodata_arg
        self.__plot_frame = PlotFrame(self)
        self.__control_panel = ControlPanel(self, self.__plot_frame, self.__iodata)

    def getControlPanel(self):
        return self.__control_panel

    def getPlotFrame(self):
        return self.__plot_frame
