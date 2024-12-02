import turtle

class NodoArbol:
    def __init__(self, valor):
        self.valor = valor
        self.izquierdo = None
        self.derecho = None

class ArbolBinario:
    def __init__(self):
        self.raiz = None

    def construir_arbol(self, inorden, postorden):
        def construir(inorden, postorden):
            if not inorden or not postorden:
                return None
            raiz_valor = postorden.pop()
            raiz = NodoArbol(raiz_valor)
            indice_raiz = inorden.index(raiz_valor)
            raiz.derecho = construir(inorden[indice_raiz + 1:], postorden)
            raiz.izquierdo = construir(inorden[:indice_raiz], postorden)
            return raiz

        self.raiz = construir(inorden, postorden)

    def obtener_preorden(self):
        def preorden(nodo):
            if nodo is None:
                return []
            return [nodo.valor] + preorden(nodo.izquierdo) + preorden(nodo.derecho)
        return preorden(self.raiz)

    def dibujar_arbol(self, grosor_lineas=2, x_inicio=0, y_inicio=0):
        turtle.speed(0)
        turtle.width(grosor_lineas)
        turtle.hideturtle()
        screen = turtle.Screen()
        screen.tracer(0, 0)
        self.__dibujar_nodo(self.raiz, x_inicio, y_inicio, 200, "blue")
        screen.update()
        turtle.done()

    def __dibujar_nodo(self, nodo, x, y, dx, color_letra):
        if nodo is not None:
            turtle.penup()
            turtle.goto(x, y - 20)
            turtle.pendown()
            turtle.circle(20)
            turtle.penup()
            turtle.goto(x, y - 10)
            turtle.pendown()
            turtle.color(color_letra)
            turtle.write(nodo.valor, align="center", font=("Arial", 12, "bold"))
            turtle.color("black")
            if nodo.izquierdo is not None:
                turtle.penup()
                turtle.goto(x, y - 20)
                turtle.pendown()
                turtle.goto(x - dx, y - 80)
                self.__dibujar_nodo(nodo.izquierdo, x - dx, y - 80, dx / 2, color_letra)
                turtle.penup()
                turtle.goto(x, y - 20)
                turtle.pendown()
            if nodo.derecho is not None:
                turtle.penup()
                turtle.goto(x, y - 20)
                turtle.pendown()
                turtle.goto(x + dx, y - 80)
                self.__dibujar_nodo(nodo.derecho, x + dx, y - 80, dx / 2, color_letra)
                turtle.penup()
                turtle.goto(x, y - 20)
                turtle.pendown()

inorden = ['D', 'M', 'A', 'T', 'L', 'C', 'B', 'I', 'K', 'U', 'S', 'R', 'O', 'N']
postorden = ['D', 'M', 'L', 'C', 'T', 'A', 'I', 'S', 'R', 'U', 'N', 'O', 'K', 'B']

arbol = ArbolBinario()
arbol.construir_arbol(inorden, postorden)

preorden = arbol.obtener_preorden()
print("Recorrido en preorden:", preorden)

arbol.dibujar_arbol()

