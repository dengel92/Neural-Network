import requests
import matplotlib.pyplot as plt
from SetAPIKey import APIKey

def API_DataGraph():
    while APIKey.api_keys != 0:
        APIurl = 'http://api.eia.gov/series'
        selec = 'series_id'
        id1 = input('Please Type First Series ID').upper()
        id2 = input('Please Type Second Series ID').upper()
        auth = 'api_key'
        key = APIKey.api_keys
        Gparam1 = dict([(selec, id1), (auth, key)])
        Gparam2 = dict([(selec, id2), (auth, key)])
        series_1 = requests.get(url=APIurl, params=Gparam1)
        series_2 = requests.get(url=APIurl, params=Gparam2)
        series_1_rawdata = series_1.json()['series'][0]['data']
        series_1_rawdata_yname = series_1.json()['series'][0]['unitsshort']
        series_1_rawdata_sname = series_1.json()['series'][0]['name']
        series_1_yaxis_data = []
        series_1_xaxis_data = []
        series_1_count = 0
        series_2_count = 0
        series_2_rawdata = series_2.json()['series'][0]['data']
        series_2_rawdata_yname = series_2.json()['series'][0]['unitsshort']
        series_2_rawdata_sname = series_2.json()['series'][0]['name']
        series_2_xaxis_data = []
        series_2_yaxis_data = []
        if len(series_1_rawdata) > len(series_2_rawdata):
            series_2_count = len(series_2_rawdata)
            series_1_count = series_2_count
        elif len(series_1_rawdata) <= len(series_2_rawdata):
            series_1_count = len(series_1_rawdata)
            series_2_count = series_1_count
        for i in range(series_2_count):
            series_2_xaxis_data.append(series_2_rawdata[i][0])
            series_2_yaxis_data.append(series_2_rawdata[i][1])
        for i in range(series_1_count):
            series_1_xaxis_data.append(series_1_rawdata[i][0])
            series_1_yaxis_data.append(series_1_rawdata[i][1])

        fig1, ax1 = plt.subplots()
        p1, = ax1.plot(series_1_xaxis_data, series_1_yaxis_data, 'r', label=series_1_rawdata_sname[0:19])
        plt.title('Price vs. volume')
        ax1.set_ylabel(series_1_rawdata_yname, color='r')
        ax1.tick_params('y', colors='r')
        ax1.set_xlabel('Dates')
        ax1.locator_params('x', nbins=23)
        series_1_xaxis_labels=[]
        i = 0
        while i<series_2_count:
            series_1_xaxis_labels.append(series_1_xaxis_data[i])
            i += (round(series_2_count/23))
        ax1.tick_params('x', rotation=22)
        ax1.set_xticklabels(reversed(series_1_xaxis_labels))
        ax2 = ax1.twinx()
        p2, = ax2.plot(series_1_xaxis_data, series_2_yaxis_data, 'b-', label=series_2_rawdata_sname[0:19])
        ax2.set_ylabel(series_2_rawdata_yname, color='b')
        ax2.tick_params('y', colors='b')
        ax2.locator_params('x', nbins=23)
        ax2.set_xticklabels(reversed(series_1_xaxis_labels))
        p = [p1, p2]
        ax1.legend(p, [p_.get_label() for p_ in p])
        plt.show()
        pass
        ch = input('Make Another Graph: y/n?')
        if ch == 'n':
            break
    else:
        print('Unauthorized Access')
