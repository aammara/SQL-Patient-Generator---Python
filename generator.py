"""
generator.py
created by Achraf Ammar : 19/12/2014
Generator.py is a python program used to generate a number of patients to be used for testing the Medifind.me website's database.
This program generates values that are 75% identic to reality basing on a lot of data collected from .txt files that represtenst the real
percenteges of British patients.
"""

from random import randint
from datetime import datetime
import random
from random import shuffle

# TABLES AND DICTIONNARIES
MFNames = []
FFNames = []
LNames = []
Gender = {"male":0, "female":0}
ageRange = {"0-9":0, "10-19":0, "20-29":0, "30-39":0, "40-49":0, "50-59":0, "60-69":0, "70-79":0, "80-89":0, "90-99":0}
BloodTypePerc = {"O-":0, "O+":0, "A-":0, "A+":0, "B-":0, "B+":0, "AB-":0, "AB+":0}
Weight = {"05-10":0, "10-40":0, "40-70":0, "70-100":0, "100-130":0, "130-160":0, "160-200":0}
Height = {"30-60":0, "60-90":0, "90-120":0, "120-150":0, "150-180":0, "180-210":0}
bloodSugar = {"0-9":0, "10-19":0, "20-29":0, "30-39":0, "40-49":0, "50-59":0, "60-69":0, "70-79":0, "80-89":0, "90-99":0}
bloodPresure = {"80/50":0, "90/60":0, "100/70":0, "110/80":0, "120/80":0, "130/80":0, "140/90":0, "150/100":0, "160/100":0, "170/100":0}
Vision = {"20/200":0, "20/100":0, "20/70":0, "20/50":0, "20/40":0, "20/30":0, "20/25":0, "20/20":0, "20/15":0, "20/10":0}

emails = []
names = []
lastnames = []
addresses = ["University of Essex, Colchester, UK -  CO4 3SQ"]
gender = []
dob = []
nhsn = []
contanctNumbers = []
icen = []
joinDate = []
bloodType = []
height = []
weight = []
BPres = []
BSugar = []
vision = []
# READ FIRST NAMES FROM FILES
def getMFNames (fileName) :
    """
    getMFNames
    this function gets male first names from a .txt file given
    fileName : String --> represent the file name that should be in the same path with generator.py
    returns none when accessing file failed
    """
    try:
        fIn = open(fileName, 'r')
        for line in fIn :
            MFNames.append(line.replace('\n',''))
    except IOError as e :
        print("Failed to open ", fileName, " - program aborted")
        return None


# READ FIRST NAMES FROM FILES
def getFFNames (fileName) :
    """
    getFFNames
    this function gets female first names from a .txt file given
    fileName : String --> represent the file name that should be in the same path with generator.py
    returns none when accessing file failed
    """
    try:
        fIn = open(fileName, 'r')
        for line in fIn :
            FFNames.append(line.replace('\n',''))
    except IOError as e :
        print("Failed to open ", fileName, " - program aborted")
        return None


# READ LAST NAMES FROM FILES
def getLNames (fileName) :
    """
    getLNames
    this function gets lasr names from a .txt file given
    fileName : String --> represent the file name that should be in the same path with generator.py
    returns none when accessing file failed
    """
    try:
        fIn = open(fileName, 'r')
        for line in fIn :
            LNames.append(line.replace('\n',''))
    except IOError as e :
        print("Failed to open ", fileName, " - program aborted")
        return None


# READ GENDER PERCENTAGE FROM FILES
def getGenderPerc (fileName) :
    """
    getGenderPerc
    this function gets gender percenteges from a .txt file given
    fileName : String --> represent the file name that should be in the same path with generator.py
    returns none when accessing file failed
    """
    try:
        fIn = open(fileName, 'r')
        for line in fIn :
            Gender[line[:line.find(':')]]= int(line[line.find(':')+1:].replace('\n',''))
    except IOError as e :
        print("Failed to open", fileName, "- program aborted")
        return None

# READ ADDRESSES FROM FILES
def getAddresses (fileName) :
    """
    getAddresses
    this function gets Addresses a .txt file given
    fileName : String --> represent the file name that should be in the same path with generator.py
    returns none when accessing file failed
    """
    try:
        fIn = open(fileName, 'r')
        for line in fIn :
            addresses.append(line.replace('\n',''))
    except IOError as e :
        print("Failed to open ", fileName, " - program aborted")
        return None

# READ AGE PERCENTAGE FROM FILES
def getAgePerc (fileName) :
    """
    getAgePerc
    this function gets age percenteges from a .txt file given
    fileName : String --> represent the file name that should be in the same path with generator.py
    returns none when accessing file failed
    """
    try:
        fIn = open(fileName, 'r')
        for line in fIn :
            ageRange[line[:line.find(':')]]= int(line[line.find(':')+1:].replace('\n',''))
    except IOError as e :
        print("Failed to open", fileName, "- program aborted")
        return None


