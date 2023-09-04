import sys, os
import pickle
import pandas as pd
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.preprocessing import StandardScaler
import numpy as np
import warnings
warnings.filterwarnings("ignore")


# Verifica si se proporcionaron los dos argumentos esperados
# if len(sys.argv) != 5:
#     print("Uso: main.py <modelo.pkl> <normalizador.pkl> <data_a_predecir.csv> <lista_de_variables.pkl>")
#     sys.exit(1)

modelpkl='model.pkl'
normalizadorpkl='normalizador.pkl'
#lista_de_variablespkl='variables.pkl'
#validate='set_validacion.pkl'

values = os.environ['values']
#new_datos = pd.DataFrame() #np.array(eval(values))
new_datos=pd.DataFrame([float(i) for i in values.split(',')]).T

# Obtiene los argumentos desde la línea de comandos
modelo = pickle.load(open(modelpkl, 'rb'))
normalizador = pickle.load(open(normalizadorpkl, 'rb'))
#variables = pickle.load(open(lista_de_variablespkl, 'rb'))
#data = pickle.load(open(validate, 'rb'))

#data['PREDS'] = modelo.predict(normalizador.transform(data[variables]))
#print(data['PREDS'])

data = modelo.predict(normalizador.transform(new_datos))
#data['PREDS'].to_csv('PREDICCIONES.csv')

print(data)     
print("\nDone\n")