from random import random
from threading import Thread
from time import sleep
from tkinter import *

from TkGraph.TkTimeGraph import TkTimeGraph


def app():
    # Create Tk Window
    root = Tk()
    root.config(background='black')
    root.geometry("1024x720")

    # Add Label to Tk Window
    Label(root, text="Live Plot", bg='black', fg='white').pack()

    # Create a TkTimeGraph inside Window
    tkTimeGraph = TkTimeGraph(master=root)

    # Start a thread to provide live data to the graph
    dataThread = DataThread(tkTimeGraph)
    dataThread.start()

    # Start the Tk Window Main Loop
    root.mainloop()

    # When  Tk Window exits, stop and wait data Thread
    dataThread.stop()
    dataThread.join()

class DataThread(Thread):

    _running : bool
    _tkTimeGraph : TkTimeGraph

    def __init__(self, tkTimeGraph):
        Thread.__init__(self)
        self._tkTimeGraph = tkTimeGraph

    def run(self):
        self._running = True
        value=0
        while(self._running):
            value=value+random()-0.5
            self._tkTimeGraph.add_point(value)
            self._tkTimeGraph.update_graph()
            sleep(.25)

    def stop(self):
        self._running = False

if __name__ == '__main__':
    app() 