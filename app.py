import streamlit as st
import pandas as pd
import numpy as np
import joblib

# Configuración de la interfaz
st.set_page_config(page_title="Predicción de Abandono", layout="centered")

st.title("📚 Sistema de Predicción de Abandono de Clientes")
st.write("Herramienta interactiva para predecir el riesgo de pérdida de compradores en librería.")

# Cargar el modelo entrenado
try:
    model = joblib.load('modelo_libreria.pkl')
    st.success("Modelo cargado correctamente")
except:
    st.error("No se encontró el modelo 'modelo_libreria.pkl'. Asegúrate de haberlo generado.")

# Formulario de entrada de datos
st.subheader("Ingrese los datos de la factura / cliente:")

monto = st.number_input("Monto Facturado ($)", min_value=1.0, value=45.0, step=1.0)
libros = st.number_input("Total de Libros Comprados", min_value=1, value=3, step=1)
dias = st.number_input("Días sin Comprar", min_value=0, value=60, step=1)

factura_elec = st.selectbox("¿Usa Factura Electrónica?", options=[(1, "Sí"), (0, "No")], format_func=lambda x: x[1])[0]
categoria = st.selectbox("Categoría más Comprada", ['Ficción', 'Libro Literatura', 'Libro Matematica', 'Ciencias Naturales', 'Libro dibujo Artistico'])
metodo_pago = st.selectbox("Método de Pago", ['Efectivo', 'Tarjeta_Credito', 'Transferencia'])

# Cálculo de variables derivadas
ticket_promedio = np.round(monto / libros, 2)
indice_fidelidad = np.round(libros / (dias + 1), 4)

# Botón para ejecutar la predicción
if st.button("🔮 Evaluar Riesgo de Abandono"):
    # Estructura de datos para el modelo
    input_data = pd.DataFrame([{
        'monto_facturado': monto,
        'total_libros_comprados': libros,
        'factura_electronica': factura_elec,
        'dias_sin_comprar': dias,
        'ticket_promedio_unidad': ticket_promedio,
        'indice_fidelidad_pago': indice_fidelidad,
        'categoria_mas_comprada_Libro Literatura': 1 if categoria == 'Libro Literatura' else 0,
        'categoria_mas_comprada_Libro Matematica': 1 if categoria == 'Libro Matematica' else 0,
        'categoria_mas_comprada_Ciencias Naturales': 1 if categoria == 'Ciencias Naturales' else 0,
        'categoria_mas_comprada_Libro dibujo Artistico': 1 if categoria == 'Libro dibujo Artistico' else 0,
        'metodo_pago_Efectivo': 1 if metodo_pago == 'Efectivo' else 0,
        'metodo_pago_Transferencia': 1 if metodo_pago == 'Transferencia' else 0,
    }])
    
    # Reordenar columnas para que coincidan con el entrenamiento
    for col in X_train.columns:
        if col not in input_data.columns:
            input_data[col] = 0
    input_data = input_data[X_train.columns]

    # Predicción
    pred = model.predict(input_data)[0]
    prob = model.predict_proba(input_data)[0][1]

    st.markdown("---")
    if pred == 1:
        st.error(f"🚨 **ALTO RIESGO DE ABANDONO** (Probabilidad: {prob*100:.1f}%)")
        st.write("Recomendación: Enviar oferta de fidelización o descuento promocional.")
    else:
        st.success(f"✅ **CLIENTE ACTIVO / RETENIDO** (Probabilidad de abandono: {prob*100:.1f}%)")
