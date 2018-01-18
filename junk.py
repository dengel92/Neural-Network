import pyforms
from pyforms import BaseWidget
from pyforms.Controls import ControlDockWidget
from pyforms.Controls import ControlMatplotlib

class test(BaseWidget):

    def __init__(self):

        super(test, self).__init__('test')
        self.itr = [1, 2, 3, 4, 5]
        for item in self.itr:
            self._graph = ControlMatplotlib(item)
            self.formset = [{
                                'tab%s' %item:['_graph']
            }]

if __name__ == "__main__":
    pyforms.start_app(test)