# READ BLOOD TYPE PERCENTAGE FROM FILES
def getBTypePerc (fileName) :
    """
    getBTypePerc
    this function gets Blood Types percenteges from a .txt file given
    fileName : String --> represent the file name that should be in the same path with generator.py
    returns none when accessing file failed
    """
    try:
        fIn = open(fileName, 'r')
        for line in fIn :
            BloodTypePerc[line[:line.find(':')]]= int(line[line.find(':')+1:].replace('\n',''))
    except IOError as e :
        print("Failed to open", fileName, "- program aborted")
        return None


# READ HEIGHT PERCENTAGE FROM FILES
def getHeightPerc (fileName) :
    """
    getHeightPerc
    this function gets height percenteges from a .txt file given
    fileName : String --> represent the file name that should be in the same path with generator.py
    returns none when accessing file failed
    """
    try:
        fIn = open(fileName, 'r')
        for line in fIn :
            Height[line[:line.find(':')]]= int(line[line.find(':')+1:].replace('\n',''))
    except IOError as e :
        print("Failed to open", fileName, "- program aborted")
        return None


# READ WEIGHT PERCENTAGE FROM FILES
def getWeightPerc (fileName) :
    """
    getWeightPerc
    this function gets weight percenteges from a .txt file given
    fileName : String --> represent the file name that should be in the same path with generator.py
    returns none when accessing file failed
    """
    try:
        fIn = open(fileName, 'r')
        for line in fIn :
            Weight[line[:line.find(':')]]= int(line[line.find(':')+1:].replace('\n',''))
    except IOError as e :
        print("Failed to open", fileName, "- program aborted")
        return None



# READ BloodSugar PERCENTAGE FROM FILES
def getBSugarPerc (fileName) :
    """
    getBSugarPerc
    this function gets Blood Sugar percenteges from a .txt file given
    fileName : String --> represent the file name that should be in the same path with generator.py
    returns none when accessing file failed
    """
    try:
        fIn = open(fileName, 'r')
        for line in fIn :
            bloodSugar[line[:line.find(':')]]= int(line[line.find(':')+1:].replace('\n',''))
    except IOError as e :
        print("Failed to open", fileName, "- program aborted")
        return None
    

# READ BloodPresure PERCENTAGE FROM FILES
def getBPresurePerc (fileName) :
    """
    getBSugarPerc
    this function gets Blood Sugar percenteges from a .txt file given
    fileName : String --> represent the file name that should be in the same path with generator.py
    returns none when accessing file failed
    """
    try:
        fIn = open(fileName, 'r')
        for line in fIn :
            bloodPresure[line[:line.find(':')]]= int(line[line.find(':')+1:].replace('\n',''))
    except IOError as e :
        print("Failed to open", fileName, "- program aborted")
        return None


# READ EyeSight PERCENTAGE FROM FILES
def getEyeSightPerc (fileName) :
    """
    getEyeSightPerc
    this function gets Eye Sight percenteges from a .txt file given
    fileName : String --> represent the file name that should be in the same path with generator.py
    returns none when accessing file failed
    """
    try:
        fIn = open(fileName, 'r')
        for line in fIn :
            Vision[line[:line.find(':')]]= int(line[line.find(':')+1:].replace('\n',''))
    except IOError as e :
        print("Failed to open", fileName, "- program aborted")
        return None

### GENERATING FUNCTIONS ###

### GENERATE GENDERS ###
def generateGenders (np) :
    """
    generateGenders
    this function generates genders based on data collected inside a dictionary called <Gender>
    np : Integer --> represent the number of patients to be generated
    <NO RETURN>
    """
    rng = range(1, round((Gender["female"]*np)/100)+1)
    for i in rng :
        gender.append("female")

    
    rng = range(1, round((Gender["male"]*np)/100)+1)
    for i in rng :
        gender.append("male")



### GENERATE FULL NAMES ###
def generateFullNames (np) :
    """
    generateFullNames
    this function generates full names based on data collected inside three arrays called <MFNames>, <FFNames> and <LNames>
    np : Integer --> represent the number of patients to be generated
    <NO RETURN>
    """

    for i in range (0, np) :
        if gender[i]=="male" :
            names.append(MFNames[randint(0, len(MFNames)-1)])
        else :
            names.append(FFNames[randint(0, len(FFNames)-1)])

    for i in range (0, np) :
        lastnames.append(LNames[randint(0, len(LNames)-1)])
    
