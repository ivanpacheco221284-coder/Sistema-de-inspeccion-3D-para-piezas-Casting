# Sistema de Inspección de Piezas Industriales (PASS/FAIL)

Este repositorio contiene un sistema de clasificación automatizado para la detección de conformidad (`PASS`/`FAIL`) en piezas industriales de fundición (casting). 

El proyecto integra un modelo óptimo de Machine Learning, una API REST con **FastAPI** para realizar inferencias en tiempo real y una interfaz gráfica interactiva utilizando **Streamlit**.

## 📋 Estructura del Proyecto

```bash
├── app.py                     # Frontend interactivo en Streamlit
├── main.py                    # Backend y API REST en FastAPI
├── modelo_random_forest.pkl   # Modelo entrenado final de Random Forest
├── Dockerfile                 # Configuración para contenedorizar la aplicación
├── requirements.txt           # Dependencias del proyecto
└── README.md                  # Documentación del proyecto
```

---

## 🧠 Análisis y Selección del Modelo

Se evaluaron tres algoritmos de clasificación sobre el conjunto de mediciones de piezas:
- **XGBoost**
- **LightGBM**
- **Random Forest**

### Resultados Comparativos:
- **Modelo Óptimo:** **Random Forest**
- **F1-Score:** `~98.7%`
- **Accuracy:** `98.75%`
- **Precisión:** `100%` (Cero falsos positivos en las pruebas de validación).

---

## 🚀 Instrucciones de Ejecución Local

### 1. Clonar el repositorio e instalar dependencias
```bash
git clone <url-de-tu-repositorio>
cd <nombre-del-repositorio>
pip install -r requirements.txt
```

### 2. Iniciar el Backend (FastAPI)
El backend sirve las predicciones del modelo en el puerto `8000`.
```bash
uvicorn main:app --host 0.0.0.0 --port 8000
```

### 3. Iniciar el Frontend (Streamlit)
En otra terminal, ejecuta el frontend que se conectará a la API local:
```bash
streamlit run app.py
```

---

## 🐳 Despliegue con Docker

Este proyecto está listo para ser contenedorizado. Puedes construir y levantar toda la solución utilizando el archivo `Dockerfile` adjunto.

### Construir la imagen
```bash
docker build -t sistema-inspeccion:latest .
```

### Ejecutar el contenedor
```bash
docker run -d -p 8000:8000 sistema-inspeccion:latest
```
La API estará disponible en `http://localhost:8000`.

---

## 🛠️ Tecnologías Utilizadas
- **Python 3.11**
- **Scikit-Learn** (Random Forest)
- **FastAPI** (Desarrollo de API)
- **Streamlit** (Dashboard / Interfaz)
- **Docker** (Despliegue y portabilidad)
- **Joblib** (Persistencia del modelo)
