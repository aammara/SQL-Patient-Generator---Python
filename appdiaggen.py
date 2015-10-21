"""
appdiaggen.py
appointments, diagnostisc generating code
"""

import random

profID = {"1":0, "2":0, "3":0, "4":0, "5":0, "6":0, "7":0, "8":0, "9":0, "10":0}
patientID = {}
diagTitlesDesc = {"Endocrine, Nutritional, Metabolic, Immunity":{"Diabetes Mellitus"},
              "Mental Disorders":{"Neurotic Disorders", "Drug Dependence", "Acute Reaction to Stress", "Depressive Disorder"},
              "Nervous System and Sense Organs":{"Migraine", "Other Retinal Disorders", "Glaucoma", "Cataract", "Disorders of Refraction and Accommodation", "Disorders of Refraction and Accommodation - Myopia", "Disorders of Conjunctiva", "Other Disorders of Eye", "Disorders of External Ear", "Nonsuppurative Otitis Media and Eustachian Tube Disorders", "Suppurative and Unspecified Otitis Media"},
              "Circulatory System":{"Essential Hypertension", "Angina Pectoris", "Cardiac Dysrhythmias", "Heart Failure"},
              "Respiratory System":{"Acute Nasopharyngitis (Common Cold)", "Acute Sinusitis", "Acute Pharyngiti", "Acute Tonsillitis", "Acute Upper Respiratory Infections of Multiple or Unspecified Sites", "Acute Bronchitis and Bronchiolitis", "Allergic Rhinitis", "Bronchitis - Not Specified as Acute or Chronic", "Asthma"},
              "Genitourinary System":{"Cystitis", "Other Disorders of Urethra and Urinary Tract", "Other Disorders of Breast", "Inflammatory Disease of Cervix, Vagina and Vulva", "Disorders of Menstruation and Other Abnormal Bleeding from Female Genital Tract", "Other Disorders of Female Genital Organs"},
              "Skin and Subcutaneous Tissue":{"Other Cellulitis and Abscess", "Contact Dermatitis and Other Eczema", "Diseases of Nail", "Diseases of Sebaceous Glands", "Other Disorders of Skin and Subcutaneous Tissue"},
              "Musculoskeletal System and Connective Tissue":{"Osteoarthrosis and Allied Disorders", "Other and Unspecified Disorder of Joint", "Other Disorders of Cervical Region - Spinal Stenosis in Cervical Region", "Other and Unspecified Disorders of Back - Backache Unspecified", "Disorders of Muscle, Ligament and Fascia", "Other Disorders of Soft Tissues", "Nonallopathic Lesions, Not Elsewhere Classified - Cervical Region", "Nonallopathic Lesions, Not Elsewhere Classified - Thoracic Region", "Nonallopathic Lesions, Not Elsewhere Classified - Lumbar Region"},
              "Symptoms, Signs and Ill-Defined Conditions":{"General Symptoms", "ymptoms Involving Nervous and Musculoskeletal Systems", "Symptoms Involving Skin and Other Integumentary Tissue", "Symptoms Concerning Nutrition, Metabolism and Development", "Symptoms Involving Head and Neck", "Symptoms Involving Cardiovascular System", "Symptoms Involving Respiratory System and Other Chest Symptoms", "Symptoms Involving Digestive System", "Symptoms Involving Urinary System", "Other Symptoms Involving Abdomen and Pelvis"},
              "Injury and Poisoning":{"Sprains and Strains of Shoulder and Upper Arm", "Sprains and Strains of Wrist and Hand", "Sprains and Strains of Hip and Thigh", "Sprains and Strains of Knee and Leg", "Sprains and Strains of Ankle and Foot", "Sprains and Strains of Other and Unspecified Parts of Back", "Sprains and Strains of Other and Unspecified Parts of Back – Neck", "Sprains and Strains of Other and Unspecified Parts of Back – Lumbar", "Injury, Other and Unspecified", "Complications of Medical Care, Not Elsewhere Classified"},
              "Human Immunodeficiency Virus (HIV) Infection with Conditions":{"HIV Infection with Certain Specified Infections", "HIV Infection Causing Other Specified Infections", "HIV Infection with Specified Malignant Neoplasms", "Acquired Immunodeficiency Syndrome with or without Other Conditions"},
              "HIV Infection Causing Other Specified Conditions":{"HIV Infection Causing Lymphadenopathy", "HIV Infection Causing Specified Diseases of the Central Nervous System", "HIV Infection Causing Other Disorders Involving the Immune Mechanism", "HIV Infection Causing Other Specified Conditions", "Acquired Immunodeficiency Syndrome-Related Complex"},
              "Other Human Immunodeficiency Virus (HIV) Infection":{"HIV Infection Causing Specified Acute Infections", "HIV Infection Not Otherwise Specified"},
              "Primary Tuberculous Infection":{"Primary Tuberculous Complex", "Tuberculous Pleurisy in Primary Progressive Tuberculosis", "Other Primary Progressive Tuberculosis", "Unspecified"},
              "Pulmonary Tuberculosis":{"Tuberculosis of Lung, Infiltrative", "Tuberculosis of Lung, Nodular", "Tuberculosis of Lung With Cavitation", "Tuberculosis of Bronchus", "Tuberculous Fibrosis of Lung", "Tuberculous Bronchiectasis", "Tuberculous Pneumonia", "Tuberculous Pneumothorax", "Other Pulmonary Tuberculosis", "Unspecified"},
              "Other Respiratory Tuberculosis":{"Tuberculous Pleurisy", "Other"},
              "Bacterial Infection in Conditions Classified Elsewhere and of Unspecified Site":{"Friedlander's Bacillus", "Haemophilus Influenzae"}}

