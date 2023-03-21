from SignalGUI.SignalDisplayFrame import *
from SignalType import SignalException
from tkinter import ttk
from tkinter import messagebox


class ControlPanel(tk.Frame):
    def __init__(self, main_window_var, plot_frame_arg, iodata_arg):
        self.__main_window = main_window_var
        self.__plot_frame = plot_frame_arg
        self.__iodata = iodata_arg
        super().__init__(master=self.__main_window)
        self.pack(side=tk.LEFT)

        self.__signal1_label_frame = tk.LabelFrame(master=self, text="Signal f(t)")
        self.__signal1_label_frame.grid(row=0, column=0, sticky=tk.W, columnspan=4, padx=2, pady=10)

        self.__signal1_type_label = tk.Label(master=self.__signal1_label_frame, text="Type:")
        self.__signal1_type_label.grid(row=0, column=0, sticky=tk.W, padx=2, pady=5)

        self.__s1_type_selection = ttk.Combobox(master=self.__signal1_label_frame)
        self.__s1_type_selection['values'] = ('Rectangular', 'Sawtooth', 'Triangular', 'Dirac')
        self.__s1_type_selection['state'] = 'readonly'
        self.__s1_type_selection.current(0)
        self.__s1_type_selection.grid(row=0, column=1, sticky=tk.W, columnspan=3, padx=2, pady=5)

        self.__signal1_t_min_label = tk.Label(master=self.__signal1_label_frame, text="t_min:")
        self.__signal1_t_min_label.grid(row=1, column=0, sticky=tk.W, padx=2, pady=5)

        self.__s1_t_min_default = tk.StringVar(self)
        self.__s1_t_min_default.set("-1.0")
        self.__s1_t_min_selection = tk.Spinbox(master=self.__signal1_label_frame, from_=-10.0, to=10.0, increment=0.1, format="%.1f", width=self.winfo_width()*5, textvariable=self.__s1_t_min_default)
        self.__s1_t_min_selection['state'] = 'readonly'
        self.__s1_t_min_selection.grid(row=1, column=1, sticky=tk.W, padx=2, pady=5)

        self.__signal1_t_max_label = tk.Label(master=self.__signal1_label_frame, text="t_max:")
        self.__signal1_t_max_label.grid(row=1, column=2, sticky=tk.W, padx=2, pady=5)

        self.__s1_t_max_default = tk.StringVar(self)
        self.__s1_t_max_default.set("1.0")
        self.__s1_t_max_selection = tk.Spinbox(master=self.__signal1_label_frame, from_=-10.0, to=10.0, increment=0.1, format="%.1f", width=self.winfo_width()*5, textvariable=self.__s1_t_max_default)
        self.__s1_t_max_selection['state'] = 'readonly'
        self.__s1_t_max_selection.grid(row=1, column=3, sticky=tk.W, padx=2, pady=5)

        self.__iodata.createSignal1(self.__s1_type_selection.get(), [float(self.__s1_t_min_selection.get()), float(self.__s1_t_max_selection.get())], 1.0)
        self.__plot_frame.displaySignal1(self.__iodata.getSignal1Type(), self.__iodata.getSignal1Val(), self.__iodata.getSignal1TMin(), self.__iodata.getSignal1TMax())

        self.__signal2_label_frame = tk.LabelFrame(master=self, text="Signal g(t)")
        self.__signal2_label_frame.grid(row=1, column=0, sticky=tk.W, columnspan=4, padx=2, pady=10)

        self.__signal2_type_label = tk.Label(master=self.__signal2_label_frame, text="Type:")
        self.__signal2_type_label.grid(row=0, column=0, sticky=tk.W, padx=2, pady=5)

        self.__s2_type_selection = ttk.Combobox(master=self.__signal2_label_frame)
        self.__s2_type_selection['values'] = ('Rectangular', 'Sawtooth', 'Triangular', 'Dirac')
        self.__s2_type_selection['state'] = 'readonly'
        self.__s2_type_selection.current(0)
        self.__s2_type_selection.grid(row=0, column=1, sticky=tk.W, columnspan=3, padx=2, pady=5)

        self.__signal2_t_min_label = tk.Label(master=self.__signal2_label_frame, text="t_min:")
        self.__signal2_t_min_label.grid(row=1, column=0, sticky=tk.W, padx=2, pady=5)

        self.__s2_t_min_default = tk.StringVar(self)
        self.__s2_t_min_default.set("-1.0")
        self.__s2_t_min_selection = tk.Spinbox(master=self.__signal2_label_frame, from_=-10.0, to=10.0, increment=0.1, format="%.1f", width=self.winfo_width() * 5, textvariable=self.__s2_t_min_default)
        self.__s2_t_min_selection['state'] = 'readonly'
        self.__s2_t_min_selection.grid(row=1, column=1, sticky=tk.W, padx=2, pady=5)

        self.__signal2_t_max_label = tk.Label(master=self.__signal2_label_frame, text="t_max:")
        self.__signal2_t_max_label.grid(row=1, column=2, sticky=tk.W, padx=2, pady=5)

        self.__s2_t_max_default = tk.StringVar(self)
        self.__s2_t_max_default.set("1.0")
        self.__s2_t_max_selection = tk.Spinbox(master=self.__signal2_label_frame, from_=-10.0, to=10.0, increment=0.1, format="%.1f", width=self.winfo_width() * 5, textvariable=self.__s2_t_max_default)
        self.__s2_t_max_selection['state'] = 'readonly'
        self.__s2_t_max_selection.grid(row=1, column=3, sticky=tk.W, padx=2, pady=5)

        self.__iodata.createSignal2(self.__s2_type_selection.get(), [float(self.__s2_t_min_selection.get()), float(self.__s2_t_max_selection.get())], 1.0)
        self.__plot_frame.displaySignal2(self.__iodata.getSignal2Type(), self.__iodata.getSignal2Val(), self.__iodata.getSignal2TMin(), self.__iodata.getSignal2TMax())

        self.__confirm_button = tk.Button(master=self, text="OK", bd=5, width=5)
        self.__confirm_button.grid(row=8, column=0, sticky=tk.W)

        self.__cancel_button = tk.Button(master=self, text="Cancel", bd=5, width=5)
        self.__cancel_button.grid(row=8, column=1, sticky=tk.W)
        self.__cancel_button['state'] = 'disabled'

        self.__s1_type_selection.bind('<<ComboboxSelected>>', self.selectS1Type)
        self.__s1_t_min_selection['command'] = self.selectS1TMin
        self.__s1_t_max_selection['command'] = self.selectS1TMax
        self.__s2_type_selection.bind('<<ComboboxSelected>>', self.selectS2Type)
        self.__s2_t_min_selection['command'] = self.selectS2TMin
        self.__s2_t_max_selection['command'] = self.selectS2TMax
        self.__confirm_button['command'] = self.pressConfirmButton
        self.__cancel_button['command'] = self.pressCancelButton

    def selectS1Type(self, event):
        signal1_type = self.__s1_type_selection.get()
        signal1_t_min = float(self.__s1_t_min_selection.get())
        signal1_t_max = float(self.__s1_t_max_selection.get())

        if signal1_type == "Dirac":
            self.__iodata.createSignal1(signal1_type, [signal1_t_min], 1.0)
            self.__signal1_t_min_label['text'] = "t_shift"
            self.__signal1_t_max_label['state'] = 'disabled'
            self.__s1_t_max_selection['state'] = 'disabled'
            self.__iodata.setSignal1TMax(float(10.0))
            self.__s1_t_max_default.set(str(10.0))
        else:
            self.__iodata.createSignal1(signal1_type, [signal1_t_min, signal1_t_max], 1.0)
            self.__signal1_t_min_label['text'] = "t_min"
            self.__signal1_t_max_label['state'] = 'active'
            self.__s1_t_max_selection['state'] = 'readonly'

        if self.__iodata.getSignal1TMin() < self.__iodata.getSignal1TMax() or signal1_type == "Dirac":
            self.__plot_frame.displaySignal1(self.__iodata.getSignal1Type(), self.__iodata.getSignal1Val(), self.__iodata.getSignal1TMin(), self.__iodata.getSignal1TMax())
        else:
            self.__plot_frame.clearSignal1()

    def getS1TypeSelection(self):
        return self.__s1_type_selection

    def selectS1TMin(self):
        signal1_t_min = float(self.__s1_t_min_selection.get())
        if signal1_t_min < self.__iodata.getSignal1TMax() or (signal1_t_min >= self.__iodata.getSignal1TMax() and self.__s1_type_selection.get() == "Dirac"):
            self.__iodata.setSignal1TMin(signal1_t_min)
            self.__plot_frame.displaySignal1(self.__iodata.getSignal1Type(), self.__iodata.getSignal1Val(), self.__iodata.getSignal1TMin(), self.__iodata.getSignal1TMax())
        else:
            self.__iodata.setSignal1TMin(float(self.__s1_t_max_selection.get()))
            self.__s1_t_min_default.set(self.__s1_t_max_selection.get())
            self.__plot_frame.clearSignal1()

    def getS1MinSelection(self):
        return self.__s1_t_min_selection

    def selectS1TMax(self):
        signal1_t_max = float(self.__s1_t_max_selection.get())
        if signal1_t_max > self.__iodata.getSignal1TMin():
            self.__iodata.setSignal1TMax(signal1_t_max)
            self.__plot_frame.displaySignal1(self.__iodata.getSignal1Type(), self.__iodata.getSignal1Val(), self.__iodata.getSignal1TMin(), self.__iodata.getSignal1TMax())
        else:
            self.__iodata.setSignal1TMax(float(self.__s1_t_min_selection.get()))
            self.__s1_t_max_default.set(self.__s1_t_min_selection.get())
            self.__plot_frame.clearSignal1()

    def getS1MaxSelection(self):
        return self.__s1_t_max_selection

    def selectS2Type(self, event):
        signal2_type = self.__s2_type_selection.get()
        signal2_t_min = float(self.__s2_t_min_selection.get())
        signal2_t_max = float(self.__s2_t_max_selection.get())

        if signal2_type == "Dirac":
            self.__iodata.createSignal2(signal2_type, [signal2_t_min], 1.0)
            self.__signal2_t_min_label['text'] = "t_shift"
            self.__signal2_t_max_label['state'] = 'disabled'
            self.__s2_t_max_selection['state'] = 'disabled'
            self.__iodata.setSignal2TMax(float(10.0))
            self.__s2_t_max_default.set(str(10.0))
        else:
            self.__iodata.createSignal2(signal2_type, [signal2_t_min, signal2_t_max], 1.0)
            self.__signal2_t_min_label['text'] = "t_min"
            self.__signal2_t_max_label['state'] = 'active'
            self.__s2_t_max_selection['state'] = 'readonly'

        if self.__iodata.getSignal2TMin() < self.__iodata.getSignal2TMax() or signal2_type == "Dirac":
            self.__plot_frame.displaySignal2(self.__iodata.getSignal2Type(), self.__iodata.getSignal2Val(), self.__iodata.getSignal2TMin(), self.__iodata.getSignal2TMax())
        else:
            self.__plot_frame.clearSignal2()

    def getS2TypeSelection(self):
        return self.__s2_type_selection

    def selectS2TMin(self):
        signal2_t_min = float(self.__s2_t_min_selection.get())
        if signal2_t_min < self.__iodata.getSignal2TMax() or (signal2_t_min >= self.__iodata.getSignal2TMax() and self.__s2_type_selection.get() == "Dirac"):
            self.__iodata.setSignal2TMin(signal2_t_min)
            self.__plot_frame.displaySignal2(self.__iodata.getSignal2Type(), self.__iodata.getSignal2Val(), self.__iodata.getSignal2TMin(), self.__iodata.getSignal2TMax())
        else:
            self.__iodata.setSignal2TMin(float(self.__s2_t_max_selection.get()))
            self.__s2_t_min_default.set(self.__s2_t_max_selection.get())
            self.__plot_frame.clearSignal2()

    def getS2MinSelection(self):
        return self.__s2_t_min_selection

    def selectS2TMax(self):
        signal2_t_max = float(self.__s2_t_max_selection.get())
        if signal2_t_max > self.__iodata.getSignal2TMin():
            self.__iodata.setSignal2TMax(signal2_t_max)
            self.__plot_frame.displaySignal2(self.__iodata.getSignal2Type(), self.__iodata.getSignal2Val(), self.__iodata.getSignal2TMin(), self.__iodata.getSignal2TMax())
        else:
            self.__iodata.setSignal2TMax(float(self.__s2_t_min_selection.get()))
            self.__s2_t_max_default.set(self.__s2_t_min_selection.get())
            self.__plot_frame.clearSignal2()

    def getS2MaxSelection(self):
        return self.__s2_t_max_selection

    def pressConfirmButton(self):
        try:
            if (self.__iodata.getSignal1TMin() < self.__iodata.getSignal1TMax()) and (self.__iodata.getSignal2TMin() < self.__iodata.getSignal2TMax()):
                self.__signal1_type_label['state'] = 'disabled'
                self.__signal1_t_min_label['state'] = 'disabled'
                self.__signal1_t_max_label['state'] = 'disabled'
                self.__signal2_type_label['state'] = 'disabled'
                self.__signal2_t_min_label['state'] = 'disabled'
                self.__signal2_t_max_label['state'] = 'disabled'
                self.__s1_type_selection['state'] = 'disabled'
                self.__s1_t_min_selection['state'] = 'disabled'
                self.__s1_t_max_selection['state'] = 'disabled'
                self.__s2_type_selection['state'] = 'disabled'
                self.__s2_t_min_selection['state'] = 'disabled'
                self.__s2_t_max_selection['state'] = 'disabled'
                self.__confirm_button['state'] = 'disabled'
                self.__cancel_button['state'] = 'active'

                self.__plot_frame.getPlotConvolution().clear()
                [t_convolution, val_convolution] = self.__iodata.calculateConvolution()
                self.__plot_frame.getCanvasFigures().plotConvolution(self.__plot_frame.getPlotConvolution(), t_convolution, val_convolution, self.__iodata.getSignal1Type(), self.__iodata.getSignal2Type())
                self.__plot_frame.getCanvasFigures().draw()
            elif (self.__iodata.getSignal1TMin() >= self.__iodata.getSignal1TMax()) and (self.__iodata.getSignal2TMin() < self.__iodata.getSignal2TMax()):
                if self.__s1_type_selection.get() == "Dirac":
                    self.__signal1_type_label['state'] = 'disabled'
                    self.__signal1_t_min_label['state'] = 'disabled'
                    self.__signal1_t_max_label['state'] = 'disabled'
                    self.__signal2_type_label['state'] = 'disabled'
                    self.__signal2_t_min_label['state'] = 'disabled'
                    self.__signal2_t_max_label['state'] = 'disabled'
                    self.__s1_type_selection['state'] = 'disabled'
                    self.__s1_t_min_selection['state'] = 'disabled'
                    self.__s1_t_max_selection['state'] = 'disabled'
                    self.__s2_type_selection['state'] = 'disabled'
                    self.__s2_t_min_selection['state'] = 'disabled'
                    self.__s2_t_max_selection['state'] = 'disabled'
                    self.__confirm_button['state'] = 'disabled'
                    self.__cancel_button['state'] = 'active'

                    self.__plot_frame.getPlotConvolution().clear()
                    [t_convolution, val_convolution] = self.__iodata.calculateConvolution()
                    self.__plot_frame.getCanvasFigures().plotConvolution(self.__plot_frame.getPlotConvolution(), t_convolution, val_convolution, self.__iodata.getSignal1Type(), self.__iodata.getSignal2Type())
                    self.__plot_frame.getCanvasFigures().draw()
                else:
                    raise SignalException.IntervalSizeException("Singal 1")
            elif (self.__iodata.getSignal1TMin() < self.__iodata.getSignal1TMax()) and (self.__iodata.getSignal2TMin() >= self.__iodata.getSignal2TMax()):
                if self.__s2_type_selection.get() == "Dirac":
                    self.__signal1_type_label['state'] = 'disabled'
                    self.__signal1_t_min_label['state'] = 'disabled'
                    self.__signal1_t_max_label['state'] = 'disabled'
                    self.__signal2_type_label['state'] = 'disabled'
                    self.__signal2_t_min_label['state'] = 'disabled'
                    self.__signal2_t_max_label['state'] = 'disabled'
                    self.__s1_type_selection['state'] = 'disabled'
                    self.__s1_t_min_selection['state'] = 'disabled'
                    self.__s1_t_max_selection['state'] = 'disabled'
                    self.__s2_type_selection['state'] = 'disabled'
                    self.__s2_t_min_selection['state'] = 'disabled'
                    self.__s2_t_max_selection['state'] = 'disabled'
                    self.__confirm_button['state'] = 'disabled'
                    self.__cancel_button['state'] = 'active'

                    self.__plot_frame.getPlotConvolution().clear()
                    [t_convolution, val_convolution] = self.__iodata.calculateConvolution()
                    self.__plot_frame.getCanvasFigures().plotConvolution(self.__plot_frame.getPlotConvolution(), t_convolution, val_convolution, self.__iodata.getSignal1Type(), self.__iodata.getSignal2Type())
                    self.__plot_frame.getCanvasFigures().draw()
                else:
                    raise SignalException.IntervalSizeException("Singal 2")
            elif (self.__iodata.getSignal1TMin() >= self.__iodata.getSignal1TMax()) and (self.__iodata.getSignal2TMin() >= self.__iodata.getSignal2TMax()):
                if self.__s1_type_selection.get() == "Dirac" and self.__s2_type_selection.get() == "Dirac":
                    self.__signal1_type_label['state'] = 'disabled'
                    self.__signal1_t_min_label['state'] = 'disabled'
                    self.__signal1_t_max_label['state'] = 'disabled'
                    self.__signal2_type_label['state'] = 'disabled'
                    self.__signal2_t_min_label['state'] = 'disabled'
                    self.__signal2_t_max_label['state'] = 'disabled'
                    self.__s1_type_selection['state'] = 'disabled'
                    self.__s1_t_min_selection['state'] = 'disabled'
                    self.__s1_t_max_selection['state'] = 'disabled'
                    self.__s2_type_selection['state'] = 'disabled'
                    self.__s2_t_min_selection['state'] = 'disabled'
                    self.__s2_t_max_selection['state'] = 'disabled'
                    self.__confirm_button['state'] = 'disabled'
                    self.__cancel_button['state'] = 'active'

                    self.__plot_frame.getPlotConvolution().clear()
                    [t_convolution, val_convolution] = self.__iodata.calculateConvolution()
                    self.__plot_frame.getCanvasFigures().plotConvolution(self.__plot_frame.getPlotConvolution(), t_convolution, val_convolution, self.__iodata.getSignal1Type(), self.__iodata.getSignal2Type())
                    self.__plot_frame.getCanvasFigures().draw()
                else:
                    raise SignalException.IntervalSizeException("Singal 2")
        except SignalException.IntervalSizeException as e:
            messagebox.showinfo(title="Interval Boundaries Exception", message="The lower boundary (t_min) of " + e.str + " must be smaller than the upper boundary (t_max). Please change at least one of the boundaries.")

    def pressCancelButton(self):
        self.__plot_frame.getPlotConvolution().clear()
        self.__plot_frame.getCanvasFigures().draw()
        self.__signal1_type_label['state'] = 'active'
        self.__signal1_t_min_label['state'] = 'active'
        self.__signal2_type_label['state'] = 'active'
        self.__signal2_t_min_label['state'] = 'active'
        self.__cancel_button['state'] = 'disabled'
        self.__s1_type_selection['state'] = 'readonly'
        self.__s1_t_min_selection['state'] = 'readonly'
        self.__s2_type_selection['state'] = 'readonly'
        self.__s2_t_min_selection['state'] = 'readonly'
        self.__confirm_button['state'] = 'active'

        if self.__iodata.getSignal1Type() != "Dirac":
            self.__s1_t_max_selection['state'] = 'readonly'
            self.__signal1_t_max_label['state'] = 'active'

        if self.__iodata.getSignal2Type() != "Dirac":
            self.__s2_t_max_selection['state'] = 'readonly'
            self.__signal2_t_max_label['state'] = 'active'
