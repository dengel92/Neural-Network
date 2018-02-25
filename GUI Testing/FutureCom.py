import pyforms
from pyforms import BaseWidget
from pyforms.controls import ControlDockWidget
from pyforms.controls import ControlMdiArea
import APIGraphFuncGUI as graph
from APIGraphFuncExtendedGUI import APIDataSepGraph as apig
from DataTables import TableData
from SetAPIKeyWindow import SetAPIKeyWindow
from DataAcquisitionWin import DataAcquisitionWin

class FutureCom(BaseWidget):
    def __OptOne(self):
        apig.APIDataSepGraph(self)

    def __OptTwo(self):
        self.table = TableData();
        self.__mainwin += self.table

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
        self.__mainwin = ControlMdiArea()
        self.mainmenu = [
            {'File':[
                {'Data Acquisition': self.__AcquisitionInit},
                {'Graph API Data': self.__OptOne},
                {'Data Tables': self.__OptTwo},
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



