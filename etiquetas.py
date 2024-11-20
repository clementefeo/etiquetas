# -*- coding: utf-8 -*-
"""
Repositorio Git: https://github.com/clementefeo/etiquetas

Librerías necesarias:
    pip install python-barcode reportlab

Descripción:
    Este script genera un PDF con etiquetas que incluyen códigos de barras Code 128 y texto.
    Se puede especificar el rango de etiquetas, el texto de la etiqueta, el título, el prefijo y el nombre del archivo de salida.
"""

import barcode
from barcode.writer import ImageWriter
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
import os
import shutil
import argparse

def generar_etiqueta(c, codigo, texto, titulo, x, y, ancho_etiqueta, alto_etiqueta):
    try:
        temp_dir = "temp_barcode_images"
        os.makedirs(temp_dir, exist_ok=True)
        filepath = os.path.join(temp_dir, f"temp_{codigo}.png")

        ean = barcode.get_barcode_class('code128')
        code = ean(codigo, writer=ImageWriter())
        code.save(filepath[:-4])

        y_barcode = y + 2 * mm
        c.drawImage(filepath, x, y_barcode, width=ancho_etiqueta, height=alto_etiqueta * 0.7, preserveAspectRatio=True)

        c.setFont("Helvetica", 8)
        texto_ancho = c.stringWidth(texto, "Helvetica", 8)
        x_texto = x + (ancho_etiqueta - texto_ancho) / 2
        margen_inferior = 2 * mm
        c.drawString(x_texto, y + margen_inferior, texto)

        c.setFont("Helvetica", 6)
        titulo_ancho = c.stringWidth(titulo, "Helvetica", 6)
        x_titulo = x + (ancho_etiqueta - titulo_ancho) / 2
        margen_superior = alto_etiqueta - 4 * mm
        c.drawString(x_titulo, y + margen_superior, titulo)

        margen_linea = 0 * mm
        c.setStrokeColorRGB(0.5, 0.5, 0.5)
        c.setLineWidth(0.5)
        c.rect(x + margen_linea, y, ancho_etiqueta - margen_linea, alto_etiqueta)

    except Exception as e:
        print(f"Error generando etiqueta para {codigo}: {e}")


def generar_etiquetas_pdf(num_etiquetas_inicio, num_etiquetas_fin, texto_etiqueta, titulo_etiqueta, prefijo_etiqueta, filename="etiquetas.pdf"):
    c = canvas.Canvas(filename, pagesize=A4)

    margen_horizontal = 10 * mm  # Margen izquierdo y derecho
    ancho_total_disponible = A4[0] - 2 * margen_horizontal
    etiquetas_por_fila = 3
    ancho_etiqueta = ancho_total_disponible / etiquetas_por_fila
    alto_etiqueta = 30 * mm

    x = margen_horizontal
    y = A4[1] - 10 * mm - alto_etiqueta  # Margen superior

    for i in range(num_etiquetas_inicio, num_etiquetas_fin + 1):
        codigo = f"{prefijo_etiqueta}-{i:05}"
        texto = texto_etiqueta
        titulo = titulo_etiqueta
        generar_etiqueta(c, codigo, texto, titulo, x, y, ancho_etiqueta, alto_etiqueta)
        x += ancho_etiqueta

        if (i % etiquetas_por_fila == 0):
            x = margen_horizontal
            y -= alto_etiqueta
            if y < 10 * mm:  # Margen inferior
                c.showPage()
                y = A4[1] - 10 * mm - alto_etiqueta

    c.save()

    try:
        shutil.rmtree("temp_barcode_images")
    except OSError as e:
        print(f"Error al eliminar la carpeta temporal: {e}")


def main():
    parser = argparse.ArgumentParser(description="Generador de etiquetas con código de barras.")
    parser.add_argument("-n", "--numero", help="Rango de etiquetas (ej. 50-100 o un solo número)", required=True)
    parser.add_argument("-t", "--texto", help="Texto para la etiqueta entre comillas simples (ej: 'ORDENADOR HP')", required=True)
    parser.add_argument("-T", "--titulo", help="Título para la etiqueta entre comillas simples (ej: 'NOMBRE EMPRESA')", required=True)
    parser.add_argument("-p", "--prefijo", help="Prefijo para el código de barras (ej: 'ORD')", default="ORD")
    parser.add_argument("-o", "--output", help="Nombre del archivo PDF de salida (opcional)", default="etiquetas.pdf")

    args = parser.parse_args()

    try:
        if "-" in args.numero:
            inicio, fin = map(int, args.numero.split("-"))
        else:
            inicio = int(args.numero)
            fin = int(args.numero)

        if inicio <= 0 or fin <= 0 or inicio > fin:
             raise ValueError("Rango de etiquetas inválido.")

        generar_etiquetas_pdf(inicio, fin, args.texto, args.titulo, args.prefijo, args.output)
        print(f"PDF generado con éxito: {args.output}")

    except ValueError as e:
        print(f"Error: {e}")
        parser.print_help()
    except Exception as e:
        print(f"Error inesperado: {e}")
        parser.print_help()


if __name__ == "__main__":
    main()
