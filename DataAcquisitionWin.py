import pyforms
from pyforms import BaseWidget
from pyforms.Controls import ControlList
from pyforms.Controls import ControlText
from pyforms.Controls import ControlButton
from pyforms.Controls import ControlCombo
from DataDownload import DataRetrieval
from DataTables import TableData
from Series import SeriesNum
from AcquiredData import ACQData
class DataAcquisitionWin(DataRetrieval, BaseWidget, SeriesNum):
    def __init__(self):
        DataRetrieval.__init__(self)
        BaseWidget.__init__(self, 'Get Data')

        self._seriesIDinput = ControlText('Series ID')
        self._DataSeq = ControlCombo('Series')
        self._serieslist = ControlList('Series IDs',
             add_function = self.__addseriesID,
             remove_function = self.__rmseriesID)
        self._mkTable = ControlButton('Make Table')
        self._getdata = ControlButton('Get Data')

        self._DataSeq.activated_event = self.change_value
        self._getdata.value = self.__acquire
        self._mkTable.value = self.__mkTable
        self.formset = ["_seriesIDinput", "_DataSeq", ("_getdata", "_mkTable"), "_serieslist"]
    def __addseriesID(self):
        SeriesNum.series_ids = self._seriesIDinput.value
        super(DataAcquisitionWin, self).addseriesID()
        self._serieslist += [SeriesNum.series_ids.upper()]
        self._DataSeq += (SeriesNum.series_ids.upper())


    def removeSID(self, index):
        super(DataAcquisitionWin, self).removeSID(index)
        self._serieslist -= index

    def change_value(self, index):
        SeriesNum.indices = index

    def __rmseriesID(self):
        self.removeSID(self._serieslist.selected_row_index)

    def __acquire(self):
        DataRetrieval.Datadownload(self)
        #print(ACQData.Series_Rawdata)
    def __mkTable(self):
        win = TableData()
        win.parent = self
        win.show()


if __name__ == "__main__": pyforms.start_app(DataAcquisitionWin)