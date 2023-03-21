import math
import tkinter as tk
from locale import str

import matplotlib
from matplotlib.figure import Figure
from matplotlib import ticker
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
matplotlib.use("TkAgg")


class PlotFrame(tk.Frame):
    def __init__(self, master_window_arg):
        super().__init__(master=master_window_arg)
        self.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

        self.__plot_figure = Figure(figsize=(9, 6), dpi=100, constrained_layout=True)
        self.__canvas_figures = PlotCanvas(self, self.__plot_figure)

        self.__plot_subfigures = self.__plot_figure.subfigures(2, 1, hspace=0.05, wspace=0.1)
        self.__plot_signals = self.__plot_subfigures[0].subplots(1, 2)
        self.__plot_signals[0].xaxis.set_major_formatter(ticker.StrMethodFormatter("{x:.1f}"))
        self.__plot_signals[1].xaxis.set_major_formatter(ticker.StrMethodFormatter("{x:.1f}"))

        self.__plot_convolution = self.__plot_subfigures[1].subplots(1, 1)

        self.__canvas_figures.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)

    def displaySignal1(self, signal1_type_arg, signal1val_arg, signal1_t_min_arg, signal1_t_max_arg): #signal1val_arg = signal1.getVal
        self.__plot_signals[0].clear()
        self.__plot_signals[0].axis("on")
        self.__plot_signals[0].grid(True)
        self.__plot_signals[0].grid(zorder=0)
        self.__plot_signals[0].set_xlabel("t")
        self.__plot_signals[0].set_ylabel("f(t)")
        self.__plot_signals[0].xaxis.set_major_formatter(ticker.StrMethodFormatter("{x:.1f}"))
        s1_plot_color = 'm'
        self.__canvas_figures.plotSignal(self.__plot_signals[0], s1_plot_color, signal1_type_arg, signal1val_arg, signal1_t_min_arg, signal1_t_max_arg)
        self.__canvas_figures.draw()

    def clearSignal1(self):
        self.__plot_signals[0].clear()
        self.__plot_signals[0].axis("on")
        self.__plot_signals[0].grid(True)
        self.__plot_signals[0].set_xlabel("t")
        self.__plot_signals[0].set_ylabel("f(t)")
        self.__canvas_figures.draw()

    def displaySignal2(self, signal2_type_arg, signal2val_arg, signal2_t_min_arg, signal2_t_max_arg):
        self.__plot_signals[1].clear()
        self.__plot_signals[1].axis("on")
        self.__plot_signals[1].grid(True)
        self.__plot_signals[1].grid(zorder=0)
        self.__plot_signals[1].set_xlabel("t")
        self.__plot_signals[1].set_ylabel("g(t)")
        self.__plot_signals[1].xaxis.set_major_formatter(ticker.StrMethodFormatter("{x:.1f}"))
        s2_plot_color = 'r'
        self.__canvas_figures.plotSignal(self.__plot_signals[1], s2_plot_color, signal2_type_arg, signal2val_arg, signal2_t_min_arg, signal2_t_max_arg)
        self.__canvas_figures.draw()

    def clearSignal2(self):
        self.__plot_signals[1].clear()
        self.__plot_signals[1].axis("on")
        self.__plot_signals[1].grid(True)
        self.__plot_signals[1].set_xlabel("t")
        self.__plot_signals[1].set_ylabel("f(t)")
        self.__canvas_figures.draw()

    def getPlotSignals(self):
        return self.__plot_signals

    def getCanvasFigures(self):
        return self.__canvas_figures

    def getPlotConvolution(self):
        return self.__plot_convolution


