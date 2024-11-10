import justpy as jp
import pandas as pd
from datetime import datetime

data = pd.read_csv("reviews.csv", parse_dates=['Timestamp'])

data['Month'] = data['Timestamp'].dt.strftime('%Y-%m')
month_average_crs = data.groupby(['Month','Course Name'])['Rating'].mean().unstack()

chart_def = """
  {

    chart: {
        type: 'streamgraph',
        marginBottom: 30,
        zooming: {
            type: 'x'
        }
    },

    // Make sure connected countries have similar colors
    
    title: {
        floating: true,
        align: 'center',
        text: 'Average Rating of Courses'
    },
    subtitle: {
        floating: true,
        align: 'left',
        y: 30,
        text: ''
    },

    xAxis: {
        maxPadding: 0,
        type: 'category',
        crosshair: true,
        categories: [],
        labels: {
            align: 'left',
            reserveSpace: false,
            rotation: 270
        },
        lineWidth: 0,
        margin: 20,
        tickWidth: 0
    },

    yAxis: {
        visible: false,
        startOnTick: false,
        endOnTick: false,
        minPadding: 0.1,
        maxPadding: 0.15
    },

    legend: {
        enabled: false
    },

    annotations: [{
        labels: [{
            point: {
                x: 0,
                xAxis: 0,
                y: 0,
                yAxis: 0
            },
            text: 'Courses Launched'
        }, {
            point: {
                x: 8,
                xAxis: 0,
                y: 3,
                yAxis: 0
            },
            text: 'Python got popular'
        }, 
		],
        labelOptions: {
            backgroundColor: 'rgba(255,255,255,0.5)',
            borderColor: 'silver'
        }
    }],

    plotOptions: {
        series: {
            label: {
                minFontSize: 5,
                maxFontSize: 15,
                style: {
                    color: 'rgba(255,255,255,0.75)'
                }
            },
            accessibility: {
                exposeAsGroupOnly: true
            }
        }
    },

    // Data parsed with olympic-medals.node.js
    series: [],

    exporting: {
        sourceWidth: 800,
        sourceHeight: 600
    }

}
"""

def app():
	wp = jp.QuasarPage()

	
	h1 = jp.QDiv(a=wp, text="Analysis of Course Reviews", classes="text-h3 text-center q-pa-md")	
	p1 = jp.QDiv(a=wp, text="These graphs represent course review analysis")

	hc = jp.HighCharts(a=wp, options=chart_def)
	hc.options.xAxis.categories = list(month_average_crs.index)

		
	#PODRIAMOS HACERLO ASÍ pero no es automatico ==> hc.options.series[0].name = month_average_crs.columns[0]
	#proceso para crear la lista de manera dinámica:
	 #primero creamos la lista [{}], v1 = titulo del curso 'name: v1'
	 	#en v2 = la fila (row) del curso

	hc_data = [{"name": v1, "data": [v2 for v2 in month_average_crs[v1]]} for v1 in month_average_crs.columns]

	hc.options.series = hc_data


	return wp

jp.justpy(app)