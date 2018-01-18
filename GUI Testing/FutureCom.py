import pyforms
from pyforms import BaseWidget
from pyforms.Controls import ControlDockWidget
from pyforms.Controls import ControlMatplotlib
import APIGraphFuncGUI as graph
from APIGraphFuncExtendedGUI import APIDataSepGraph as apig
from APIGraphFuncExtendedGUI import APIDataComparaGraph as CMPG
from SetAPIKeyWindow import SetAPIKeyWindow
from DataAcquisitionWin import DataAcquisitionWin

class FutureCom(BaseWidget):
    def __OptOne(self):
        apig.DataAcquisition_SepGraph(self)
    def __OptTwo(self):
        CMPG.API_ComparaGraph(self)
    def __OptThree(self):
        graph.API_DataGraph()
    def __setAPIKey(self):
        win = SetAPIKeyWindow()
        win.parent = self
        win.show()

    def __AcquisitionInit(self):
        win = DataAcquisitionWin()
        win.parent = self
        self.__panel.value = win
    def __init__(self):
        super(FutureCom,self).__init__('FutureCom')

        #Definition of the forms fields
        self.__panel = ControlDockWidget()
        self.__graphs = ControlMatplotlib('Data')
        self.mainmenu = [
            {'File':[
                {'Data Acquisition': self.__AcquisitionInit},
                {'Graph API Data': self.__OptOne},
                {'Comparative Graphs(Do Not use yet In development)': self.__OptTwo},
                {'Comparative Graphs(Lite Alpha version)': self.__OptThree}
            ]
            },
            {'Edit':[
                {'APIKey': self.__setAPIKey}
            ]}
        ]




# Execute the application
if __name__ == "__main__":
    pyforms.start_app(FutureCom, geometry=(480, 270, 1280, 720))



