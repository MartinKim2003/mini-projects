from modules.datos import cargar_datos, calcular_resumen, calcular_gastos_categoria, imprimir_resumen, imprimir_categoria
from modules.planning import pedir_ingreso, calcular_distribucion, imprimir_distribucion, alertas
from modules.graficos import grafico_torta, grafico_barras_presupuesto, grafico_evolucion_mensual
from modules.cotizaciones import obtener_cotizaciones, convertir_a_dolar, imprimir_conversion
from modules.asesor import consultar_claude

# 1. Datos del Excel
df = cargar_datos("data/raw/gastos_ejemplo.xlsx")
resumen = calcular_resumen(df)
gastos_cat = calcular_gastos_categoria(df)
imprimir_resumen(resumen)
imprimir_categoria(gastos_cat)

# 2. Distribución
ingreso = pedir_ingreso()
distribucion = calcular_distribucion(ingreso)
imprimir_distribucion(distribucion)
alertas(distribucion, resumen)

# 3. Cotizaciones
cotizaciones = obtener_cotizaciones()
conversion = convertir_a_dolar(resumen["total_gastos"], cotizaciones)
imprimir_conversion(conversion, cotizaciones)

# 4. Gráficos
grafico_torta(gastos_cat)
grafico_barras_presupuesto(distribucion, resumen)
grafico_evolucion_mensual(df)

# 5. Asesor
print("\n=== TU ASESOR FINANCIERO ===")
consejo = consultar_claude(resumen, gastos_cat, distribucion)
print(consejo)