from DataAcquisition import DataAcquisition
import requests as Req
from SetAPIKey import APIKey
from AcquiredData import ACQData
class DataRetrieval(DataAcquisition, APIKey):
    def __init__(self):
        DataAcquisition.__init__(self)
        self.selec = 'series_id'
        self.APIurl = 'http://api.eia.gov/series'
        self.auth = 'api_key'
        self.Getparams = []
        self.series_list = []
        self.series_rawdata = []
        self.series_rawdata_yname = []
        self.series_rawdata_sname = []
        self.series_Yaxis_data = []
        self.series_Xaxis_data = []
        self.series_count_init = []
        self.series_count = 0

    def Datadownload(self):
        # print(self.numbseries)
        for n in range(self.numbseries):
            self.Getparams.append(dict([(self.selec, self.series_id[n]), (self.auth, APIKey.api_keys)]))
            self.series_list.append(Req.get(url=self.APIurl, params=self.Getparams[n]).json())
            self.series_rawdata.append(self.series_list[n]['series'][0]['data'])
            self.series_rawdata_yname.append(self.series_list[n]['series'][0]['unitsshort'])
            self.series_rawdata_sname.append(self.series_list[n]['series'][0]['name'])
            self.series_count_init.append(len(self.series_rawdata[n]))
            self.series_Yaxis_data.append([])
            self.series_Xaxis_data.append([])

        self.series_count = min(self.series_count_init)
        for n in range(self.numbseries):
            for t in range(self.series_count):
                self.series_Yaxis_data[n].append(self.series_rawdata[n][t][1])
                self.series_Xaxis_data[n].append(self.series_rawdata[n][t][0])
        # print(self.series_Xaxis_data)
        ACQData.GetParams = self.Getparams
        ACQData.Series_Rawdata = self.series_rawdata
        ACQData.Series_Rawdata_Yname = self.series_rawdata_yname
        ACQData.Series_Rawdata_Sname = self.series_rawdata_sname
        ACQData.Series_YAxis_Data = self.series_Yaxis_data
        ACQData.Series_XAxis_Data = self.series_Xaxis_data
        ACQData.Series_Count = self.series_count