import sqlite3
import matplotlib.pyplot as plt

def generar_bar_chart(labels, values):
    fig, ax = plt.subplots()
    ax.bar(labels, values)
    plt.show()

conexion = sqlite3.connect('Censos.db')
pais = input("Ingrese el pais a consultar: ")
cur = conexion.cursor()
cur.execute("SELECT Veintidos, Veinte, Quince, Diez, Dos_mil, Noventa, Ochenta, Setenta FROM world_population WHERE Country = ?", (pais, ))
censos = cur.fetchone()
labels = ["2022", "2020", "2015", "2010", "2000", "1990", "1980", "1970"]
values = list(censos)

generar_bar_chart(labels, values)