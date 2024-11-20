# Generador de Etiquetas con Código de Barras

Este script de Python genera un PDF con etiquetas que incluyen códigos de barras Code 128 y texto personalizable.  Es ideal para generar etiquetas para inventarios, productos, etc.

## Ejemplo

![Ejemplo de etiquetas generadas](https://raw.githubusercontent.com/clementefeo/etiquetas/main/Ejemplo.png)

## Características

* Genera códigos de barras Code 128.
* Permite personalizar el texto de la etiqueta.
* Genera un PDF con múltiples etiquetas por página.
* Incluye líneas de corte para facilitar la separación de las etiquetas.
* Permite especificar el rango de etiquetas a generar.
* Manejo de errores y ayuda por línea de comandos.


## Dependencias

* **Python 3.6+:** 
* **python-barcode:** `pip install python-barcode`
* **reportlab:** `pip install reportlab`

## Instalación

1. Clona este repositorio:
   ```bash
   git clone https://github.com/clementefeo/etiquetas
   ```

2. Instala las dependencias:
   ```bash
   pip install python-barcode reportlab
   ```

## Uso

```bash
python3 etiquetas.py -n <RANGO_ETIQUETAS> -t <TEXTO_ETIQUETA> [-o <NOMBRE_ARCHIVO>]
```

* **-n, --numero:** Rango de etiquetas a generar. Se puede especificar un solo número (ej. `25`) o un rango (ej. `50-100`).  Obligatorio.
* **-t, --texto:**  Texto que aparecerá en la etiqueta debajo del código de barras. Obligatorio.
* **-o, --output:** Nombre del archivo PDF de salida. Opcional.  Por defecto: `etiquetas.pdf`.

**Ejemplos:**

```bash
python3 etiquetas.py -n 10-20 -t "Producto A"  # Genera etiquetas del 10 al 20 con el texto "Producto A".
python3 etiquetas.py -n 5 -t "Ejemplo" -o mis_etiquetas.pdf # Genera la etiqueta 5 con el texto "Ejemplo" y guarda el PDF como "mis_etiquetas.pdf".
```

## Licencia

[MIT](https://choosealicense.com/licenses/mit/)


## Contribuciones

Las contribuciones son bienvenidas.  Por favor, crea un *fork* del repositorio y envía un *pull request*.


