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

