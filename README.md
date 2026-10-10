
Clasificación Inteligente de Piezas Industriales mediante Machine Learning y Hugging Face
Autor
Pablo Iván Pacheco García
Matrícula: AL07181329

📋 Resumen Ejecutivo
Este proyecto desarrolla una solución de clasificación automática para inspección de calidad industrial utilizando técnicas de Machine Learning. El objetivo consiste en identificar piezas conformes (PASS) y no conformes (FAIL) a partir de mediciones dimensionales registradas durante el proceso de manufactura.

La investigación se realizó utilizando Google Colab, el ecosistema Hugging Face y algoritmos de clasificación supervisada, evaluando y comparando el desempeño de tres modelos:

Random Forest
XGBoost
LightGBM
La comparación considera indicadores de desempeño, eficiencia computacional y viabilidad de implementación en entornos industriales alineados con los principios de Industria 4.0.

🎯 Objetivo
Identificar e implementar el modelo preentrenado o algoritmo de aprendizaje automático más adecuado para un caso de uso industrial, comparando precisión, velocidad de ejecución y consumo de recursos.

🏭 Caso de Uso
Las líneas de producción modernas generan grandes cantidades de información provenientes de sensores, sistemas de visión artificial y equipos de inspección.

En este proyecto se analiza un conjunto de datos de medición dimensional de piezas industriales para determinar automáticamente si una pieza cumple con las especificaciones de calidad requeridas.

Beneficios esperados
Reducción de inspecciones manuales.
Disminución de errores humanos.
Detección temprana de defectos.
Incremento en la eficiencia operativa.
Apoyo a estrategias de Manufactura Inteligente e Industria 4.0.
📊 Dataset
Descripción
El conjunto de datos contiene registros de inspección dimensional de piezas industriales.

Campos disponibles
Variable	Descripción
Index1	Identificador de la muestra
Measured	Valor dimensional medido
Conformance	Resultado de conformidad (PASS / FAIL)
Time	Fecha y hora de captura
Variables generadas
Durante el preprocesamiento se crearon las siguientes variables:

Variable	Descripción
Hour	Hora de captura
Minute	Minuto de captura
Estas características permiten capturar posibles patrones relacionados con el comportamiento temporal del proceso productivo.

🧠 Ecosistema Hugging Face Utilizado
El proyecto utiliza componentes fundamentales de Hugging Face:

Hugging Face Models
Repositorio centralizado para exploración y selección de modelos de IA.

Hugging Face Datasets
Fuente de referencia para administración y distribución de conjuntos de datos.

Hugging Face Hub
Plataforma empleada para autenticación, experimentación y despliegue de modelos.

⚙️ Entorno de Ejecución
Hardware
Google Colab
GPU NVIDIA (cuando disponible)
Software
Python 3.11+
Jupyter Notebook
Google Colab
📦 Dependencias
pip install transformers datasets huggingface_hub
pip install scikit-learn xgboost lightgbm openpyxl
pip install pandas numpy matplotlib seaborn
🔎 Metodología
La metodología implementada consta de las siguientes etapas:

1. Carga de datos
Importación del dataset desde Google Colab.

2. Preprocesamiento
Limpieza de datos.
Conversión de variables.
Extracción de características temporales.
Codificación de etiquetas.
3. División del conjunto de datos
Entrenamiento: 80%
Prueba: 20%
4. Entrenamiento de modelos
Implementación de:

XGBoost
Random Forest
LightGBM
5. Evaluación
Cálculo de:

Accuracy
Precision
Recall
F1-Score
Latencia
6. Comparación
Análisis cuantitativo y cualitativo del desempeño de cada modelo.

📈 Métricas de Evaluación
Métrica	Descripción
Accuracy	Proporción de predicciones correctas
Precision	Exactitud de las predicciones positivas
Recall	Capacidad para detectar casos positivos
F1-Score	Balance entre Precision y Recall
Latencia	Tiempo requerido para entrenamiento
🤖 Modelos Evaluados
Random Forest
Modelo basado en múltiples árboles de decisión que combina las predicciones mediante votación.

Aplicaciones
Clasificación industrial.
Detección de anomalías.
Control de calidad.
XGBoost
Algoritmo de Gradient Boosting ampliamente utilizado en aplicaciones empresariales e industriales.

