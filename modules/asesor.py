"""MVP 3"""
# =================================================
# ASESOR
# =================================================
import os
from dotenv import load_dotenv
from anthropic import Anthropic

load_dotenv() # lee el archivo .env y carga las variables
client = Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

def consultar_claude(resumen, gastos_categoria, distribucion):
    """
    Arma un prompt con los datos reales del mes
    y le pide a Claude un análisis personalizado
    """
    prompt = f"""Eres un asesor financiero experimentado. Analiza los gastos de un estudiante universitario argentino de 22 años que vive en Buenos Aires
    y genera recomendaciones prácticas y directas.

    DATOS FINANCIEROS DEL MES:
    - Ingresos total: {resumen["total_ingresos"]: ,.0f} ARS
    - Gastos Totales: {resumen["total_gastos"]: ,.0f} ARS
    - Balance net: {resumen ["balance"]: ,.0f} ARS
    - Presupuesto asignado (75%): {distribucion["gasto"]: ,.0f} ARS
    - Inversión recomendada (15%): {distribucion["inversion"]: ,.0f} ARS
    - Ahorro objetivo (10%): {distribucion["ahorros"]: ,.0f} ARS
    
    DESGLOSE DE GASTOS POR CATEGORIA: 
    {gastos_categoria.to_string()}
    
    OUTPUT:
    1.Resumen en 2-3 líneas como le fue este mes (si estuvo dentro del presupuesto, donde gasto mas, etc)
    2.Identifica la categoria donde mas gasta y si es necesaria o prescindible
    3.Dame 3 recomendaciones concretas y accionables para proximos meses
    4.Sugiere una estrategia paaara alcanzar sus objetivos de inversión y ahorro
    
    Se directo, no uses rodeos. Habla como si estuvieras en una reunión personal pero amigable
    """
    
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

