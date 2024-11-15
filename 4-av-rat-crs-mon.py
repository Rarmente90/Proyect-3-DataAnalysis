import justpy as jp
import pandas as pd
from datetime import datetime

data = pd.read_csv("reviews.csv", parse_dates=['Timestamp'])

data['Month'] = data['Timestamp'].dt.strftime('%Y-%m')
month_average_crs = data.groupby(['Month','Course Name'])['Rating'].count().unstack()

chart_def = """
 {
    chart: {
        type: 'spline'
    },
    title: {
        text: 'Amount of reviews of Courses by Month',
        align: 'center'
    },

    legend: {
        layout: 'vertical',
        align: 'left',
        verticalAlign: 'top',
        x: 150,
        y: 100,
        floating: false,
        borderWidth: 1,
        backgroundColor:
            Highcharts.defaultOptions.legend.backgroundColor || '#FFFFFF'
    },
    xAxis: {
        categories: [
			'Monday',
			'Tuesday',
			'Wednesday',
			'Thursday',
			'Friday',
			'Saturday',
			'Sunday'
		],
        plotBands: [{ // visualize the weekend
            from: 4.5,
            to: 6.5,
            color: 'rgba(68, 170, 213, .2)'
        }]
    },
    yAxis: {
        title: {
            text: 'Quantity'
        }
    },
    tooltip: {
        shared: true,
        headerFormat: ''
    },
    credits: {
        enabled: false
    },
    plotOptions: {
        series: {
            pointStart: 2000
        },
        areaspline: {
            fillOpacity: 0.5
        }
    },
    series: [{
        name: 'Jonh',
        data: [3, 4, 3, 5, 4, 10, 12]
    }, {
        name: 'Jane',
        data: [1, 3, 4, 3, 3, 5, 4]
    }]
}
"""

def app():
	wp = jp.QuasarPage()

	
	h1 = jp.QDiv(a=wp, text="Analysis of Course Reviews", classes="text-h3 text-center q-pa-md")	
	p1 = jp.QDiv(a=wp, text="These graphs represent course review analysis")

	hc = jp.HighCharts(a=wp, options=chart_def)
	hc.options.xAxis.categories = list(month_average_crs.index)

	hc_data = [{"name": v1, "data": [v2 for v2 in month_average_crs[v1]]} for v1 in month_average_crs.columns]

	hc.options.series = hc_data


	return wp

jp.justpy(app)