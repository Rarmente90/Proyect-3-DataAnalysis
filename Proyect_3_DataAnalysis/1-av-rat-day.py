import justpy as jp
import pandas as pd

data = pd.read_csv("reviews.csv", parse_dates=['Timestamp'])
data['Day'] = data['Timestamp'].dt.date
day_average = data.groupby(['Day'])[data.select_dtypes(include=['number']).columns].mean()

#Aquí metemos el grafico de 'https://www.highcharts.com/'
#Para Python funciona como un DICCIONARIO JSON
chart_def = """
 {
    chart: {
        type: 'spline',
        inverted: false
    },
    title: {
        text: 'Atmosphere Temperature by Altitude',
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
            text: 'Date'
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
            text: 'Average Rating'
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
        name: 'Average Rating',
        data: []

    }]
}
"""
#Objeto principal(web page)
def app():
	wp = jp.QuasarPage() #Creamos la instacia quásar del objeto

	#-----------Aquí creamos los elementos que contendrá la web-----------
	h1 = jp.QDiv(a=wp, text="Analysis of Course Reviews", #Header, Quásar división
	classes="text-h3 text-center q-pa-md")	
	p1 = jp.QDiv(a=wp, text="These graphs represent course review analysis")
	#------HihhCharts componente-------------
	hc = jp.HighCharts(a=wp, options=chart_def) 
	#DISCLAIMER! justpy convierte el hc.options en diccionario
	#De esta manera accedemos al diccionario
	hc.options.title.text = "Average Rating by Day" 

	#Accedemos al diccionario para cambiar los datos
	#series es una lista de listas, lets practice estructura datos en Python
	#series[0] = accedemos al primer valor de la lista, que es el diccionario [{name: 'temp...}]
	
	#Creamos .categories
	hc.options.xAxis.categories = list(day_average.index)
	hc.options.series[0].data = list(day_average['Rating'])
	
	
	return wp

jp.justpy(app)