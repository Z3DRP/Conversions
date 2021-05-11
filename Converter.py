#Converter methods - by Zach Palmer

class Conversions:
    """Conversion Algorithms"""


    @staticmethod
    def MileToKm(mi):
        if not isinstance(mi,(int,float)): # ask if mi is int or float
            try:
                mi = float(mi) #buble up exceptions
            except ValueError: #raise errors wont handle exception jsut throw back to main program
                raise Exception("Miles input was not numeric")
        if mi <= 0:
            #error: not a legal value for conversion
            #buble up valueerror
            raise ValueError("Miles must be positive")
        
        km = mi * 1.60934
        return km

    @staticmethod
    def OunceToGram(oz):
        if not isinstance(oz,(int,float)):
            try:
                oz = float(oz)
            except ValueError:
                raise Exception("Ounces input was not numeric")
        if oz <= 0:
            raise ValueError("Ounces must be positive")

        gram = 28.3495 * oz
        return gram

    @staticmethod
    def FahrenheitToCel(fh):
        if not isinstance(fh,(int,float)):
            try:
                fh = float(fh)
            except ValueError:
                raise Exception("Fahrenheit input was not numeric")
        if fh <= -459.67:
            raise ValueError("This temperature is not possible,as it is below 0 K")

        cel = (5/9) * (fh - 32)
        return cel

    @staticmethod
    def CelciusToFahrn(cel):
        if not isinstance(cel,(int,float)):
            try:
                cel = float(cel)
            except ValueError:
                raise Exception("Celcius input was not numeric")
        if cel <= -273.15:
            raise ValueError("This temperature is not possible, as it is below 0 K")

        fahren = ((9/5) * cel) + 32
        return fahren

    @staticmethod
    def MeterToFt(m):
        if not isinstance(m,(int,float)):
            try:
                m = float(m)
            except ValueError:
                raise Exception("Meter input was not numeric")
        if m <= 0:
            raise ValueError("Meters must be positive")

        ft = m * 3.2808
        return ft

    @staticmethod
    def LiterToGal(l):
        if not isinstance(l,(int,float)):
            try:
                l = float(l)
            except ValueError:
                raise Exception("Liter input was not numeric")
        if l <= 0:
            raise ValueError("Liters must be positive")

        gal = .26417 * l
        return gal

    @staticmethod
    def CelciusToKel(cel):
        if not isinstance(cel,(int,float)):
            try:
                cel = float(cel)
            except ValueError:
                raise Exception("Celcius was not numeric")
        if cel <= -273.15:
            raise ValueError("This temperature is not possible,as it is below 0 K")

        kel = cel + 273.15
        return kel
        
        
