""" INHERITANCE - Multiple Ingheritance """
class vehicle:
    cc=0
    no=""
    tp=""
    def vdtls(self):
        self.no=input(" Enter Reg. No. : ")
        self.cc=int(input(" Enter Engine Capacity : "))
        self.tp=input(" Enter Vehicle Type (Transport/Non-Transport) : ")
    def disp(self):
        print(" Engine No. : ",self.no)
        print(" Vehicle Registration No. : ",self.no)
        print(" Vehile Type : ",self.tp)

class car(vehicle):
    mk=""
    clr=""
    mdl=""
    def __init__(self):
        print(" Enter CAR details ")
        self.mk=input(" Enter Manufacturer : ")
        self.clr=input(" Enter Colour : ")
        self.mdl=input(" Enter model : ")
        vehicle.vdtls(self)
    def show(self):
        print(" Manufacturer : ",self.mk)
        print(" Colour : ",self.clr)
        print(" Model : ",self.mdl)
        vehicle.disp(self)
class bus(vehicle):
    mk=""
    sc=""
    def __init__(self):
        print(" Enter BUS details ")
        self.mk=input(" Enter Manufacturer : ")
        self.sc=input(" Enter Seating Capacity : ")
        vehicle.vdtls(self)
    def show(self):
        print(" Manufacturer : ",self.mk)
        print(" Seating Capacity : ",self.sc)
        vehicle.disp(self)
class truck(vehicle):
    mk=""
    lc=""
    def __init__(self):
        print(" Enter TRUCK details ")
        self.mk=input(" Enter Manufacturer : ")
        self.lc=input(" Enter Load Capacity : ")
        vehicle.vdtls(self)
    def show(self):
        print(" Manufacturer : ",self.mk)
        print(" load Capacity : ",self.lc)
        vehicle.disp(self)


V=vehicle()
print(" Enter Vehicle details ")
V.vdtls()
V.disp()
C=car()
C.show()
B=bus()
B.show()
T=truck()
T.show()
