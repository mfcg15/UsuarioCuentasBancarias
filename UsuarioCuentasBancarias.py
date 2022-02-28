class CuentaBancaria:

    todas_las_cuentas = []

    def __init__(self,tasa_interes,balance):
        self.tasa_interes = tasa_interes/100
        self.balance = balance
        CuentaBancaria.todas_las_cuentas.append(self)
    
    def hacer_deposito(self,amount):
        self.balance += amount

    def hacer_retiro(self,amount):
        auxBalnce = self.balance - amount
        if(auxBalnce>0):
            self.balance -= amount
        else:
            print("Fondos insuficientes: cobrando una tarifa de $5")
            self.balance = self.balance-5

    def info_cuenta(self):
        return str(self.balance)

    def generar_initeres(self):
        if(self.balance>0):
            self.balance = self.balance * self.tasa_interes
        else:
            print("El balance actual es negativo")

    @classmethod
    def mostrar_informacion_banco(cls):
        for cuenta in cls.todas_las_cuentas:
            cuenta.info_cuenta()


class Usuario :

    def __init__(self,name):
        self.name = name
        self.cuenta = { "ckecking": CuentaBancaria(10,900),
        "savings": CuentaBancaria(10,3000)}

    def mostrar_info_cuenta(self):
        print("User: "+self.name+", Ckecking Balance: "+self.cuenta['ckecking'].info_cuenta())
        print("User: "+self.name+", Savings Balance: "+self.cuenta['savings'].info_cuenta())
        return self
    
    def transfer_dinero(self,other_user,amount):
        other_user.hacer_depositio(amount)
        self.balance_cuenta -=amount


usario1 = Usuario("Adrien")
usario1.cuenta['ckecking'].hacer_deposito(200)
usario1.mostrar_info_cuenta()
