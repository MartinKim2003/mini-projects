import streamlit as st
import plotly.express as px
from modules.datos import cargar_datos, calcular_resumen, calcular_gastos_categoria
from modules.planning import calcular_distribucion, alertas
from modules.cotizaciones import obtener_cotizaciones, convertir_a_dolar
from modules.asesor import consultar_claude

# =================================================
# CONFIGURACIÓN
# =================================================
st.set_page_config(page_title="App de Gastos", page_icon="💰", layout="centered")
st.title("💰 App de Gastos Personales")

# =================================================
# CARGAR DATOS
# =================================================
df = cargar_datos("data/raw/gastos_ejemplo.xlsx")
resumen = calcular_resumen(df)
gastos_cat = calcular_gastos_categoria(df)

# =================================================
# SECCIÓN 1 - RESUMEN DEL MES
# =================================================
st.header("📊 Resumen del mes")

col1, col2, col3 = st.columns(3)
col1.metric("Ingresos", f"${resumen['total_ingresos']:,.0f} ARS")
col2.metric("Gastos", f"${resumen['total_gastos']:,.0f} ARS")
col3.metric("Balance", f"${resumen['balance']:,.0f} ARS")

# =================================================
# SECCIÓN 2 - DISTRIBUCIÓN 75/15/10
# =================================================
st.header("📋 Distribución del ingreso")

ingreso = resumen["total_ingresos"]
distribucion = calcular_distribucion(ingreso)

col1, col2, col3 = st.columns(3)
col1.metric("Podés gastar (75%)", f"${distribucion['gasto']:,.0f} ARS")
col2.metric("Invertir (15%)", f"${distribucion['inversion']:,.0f} ARS")
col3.metric("Ahorrar (10%)", f"${distribucion['ahorros']:,.0f} ARS")

limite = distribucion["gasto"]
gasto_real = resumen["total_gastos"]
diferencia = limite - gasto_real

if diferencia < 0:
    st.error(f"🚨 Te pasaste del presupuesto por ${abs(diferencia):,.0f} ARS")
elif diferencia < 20000:
    st.warning(f"⚠️ Cuidado, te quedan solo ${diferencia:,.0f} ARS")
else:
    st.success(f"✅ Vas bien, te quedan ${diferencia:,.0f} ARS")
# =================================================
# SECCIÓN 3 - GRÁFICOS
# =================================================
st.header("📈 Gráficos")

# Torta
fig_torta = px.pie(
    values=gastos_cat.values,
    names=gastos_cat.index,
    title="Gastos por categoría"
)
st.plotly_chart(fig_torta)

# Barras presupuesto vs real (solo si ingresaron sueldo)
if ingreso > 0:
    fig_barras = px.bar(
        x=["Presupuesto (75%)", "Gasto real"],
        y=[distribucion["gasto"], resumen["total_gastos"]],
        color=["Presupuesto (75%)", "Gasto real"],
        color_discrete_map={"Presupuesto (75%)": "green", "Gasto real": "red"},
        title="Presupuesto vs Gasto real"
    )
    st.plotly_chart(fig_barras)

# Evolución mensual
import pandas as pd
solo_gastos = df[df["tipo"] == "gasto"].copy()
solo_gastos["mes"] = pd.to_datetime(solo_gastos["fecha"]).dt.to_period("M").astype(str)
gastos_por_mes = solo_gastos.groupby("mes")["monto"].sum().reset_index()
fig_mensual = px.bar(gastos_por_mes, x="mes", y="monto", title="Evolución mensual de gastos")
st.plotly_chart(fig_mensual)

# =================================================
# SECCIÓN 4 - COTIZACIONES
# =================================================
st.header("💵 Tus gastos en dólares")

cotizaciones = obtener_cotizaciones()
conversion = convertir_a_dolar(resumen["total_gastos"], cotizaciones)

col1, col2, col3 = st.columns(3)
col1.metric("Dólar oficial", f"${conversion['oficial']:,.0f} USD", f"Cotización: {cotizaciones['oficial']:,.0f}")
col2.metric("Dólar blue", f"${conversion['blue']:,.0f} USD", f"Cotización: {cotizaciones['blue']:,.0f}")
col3.metric("Dólar tarjeta", f"${conversion['tarjeta']:,.0f} USD", f"Cotización: {cotizaciones['tarjeta']:,.0f}")

# =================================================
# SECCIÓN 5 - ASESOR IA
# =================================================
st.header("🤖 Asesor Financiero IA")

if st.button("Generar análisis con IA"):
    with st.spinner("Consultando a Claude..."):
        consejo = consultar_claude(resumen, gastos_cat, distribucion)
        st.markdown(consejo)
