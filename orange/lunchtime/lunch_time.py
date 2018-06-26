import sys
import numpy

import Orange.data
from Orange.widgets.widget import OWWidget, Input, Output
from Orange.widgets import gui

import datetime

class Valdir(OWWidget):
    name = "Is it lunchtime"
    description = "Tells if it is lunchtime"
    icon = "icons/lunch.svg"
    priority = 10

    class Inputs:
        data = Input("Data", Orange.data.Table)

    class Outputs:
        sample = Output("Sampled Data", Orange.data.Table)

    want_main_area = False

    def __init__(self):
        super().__init__()

        # GUI
        t = datetime.datetime.now().time()

        after = t < datetime.time(14,45)
        before = t > datetime.time(11,45) 
        box = gui.widgetBox(self.controlArea, "Info")

        if after and before:
            self.infoa = gui.widgetLabel(box, 'Yes, it is lunch time.')
        elif after: 
            self.infoa = gui.widgetLabel(box, 'Calm your teeth. It is not lunch time yet.')
        else:
            self.infoa = gui.widgetLabel(box, 'Well, actually, you missed lunch time. It is too late.')

        self.infob = gui.widgetLabel(box, '')

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
