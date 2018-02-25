import matplotlib.pyplot as plt
from AcquiredData import ACQData

class APIDataSepGraph(ACQData):


    def DataAcquisition_SepGraph(self):
            #  first part retrieves stored data
            series_rawdata_yname = ACQData.Series_Rawdata_Yname
            series_rawdata_sname = ACQData.Series_Rawdata_Sname
            series_Yaxis_data = ACQData.Series_YAxis_Data
            series_Xaxis_data = ACQData.Series_XAxis_Data
            series_count = ACQData.Series_Count

            # Sets data into iterable tuples for plots

            plots = zip(series_Xaxis_data, series_Yaxis_data)

            # loop to create plot for each dataset of interest

            def loop_plot(plots):
                figs = {}
                axs = {}
               ## this is a comment
                for idx, plot in enumerate(plots):
                    figs[idx] = plt.figure()
                    axs[idx] = figs[idx].add_subplot(111)
                    axs[idx].plot(plot[0], plot[1], 'o')
                    series_xlabel = []
                    i = 0
                    while i < series_count:
                        series_xlabel.append(plot[0][i])
                        i += round(series_count / 23)
                    axs[idx].set_xticklabels(reversed(series_xlabel))
                    axs[idx].locator_params('x', nbins=23)
                    axs[idx].tick_params('x', rotation=22)
                    axs[idx].set_xlabel('Dates')
                    axs[idx].set_ylabel(series_rawdata_yname[idx])
                    axs[idx].set_title(series_rawdata_sname[idx])
                return figs, axs
            figs, axs = loop_plot(plots)
            plt.show()

'''
class in possible works. For now the code below does nothing.
'''

class APIDataComparaGraph(ACQData):
    def API_ComparaGraph(self):
        series_rawdata_yname = self.Series_Rawdata_Yname
        series_rawdata_sname = self.Series_Rawdata_Sname
        series_Yaxis_data = self.Series_YAxis_Data
        series_Xaxis_data = self.Series_XAxis_Data
        series_count = self.Series_Count

