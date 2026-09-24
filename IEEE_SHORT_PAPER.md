
Predicción de Abandono de Clientes y Optimización de Ventas en un Sistema de Gestión de Librería Comercial mediante Algoritmos de Minería de Datos
Juan Lucio Grefa Alvarado
Facultad/ Ingeniería de Tecnologías de Información Comunicación.
Universidad Estatal Amazónica (UEA)
Puyo, Ecuador
jlgrefaa@uea.edu.ec

RESUMEN (ABSTRACT)
El sector de la comercialización minorista de libros enfrenta desafíos significativos debido a los cambios en los hábitos de consumo y la competencia digital. Este artículo presenta la implementación de un pipeline completo de minería de datos aplicado sobre la base de datos transaccional (N = 6,100 registros) de un punto de venta (POS) de una librería comercial. Se aplicaron técnicas de preprocesamiento, auditoría de calidad de datos, ingeniería de características e implementación de modelos de aprendizaje supervisado (Regresión Logística, Árboles de Decisión y Random Forest) para predecir el abandono de clientes (Customer Churn). El modelo Random Forest obtuvo el mejor desempeño con un Accuracy del 82.8% y un área bajo la curva ROC (AUC-ROC) de 0.864. Los resultados demuestran que la recencia de compra y el ticket promedio son determinantes clave para la retención.
Palabras Clave— Minería de datos, Customer Churn, Random Forest, Sistema POS, Librería Comercial, IEEE Short Paper.
I. INTRODUCCIÓN
En el entorno comercial actual, la retención de clientes es considerablemente más rentable que la adquisición de nuevos usuarios. En el contexto de las librerías comerciales, comprender los patrones de consumo permite optimizar la gestión de inventario por categorías bibliográficas (ej. Literatura, Matemáticas, Ciencias) y diseñar campañas de fidelización personalizadas.
El objetivo de este trabajo es desarrollar un modelo predictivo mediante técnicas de minería de datos para identificar a los clientes con mayor probabilidad de abandono (cliente_abandonó = 1) a partir del historial transaccional de un sistema de facturación POS.
II. METODOLOGÍA
A. Arquitectura del Dataset y Preprocesamiento
Se analizó una muestra representativa de 6,100 facturas comerciales procesadas en el sistema de ventas. El dataset incluye 9variables estructurales:
1.	Identificadores: id_factura, id_cliente.
2.	Variables Métricas: monto_facturado (USD), total_libros_comprados, dias_sin_comprar.
3.	Variables Categóricas y Binarias: categoria_mas_comprada, metodo_pago, factura_electronica.
4.	Variable Objetivo (Target): cliente_abandonó (1= Inactivo/Abandonó, 0= Activo).
Se realizó un diagnóstico de integridad utilizando las funciones isnull (). mean () y duplicated(). sum (), verificando la ausencia de datos faltantes (0\% nulos) y la unicidad de las facturas registrados.

B. Análisis Exploratorio y Estadísticas Descriptivas
El análisis descriptivo mediante df.describe() reveló que el ticket promedio de compra en la librería es de 49.84 (STD = 45.03), con un volumen promedio de 4.97 libros por transacción. La variable de recencia (dias_sin_comprar) presentó una media de 89.4 días. La tasa base de abandono de la muestra se situó en el 25.46% (mean = 0.254590).

C. Modelado Predictivo
Para la clasificación binaria del abandono, se dividió el conjunto de datos en entrenamiento (80\%) y prueba (20\%), y se evaluaron tres clasificadores:
1.	Regresión Logística: Como modelo de línea base (baseline).
2.	Árbol de Decisión (Decision Tree): Para capturar reglas de decisión no lineales.
3.	Bosques Aleatorios (Random Forest Classifier): Un ensamble de árboles con 100 estimadores para reducir el varianza y mejorar la generalización.
   
III. RESULTADOS Y DISCUSIÓN
A. Evaluación Comparativa de Modelos
Los algoritmos fueron evaluados utilizando validación cruzada (K=5) 
sobre el conjunto de prueba. La Tabla I resume las métricas obtenidas:
TABLA I. COMPARATIVA DE RENDIMIENTO DE MODELOS
 
B. Importancia de las Características
El modelo Random Forest identificó que las variables con mayor peso predictivo para determinar el abandono del cliente son:
1.	dias_sin_comprar (Recencia): Clientes con más de 120 días sin actividad presentan un incremento del 65% en el riesgo de churn.
2.	monto_facturado: Compradores con tickets promedio bajos (leq 18.32) muestran menor lealtad comercial.
3.	categoria_mas_comprada: Las categorías de Literatura y Matemáticas presentan mayor recurrencia comparadas con Dibujo Artístico.
   
IV. CONCLUSIONES Y TRABAJO FUTURO
1.	La implementación del modelo Random Forest demostró una capacidad robusta (82.8% de exactitud) para anticipar la pérdida de clientes en la librería comercial.
2.	La variable dias_sin_comprar constituye el indicador más crítico. Se recomienda activar campañas de email marketing automatizadas cuando un cliente supere los 90 días de inactividad.
3.	Como trabajo futuro, se contempla integrar técnicas de agrupación (K-Means) para segmentar el catálogo de libros y construir un sistema de recomendación personalizado.



REFERENCIAS
•	[1] J. Han, M. Kamber, and J. Pei, Data Mining: Concepts and Techniques, 3rd ed. Morgan Kaufmann, 2011.
•	[2] F. Pedregosa et al., "Scikit-learn: Machine Learning in Python," Journal of Machine Learning Research, vol. 12, pp. 2825-2830, 2011.
•	[3] J. L. Grefa Alvarado, "Repositorio Código Fuente del Proyecto de Minería de Datos," GitHub, 2026. [En línea]. Disponible en: 
https://github.com/JUANLUCIO93/Mineria_Datos_Libreria_UEA
https://github.com/JUANLUCIO93/Mineria_Datos_Libreria_UEA/blob/main/PROYECTO_FINAL_ANALISIS_DE_DATOS_DE_UN_SISTEMA_DE_UNA_LIBRERIA_COMERCIAL.ipynb




