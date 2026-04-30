"""MVP 2"""
# =================================================
# GRÁFICOS
# =================================================
import pandas as pd
import matplotlib.pyplot as plt

def grafico_torta(gastos_categoria):
    
    plt.figure(figsize=(8, 6))  # tamaño del gráfico
    plt.pie(
        gastos_categoria.values,       # los montos
        labels=gastos_categoria.index, # los nombres de categoría
        autopct='%1.1f%%'              # muestra el porcentaje en cada porción
    )
    plt.title("Gastos por categoría")
    plt.show()

#grafico_torta(gastos_cat)

def grafico_barras_presupuesto(distribucion, resumen):
    # Los dos valores a comparar
    valores = [distribucion["gasto"], resumen["total_gastos"]]
    etiquetas = ["Presupuesto (75%)", "Gasto real"]
    
    plt.figure(figsize=(6, 5))
    plt.bar(etiquetas, valores, color=["green", "red"])
    plt.title("Presupuesto vs Gasto real")
    plt.ylabel("ARS")
    plt.show()

#grafico_barras_presupuesto(distribucion, resumen)

def grafico_evolucion_mensual(df):
    # Filtramos solo gastos
    solo_gastos = df[df["tipo"] == "gasto"]
    
    # Extraemos el mes de la columna fecha y agrupamos
    solo_gastos["mes"] = pd.to_datetime(solo_gastos["fecha"]).dt.to_period("M")
    gastos_por_mes = solo_gastos.groupby("mes")["monto"].sum()
    
    plt.figure(figsize=(8, 5))
    plt.bar(gastos_por_mes.index.astype(str), gastos_por_mes.values, color="steelblue")
    plt.title("Evolución mensual de gastos")
    plt.ylabel("ARS")
    plt.xlabel("Mes")
    plt.show()
