from abc import ABC,abstractmethod
from datetime import datetime, date
import os


def limpiar():        
    os.system("cls")

class Persona(ABC):# -> clase abstracta
    _secuencia=0
    def __init__(self,nom,estado):
        Persona._secuencia=Persona._secuencia+1
        self.__idcode=Persona._secuencia
        self.nombre = nom
        self.estado= estado
    
    @property
    def idcode(self):
        return self.__idcode

    @abstractmethod 
    def mostrarDatos(self):
        pass

class Cliente(Persona):
    _secuencia=0
    def __init__(self, nom, estado,cedu):
        super().__init__(nom, estado)
        Cliente._secuencia =Cliente._secuencia+1
        self.__idclient=Cliente._secuencia
        self.cedula=cedu
    
    @property
    def idclient(self):
        return self.__idclient
        
    def mostrarDatos(self): 
        print(f"Id_Cliente: {self.idclient} Nombre: {self.nombre} c.i: {self.cedula} estado: {self.estado}")

class Factura():
    _secuencia=0
    def __init__(self,client,fech,total,estado):
        Factura._secuencia=Factura._secuencia+1
        self.idfact=Factura._secuencia
        self.cliente=client
        self.total=total
        self.fecha=fech
        self.estado=estado
        
    @property
    def iDfact(self):
        return self.idfact

    def mostrarDatos(self): 
        print(f"Factura_N# {self.idfact} fecha: {self.fecha} total: {self.total} Estado: {self.estado}")

class Calculo(ABC): # -> clase interfaz
    
    @abstractmethod
    def realizarpago():
        pass

class Pago: 
    _secuencia=0
    def __init__(self,fecha_pago,val):
        Pago._secuencia=Pago._secuencia+1
        self.__idPago=Pago._secuencia
        self.fechapago=fecha_pago
        self.valor=val
    
    @property
    def Idpago(self):
        return self.__idPago
    
    def realizarpago(self,realizar):
        self.valor = CabCredito.deuda - self.valor
        print("Se realizo de manera exitiosa:", self.valor)
    
    def mostrarDatos(self): 
        print(f"Numero De Pago: {self.idPago} Fecha a Pagar: {self.fechaPago} Valor: {self.valor}")


class DetCredito(): 
    _secuencia=0
    def __init__(self,aamm,cuot,detpago,estado):
        DetCredito._secuencia=DetCredito._secuencia+1
        self.__iddetcredit=DetCredito._secuencia
        self.aamm=aamm
        self.cuota=cuot
        self.detpago=detpago
        self.estado=estado
    
    @property
    def IdDetCredito(self):
        return self.__iddetcredit
    
    def mostrarDatos(self): 
        print(f"DetCredito N#: {self.idDetCredito} aamm: {self.aamm} cuota: {self.cuota} detPago: {self.detPago.idPago} estado: {self.estado}")

    def agregarPago(self):
        self.detPago.realizarpago()
        self.estado = bool(True)
        print("El pago se realizo exitosamente")

class CabCredito: #clase incompleta
    _secuencia=0
    def __init__(self,fech,fact,deuda,Cuot,aammInicial,NCuotas,detaCredi,estado):
        CabCredito._secuencia=CabCredito._secuencia+1
        self.__idcabcredit=CabCredito._secuencia
        self.fecha= fech
        self.factura=fact
        self.Deuda = deuda
        self.NumeroCuota=NCuotas
        self.Cuota=Cuot
        self.aammInicial=aammInicial
        self.detalleCredito=detaCredi
        self.estado=estado
    
    @property
    def IdCadCredito(self):
        return self.__idcabcredit

    def mostrarDatos(self):
        print(f"CadCredito N#: {self.idCadCredito} Cod_factura: {self.factura} fecha: {self.fecha} Total de deuda: {self.deuda}")
        print(f"n# Cuotas: {self.numeroCuotas} cuota: {self.cuota} AAMM inicial: {self.aamminicial} Detalle del crédito: {self.detalleCredito} estado: {self.estado}")
        
    
    @staticmethod
    def getinteres():
        return "Interes aprobado"
           
