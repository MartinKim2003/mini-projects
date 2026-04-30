"""MVP 3"""
# =================================================
# ASESOR
# =================================================
import os
from dotenv import load_dotenv
from anthropic import Anthropic
import streamlit as st
import sys
sys.stdout.reconfigure(encoding='utf-8')
import locale
locale.setlocale(locale.LC_ALL, 'C.UTF-8')



api_key = st.secrets.get("ANTHROPIC_API_KEY") or os.getenv("ANTHROPIC_API_KEY")
client = Anthropic(api_key=api_key)

def consultar_claude(resumen, gastos_categoria, distribucion):
    """
    Arma un prompt con los datos reales del mes
    y le pide a Claude un análisis personalizado
    """
    gastos_str = gastos_categoria.to_string().encode('ascii', 'ignore').decode('ascii')
    prompt = f"""Eres un asesor financiero experimentado. Analiza los gastos de un estudiante universitario argentino de 22 anos que vive en Buenos Aires y genera recomendaciones practicas y directas.

    DATOS FINANCIEROS DEL MES:
    - Ingresos total: {resumen["total_ingresos"]:,.0f} ARS
    - Gastos Totales: {resumen["total_gastos"]:,.0f} ARS
    - Balance neto: {resumen["balance"]:,.0f} ARS
    - Presupuesto asignado (75%): {distribucion["gasto"]:,.0f} ARS
    - Inversion recomendada (15%): {distribucion["inversion"]:,.0f} ARS
    - Ahorro objetivo (10%): {distribucion["ahorros"]:,.0f} ARS

    DESGLOSE DE GASTOS POR CATEGORIA:
    {gastos_str}

    OUTPUT:
    1. Resumen en 2-3 lineas de como le fue este mes
    2. Identifica la categoria donde mas gasta y si es necesaria o prescindible
    3. Dame 3 recomendaciones concretas y accionables para proximos meses
    4. Sugiere una estrategia para alcanzar sus objetivos de inversion y ahorro

    Se directo, no uses rodeos. Habla como si estuvieras en una reunion personal pero amigable."""    
    mensaje = client.messages.create(
        model = "claude-haiku-4-5-20251001",
        max_tokens = 800,
        messages = [
            {
                "role": "user",
                "content": prompt
            }
        ]

    )
    
    return mensaje.content[0].text