Aplicaciones
Machine Learning tabular.
Sistemas predictivos.
Optimización de procesos.
LightGBM
Implementación eficiente de Gradient Boosting diseñada para alto rendimiento computacional.

Aplicaciones
Clasificación masiva.
Sistemas en tiempo real.
Big Data.
📊 Resultados Experimentales
Modelo	       Accuracy	  Precision     Recall	  F1-Score	Latencia
Random Forest	98.8 %	   100 %	 97.5 %	   98.7 %	  0.50 s
LightGBM	95.0 %	   92.8 %	 97.5 %	   95.1 %	  0.02 s
XGBoost	        95.0 %	   95.0 %	 95.0 %	   95.0 %	  0.02 s
⚖️ Análisis de Trade-Offs
Comparativa Precisión vs Eficiencia
Modelo	Ventajas	Desventajas
Random Forest	Mayor Accuracy, Precision y F1-Score. Menos errores de clasificación.	Mayor latencia y uso de memoria.
LightGBM	Entrenamiento rápido. Excelente escalabilidad. Bajo consumo de recursos.	Menor precisión global.
XGBoost	Buen equilibrio entre rendimiento y velocidad. Amplio soporte industrial.	No supera a Random Forest en precisión ni a LightGBM en velocidad.
Conclusión del Trade-Off
Existe una relación directa entre rendimiento predictivo y costo computacional.

Random Forest prioriza la precisión.
LightGBM prioriza la velocidad.
XGBoost ofrece una alternativa equilibrada.
✅ Modelo Recomendado
Random Forest
Justificación
El modelo obtuvo los mejores resultados globales en todas las métricas analizadas:

Accuracy: 98.8 %
Precision: 100 %
Recall: 97.5 %
F1-Score: 98.7 %
Además, presentó la menor cantidad de errores observados en las matrices de confusión, demostrando una alta capacidad para identificar piezas defectuosas.

Aunque su tiempo de entrenamiento fue superior al de LightGBM y XGBoost, la diferencia resulta aceptable frente a la mejora significativa en desempeño predictivo.

⚠️ Riesgos y Limitaciones
Riesgos Técnicos
Sobreajuste
El modelo puede aprender patrones específicos del conjunto de entrenamiento.

Deriva del Proceso
Cambios futuros en maquinaria o condiciones de operación podrían afectar la precisión.

Nuevos Modos de Falla
Pueden surgir defectos no representados en los datos históricos.

Calidad de Datos
Mediciones incorrectas pueden impactar directamente el rendimiento del modelo.

📂 Estructura del Repositorio
Act4_HuggingFace_Industrial_Quality
│
├── README.md
├── requirements.txt
│
├── data
│   └── Dataset medicion de piezas.xlsx
│
├── notebooks
│   └── Act4_HuggingFace_Medicion_Piezas.ipynb
│
├── src
│   └── Act4_HuggingFace_Medicion_Piezas.py
│
├── results
│   ├── metricas_comparativas.csv
│   ├── confusion_matrix_rf.png
│   ├── confusion_matrix_xgb.png
│   ├── confusion_matrix_lgbm.png
│   └── comparativa_metricas.png
│
└── docs
    └── Analisis_Comparativo_Act4.docx
🚀 Cómo Ejecutar el Proyecto
Clonar el repositorio
git clone https://github.com/usuario/repositorio.git
Instalar dependencias
pip install -r requirements.txt
Abrir Notebook
notebooks/Act4_HuggingFace_Medicion_Piezas.ipynb
Ejecutar todas las celdas
Al finalizar se generará automáticamente:

metricas_comparativas.csv
matrices de confusión
gráficos comparativos
ranking de modelos
🏆 Conclusiones
El análisis comparativo demostró que los tres modelos son capaces de clasificar correctamente piezas industriales con altos niveles de precisión. Sin embargo, Random Forest obtuvo el mejor desempeño global, alcanzando la mayor Accuracy, Precision y F1-Score.

Por lo tanto, se recomienda su implementación como modelo principal para sistemas de inspección automática de calidad donde la reducción de errores sea prioritaria.

Los resultados obtenidos validan la viabilidad del uso de técnicas de Machine Learning y herramientas del ecosistema Hugging Face para automatizar procesos de control de calidad industrial, contribuyendo al desarrollo de soluciones de Manufactura Inteligente e Industria 4.0.
