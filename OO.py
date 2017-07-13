class Televisao:
       def __init__(self):
              self.ligada = False
              self.canal = 2

       def ProximoCanal(self,nome):
              print(nome)
              self.canal += 1

       def AnteriorCanal(self):
              self.canal -=1

       def Magic(self):
              if(self.canal % 2 == 0):
                     ProximoCanal('Alciomar')
              else:
                     AnteriorCanal()
       