def generateProfId () :
    """
    generateProfId
    this function generates professional IDs related diagnostics
    no parametere
    returns Integer : prid
    """
    prid = random.randint(1, 10)
    while (profID[str(prid)] >= 500) :
        prid = random.randint(1, 10)
    profID[str(prid)]=profID[str(prid)]+1
    return prid


def generatePatientId () :
    """
    generatePatientId
    this function generates patient IDs related diagnostics
    no parametere
    returns Integer : ptid
    """
    for i in range(1, 1001) :
        patientID[str(i)]= 0
    ptid = random.randint(1, 1000)
    while (patientID[str(ptid)] > 500) :
        ptid = random.randint(1, 1000)
    patientID[str(ptid)]=patientID[str(ptid)]+1
    return ptid

def generateRandDate () :
    """
    generateRandDate
    this function generates random dates related to diagnostics
    no parametere
    returns Integer : date
    """
    year  = random.choice(range(2014, 2016))
    month = random.choice(range(1, 13))
    monthStr = str(month)
    if (month < 10) : monthStr = "0"+str(month)
    day   = random.choice(range(1, 29))
    dayStr = str(day)
    if (day < 10) : dayStr = "0"+str(day)
    date  = str(year)+"-"+monthStr+"-"+dayStr
    return date

def generateExpDate (date) :
    """
    generateExpDate
    this function generates random expiry dates related to diagnostics
    no parametere
    returns Integer : exp_date
    """
    year  = int(date[:4])
    month = int(date[5:7]) + 3
    if (month > 12) :
        month = month - 12
        year = year + 1

    monthStr = str(month)
    if (month < 10) : monthStr = "0"+str(month)
        
    day   = int(date[8:10])
    dayStr = str(day)
    if (day < 10) :
        dayStr = "0"+str(day)
        
    exp_date  = str(year)+"-"+monthStr+"-"+dayStr
    return exp_date

def generateRandTime () :
    """
    generateRandTime
    this function generates random Time related to diagnostics
    no parametere
    returns Integer : time
    """
    hours   = random.randint(8, 18)
    hoursStr = str(hours)
    if (hours < 10) : hoursStr = "0"+str(hours)
    minutes = random.randint(0, 59)
    minutesStr = str(minutes)
    if (minutes < 10) : minutesStr = "0"+str(minutes)
    seconds = random.randint(0, 59)
    secondsStr = str(seconds)
    if (seconds < 10) : secondsStr = "0"+str(seconds)
    time    = hoursStr+":"+minutesStr+":"+secondsStr
    return time


def generateApp_AND_Diag (appid) :
    """
    generateApp_AND_Diag
    this function generates an SQL script line for both tables 'tb_appointments' & 'tb_diagnostics'
    Parametere(s) : appid = appointment id given from a previous loop function
    returns String : script_line
    """
    profid  = str(generateProfId())
    ptid    = str(generatePatientId())
    appid   = str(appid)
    time    = str(generateRandTime())
    date    = str(generateRandDate())
    expDate = str(generateExpDate(date))
    title   = random.choice(list(diagTitlesDesc.keys()))
    descp   = random.choice(list(diagTitlesDesc[title]))
    
    lineApp  = "INSERT INTO tb_appointments VALUES ("+appid+", "+profid+", "+ptid+", '"+time+"', '"+date+"');"
    lineDiag = "INSERT INTO tb_diagnostics VALUES ("+appid+", "+ptid+", "+profid+", '"+title+"', '"+descp+"', '"+date+"', '"+expDate+"');"
    script_line = lineApp+" \n"+lineDiag+" \n"
    return script_line

def generateScriptFile () :
    """
    generateScriptFile
    this function generates a final SQL Script file
    Parametere(s) : none
    returns : none
    """
    
    sf = open('script_app_diag.sql', 'w')
    script = ""
    for i in range(1, 5000):
        line = generateApp_AND_Diag (i)
        script = script + line

    sf.write (script)
    sf.close()

generateScriptFile()
