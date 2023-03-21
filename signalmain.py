from IOData import IOData
from SignalGUI import MainWindow


if __name__ == "__main__":
    iodata = IOData.IOData()
    main_window = MainWindow.MainWindow(iodata)

    main_window.mainloop()