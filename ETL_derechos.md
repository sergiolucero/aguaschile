# ETL Derechos de agua

Fuente: http://www.dga.cl/productosyservicios/derechos_historicos/Paginas/default.aspx

El archivo original (descargado en Excel y transformado al formato CSV comprimido como csv.gz) 
contiene múltiples detalles que fueron corregidos en el proceso de ETL 
(extracción, transformación y carga, por sus siglas en inglés). Detallamos el proceso a continuación.

1. Dimensiones

El archivo contiene 125'752 registros al mes de abril de 2019. Cada registro tiene 69 columnas, clasificables entre 

identificadores, fechas, geográficas y numéricas

1A. Variables geográficas

Región, Provincia y Comuna: venían con muchos espacios a la derecha (ej: "Metropolitana    "), por lo que se eliminó este relleno. 
En el caso de las Comunas, había 1149 archivos (un 0.9% del total) sin información (NaN) que fueron eliminados, 
grabándolos al archivo sin_comuna.csv.

1B. Variables numéricas

Caudal: definido por meses, variables Enero, Febrero, ..., Diciembre. Venía con muchos espacios que fueron transformados a 0.0
Hay un error grueso: ND-1305-4288 le daría 500 MILLONES de litros/segundo a Viña Ventisquero en Melipilla (son 500).
