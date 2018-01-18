import requests
import matplotlib.pyplot as plt
#import Config_2 as conf
#import collections as col
import itertools as combi


choice_number = None
def DataAcquisition_SepGraph(choice_number):
    while True:
        numbseries = input("How Many Series Do You Want To Look At?")
        APIurl = 'http://api.eia.gov/series'
        selec = 'series_id'
        s_id = [input('Please Type Series ID#%s' % n).upper() for n in range(eval(numbseries))]
        #for n in range(eval(numbseries)):
            #s_id.append(input('Please Type Series ID#%s' % n).upper())
        auth = 'api_key'
        key = input('Type API Key Code')
        Getparams = []
        series_list = []
        series_rawdata = []
        series_rawdata_yname = []
        series_rawdata_sname = []
        series_Yaxis_data = []
        series_Xaxis_data = []
        series_count_init = []
        series_count = 0
        for n in range(eval(numbseries)):
            Getparams.append(dict([(selec, s_id[n]), (auth, key)]))
            series_list.append(requests.get(url=APIurl, params=Getparams[n]).json())
            series_rawdata.append(series_list[n]['series'][0]['data'])
            series_rawdata_yname.append(series_list[n]['series'][0]['unitsshort'])
            series_rawdata_sname.append(series_list[n]['series'][0]['name'])
            series_count_init.append(len(series_rawdata[n]))
            series_Yaxis_data.append([])
            series_Xaxis_data.append([])

        if max(series_count_init) > min(series_count_init):
            series_count = min(series_count_init)
        for n in range(eval(numbseries)):
            for t in range(series_count):
                series_Yaxis_data[n].append(series_rawdata[n][t][1])
                series_Xaxis_data[n].append(series_rawdata[n][t][0])
        if choice_number == 1:
            pass
        elif choice_number == 2:
            return series_rawdata_sname, series_rawdata_yname, series_Xaxis_data, series_Yaxis_data, series_count

        plots = zip(series_Xaxis_data, series_Yaxis_data)
        def loop_plot(plots):
            figs = {}
            axs = {}
            for idx, plot in enumerate(plots):
                figs[idx] = plt.figure()
                axs[idx] = figs[idx].add_subplot(111)
                axs[idx].plot(plot[0], plot[1])
                axs[idx].set_xlabel('Dates')
                axs[idx].set_ylabel(series_rawdata_yname[idx])
                axs[idx].set_title(series_rawdata_sname[idx])
            return figs, axs
        figs, axs = loop_plot(plots)
        plt.show()
        pass
        ch = input('Make Another Graph: y/n?')
        if ch == 'n':
            break
    return series_rawdata_sname, series_rawdata_yname, series_Xaxis_data, series_Yaxis_data, series_count


def API_ComparaGraph():
    series_rawdata_sname, series_rawdata_yname, series_Xaxis_data, series_Yaxis_data, series_count = DataAcquisition_SepGraph(2)

    print(series_Yaxis_data)
    keys = []
    for F in range(len(series_Yaxis_data)):
        keys.append('Plot%s' % F)
    Ydata_init_combinations = sorted(dict(zip(keys, combi.combinations(series_Yaxis_data, 2))).items(), key=lambda t: t[0])
    #Ydata_final_combinations = col.OrderedDict(sorted(Ydata_init_combinations.items(), key=lambda t: t[0]))
    plots2 = zip(series_Xaxis_data, Ydata_init_combinations)
    enum_test = list(enumerate(plots2, 1))
    print(enum_test)

    #def two_scales(ax1, time, data1, data2, c1, c2):
        #ax2 = ax1.twinx()

       # ax1.plot(time, data1, color=c1)
       # ax1.set_xlabel('time (s)')
       # ax1.set_ylabel('exp')

       # ax2.plot(time, data2, color=c2)
       # ax2.set_ylabel('sin')
       # return ax1, ax2
    #fig = {}
   # ax = {}

   # fig, ax = plt.subplots()
    #ax1, ax2 = two_scales(ax, t, s1, s2, 'r', 'b')
    #print(plots2[0])
      #  fig1, ax1 = plt.subplots()
      #  p1, = ax1.plot(series_1_xaxis_data, series_1_yaxis_data, 'r', label=series_1_rawdata_sname[0:19])
      #  plt.title('Price vs. volume')
      #  ax1.set_ylabel(series_1_rawdata_yname, color='r')
      #  ax1.tick_params('y', colors='r')
      #  ax1.set_xlabel('Dates')
      #  ax1.locator_params('x', nbins=23)
      #  series_1_xaxis_labels=[]
     #   i = 0
     #   while i<series_2_count:
      #      series_1_xaxis_labels.append(series_1_xaxis_data[i])
     #       i += (round(series_2_count/23))
      #  ax1.tick_params('x', rotation=22)
     #   ax1.set_xticklabels(reversed(series_1_xaxis_labels))
      #  ax2 = ax1.twinx()
       # p2, = ax2.plot(series_1_xaxis_data, series_2_yaxis_data, 'b-', label=series_2_rawdata_sname[0:19])
      #  ax2.set_ylabel(series_2_rawdata_yname, color='b')
      #  ax2.tick_params('y', colors='b')
      #  ax2.locator_params('x', nbins=23)
      #  ax2.set_xticklabels(reversed(series_1_xaxis_labels))
      #  p = [p1, p2]
      #  ax1.legend(p, [p_.get_label() for p_ in p])
      #  plt.show()
      #  pass
      #  ch = input('Make Another Graph: y/n?')
       # if ch == 'n':
      #      break


