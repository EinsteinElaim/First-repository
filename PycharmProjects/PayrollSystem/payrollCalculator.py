#Class is a collection of related methods and variables
#A method is a function inside a class
#An object is an instance of a class
#A constructor is the first method that runs when a class is instanciated
#A class must begin with a capital letter


class Payrollcalculator:
    payee = 0
    nssf = 0
    nhif = 0
    grosssalary = 0

    def __init__(self, basic, over, house, other):
        self.grosssalary = basic+over+other+house
        self.getpayee()
        self.getnssf()
        self.getnhif()

    def getpayee(self):
        gross = self.grosssalary
        if gross >= 0 and gross < 12298:
            numpayee = int(gross) * 0.1
        elif gross > 12298 and gross <= 23885:
            numpayee = int(gross) * 0.15
        elif gross < 23885 and gross <= 35472:
            numpayee = int(gross) * 0.2
        elif gross > 35472 and gross <= 47059:
            numpayee = int(gross) * 0.25
        elif gross > 47059:
            numpayee = int(gross) * 0.3
        self.payee=numpayee

    def getnssf(self):
        gross = self.grosssalary
        if gross < 6000:
            nssf = 360
        elif gross >= 6000 and gross <= 18000:
            nssf = int(gross) * 0.06
        elif gross > 18000:
            nssf = 1080
            self.nssf = nssf

    def getnhif(self):
        gross = self.grosssalary
        if gross <= 5999:
            nhif = 150
        elif gross > 5999 and gross <= 7999:
            nhif = 300
        elif gross > 7999 and gross <= 11999:
            nhif = 400
        elif gross > 11999 and gross <= 14999:
            nhif = 500
        elif gross > 14999 and gross <= 19999:
            nhif = 600
        elif gross > 19999 and gross <= 24999:
            nhif = 750
        elif gross > 24999 and gross <= 29999:
            nhif = 850
        elif gross > 29999 and gross <= 34999:
            nhif = 900
        elif gross > 34999 and gross <= 39999:
            nhif = 950
        elif gross > 39999 and gross <= 44999:
            nhif = 1000
        elif gross > 44999 and gross <= 49999:
            nhif = 1100
        elif gross > 49999 and gross <= 59999:
            nhif = 1200
        elif gross > 59999 and gross <= 69999:
            nhif = 1300
        elif gross > 69999 and gross <= 79999:
            nhif = 1400
        elif gross > 79999 and gross <= 89999:
            nhif = 1500
        elif gross > 89999 and gross <= 99999:
            nhif = 1600
        elif gross > 99999:
            nhif = 1700
        self.nhif = nhif