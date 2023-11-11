import math

class TrianguloRectangulo:
  def _Init_ (self, diametro, angulo):
    self.diametro = diaetro
    self.angulo = angulo

  def catetoA (self):
    self.catetoA = math.sin(self.angulo)
    return self.catetoA
  def CatetoB (self):  
    self.catetob = math.cos(self.angulo)
    return self.catetoA

  def area (self, catetoA, catetoB):
    self.area = (catetoA*catetoB)/2
    return self area

x = input ("ingrese la hipotenusa del triangulo: ")
y =input("ingrese el angulo del triangulo: ") 
tri = TrianguloRectangulo(int(x), int(y))
print("el area del triangulo es:", tri.area())
