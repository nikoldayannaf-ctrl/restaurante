# Limpieza CSV — restaurante

Este pequeño script limpia el CSV eliminando tildes/diacríticos y reemplazando valores `NA` o campos vacíos por la cadena `None`.

Uso rápido:

```powershell
python clean_csv.py dataset6_restaurant_orders.csv
# Resultado por defecto: dataset6_restaurant_orders_clean.csv
```

Versiones disponibles:

- `clean_csv.py` — usa pandas (mejor para datasets grandes, requiere instalar `pandas`).
- `clean_csv_nopandas.py` — no necesita instalar nada (usa sólo la librería estándar de Python). Recomendado si no quieres instalar paquetes.

Si usas la versión con pandas instala dependencias:

```powershell
python -m pip install -r requirements.txt
```

Qué hace el script:
- Lee el CSV como texto para preservar el contenido original.
- Para cada columna de texto elimina acentos (Sofía -> Sofia, Ensalada César -> Ensalada Cesar, Sí -> Si)
- Reemplaza valores literales 'NA' (mayúsc/ minúsc) y celdas vacías por la cadena `None`.

Si quieres que `None` se interprete como nulo (vacío) al guardarlo, modifica el script para escribir valores NaN en lugar de la cadena "None".

Ejemplo — uso sin instalar paquetes (solo Python):

```powershell
python clean_csv_nopandas.py dataset6_restaurant_orders.csv
# Crea: dataset6_restaurant_orders_limpio.csv
```

Ejemplos de transformación (mini-diff):

- "Sofía"  -> "Sofia"
- "Ensalada César" -> "Ensalada Cesar"
- "Sí" -> "Si"
- campo con "NA" -> "None"
- campo vacío -> "None"
