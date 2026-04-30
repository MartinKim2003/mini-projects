"""MVP 1"""
# =================================================
# RESUMÉN DE GASTOS
# =================================================
import pandas as pd

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