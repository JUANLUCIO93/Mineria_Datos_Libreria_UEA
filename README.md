# Mineria_Datos_Libreria_UEA
# 📚 Proyecto Final: Análisis y Minería de Datos para un Sistema de Gestión de Librería Comercial

**Asignatura:** Minería de Datos  
**Estudiante:** Juan Lucio Grefa Alvarado  
**Institución:** Universidad Estatal Amazónica (UEA)  
**Semestre:** Sexto Semestre  
**Fecha:** 24 de Septiembre 2026  

---

## 📖 Descripción del Proyecto
Este repositorio contiene el desarrollo analítico y los modelos de minería de datos aplicados sobre la base de datos transaccional de un **Sistema de Gestión de Librería Comercial**. El objetivo principal es predecir la fuga o inactividad de clientes (*Customer Churn*), optimizar el control de inventario de títulos bibliográficos y analizar patrones de compra para estrategias de recomendación personalizada.

---

## 🛠️ Estructura del Repositorio
* `PROYECTO_FINAL_ANALISIS_DE_DATOS_DE_UN_SISTEMA_DE_UNA_LIBRERIA_COMERCIAL.ipynb`: Cuaderno principal de Google Colab con el preprocesamiento, análisis exploratorio y evaluación de algoritmos (Regresión Logística, Árboles de Decisión y Random Forest).
* `README.md`: Documentación e introducción al proyecto.

---

## 📊 Metodología y Modelos Evaluados
1. **Limpieza y Preprocesamiento:** Imputación de nulos, eliminación de duplicados y codificación categórica (*One-Hot Encoding*).
2. **Feature Engineering:** Creación de variables derivadas como `ticket_promedio_unidad` e `indice_fidelidad_pago`.
3. **Modelado y Validación:**
   * Regresión Logística
   * Árboles de Decisión
   * Random Forest (Modelo Ganador con 82.8% de Accuracy y AUC-ROC de 0.864)
4. **Evaluación:** Validación Cruzada (K=5) y análisis mediante Matrices de Confusión.

---

## 🚀 Cómo ejecutar este cuaderno
Puedes abrir y ejecutar directamente el código en Google Colab haciendo clic en el siguiente enlace:

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/JUANLUCIO93/Mineria_Datos_Libreria_UEA/blob/main/PROYECTO_FINAL_ANALISIS_DE_DATOS_DE_UN_SISTEMA_DE_UNA_LIBRERIA_COMERCIAL.ipynb)

---

## 📬 Contacto
* **Autor:** Juan Lucio Grefa Alvarado
* **Universidad:** Universidad Estatal Amazónica
