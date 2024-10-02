import pandas as pd
import matplotlib.pyplot as plt

def mean (lista):
    """Esta funcion genera el promedio de una lista 
    mean(lista)
    ejemplo
    a= [1,2,3,4]
    mean(a)
    """
    return sum(lista)/ len(lista)
#Predicciòn del valor de una acciòn, "Mètodo Ingenuo" 
a=  pd.read_csv("./netflix.csv")
ventana = 5
bx= (mean(a["precio"]))
precio = a["precio"]
promedio= [ bx  for p in range(ventana)]
precio= list(precio)
precio.extend(promedio)

fecha= a["fecha"]
fecha = pd.to_datetime(fecha, format= "%d/%m/%Y")
fecha= list(fecha)

fecha2 = [fecha[-1] for dia in range (ventana)]
fecha3= [dia + pd.Timedelta(days= i) for i, dia in enumerate (fecha2, start = 1)]
fecha.extend(fecha3)
plt.plot(fecha, precio)

plt.show()
#"Mètodo media movil"
precio= a["precio"]
precio= list(a["precio"])
fecha = list (a["fecha"])
fecha = pd.to_datetime(fecha, format= "%d/%m/%Y")
l_base= {}
l_base["fecha"] = fecha
l_base["precio"]= precio
l_base= pd.DataFrame(l_base["precio"], index=l_base["fecha"])

m_movil= [(precio[i] + precio[i+1])/2 for  i in range (len(precio)-1)]
m_movil = list(m_movil)
f_movil= fecha + pd.Timedelta(days= 2) 
fecha2= (f_movil [0: 19])
l_predicha = pd.DataFrame (m_movil, index= fecha2)

df_predicha =pd.concat([l_base, l_predicha], axis= 1)
print(df_predicha)
df_predicha.plot(
    title= "Media movil precio de acciones de Netflix",
    marker= "o",
    color= "green",
    xlabel= "Fecha",
    ylabel= "Precios"
)
plt.show()



     


    


