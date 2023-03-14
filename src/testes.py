Python 3.3.0 (v3.3.0:bd8afb90ebf2, Sep 29 2012, 10:55:48) [MSC v.1600 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import jogovelha

import sys

erroInicializar = False

jogo = jogovelha.inicializar()

if len(jogo) != 3:

erroInicializar = True

else:

for linha in jogo:

if len(linha) != 3:

erroInicializar = True

else:

for elemento in linha:

if elemento != '.':

erroInicializar = True

if erroInicializar:

sys.exit(1)

else:

sys.exit(0)
