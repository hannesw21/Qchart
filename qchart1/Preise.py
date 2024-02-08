from PyQt6.QtCharts import QLineSeries, QChart, QChartView, QSplineSeries, QValueAxis, QAbstractAxis, QDateTimeAxis
from PyQt6.QtCore import Qt, QDateTime, pyqtSlot
from PyQt6.QtGui import QColor


class Preise(QChartView):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.series = QLineSeries()
        self.series.setName("Preisanstieg Döner")
        self.series.setColor(QColor("brown"))

        self.series1 = QSplineSeries()
        self.series1.setName("Preisanstieg Bier")

        self.chart = QChart()
        self.chart.setTitle("Bier-Döner Preisanstieg")
        self.chart.addSeries(self.series)
        self.chart.addSeries(self.series1)

        self.date_time_axis = QDateTimeAxis()
        #self.date_time_axis.setFormat("hh:mm:ss")


        axis_x = QValueAxis()
        axis_x.setRange(2014, 2024)

        axis_y = QValueAxis()
        axis_y.setRange(0, 20)

        self.chart.addAxis(axis_x, Qt.AlignmentFlag.AlignTop)
        self.series.attachAxis(axis_x)
        self.series1.attachAxis(axis_x)

        self.chart.addAxis(axis_y, Qt.AlignmentFlag.AlignLeft)
        self.series.attachAxis(axis_y)
        self.series1.attachAxis(axis_y)

        self.series.attachAxis(axis_x)
        self.series.attachAxis(axis_y)

        self.series1.attachAxis(axis_x)
        self.series1.attachAxis(axis_y)

        self.series.append(0, 0)
        self.series.append(2014, 3)
        self.series.append(2016,4)
        self.series.append(2018,5)
        self.series.append(2020, 6)
        self.series.append(2024, 7)


        self.series1.append(2014, 10)
        self.series1.append(2016,12)
        self.series1.append(2018,14)
        self.series1.append(2020, 16)
        self.series1.append(2024, 18)





        self.setChart(self.chart)