class PlotCanvas(FigureCanvasTkAgg):
    def __init__(self, master_frame_var, plot_figure_var):
        self.__master_frame = master_frame_var
        self.__plot_figure = plot_figure_var
        super().__init__(self.__plot_figure, master=self.__master_frame)

    def plotSignal(self, plot_signal_fig, plot_color, signal_type, signal_val, *t_data):
        t_part1 = []
        s_part1 = []
        s_part1_style = ''
        t_part2 = []
        s_part2 = []
        s_part2_style = ''

        if signal_type == "Dirac":
            t_eps = 1.0
            t_lim_min = math.floor(t_data[0] - t_eps)
            t_lim_max = math.ceil(t_data[0] + t_eps)
            plot_signal_fig.set_xlim(t_lim_min, t_lim_max)
            plot_signal_fig.plot([t_lim_min, t_lim_max], [0.0, 0.0], color=plot_color)
            plot_signal_fig.arrow(t_data[0], 0, 0, 1, length_includes_head=True, head_width=0.05, color=plot_color, zorder=2)
        else:
            signal_min_boundary = t_data[0]
            signal_max_boundary = t_data[1]
            t_eps = (signal_max_boundary - signal_min_boundary) / 2.0
            t_lim_min = math.floor(signal_min_boundary - t_eps)
            t_lim_max = math.ceil(signal_max_boundary + t_eps)
            plot_signal_fig.set_xlim(t_lim_min, t_lim_max)

            if signal_type == "Rectangular":
                t_mid = (signal_max_boundary + signal_min_boundary) / 2.0
                t_part1 = [t_lim_min, signal_min_boundary, t_mid]
                s_part1 = []
                for t in t_part1:
                    s_part1.append(signal_val(t))
                    t_part2 = [t_mid, signal_max_boundary, t_lim_max]
                s_part2 = []
                for t in t_part2:
                    s_part2.append(signal_val(t))
                s_part1_style = 'steps-post'
                s_part2_style = 'steps-pre'
            elif signal_type == "Sawtooth":
                t_part1 = [t_lim_min, signal_min_boundary, signal_max_boundary]
                s_part1 = []
                for t in t_part1:
                    s_part1.append(signal_val(t))
                t_part2 = [signal_max_boundary, t_lim_max]
                s_part2 = []
                for t in t_part2:
                    s_part2.append(signal_val(t))
                s_part1_style = 'default'
                s_part2_style = 'steps-pre'
            elif signal_type == "Triangular":
                t_mid = (signal_max_boundary + signal_min_boundary) / 2.0
                t_part1 = [t_lim_min, signal_min_boundary, t_mid]
                s_part1 = []
                for t in t_part1:
                    s_part1.append(signal_val(t))
                t_part2 = [t_mid, signal_max_boundary, t_lim_max]
                s_part2 = []
                for t in t_part2:
                    s_part2.append(signal_val(t))
                s_part1_style = 'default'
                s_part2_style = 'default'

            plot_signal_fig.plot(t_part1, s_part1, drawstyle=s_part1_style, color=plot_color)
            plot_signal_fig.plot(t_part2, s_part2, drawstyle=s_part2_style, color=plot_color)

    def plotConvolution(self, plot_convolution_fig, t_val_var, c_val_var, s1_type, s2_type):
        plot_convolution_fig.axis("on")
        plot_convolution_fig.grid(True)
        plot_convolution_fig.grid(zorder=0)
        plot_convolution_fig.set_xlabel("t")
        plot_convolution_fig.set_ylabel("(f * g)(t)")

        if s1_type == "Dirac" and s2_type == "Dirac":
            t_eps = 1.0
            t_lim_min = t_val_var[0] - t_eps
            t_lim_max = t_val_var[0] + t_eps
            plot_convolution_fig.set_xlim(t_lim_min, t_lim_max)

            plot_convolution_fig.plot([t_lim_min, t_lim_max], [0.0, 0.0], color='b')
            plot_convolution_fig.arrow(t_val_var[0], 0, 0, 1, length_includes_head=True, head_length=0.07, head_width=0.03, color='b', zorder=2)
        else:
            if (s1_type == "Dirac" and s2_type == "Rectangular") or (s1_type == "Rectangular" and s2_type == "Dirac"):
                t_val_min = min(t_val_var)
                t_val_max = max(t_val_var)
                t_eps = (t_val_max - t_val_min) / 2.0
                t_part1 = [t_val_min - t_eps, t_val_min]
                c_part1 = [0.0, c_val_var[0]]
                t_part3 = [t_val_max, t_val_max + t_eps]
                c_part3 = [c_val_var[len(c_val_var) - 1], 0.0]
                c_part1_style = 'steps-post'
                c_part2_style = 'default'
                c_part3_style = 'steps-pre'

                plot_convolution_fig.set_xlim(min(t_part1), max(t_part3))
                plot_convolution_fig.plot(t_part1, c_part1, drawstyle=c_part1_style, color='b')
                plot_convolution_fig.plot(t_val_var, c_val_var, drawstyle=c_part2_style, color='b')
                plot_convolution_fig.plot(t_part3, c_part3, drawstyle=c_part3_style, color='b')
            elif (s1_type == "Dirac" and s2_type == "Sawtooth") or (s1_type == "Sawtooth" and s2_type == "Dirac"):
                t_val_min = min(t_val_var)
                t_val_max = max(t_val_var)
                t_eps = (t_val_max - t_val_min) / 2.0
                t_part1 = [t_val_min - t_eps, t_val_min]
                c_part1 = [0.0, c_val_var[0]]
                t_part3 = [t_val_max, t_val_max + t_eps]
                c_part3 = [c_val_var[len(c_val_var) - 1], 0.0]
                c_part1_style = 'default'
                c_part2_style = 'default'
                c_part3_style = 'steps-pre'

                plot_convolution_fig.set_xlim(min(t_part1), max(t_part3))
                plot_convolution_fig.plot(t_part1, c_part1, drawstyle=c_part1_style, color='b')
                plot_convolution_fig.plot(t_val_var, c_val_var, drawstyle=c_part2_style, color='b')
                plot_convolution_fig.plot(t_part3, c_part3, drawstyle=c_part3_style, color='b')
            elif (s1_type == "Dirac" and s2_type == "Triangular") or (s1_type == "Triangular" and s2_type == "Dirac"):
                t_val_min = min(t_val_var)
                t_val_max = max(t_val_var)
                t_eps = (t_val_max - t_val_min) / 2.0
                t_part1 = [t_val_min - t_eps, t_val_min]
                c_part1 = [0.0, c_val_var[0]]
                t_part3 = [t_val_max, t_val_max + t_eps]
                c_part3 = [c_val_var[len(c_val_var) - 1], 0.0]
                c_part1_style = 'default'
                c_part2_style = 'default'
                c_part3_style = 'default'

                plot_convolution_fig.set_xlim(min(t_part1), max(t_part3))
                plot_convolution_fig.plot(t_part1, c_part1, drawstyle=c_part1_style, color='b')
                plot_convolution_fig.plot(t_val_var, c_val_var, drawstyle=c_part2_style, color='b')
                plot_convolution_fig.plot(t_part3, c_part3, drawstyle=c_part3_style, color='b')
            else:
                plot_convolution_fig.axis("on")
                plot_convolution_fig.grid(True)
                plot_convolution_fig.set_xlabel("t")
                plot_convolution_fig.set_ylabel("(f * g)(t)")
                t_part2_min = min(t_val_var)
                t_part2_max = max(t_val_var)
                t_eps = (t_part2_max - t_part2_min) / 2.0
                t_part1 = [t_part2_min - t_eps, t_part2_min]
                c_part1 = [0.0, 0.0]
                t_part3 = [t_part2_max, t_part2_max + t_eps]
                c_part3 = [0.0, 0.0]

                plot_convolution_fig.set_xlim(min(t_part1), max(t_part3))
                plot_convolution_fig.plot(t_part1, c_part1, color='b')
                plot_convolution_fig.plot(t_val_var, c_val_var, color='b')
                plot_convolution_fig.plot(t_part3, c_part3, color='b')