### GENERATE BIRTH DATES ###
def generateBirthDates (np) :
    """
    generateBirthDates
    this function generates Birth dates based on data collected inside a dictionary called <ageRange>
    np : Integer --> represent the number of patients to be generated
    <NO RETURN>
    """
    for i in range(0, 100, 10) :
        rng = str(i)+"-"+str(i+10-1)
        perc = ageRange[rng]
        for j in range (0, round((perc*np)/100)) :
            year = random.choice(range(2014-(i+10), 2014-i))
            month = random.choice(range(1, 13))
            day = random.choice(range(1, 29))
            birthDate = datetime(year, month, day)
            dob.append(str(birthDate)[:10])
    sorted(dob)
            


### GENERATE BLOOD TYPE ###
def generateBloodType (np) :
    """
    generateBloodType
    this function generates Blood type based on data collected inside a dictionary called <BloodTypePerc>
    np : Integer --> represent the number of patients to be generated
    <NO RETURN>
    """
    for i in range(0, len(BloodTypePerc)) :
        key = list(BloodTypePerc.keys())[i]
        perc = BloodTypePerc[key]
        for j in range (0, round((perc*np)/100)) :
            bloodType.append(key)
    if (len(bloodType)<np) : bloodType.append(key)


#CALCULATE AGE FROM BIRTHDATE
def calculateAge(dob) :
    """
    """
    return 2015-int(dob[:dob.find("-")])

### GENERATE WEIHT ###
def generateWeight (np) :
    """
    generateWeight
    this function generates Weight based on data collected inside a dictionary called <Weight>
    np : Integer --> represent the number of patients to be generated
    <NO RETURN>
    """
    for i in range(0, np) :
        if (gender[i]=="male"):
            weight.append(GenAvg(50,110,80))
        elif (gender[i]=="female") : weight.append(GenAvg(40,95,67))

             
### GENERATE WEIGHT BY TAL ###
def GenAvg(low, high, bias):
    rnd1 = random.randrange(low,high)
    rnd2 = random.randrange(low,high)
    rnd3 = random.randrange(low,high)

    
    if abs(rnd1 - bias) < abs(rnd2 - bias):
        if abs(rnd1 - bias) < abs(rnd3 - bias):
            closest = rnd1
        else:
            closest = rnd3
    else:
        if abs(rnd2 - bias) < abs(rnd3 - bias):
            closest = rnd2
        else:
            closest = rnd3
        
    return closest


### GENERATE HEIHT ###
def generateHeight (np) :
    """
    generateHeight
    this function generates Height based on data collected inside a dictionary called <Height>
    np : Integer --> represent the number of patients to be generated
    <NO RETURN>
    """
    for i in range(0, np) :
        if (gender[i]=="male"):
            height.append(GenAvg(150,210,180))
        elif (gender[i]=="female") : height.append(GenAvg(140,180,165))


### GENERATE BLOOD PRESURE ###
def generateBloodPresure (np) :
    """
    generateBloodPresure
    this function generates Blood Presure based on data collected inside a dictionary called <bloodPresure>
    np : Integer --> represent the number of patients to be generated
    <NO RETURN>
    """
    for i in range(0, len(bloodPresure)) :
        key = list(bloodPresure.keys())[i]
        perc = bloodPresure[key]
        for j in range (0, round((perc*np)/100)) :
            val1=random.choice(range(int(key[key.find("/")+1:]), int(key[key.find("/")+1:])+15))
            val2=random.choice(range(int(key[:key.find("/")])-15, int(key[:key.find("/")]) ))
            BPres.append(str(val1)+"/"+str(val2))


### GENERATE BLOOD SUGAR ###
def generateBloodSugar (np) :
    """
    generateBloodSugar
    this function generates Blood Sugar based on data collected inside a dictionary called <bloodSugar>
    np : Integer --> represent the number of patients to be generated
    <NO RETURN>
    """
    for i in range(0, 100, 10) :
        rng = str(i)+"-"+str(i+10-1)
        perc = ageRange[rng]
        for j in range (0, round((perc*np)/100)) :
            value = bloodSugar[rng]
            BSugar.append(value)


### GENERATE EYE SIGHT ###
def generateEyeSight (np) :
    """
    generateEyeSight
    this function generates Eye Sight based on data collected inside a dictionary called <Vision>
    np : Integer --> represent the number of patients to be generated
    <NO RETURN>
    """
    for i in range(0, len(Vision)) :
        key = list(Vision.keys())[i]
        perc = Vision[key]
        for j in range (0, round((perc*np)/100)) :
            vision.append(key)


### GENERATE EMAILS ###
def generateEmails (np) :
    """
    generateEmails
    this function generates Emails based on data collected inside 3 arrays called <names>, <lastnames> and <dob>
    np : Integer --> represent the number of patients to be generated
    <NO RETURN>
    """
    for i in range(0, np):
        email=names[i].lower()+"."+(lastnames[i].lower()).replace(" ", "_")+"."+dob[i][:4]+"@mail.co.uk"
        if email in emails :
            email=names[i].lower()+"."+(lastnames[i].lower()).replace(" ", "_")+"."+dob[i][:4]+str(i)+"@mail.co.uk"
        emails.append(email)


