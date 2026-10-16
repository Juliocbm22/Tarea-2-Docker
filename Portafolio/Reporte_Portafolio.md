# Portafolio de Prácticas y Proyecto Individual de Docker

**Nombre:** Julio ...
**Código:** ...
**Materia:** ...
**Sección:** ...
**Fecha:** 2026-10-15

---

## Parte 1. Prácticas realizadas durante el curso

### Práctica 1: <Nombre de la práctica>

**1. Archivos del proyecto**
```
<estructura de carpetas y archivos>
```
*Captura de pantalla aquí* (insertar imagen).

**2. Construcción de la imagen**
```bash
$ docker build -t nombre-imagen:tag .
```
*Captura de terminal con salida*.

**3. Imagen creada**
```bash
$ docker images
```
*Captura de salida*.

**4. Ejecución del contenedor**
```bash
$ docker run -d --name nombre-contenedor nombre-imagen:tag
```
*Captura de terminal*.

**5. Contenedor en ejecución**
```bash
$ docker ps
```
*Captura de salida*.

**6. Funcionamiento**
*Descripción breve del resultado (p. ej., aplicación web accesible en http://localhost:8080)*.

**7. Característica principal**
*Volumen / Puerto / Compose / Multietapa / CMD / ENTRYPOINT, según corresponda.*

**8. Explicación**
Se construyó una imagen que ... Se utilizó ... para ...
---

*(Repetir la sección anterior para cada práctica realizada.)*

---

## Parte 2. Proyecto individual – Machine Learning con Docker

### 1. Estructura del proyecto
```
Proyecto_ML_Docker/
├─ data/               # Dataset (ej. csv)
├─ model/              # Modelo entrenado (model.pkl)
├─ src/
│   ├─ train.py        # Script de entrenamiento
│   └─ app.py          # API FastAPI
├─ requirements.txt    # Dependencias Python
├─ Dockerfile          # Instrucciones de construcción
├─ .dockerignore       # Archivos a excluir
└─ README.md           # Instrucciones de uso
```
*Captura de árbol de carpetas*.

### 2. Entrenamiento
```bash
$ python src/train.py --data data/dataset.csv --output model/model.pkl
```
*Captura de terminal con salida*.

### 3. Dockerfile
```Dockerfile
FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY src/ ./src
COPY model/ ./model
EXPOSE 8000
CMD ["uvicorn", "src.app:app", "--host", "0.0.0.0", "--port", "8000"]
```
*Captura de archivo Dockerfile*.

### 4. Construcción de la imagen
```bash
$ docker build -t proyecto-ml:latest .
```
*Captura de terminal*.

### 5. Imagen creada
```bash
$ docker images | grep proyecto-ml
```
*Captura de salida*.

### 6. Contenedor
```bash
$ docker run -d -p 8000:8000 --name proyecto-ml proyecto-ml:latest
```
*Captura de terminal*.

### 7. Contenedor activo
```bash
$ docker ps
```
*Captura de salida*.

### 8. FastAPI accesible
Abrir en navegador: `http://localhost:8000/docs`
*Captura de pantalla de la documentación*.

### 9. Predicción
```bash
$ curl -X POST "http://localhost:8000/predict" -H "Content-Type: application/json" -d '{"features": [ ... ]}'
```
*Captura de respuesta*.

### 10. Logs del contenedor
```bash
$ docker logs proyecto-ml
```
*Captura de logs*.

### 11. Explicación del proyecto
Breve descripción del flujo de datos, entrenamiento, guardado del modelo y exposición vía API. Se utilizó Docker para garantizar que todas las dependencias y el entorno se mantengan consistentes entre diferentes máquinas.

---

## Preguntas conceptuales
1. **Diferencia entre imagen y contenedor:** ...
2. **Función de requirements.txt:** ...
3. **Función del Dockerfile:** ...
4. **Uso de .dockerignore:** ...
5. **Significado del mapeo de puertos:** ...
6. **Cambio 8000:8000 a 8001:8000:** ...
7. **Ventaja de Docker vs instalación manual:** ...
8. **Ejecutar con solo la imagen:** ...

---

*Nota:* Reemplazar los textos entre `< >` y los placeholders con la información y capturas reales de cada práctica.
