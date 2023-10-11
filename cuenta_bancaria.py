class CuentaBancaria:
# ¡No olvides agregar algunos valores predeterminados para estos parámetros!
    def __init__(self, tasa_interés, balance):
        self.tasa_interés = tasa_interés
        self.balance = balance

# tu código aquí (recuerda, los atributos de instancia van aquí)
# no te preocupes por la información del usuario aquí; pronto involucraremos la clase de usuario
    def depósito(self, amount):
        self.balance += amount
        return self

    def retiro(self, amount):
        if amount <= self.balance:
            self.balance -= amount

            
        elif amount > self.balance:
            print("Fondos insuficientes: cobrando una tarifa de $5")
            self.balance -= 5
        return self
    
    def generar_interés(self):
        if self.balance > 0:
            self.balance += self.balance * self.tasa_interés
        return self


    def mostrar_info_cuenta(self):
        print(self.balance)



cuenta1 = CuentaBancaria(0.01, 0)
cuenta2 = CuentaBancaria(0.01, 3000)
print("------------")
cuenta1.depósito(5000).depósito(1000).depósito(1000).retiro(1000).generar_interés().mostrar_info_cuenta()
print("------------")
cuenta2.depósito(2000).depósito(3000).retiro(2000).retiro(500).retiro(750).retiro(1000).generar_interés().mostrar_info_cuenta()
print("------------")