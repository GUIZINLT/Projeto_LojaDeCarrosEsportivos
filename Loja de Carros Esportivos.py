# Loja de SUPER Carros.

from abc import ABC, abstractmethod

class Motor(ABC):
    @abstractmethod
    def get_info(self) -> str: pass

class MotorV8(Motor):
    def get_info(self) -> str: return "V8 Biturbo - 650cv"

class MotorEletrico(Motor):
    def get_info(self) -> str: return "Elétrico - 800cv"

class Carro(ABC):
    def __init__(self, modelo: str, motor: Motor, preco: float):
        self.modelo = modelo
        self.motor = motor
        self.preco = preco
    
    @abstractmethod
    def get_tipo(self) -> str: pass
    
    def calcular_preco(self) -> float:
        return self.preco
    
    def info(self) -> str:
        return f"{self.modelo} | {self.get_tipo()} | {self.motor.get_info()} | R$ {self.calcular_preco():,.2f}"

class SuperCarro(Carro):
    def get_tipo(self) -> str: return "Super"
    def calcular_preco(self) -> float: return self.preco * 1.5

class HyperCarro(Carro):
    def get_tipo(self) -> str: return "Hyper" 
    def calcular_preco(self) -> float: return self.preco * 2.0

class CarroFactory:
    @staticmethod
    def criar(tipo: str, modelo: str, motor: Motor, preco: float) -> Carro:
        if tipo == "super": return SuperCarro(modelo, motor, preco)
        if tipo == "hyper": return HyperCarro(modelo, motor, preco)
        raise ValueError("Tipo inválido")

class Loja:
    _instance = None
    def __new__(cls):
        if not cls._instance:
            cls._instance = super().__new__(cls)
            cls._instance.carros = []
        return cls._instance
    
    def add_carro(self, carro: Carro):
        self.carros.append(carro)
    
    def lista(self):
        for carro in self.carros:
            print(f"🚗 {carro.info()}")

if __name__ == "__main__":
    loja = Loja()
    

    carros = [
        CarroFactory.criar("super", "Ferrari 488", MotorV8(), 800000),
        CarroFactory.criar("hyper", "Koenigsegg", MotorV8(), 1500000),
        CarroFactory.criar("super", "Lamborghini", MotorEletrico(), 1200000),
    ]
    
    for carro in carros:
        loja.add_carro(carro)
    
    loja.lista()

