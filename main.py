import pandas as pd
import matplotlib.pyplot as plt

"""MVP 1"""
# =================================================
# RESUMÉN DE GASTOS
# =================================================

def cargar_datos(ruta):
    """
    Lee el Excel y devuelve un DataFrame limpio.
    Recibe la ruta del archivo comos str
    """
    df = pd.read_excel(ruta)
    return df

def calcular_resumen(df):
    """
    Recibe el DataFrame completo y devuelve un diccionario
    con total_gastos, total_ingresos, balance.
    Por qué un diccionario: Porque necesito devolver tres valores juntos!!
    """
    total_gastos = df[df["tipo"] == "gasto"]["monto"].sum()
    total_ingresos = df[df["tipo"] == "ingreso"]["monto"].sum()
    balance = total_ingresos - total_gastos
    return {
        "total_gastos": total_gastos,
        "total_ingresos": total_ingresos,
        "balance": balance
    }

def calcular_gastos_categoria(df):
    """
    Recibe el DataFrame completo y devuelve una Serie
    con los gastos agrupados por categoria, ordenados de mayor a menor.
    """
    solo_gastos = df[df["tipo"]=="gasto"]
    return solo_gastos.groupby("categoria")["monto"].sum().sort_values(ascending=False)

def imprimir_resumen(resumen):
    """
    Recibe el diccionario de calcular_resumen() y lo imprime
    Separamos impresión de cálculo: cada función hace una sola cosa
    """
    print("\n=== RESUMEN DEL MES ===")
    print(f"Total ingresos: {resumen["total_ingresos"]: ,.0f} ARS")
    print(f"Total gastos: {resumen["total_gastos"]: ,.0f} ARS")
    print(f"Balance: {resumen["balance"]: ,.0f} ARS")
    
def imprimir_categoria (gastos_categoria):
    """
    Recibe la serie de calcular_gastos_categoria() y la imprime
    """
    print("\n=== GASTOS POR CATEGORÍA ===")
    print(gastos_categoria)

    print("\n=== TOP 5 ===")
    print(gastos_categoria.head(5))

"""
EJECUCIÓN
"""   
df = cargar_datos("data/raw/gastos_ejemplo.xlsx")
resumen = calcular_resumen(df)
gastos_cat= calcular_gastos_categoria(df)
resumen_imp = imprimir_resumen(resumen)
categoria = imprimir_categoria(gastos_cat)
    
    
"""MVP 2"""
# =================================================
# ANOTACIÓN SUELDO + 50/30/20
# =================================================

# Le pedis el sueldo al usuario 
def pedir_ingreso():
    while True:
        try:
            sueldo = int(input("Ingrese su sueldo: "))
            return sueldo
        except ValueError:
            print("No ha ingresado un sueldo. Intente de nuevo")


# Calculas la distribución en base a (75/15/10)
def calcular_distribucion(ingreso):
    gasto = ingreso * 0.75
    inversion = ingreso * 0.15
    ahorros = ingreso * 0.10
    return {
        "gasto": gasto, 
        "inversion": inversion,
        "ahorros": ahorros         
    }

# Mostras las distribuciones
def imprimir_distribucion(distribucion):    
    print("\n=== RESUMEN DEL MES ===")
    print(f"Este mes podes gastar: {distribucion["gasto"]: ,.0f} ARS")
    print(f"Este mes debes invertir {distribucion["inversion"]: ,.0f} ARS")
    print(f"Este mes debes ahorrar {distribucion["ahorros"]: ,.0f} ARS")

ingreso = pedir_ingreso()
distribucion = calcular_distribucion(ingreso)
resumen_distr = imprimir_distribucion(distribucion)

# =================================================
# BLOQUE ALERTAS
# =================================================

# Límite del gasto (75% del ingreso)
# Total gastado real (viene de calcular_distribucion)
# Diferencia entre límite y gasto real

def alertas (distribucion, resumen):
    # Cuánto puedo gastar vs cuánto gasté
    limite = distribucion["gasto"]
    gasto_real = resumen["total_gastos"]
    diferencia = limite - gasto_real
    
    # Caso 1: pasas del límite
    if diferencia < 0:
        print(f"\n🚨 Te pasaste del presupuesto por {abs(diferencia):,.0f} ARS")
    
    # Caso 2: me quedan menos de 20,000
    elif diferencia < 20000:
        print(f"\n⚠️  Cuidado, te quedan solo {diferencia:,.0f} ARS")
    
    # Caso 3: todo bien
    else:
        print(f"\n✅ Vas bien, te quedan {diferencia:,.0f} ARS")


# =================================================
# GRÁFICOS
# =================================================
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

