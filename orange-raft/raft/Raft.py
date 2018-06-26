import sys
import numpy

import Orange.data
from Orange.widgets.widget import OWWidget, Input, Output
from Orange.widgets import gui

class Raft(OWWidget):
    name = "Raft"
    description = "Calls raft to run reconstructions from orange-canvas"
    icon = "icons/louie.JPG"
    priority = 10

    class Inputs:
        data1 = Input("Data1", int)
        data2 = Input("Data2", int)

    class Outputs:
        sample = Output("Summed data", int)

    want_main_area = False

    def __init__(self):
        super().__init__()
        self.data1 = None
        self.data2 = None

        # GUI
        box = gui.widgetBox(self.controlArea, "Info")
        self.infoa = gui.widgetLabel(box, 'No data on input yet, waiting to get something.')
        self.infob = gui.widgetLabel(box, '')

    @Inputs.data1
    def set_data1(self, data1):
        self.data1 = data1

    @Inputs.data2
    def set_data2(self, data1):
        self.data2 = data2

'''
    @Inputs.data
    def set_data(self, dataset):
        if dataset is not None:
            self.infoa.setText('%d instances in input dataset' % len(dataset))
            indices = numpy.random.permutation(len(dataset))
            indices = indices[:int(numpy.ceil(len(dataset) * 0.1))]
            sample = dataset[indices]
            self.infob.setText('%d sampled instances' % len(sample))
            self.Outputs.sample.send(sample)
        else:
            self.infoa.setText('No data on input yet, waiting to get something.')
            self.infob.setText('')
            self.Outputs.sample.send("Sampled Data")
'''
