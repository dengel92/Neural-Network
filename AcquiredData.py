class ACQData(object):
    def __init__(self, params, label, sname, yaxis, xaxis, count, raw):
        self.GetParams = params
        self.Series_Rawdata = raw
        self.Series_Rawdata_Yname = label
        self.Series_Rawdata_Sname = sname
        self.Series_YAxis_Data = yaxis
        self.Series_XAxis_Data = xaxis
        self.Series_Count = count
class SeriesNum(object):
    def __init__(self, series, indice):
        self.series_ids = series
        self.indices = indice