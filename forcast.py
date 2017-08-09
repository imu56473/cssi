def __init__ (self,mode):
    self.mode = mode
    self.weekly_forcast = {"mon":1,"tue":2,"wed":3,"thu":4,"fri":5,"sat":6,"sun":7}

def __f2C__(self,n):
    return 5./9 * (n - 32)
def __f2K__(self,n):
    return 5./9 * (n + 459.67)
def setMode(self,new_mode):
    if new_mode == "f" or new_mode == "c" or new_mode == "k":
        self.mode = new_mode

def getmontemp(self):
    result = self.weekly_forcast["mon"]
    if self.mode == "c":
        return self. __f2C__(result)
    elif self.mode == "k":
        return self. __f2K__(result)
    else:
        return result

def gettuetemp(self):
    result = self.weekly_forcast["tue"]
    if self.mode == "c":
        return self. __f2C__(result)
    elif self.mode == "k":
        return self. __f2K__(result)
    else:
        return result

def getwedtemp(self):
    result = self.weekly_forcast["wed"]
    if self.mode == "c":
        return self. __f2C__(result)
    elif self.mode == "k":
        return self. __f2K__(result)
    else:
        return result

def getthutemp(self):
    result = self.weekly_forcast["thu"]
    if self.mode == "c":
        return self. __f2C__(result)
    elif self.mode == "k":
        return self. __f2K__(result)
    else:
        return result

def getfritemp(self):
    result = self.weekly_forcast["fri"]
    if self.mode == "c":
        return self. __f2C__(result)
    elif self.mode == "k":
        return self. __f2K__(result)
    else:
        return result

def getsatemp(self):
    result = self.weekly_forcast["sat"]
    if self.mode == "c":
        return self. __f2C__(result)
    elif self.mode == "k":
        return self. __f2K__(result)
    else:
        return result
def getsuntemp(self):
    result = self.weekly_forcast["sun"]
    if self.mode == "c":
        return self. __f2C__(result)
    elif self.mode == "k":
        return self. __f2K__(result)
    else:
        return result

def WeekForcast(For):
    thisis = "sun:" + str(round(For.getsuntemp(),2)) + ";"
    thisis = thisis + "mon:" + str(round(For.getmontemp(),2)) + ";"
    thisis = thisis + "tue:" + str(round(For.gettuetemp(),2)) + ";"
    thisis = thisis + "wed:" + str(round(For.getwedtemp(),2)) + ";"
    thisis = thisis + "thu:" + str(round(For.getthrtemp(),2)) + ";"
    thisis = thisis + "fri:" + str(round(For.getfritemp(),2)) + ";"
    thisis = thisis + "sat:" + str(round(For.getsatemp(),2)) + ";"
    print thisis


forcast1 = Forcast('F')
forcast2 = Forcast('C')
WeekForcast(forcast1)

print forcast1.mode
print forcast2.mode
print forcast1.__f2C__(98)
print forcast2.__f2K__(98)
print
print forcast1.getmontemp()
forcast1.setMode('K')
print forcast1.getmontemp()
