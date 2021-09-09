class Nodo: #clase que representa cada nodo
  def __init__(self,dato):#Es el dato que le llega al nodo
    self.izquierda=None #Le indicamos que en el nodo izquierdo no existe nada
    self.derecha=None #Le indicamos que en el nodo derecho no existe nada
    self.dato=dato

#La anterior clase nos permite representar los nodos iniciales
#creamos una funcion que nos permita ingresar datos al arbol
def insertar(raiz,nodo): #Tendremos el modo raiz y el modo insertar
  if raiz is None:#Preguntamos si la raiz esta vacia
    raiz =nodo#Si esta vacia se convierta en el modo actual. Sera el primer nodo del arbol
  #SI no se cumple pasamos a comprobar los dos datos (Derecho e izquierdo)
  else:
    if raiz.dato < nodo.dato:#Verificamos si el dato de la raiz es menor que el que trae el nodo
      if raiz.derecha is None:#Preguntamos si derecho esta vacio
        raiz.derecha=nodo
      else:
         insertar(raiz.derecha,nodo)
    else:
      if raiz.izquierda is None:
        raiz.izquierda=nodo
      else:
        insertar(raiz.izquierda,nodo)

#Realizamos un recorrido inorden
def inorden(raiz):
  if raiz is not None:
    inorden(raiz.izquierda)
    print(raiz.dato) 
    inorden(raiz.derecha)

#Realizamos una prueba de insercion.
raiz = Nodo(23)
insertar(raiz, Nodo(13))
insertar(raiz, Nodo(10))
insertar(raiz, Nodo(33))
insertar(raiz, Nodo(18))
insertar(raiz, Nodo(25))
insertar(raiz, Nodo(40))
inorden(raiz)

def ingresar_datos(valor_raiz):
  raiz=Nodo(valor_raiz)
  iniciador="1"
  while iniciador=="1":
    valor=int(input("Ingrese datos:"))
    insertar(raiz, Nodo(valor))
    iniciador=input("Digite 1 para seguir:")
  print("Los datos en forma inorden:")
  inorden(raiz)

def init():
    ingresar_datos(23)

if __name__ == "__name__":
    init()