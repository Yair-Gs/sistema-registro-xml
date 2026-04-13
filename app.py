from flask import Flask, render_template, request
import xml.etree.ElementTree as ET
from datetime import datetime
import os

app = Flask(__name__)

ARCHIVO_XML = "registro_clientes.xml"

def crear_xml_si_no_existe():
    if not os.path.exists(ARCHIVO_XML):
        root = ET.Element("clientes")
        tree = ET.ElementTree(root)
        tree.write(ARCHIVO_XML, encoding="utf-8", xml_declaration=True)

@app.route("/", methods=["GET", "POST"])
def formulario():
    crear_xml_si_no_existe()

    if request.method == "POST":
        nombre = request.form["nombre"]
        apellido = request.form["apellido"]
        correo = request.form["correo"]

        tree = ET.parse(ARCHIVO_XML)
        root = tree.getroot()

        cliente = ET.SubElement(root, "cliente")
        ET.SubElement(cliente, "nombre").text = nombre
        ET.SubElement(cliente, "apellido").text = apellido
        ET.SubElement(cliente, "correo").text = correo
        ET.SubElement(cliente, "fecha_registro").text = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        tree.write(ARCHIVO_XML, encoding="utf-8", xml_declaration=True)

        return render_template("index.html", mensaje="✅ Cliente registrado correctamente")

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)