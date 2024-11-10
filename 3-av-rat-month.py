import justpy as jp
import pandas as pd
from datetime import datetime
from pytz import utc

data = pd.read_csv("reviews.csv", parse_dates=['Timestamp'])
data['Month'] = data['Timestamp'].dt.strftime('%Y %m')
month_average = data.groupby(['Month'])[data.select_dtypes(include=['number']).columns].mean()

chart_def = """
 {
    chart: {
        type: 'spline',
        inverted: false
    },
    title: {
        text: 'Average Rating by Month',
        align: 'center'
    },
    subtitle: {
        text: 'Acccording to the Course Reviews Dataset',
        align: 'center'
    },
    xAxis: {
        reversed: false,
        title: {
            enabled: true,
            text: 'Month'
        },
        labels: {
            format: '{value}'
        },
        accessibility: {
            rangeDescription: 'Range: 0 to 80 km.'
        },
        maxPadding: 0.05,
        showLastLabel: true
    },
    yAxis: {
        title: {
            text: 'Rating'
        },
        labels: {
            format: '{value}'
        },
        accessibility: {
            rangeDescription: 'Range: -90°C to 20°C.'
        },
        lineWidth: 2
    },
    legend: {
        enabled: false
    },
    tooltip: {
        headerFormat: '<b>{series.name}</b><br/>',
        pointFormat: '{point.x} {point.y}'
    },
    plotOptions: {
        spline: {
            marker: {
                enable: false
            }
        }
    },
    series: [{
        name: 'Rating',
        data: []

    }]
}
"""
def app():
	wp = jp.QuasarPage()

	h1 = jp.QDiv(a=wp, text="Analysis of Course Reviews", classes="text-h3 text-center q-pa-md")	
	p1 = jp.QDiv(a=wp, text="These graphs represent course review analysis")

	hc = jp.HighCharts(a=wp, options=chart_def)

	hc.options.xAxis.categories = list(month_average.index) #Creamos .categories y convertimos en list()
	hc.options.series[0].data = list(month_average['Rating'])
	

	return wp

jp.justpy(app)