### GENERATE NHS NUMBERS ###
def generateNHSN (np) :
    """
    generateNHSN
    this function generates National Health Insurance Numbers RANDMOLY -- EVERY NUMBER OCURES ONCE --
    np : Integer --> represent the number of patients to be generated
    <NO RETURN>
    """
    for i in range(0, np) :
        number = random.choice(range(1000000000, 9999999999))
        while number in nhsn :
            number = random.choice(range(1000000000, 9999999999))
        nhsn.append(number)
 

### GENERATE CONTACT NUMBERS ###
def generateContactNumbers (np) :
    """
    generateContactNumbers
    this function generates Contact Numbers RANDMOLY -- EVERY NUMBER OCURES ONCE --
    np : Integer --> represent the number of patients to be generated
    <NO RETURN>
    """
    for i in range(0, np) :
        number = random.choice(range(700000000, 799999999))
        while number in contanctNumbers :
            number = random.choice(range(700000000, 799999999))
        contanctNumbers.append(number)


### GENERATE ICE NUMBERS ###
def generateICEN (np) :
    """
    generateICEN
    this function generates In Case of Emergency Numbers RANDMOLY -- EVERY NUMBER OCURES ONCE --
    np : Integer --> represent the number of patients to be generated
    <NO RETURN>
    """
    for i in range(0, np) :
        number = random.choice(range(700000000, 799999999))
        while (number in icen) or (number == contanctNumbers[i]) :
            number = random.choice(range(700000000, 799999999))
        icen.append(number)


### GENERATE JOIN DATES ###
def generateJoinDates (np) :
    """
    generateJoinDates
    this function generates Joining dates of patients to the system -- RANDOMLY --
    np : Integer --> represent the number of patients to be generated
    <NO RETURN>
    """
    for i in range(0, np) :
        year = 2014
        month = random.choice(range(8, 13))
        day = random.choice(range(1, 29))
        jd = datetime(year, month, day)
        joinDate.append(str(jd)[:10])

    


### GENERATE SQL SCRIPT FILE ###
def GSSF (np):
    """
    GSSF = Generate Sql Script File
    this function generates the final SQL Script as a form of an INSERT QUERY sotred inside an .sql file called <script.sql>
    np : Integer --> represent the number of patients to be generated
    <NO RETURN>
    """
    sf = open('script.sql', 'w')
    script = "INSERT INTO tb_patients VALUES "
    for i in range(0, np):
        line = "("+str(i+1)+", '$2y$10$bRp3cyH8/n9CbzMv5THtx.2dGHdzmkQcW6RphMEpBMzuhVUI9ZIvq', '"+names[i]+"', '"+lastnames[i]+"', '"+str(emails[i])+"', '"+addresses[random.choice(range(0, len(addresses)))]+"', "+str(nhsn[i])+", "+str(random.choice(range(1, 10)))+", '"+dob[i]+"', '"+gender[i]+"', 'British', '0"+str(contanctNumbers[i])+"', '0"+str(icen[i])+"', '"+joinDate[i]+"', '"+bloodType[i]+"', "+str(weight[i])+", "+str(height[i])+", "+str(BSugar[i])+", '"+BPres[i]+"', '"+str(vision[i])+"', '')"
        
        if i+1 == np :
            script = script+line+";"
        else : script = script+line+", "
    sf.write (script)
    sf.close()





# MAIN BODY

   # LOADING DATA FROM FILES
getMFNames      ("maleFirstNames.txt")
getFFNames      ("femaleFirstNames.txt")
getLNames       ("lastNames.txt")
getAddresses    ("addresses.txt")
getGenderPerc   ("gender.txt")
getAgePerc      ("ages.txt")
getBTypePerc    ("bloodType.txt")
getHeightPerc   ("height.txt")
getWeightPerc   ("weight.txt")
getBSugarPerc   ("bloodSugar.txt")
getBPresurePerc ("bloodPresure.txt")
getEyeSightPerc ("eyeSight.txt")

   # GET NUMBER OF PATIENTS TO GENERATE
np = int(input("please enter the number of patients to generate : "))

  # GENERATE DATA
generateGenders(np)

  #SHUFFLE
shuffle(gender)

  # GENERATE DATA
generateFullNames(np)
generateBirthDates(np)
generateBloodType(np)
generateEmails(np)
generateNHSN(np)
generateContactNumbers(np)
generateICEN(np)
generateJoinDates(np)
generateWeight(np)
generateHeight(np)
generateBloodPresure(np)
generateBloodSugar(np)
generateEyeSight(np)




  # GENERATE SCRIPT FILE
GSSF (np)
