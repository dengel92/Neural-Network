import pyforms
from pyforms import BaseWidget
from pyforms.controls import ControlList
from pyforms.controls import ControlButton
from pyforms.controls import ControlCombo
from DataDownload import DataRetrieval
from AcquiredData import SeriesNum

class DataAcquisitionWin(DataRetrieval, BaseWidget, SeriesNum):
    def __init__(self):
        DataRetrieval.__init__(self)
        BaseWidget.__init__(self, 'Get Data')

        # Data set selection
        self._seriesIDinput = ControlCombo('Series ID')
        self._DataSeq = ControlCombo('Series')
        self._serieslist = ControlList('Series IDs',
             add_function = self.__addseriesID,
             remove_function = self.__rmseriesID)
        self._getdata = ControlButton('Get Data')

        # Set functions for widgets
        self._seriesIDinput += ('Crude Runs', ['PET.WCRRIP12.W', 'PET.WCRRIP22.W', 'PET.WCRRIP32.W', 'PET.WCRRIP42.W', 'PET.WCRRIP52.W'])
        self._seriesIDinput += ('Crude Production', ['PET.MCRFPP12.M', 'PET.MCRFPP22.M', 'PET.MCRFPP32.M', 'PET.MCRFPP42.M', 'PET.MCRFPP52.M', 'PET.MCRFP5F1.M', 'PET.MCRFP5F2.M'])
        self._seriesIDinput += ('Crude Import')
        # self._seriesIDinput.activated_event = self.check
        self._DataSeq.activated_event = self.change_value
        self._getdata.value = self.__acquire
        self.formset = ["_seriesIDinput", "_DataSeq", "_getdata", "_serieslist"]
    # Troubleshoot
    # def check(self, index):
    #     print(self._seriesIDinput.value)
    #     s_id = self._seriesIDinput.value
    #     print(len(s_id))
    def __addseriesID(self):

        # Sets value of series_id to text value of category selection drop down menu
        self._serieslist.clear()
        s_id = self._seriesIDinput.value
        for id in range(len(s_id)):
            SeriesNum.series_ids = self._seriesIDinput.value[id]
            super(DataAcquisitionWin, self).addseriesID()
            self._serieslist += [SeriesNum.series_ids.upper()]
            self._DataSeq += (SeriesNum.series_ids.upper())

    # Remove series from list connected to '__rmseriesID'
    def removeSID(self, index):
        super(DataAcquisitionWin, self).removeSID(index)
        self._serieslist -= index

    # Change table data set
    def change_value(self, index):
        SeriesNum.indices = index

    # Remove series from list for data retrieval
    def __rmseriesID(self):
        self.removeSID(self._serieslist.selected_row_index)

    # retrieve and store series data in AcquiredData.py
    def __acquire(self):
        DataRetrieval.Datadownload(self)




if __name__ == "__main__": pyforms.start_app(DataAcquisitionWin)