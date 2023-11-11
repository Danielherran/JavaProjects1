class Circulo:
  pi = 3.14
  def _init_(self, diametro):
    self.radio = diametro / 2
    
  def area(self):
    return self.pi * self.radio ** 2
    
  def perimetro (self):
    return self-pi * 2 * self.radio

x = input ("Ingrese el diametro del lote: ")
lote - Circulo(int(x))
print ("Area de lote:", lote.area() ) 
print("Perimetro de lote:", lote.perimetro())
