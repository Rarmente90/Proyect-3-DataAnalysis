import justpy as jp
import pandas as pd
from datetime import datetime

data = pd.read_csv("reviews.csv", parse_dates=['Timestamp'])
data['Weekday'] = data['Timestamp'].dt.strftime('%A') 
data['Daynumber'] = data['Timestamp'].dt.strftime('%w')

weekday_average = data.groupby(['Weekday', 'Daynumber'])[data.select_dtypes(include=['number']).columns].mean()
weekday_average = weekday_average.sort_values('Daynumber')

chart_def = """
{
    chart: {
        type: 'spline',
        inverted: false
    },
    title: {
        text: 'Average Happiest Day',
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
            text: 'Day'
        },
        labels: {
            format: '{value}'
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

	hc.options.xAxis.categories = list(weekday_average.index.get_level_values(0))
	hc.options.series[0].data = list(weekday_average['Rating'])
	return wp

jp.justpy(app) 