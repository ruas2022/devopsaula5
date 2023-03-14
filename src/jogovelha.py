Python 3.3.0 (v3.3.0:bd8afb90ebf2, Sep 29 2012, 10:55:48) [MSC v.1600 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> def inicializar():

tab = [ ]

for i in range(3):

linha = [ ]

for j in range(3):

linha.append(".")

tab.append(linha)

return tab

def main( ):

jogo = inicializar( )

print (jogo)

if __name__ == "__main__":

main()
