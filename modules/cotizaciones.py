"""MVP 4"""
# =================================================
# ESTRUCTURA
# =================================================

import requests

def obtener_cotizaciones():
    url = (f"https://dolarapi.com/v1/dolares")
    response = requests.get(url)
    data = response.json()
    return {
        "oficial": data[0]["venta"],
        "blue": data[1]["venta"],
        "tarjeta": data[4]["venta"]
    }

def convertir_a_dolar(monto, cotizaciones):
    oficial = cotizaciones["oficial"]
    blue = cotizaciones["blue"]
    tarjeta = cotizaciones["tarjeta"]
    
    monto_oficial = monto / oficial
    monto_blue = monto / blue
    monto_tarjeta = monto / tarjeta
    
    return {
        "oficial": monto_oficial,
        "blue": monto_blue,
        "tarjeta": monto_tarjeta
    }
    
def imprimir_conversion(conversion, cotizacion):
    print("\n=== TUS GASTOS EN DÓLARES ===")
    print(f"Dolar oficial: $ {conversion["oficial"]: ,.0f} USD (cotizacion {cotizacion["oficial"]: ,.0f} ARS)")
    print(f"Dolar blue: ${conversion["blue"]: ,.0f} USD (cotizacion{cotizacion["blue"]: ,.0f} ARS)")
    print(f"Dolar tarjeta: ${conversion["tarjeta"]: ,.0f} USD (cotizacion{cotizacion["tarjeta"]: ,.0f} ARS)")