def menu():
    limpiar()
    while True:
        print(""" 
        ------------------------------------------------------
        ------BIENVENIDO SR/A USUARIO A LA CARTERA DIGITAL----
        ------------------------------------------------------
        MENU DE OPCIONES
        1) Clientes
        2) Facturas
        3) Creditos
        4) Pagos
        5) Consulta General
        6) Salir
        ------------------------------------------------------
        """ + "\n")

        op = int(input('ELIJA LA OPCION QUE DESEA ---> '))
        
        if op == 1:
            limpiar()
            while True:
                print("""
                ------------------------------------------------------
                -----------------REGISTRO DE CLIENTES-----------------
                ------------------------------------------------------
                1) Ingresar Cliente
                2) Mostrar Cliente
                3) Volver Atras
                ------------------------------------------------------
                """ + "\n")
                op = int(input('ELIJA LA OPCION QUE DESEA ---> '))

                if op == 1:
                    limpiar()
                    print("""
                    ------------------------------------------------------
                    -----------------INGRESE NUEVO CLIENTE----------------
                    ------------------------------------------------------
                    """ + "\n")
                    print("ïd_cliente", Cliente._secuencia)
                    Persona.nom = input("Digite nombre:" + "\n")
                    Persona.cedu = input("Digite cedula:" + "\n")
                    Persona.estado = True
                    print("=====================================================")
                    cliente = Cliente(Persona.nom, Persona.cedu, Persona.estado)
                    Clitxt.append(cliente)
                    with open("cliente.txt","a") as file:
                        for cli in Clitxt:
                            file.write("nombre: "+ cli.nombre + "\n")
                            file.write("cedula: "+ str(cli.estado) + "\n")
                            file.write("estado:" + str(cli.cedula) + "\n")
                            file.write("-------------------"+"\n")
                    limpiar()
                    print("""
                    ---------------------------------
                    SE REGISTRO EL CLIENTE CON EXITO
                    ---------------------------------
                    """)
                elif op == 2:
                    limpiar()
                    try:
                        with open("cliente.txt","r") as file:
                            print("------------")
                            print(file.read())
                    except ValueError:
                        print("Error, No Existe Datos")
                elif op == 3:
                    limpiar()
                    break

        elif op == 2:
            limpiar()
            while True:
                   print("""
                    ------------------------------------------------------
                    ----------------SISTEMA DE FACTURACION----------------
                    ------------------------------------------------------
                  1) Ingresar Factura
                  2) Mostrar Factura
                  3) Volver Atras
                    ------------------------------------------------------
                  """ + "\n")
                   op = int(input('ELIJA LA OPCION QUE DESEA ---> '))

                   if op == 1:
                    limpiar()
                    print("""
                    ------------------------------------------------------
                    -----------------INGRESE NUEVA FACTURA----------------
                    ------------------------------------------------------
                    """)
                    print("ïd_fact", Factura._secuencia)
                    Factura.cliente= input("Ingrese el nombre del cliente:" + "\n")
                    Factura.total = input("Ingrese Total $:" + "\n")
                    Factura.fech= date.today()
                    print("===============================================================")
                    factura = Factura(Factura.cliente,Factura.total,Factura.fech,estado = True)
                    Facttxt.append(factura)
                    with open("Factura.txt","a") as file:
                         for fact in Facttxt:
                            file.write("Cliente:"+ fact.cliente + "\n")
                            file.write("Total $: "+ str(fact.fecha) + "\n")
                            file.write("Fecha_Emision: "+ str(fact.total)  + "\n")
                            file.write("Estado: "+ str(fact.estado)+ "\n")
                            file.write("-------------------"+"\n")
                    limpiar()
                    print("""
                     -------------------------------
                        FACTURA EMITIDA CON EXITO
                     -------------------------------
                     """)
                   elif op == 2:
                    limpiar()
                    try:
                        with open("Factura.txt","r") as file:
                            print(file.read())
                    except ValueError:
                        print("Error, No Existe Datos")
                   elif op == 3:
                       break
        elif op == 3:
            limpiar()
            while True:
                print("""
                ------------------------------------------------------
                -----------------REGISTRO DE CREDITO------------------
                ------------------------------------------------------
                1) Ingresar Credito
                2) Mostrar Credito
                3) Volver Atras
                ------------------------------------------------------
                """ + "\n")
                op = int(input('ELIJA LA OPCION QUE DESEA ---> '))
                
                if op == 1:
                    limpiar()
                    print("""
                    ------------------------------------------------------
                    -----------------INGRESE NUEVO CREDITO----------------
                    ------------------------------------------------------
                    """)
                    print("ïd_fact", CabCredito._secuencia)
                    CabCredito.fecha= date.today()
                    CabCredito.factura=input("Digite Nro# de Factura: " + "\n")
                    CabCredito.Deuda=float(input("Digite la deuda del cliente:" + "\n"))
                    CabCredito.NumeroCuota=int(input("Ingrese el Nro de cuoata a pagar:" + "\n"))
                    CabCredito.Cuota=float(input("Digite la cuoata a pagar:" + "\n"))
                    CabCredito.aammInicial=input("Digite El AAMM Inicial: " + "\n")
                    CabCredito.detalleCredito=input("Digite algun detalle a considerar: " + "\n")
                    print("===============================================================")
                    cabcredi= CabCredito(CabCredito.fecha, CabCredito.factura, CabCredito.Deuda, CabCredito.NumeroCuota, CabCredito.Cuota, CabCredito.aammInicial,CabCredito.detalleCredito, estado = True) 
                    Cabcreditxt.append(cabcredi)
                    with open("Cabcredito.txt","a") as file:
                         for cbcred in Cabcreditxt:
                            file.write("fecha:"+ str(cbcred.fecha) + "\n")
                            file.write("Factura Nro: "+ cbcred.factura + "\n")
                            file.write("Deuda $:"+ str(cbcred.Deuda)  + "\n")
                            file.write("Numero de Cuoatas a Pagar: "+ str(cbcred.NumeroCuota)+ "\n")
                            file.write("Cuota $"+ str(cbcred.Cuota)+ "\n")
                            file.write("El AAMM Inicial: "+ str(cbcred.aammInicial) + "\n")
                            file.write("Detalle: "+ cbcred.detalleCredito + "\n")
                            file.write("Estado: "+ str(cbcred.estado)+ "\n")
                            file.write("-------------------"+"\n")
                    limpiar()
                    print("""
                    ------------------------------------
                      SE EMITIO EL CREDITO EXITOSAMENTE
                    ------------------------------------
                     """)
                elif op == 2:
                    limpiar()
                    try:
                        with open("Cabcredito.txt","r") as file:
                            print(file.read())
                    except ValueError:
                        print("Error, No Existe Datos")
                elif op == 3:
                    limpiar()
                    break
    
        elif op == 4:
            limpiar()
            while True:
                print("""
                ------------------------------------------------------
                -----------------REGISTRO DE PAGOS--------------------
                ------------------------------------------------------
                1) Ingresar Pago
                2) Mostrar Pago
                3) Volver Atras
                ------------------------------------------------------
                """ + "\n")
                op = int(input('ELIJA LA OPCION QUE DESEA ---> '))
                if op == 1:
                    limpiar()
                    print("""
                    ------------------------------------------------------
                    -----------------INGRESE NUEVO PAGO-------------------
                    ------------------------------------------------------
                    """)
                    print("ïd_Pago", Pago._secuencia)
                    Pago.fechapago= date.today()
                    Pago.valor = input("Digite el valor Total $:" + "\n")
                    print("===============================================================")
                    pag = Pago(Pago.fechapago,Pago.valor)
                    Pagtxt.append(pag)
                    with open("Pago.txt","a") as dato:
                         for pago in Pagtxt:
                            dato.write("Fecha_Pago:" + str(pago.fechapago) + "\n")
                            dato.write("Valor $:" + str(pago.valor) + "\n")
                            dato.write("-------------------"+"\n")
                    limpiar()
                    print("""
                    -------------------------------
                     SE REGISTRO EL PAGO CON EXITO
                    -------------------------------
                     """)
                elif op == 2:
                    limpiar()
                    try:
                        with open("Pago.txt","r") as dato:
                            print(dato.read())
                    except ValueError:
                        print("Error, No Existe Datos")
                elif op == 3:
                    limpiar()
                    break
        elif op == 5:
            limpiar()
            while True:
                print("""
                ------------------------------------------------------
                -----------------CONSULTA GENERAL---------------------
                ------------------------------------------------------ 
                1) Consultar Registro de Clientes
                2) Consultar Registro de Facturas
                3) Consultar Registro de Creditos
                4) Consultar Registro de Pagos
                5) Volver Atras
                ------------------------------------------------------ 
                """ + "\n")
                op = int(input('ELIJA LA OPCION QUE DESEA ---> '))

                if op == 1:
                    limpiar()
                    try:
                        with open("cliente.txt","r") as file:
                            print("------------")
                            print(file.read())
                    except ValueError:
                        print("Error, No Existe Datos")
                elif op == 2:
                    limpiar()
                    try:
                        with open("Factura.txt","r") as file:
                            print(file.read())
                    except ValueError:
                        print("Error, No Existe Datos")
                elif op == 3:
                    limpiar()
                    try:
                        with open("Cabcredito.txt","r") as file:
                            print(file.read())
                    except ValueError:
                        print("Error, No Existe Datos")
                elif op == 4:
                    limpiar()
                    try:
                        with open("Pago.txt","r") as dato:
                            print(dato.read())
                    except ValueError:
                        print("Error, No Existe Datos")
                elif op == 5:
                    limpiar()
                    break
        elif op == 6:
            limpiar()
            print("""
                -------------------------------------------------
                GRACIAS POR USAR NUESTRO PROGRAMA. VUELVA PRONTO
                -------------------------------------------------
                """)
            exit()

#-- Instancias --#
Clitxt = []
Facttxt= []
Cabcreditxt=[]
Pagtxt=[]
menu()
