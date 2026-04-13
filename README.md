# 📋 Sistema de Registro de Clientes (Flask + XML)

## 🖥️ Descripción del Proyecto

Aplicación web desarrollada en Python utilizando Flask, que permite registrar clientes mediante un formulario y almacenar la información en un archivo XML. El sistema gestiona datos como nombre, apellido, correo electrónico y fecha de registro, funcionando como una base de datos ligera basada en archivos.

---

## ⚙️ Tecnologías utilizadas

- Python  
- Flask (framework web)  
- HTML5  
- Bootstrap 5 (interfaz gráfica)  
- XML (almacenamiento de datos)  
- xml.etree.ElementTree (manejo de XML)  
- datetime (registro de fecha y hora)

---

## 🚀 Funcionalidades

- Registro de clientes mediante formulario web  
- Validación de campos obligatorios  
- Almacenamiento de datos en archivo XML  
- Creación automática del archivo XML si no existe  
- Registro de fecha y hora de cada cliente  
- Interfaz web sencilla y responsiva  
- Mensaje de confirmación tras registro exitoso

## 🔧 Instalación

Instalar las dependencias necesarias:

```bash
pip install flask
```
## ▶️ Ejecución del proyecto

1. 🧪 Ejecutar el siguiente comando:

```bash
python app.py
```
## 🌐 Abrir en el navegador

Una vez que el servidor esté en ejecución, abre tu navegador web y entra a la siguiente dirección:

http://127.0.0.1:5000/

📋 Se abrirá la interfaz del sistema de registro de clientes, donde podrás ingresar los datos y realizar registros.

## 🧩 Cómo funciona

El sistema utiliza Flask para gestionar las rutas web y recibir los datos del formulario mediante el método POST.

Los datos ingresados por el usuario son procesados en el servidor y almacenados en un archivo XML utilizando la librería `xml.etree.ElementTree`.

Si el archivo XML no existe, el sistema lo crea automáticamente con la estructura base `<clientes>`.

Cada nuevo registro se añade como un nodo `<cliente>` con sus respectivos campos.

---

## 💡 Valor del proyecto

Este sistema permite comprender el manejo de datos en aplicaciones web utilizando Flask, así como el uso de XML como alternativa a bases de datos tradicionales.

Es útil en proyectos académicos para aprender:

- Arquitectura cliente-servidor  
- Manejo de formularios web  
- Persistencia de datos sin base de datos  
- Integración de backend con frontend 
