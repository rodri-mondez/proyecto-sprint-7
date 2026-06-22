# Dashboard Interactivo de Análisis del Mercado Automotriz

## 📝 Descripción breve del problema que resuelve
Al comprar o vender un auto usado, es difícil determinar si el precio es justo debido a la cantidad de variables involucradas (kilometraje, año, tipo de combustible, condición, etc.). Este proyecto resuelve la falta de transparencia en el mercado automotriz de EE. UU. mediante una herramienta interactiva que permite explorar visualmente cómo influye cada característica del vehículo en su precio final, facilitando decisiones de compra/venta basadas en datos reales.

## 🛠️ Tecnologías usadas
- **Python**: Lenguaje principal de desarrollo.
- **Pandas**: Para la carga, limpieza, manejo de valores nulos (`NaN`) y transformación del dataset (`vehicles_us.csv`).
- **Plotly Express**: Para la creación de gráficos interactivos (histogramas y gráficos de dispersión).
- **Streamlit**: Para construir y estructurar la aplicación web interactiva (`app.py`).
- **Jupyter Notebook (EDA.ipynb)**: Entorno utilizado para la etapa inicial de Análisis Exploratorio de Datos.

## 🚀 Cómo ejecutarlo
Para correr este proyecto de forma local, sigue estos pasos:

1. **Clona este repositorio:**
   ```bash
   git clone [https://github.com/rodri-mondez/Proyectos-Data-Science.git](https://github.com/rodri-mondez/Proyectos-Data-Science.git)
   cd Proyectos-Data-Science
**Instala las dependencias necesarias:**
(Asegúrate de tener Python instalado)

pip install -r requirements.txt

**Ejecuta la aplicación de Streamlit:**

streamlit run app.py
Se abrirá automáticamente una pestaña en tu navegador web con el dashboard interactivo.
