from datetime import datetime, timedelta
from tkinter import *

from matplotlib.axes import Axes
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure


class TkTimeGraph:

    _master : Tk
    _top : Tk
    _bottom : Tk
    _figure : Figure
    _axes : Axes
    _graph : FigureCanvasTkAgg
    _x = []
    _y = []
    _timeSpan = 10

    def __init__(self, master):
        self._master = master

        # Create figure object with a subplot axes
        self._figure = Figure()
        self._axes = self._figure.add_subplot(111)

        # Create TOP frame with graph on it
        self._top = Frame(self._master)
        self._top.pack(side=TOP, fill=BOTH, expand=True)

        self._graph = FigureCanvasTkAgg(self._figure, master=self._top)
        self._graph.get_tk_widget().pack(side=TOP, fill=BOTH, expand=True)

        # Create BOTTOM frame with zoom buttons on it
        self._bottom = Frame(self._master)
        self._bottom.pack(side=BOTTOM)

        Button(self._bottom, text="+", width=5, command=self.decrease_timespan).pack(side=RIGHT)
        Button(self._bottom, text="-", width=5, command=self.increase_timespan).pack(side=LEFT)

    def add_point(self, p):
        self._x.append(datetime.now())
        self._y.append(p)

    def update_graph(self):
        self._axes.cla()
        self._axes.set_xlabel("Time")
        self._axes.set_ylabel("Value")
        self._axes.set_xlim(xmin=self._x[len(self._x)-1]-timedelta(seconds=self._timeSpan), xmax=self._x[len(self._x)-1])
        self._axes.grid()
        self._axes.plot(self._x, self._y)
        self._graph.draw()

    def increase_timespan(self):
        self._timeSpan = self._timeSpan * 2
        self.update_graph()

    def decrease_timespan(self):
        self._timeSpan = self._timeSpan / 2
        self.update_graph()