import pyforms
from pyforms import BaseWidget
from pyforms.controls import ControlDockWidget
from pyforms.controls import ControlMdiArea
# from AcquiredData import ACQData
from APIGraphFuncExtendedGUI import APIDataSepGraph as apig
from DataTables import TableData
from SetAPIKeyWindow import SetAPIKeyWindow
from DataAcquisitionWin import DataAcquisitionWin

class FutureCom(BaseWidget):
    def __OptOne(self):
        apig.DataAcquisition_SepGraph(self)

    def __OptTwo(self):
        self.table = TableData();
        self.__mainwin += self.table

    # def __OptThree(self):
    #     print(ACQData.Series_Rawdata_Yname)

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
                # {'Troubleshoot': self.__OptThree}
            ]
            },
            {'Edit':[
                {'APIKey': self.__setAPIKey}
            ]}
        ]




# Execute the application
if __name__ == "__main__":
    pyforms.start_app(FutureCom, geometry=(480, 270, 1280, 720))



