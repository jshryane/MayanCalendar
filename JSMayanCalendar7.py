def GetMayanDate():
    MDate = input("Please enter the Mayan date ")
    return MDate

def ConvertMayanDateToMayanDays(M_Date): 
    DateList = M_Date.split() # splits the string using the spaces and assigns each part to a list

    # get each unit's value back out of the list and convert it from a string to an integer
    ba = int(DateList[0])
    ka = int(DateList[1])
    tu = int(DateList[2])
    ui = int(DateList[3])
    ki = int(DateList[4])

    Days = ki + (20*ui) + (20*18*tu) + (20*18*20*ka) + (20*18*20*20*ba)
    return(Days)

def CalculateDaysSinceBaseDate(MDays):
    DaysSince = MDays - 2018843
    return (DaysSince)

def CalculateGregorianDate(DaysBeyondBase):
    # base date is:
    Y = 2000
    M = 1
    D = 1
    while DaysBeyondBase >=31:
        if DaysBeyondBase >= 31:                        # Jan
            M = M + 1
            DaysBeyondBase = DaysBeyondBase - 31
        if Y % 4 == 0:
            if DaysBeyondBase >= 29:                    # Feb in leap year
                M = M + 1
                DaysBeyondBase = DaysBeyondBase - 29                
        else:
            if DaysBeyondBase >= 28:                    # Feb not in leap year
                M = M + 1
                DaysBeyondBase = DaysBeyondBase - 28            
        if DaysBeyondBase >= 31:                        # March
            M = M + 1
            DaysBeyondBase = DaysBeyondBase - 31
        if DaysBeyondBase >= 30:                        # April
            M = M + 1
            DaysBeyondBase = DaysBeyondBase - 30
        if DaysBeyondBase >= 31:                        # May
            M = M + 1
            DaysBeyondBase = DaysBeyondBase - 31
        if DaysBeyondBase >= 30:                        # June
            M = M + 1
            DaysBeyondBase = DaysBeyondBase - 30
        if DaysBeyondBase >= 31:                        # July
            M = M + 1
            DaysBeyondBase = DaysBeyondBase - 31
        if DaysBeyondBase >= 31:                        # August
            M = M + 1
            DaysBeyondBase = DaysBeyondBase - 31
        if DaysBeyondBase >= 30:                        #Sept
            M = M + 1
            DaysBeyondBase = DaysBeyondBase - 30        
        if DaysBeyondBase >= 31:                        # Oct
            M = M + 1
            DaysBeyondBase = DaysBeyondBase - 31
        if DaysBeyondBase >= 30:                        # Nov
            M = M + 1
            DaysBeyondBase = DaysBeyondBase - 30
        if DaysBeyondBase >= 31:                        # Dec
            M = 1                                       # reset the month to Jan
            Y = Y + 1                                   # increment the year
            DaysBeyondBase = DaysBeyondBase - 31        

    D = D + DaysBeyondBase                              # add the remaining days to the days variable
    return(D,M,Y)

def OutputGregorianDate(Dy,Mnth,Yr):
    print(Dy,Mnth,Yr)


# main program below
response = "Y"
while response != "N":
    MayanDate = GetMayanDate()
    MayanDays = ConvertMayanDateToMayanDays(MayanDate)
    DaysSinceBaseDate = CalculateDaysSinceBaseDate(MayanDays)
    Day,Month,Year = CalculateGregorianDate(DaysSinceBaseDate)
    OutputGregorianDate(Day,Month,Year)
    response = input("Would you like to convert another date? Y or N")


input("Press any key to exit")
