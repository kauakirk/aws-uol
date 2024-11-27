class Veiculo:
    def movimentar(self):
        print("Movimentei")
    def __init__(self, fabricante, modelo):
        self.__fabricante = fabricante
        self.__modelo = modelo
        self.__registro = None
    
    def get_fabri_modelo(self):
        print(f"modelo {self.__modelo}, fabricante {self.__fabricante} ")

    def set_num_registros(self, registro):
        self.__registros = registro


    def get_num_registros(self):
        return self.__registros
    

class Carro(Veiculo):
    def movimentar(self):
        print("eu sou um carro andando")

       



    
if __name__=='__main__':
    meu_veiculo = Veiculo('gm', 'cadillac')
    meu_veiculo.movimentar
    meu_veiculo.get_fabri_modelo
    meu_veiculo.set_num_registros(999)