import justpy as jp

#Objeto principal(web page)
def app():
	wp = jp.QuasarPage() #Creamos la instacia quásar del objeto

	#-----------Aquí creamos los elementos que contendrá la web-----------
	h1 = jp.QDiv(a=wp, text="Analysis of Course Reviews", #Header, Quásar división
	classes="text-h3 text-center q-pa-md")	
	p1 = jp.QDiv(a=wp, text="These graphs represent course review analysis")

	
	return wp

jp.justpy(app) #Llamamos a la función