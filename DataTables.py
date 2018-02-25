import pyforms
from pyforms import BaseWidget
from pyforms.controls import ControlList
from AcquiredData import ACQData
from Series import SeriesNum

class TableData(BaseWidget):

    def __init__(self):
        BaseWidget.__init__(self, ACQData.Series_Rawdata_Sname[SeriesNum.indices])

        self._data = ControlList('Series Data')
        # self._data_acq = ControlButton('Make Table')
        self._data.horizontal_headers = ['Date', ACQData.Series_Rawdata_Yname[SeriesNum.indices]]
        # self._data_acq.value = self.__table_creation
        self._data.value = [(x, y,) for x, y in ACQData.Series_Rawdata[SeriesNum.indices]]


    # def __table_creation(self):



if __name__ == "__main__": pyforms.start_app(TableData)