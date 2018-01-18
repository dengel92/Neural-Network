import matplotlib.pyplot as plt
from DataDownload import DataRetrieval as API
from AcquiredData import ACQData as DR
choice_number = None
class APIDataSepGraph(DR):

    def DataAcquisition_SepGraph(self):

            series_rawdata_yname = DR.Series_Rawdata_Yname
            series_rawdata_sname = DR.Series_Rawdata_Sname
            series_Yaxis_data = DR.Series_YAxis_Data
            series_Xaxis_data = DR.Series_XAxis_Data
            series_count = DR.Series_Count

            plots = zip(series_Xaxis_data, series_Yaxis_data)
            def loop_plot(plots):
                figs = {}
                axs = {}
               ## this is a comment
                for idx, plot in enumerate(plots):
                    figs[idx] = plt.figure()
                    axs[idx] = figs[idx].add_subplot(111)
                    axs[idx].plot(plot[0], plot[1])
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



class APIDataComparaGraph(DR):
    def API_ComparaGraph(self):
        series_rawdata_yname = DR.Series_Rawdata_Yname
        series_rawdata_sname = DR.Series_Rawdata_Sname
        series_Yaxis_data = DR.Series_YAxis_Data
        series_Xaxis_data = DR.Series_XAxis_Data
        series_count = DR.Series_Count

