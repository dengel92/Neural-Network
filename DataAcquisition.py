from AcquiredData import SeriesNum

class DataAcquisition(SeriesNum):
    def __init__(self):
        self.series_id = []
        self.numbseries = 0
    def addseriesID(self):
        self.numbseries +=1
        self.series_id.append(SeriesNum.series_ids.upper())
    def removeSID(self, index):
        self.numbseries -= 1
        return self.series_id.pop(index)
