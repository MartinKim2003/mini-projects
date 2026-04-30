# App de Gastos Personales

App de finanzas personales construida en Python. Permite registrar gastos e ingresos en un Excel, analizarlos automáticamente y recibir recomendaciones personalizadas con IA.

## ¿Qué hace?

- Lee un archivo Excel con los gastos del mes
- Calcula totales, balance y breakdown por categoría
- Aplica la regla 75/15/10 para distribuir el ingreso
- Alerta cuando estás cerca o te pasaste del presupuesto
- Muestra los gastos convertidos a dólares (oficial, blue, tarjeta)
- Genera gráficos de torta, barras y evolución mensual
- Produce un análisis financiero personalizado con la API de Claude

## Tecnologías

- Python
- pandas
- matplotlib
- anthropic (Claude API)
- requests
- python-dotenv

## Cómo correrlo

1. Cloná el repositorio
2. Creá un archivo `.env` con tu API key: `ANTHROPIC_API_KEY=tu_key`
3. Instalá las dependencias: `pip install -r requirements.txt`
4. Completá el Excel en `data/raw/gastos_ejemplo.xlsx`
5. Corrés `python main.py`

## Estructura
