
```
+----------------------------------------------------------------------+
| ----            GENERADOR DE DICCIONARIOS CON RUTs CHILENOS      ----|
| ----            0xr94                                            ----|
| ----            Contact : 0xr94@proton.me                        ----|
| ----            Version : 2.1                                    ----|
+----------------------------------------------------------------------+
```

# Descripción

**rutchile.py** es una herramienta que permite generar diccionarios con **ruts chilenos válidos** en distintos formator para nuestros ejercicios de Ethical Hacking.

**Nota**: La herramienta fue desarrollada para fines eticos, no me hago responsable por el mal uso de la herramienta.


## Instalación

```
pip install -r requirements.txt
```

## Uso

```
+-----------+--------------------------------------------------------------------------------------+-----------------------+
| Argumento |                                     Descripción                                      |        Ejemplo        |
+-----------+--------------------------------------------------------------------------------------+-----------------------+
|     -f    | Generar diccionario de RUTs con puntos, guión y dígito verificador Ej: 12.345.678-9  | python rutchile.py -f |
|     -d    |        Generar diccionario de RUTs solo con dígito verificador Ej: 12345678-9        | python rutchile.py -d |
|     -l    | Generar diccionario de RUTs sin puntos ni guión con dígito verificador Ej: 123456789 | python rutchile.py -l |
|     -m    |           Generar diccionario de RUTs sin dígito verificador Ej: 12345678            | python rutchile.py -m |
+-----------+--------------------------------------------------------------------------------------+-----------------------+
```
