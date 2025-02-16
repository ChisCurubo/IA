# Manipulación de datos
import pandas as pd
# Operaciones numéricas
import numpy as np
# Para medición del tiempo que toma ejecutar los procesos
from time import time
# Para separar datos de entrenamiento y prueba
from sklearn.model_selection import train_test_split
# Librería para SVM
from sklearn.svm import SVR
# Medición de precisión
from sklearn.metrics import accuracy_score, confusion_matrix
# Generar gráficos
import matplotlib.pyplot as plt
#subir archivo
from google.colab import files
#visualizaciòn netamente estadistica
import seaborn as sns
#calculador del estandar
from sklearn.preprocessing import StandardScaler

from sklearn.metrics import mean_squared_error, r2_score



#Importa archivos desde la computadora
uploaded = files.upload()


df = pd.read_csv(r'caso_estudio.csv')
# Mostrar información sobre el set de datos
df.info()

df.head()

# Contar los valores únicos de una columna en un DataFrame
#gender,Partner,Dependents,PhoneService,MultipleLines,InternetService,SeniorCitizen,MonthlyCharges
df['Outcome'].value_counts()
df = df.dropna()


# Crearemos un nuevo df llamado X (notar mayus) con las columnas de características
# Se obtiene generando una lista de columnas del df a utilizar
lista_caract = [
    'Pregnancies',
    'Glucose',
    'BloodPressure',
    'SkinThickness',
    'Insulin',
    'BMI',
    'DiabetesPedigreeFunction',
    'Age'
]
# Luego tomando esa lista del df original
X = df[lista_caract]
# Mostraremos los primeros cinco registros para conocer cómo se compone X
X.head()

# Utilizaremos el mismo procedimiento para generar y
lista_etiq = ['Outcome']
y = df[lista_etiq]
y.head()


# Separar en datos de entrenamiento y datos de prueba
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y
)

# Mostraremos la cantidad de datos a utilizar para el entrenamiento
X_train.shape
y_train.shape


# Luego, la cantidad de datos a utilizar para validar
X_test.shape
y_test.shape

# Definició del modelo que llamaremos clf para llamar a la regresiòn
clf = SVR(kernel='linear')

# Guardamos el registro del momento en el que empezamos el entrenamiento
hora_inicio = time()


# Iniciamos el entrenamiento ejecutando el metodo fit
# Los valores que enviamos son los valores de X y y
#
# El .ravel() que final de y.values es un pequeño truco para cambiar su forma
# esto permite convertir una matriz de dos dimensiones en una sola dimesión,
# con ello, cada elemento de esta nueva matriz corresponde a un registro de X
clf.fit(X_train.values, y_train.values.ravel())

# Imprimimos el tiempo tomado para el entrenamiento
print("Entrenamiento terminado en {} segundos".format(time() - hora_inicio))


# Otra vez guardaremos registro del tiempo que nos toma crear esta predicción
hora_inicio = time()
# Iniciamos la predicción con nuestra X de prueba
y_pred = clf.predict(X_test)
# Mostramos el tiempo tomado para la predicción
print("Predicción terminada en {} segundos".format(time() - hora_inicio))


#coeficiente de determinaciòn
print(r2_score(y_test, y_pred))


cantidad_probar = len(y_test)
X_axis = np.arange(cantidad_probar)

fig, ax = plt.subplots()
ax.scatter(X_axis, y_test.iloc[0:cantidad_probar].values)
ax.scatter(X_axis, y_pred[0:cantidad_probar])
plt.show()

sns.set_theme(style='whitegrid', context='notebook')
cols = ['Pregnancies',
    'Glucose',
    'BloodPressure',
    'SkinThickness',
    'Insulin',
    'BMI',
    'DiabetesPedigreeFunction',
    'Age',
    'Outcome']
sns.pairplot(df[cols])
plt.show()


cm=np.corrcoef(df[cols].values.T)
sns.set(font_scale=1.0)
hm=sns.heatmap(cm, cbar=True, annot=True, square=True, fmt='.2f',annot_kws={'size':8}, yticklabels=cols, xticklabels=cols)
plt.show()