class Tests:
    def __init__(self, Patient_ID, Anemia,Diabetes,High_BP,Platelets,Creatinine,Sodium):
        self.Patient_ID = Patient_ID
        self.Anemia = Anemia
        self.Diabetes = Diabetes
        self.High_BP = High_BP
        self.Platelets = Platelets
        self.Creatinine = Creatinine
        self.Sodium = Sodium
   
    def printResults(self,result,patient):
        """
        

        Parameters
        ----------
        result : int
            Chooses which patient result to generate based on user input.
        patient : int
            Chooses which patient to select based on user input.

        Returns
        -------
        Returns a test_result object.

        """
        if result == 1:
            print("Patient #"+str(patient)+"'s Anemia level is " + str(self.Anemia))
        elif result == 2:
            print("Patient #"+str(patient)+"'s Diabetes levels are " + str(self.Diabetes))
        elif result == 3:
            print("Patient #"+str(patient)+"'s High Blood Pressure levels are " + str(self.High_BP))
        elif result == 4:
            print("Patient #"+str(patient)+"'s Platelet leves are " + str(self.Platelets))
        elif result == 5:
            print("Patient #"+str(patient)+"'s Creatinine levels are " + str(self.Creatinine))
        elif result == 6:
            print("Patient #"+str(patient)+"'s Sodium levels are " + str(self.Sodium))
    
    def modifyResults(self,selection,new_result):
        """
        

        Parameters
        ----------
        selection : int
            Selects the test to be modified based on user input.
        new_result : int or float
            This is the value that replace the specified test result.

        Returns
        -------
        Returns a modifed test result.

        """
        if selection == 1:
            self.Anemia = int(new_result)
        elif selection == 2:
            self.Diabetes = int(new_result)
        elif selection == 3:
            self.High_BP = int(new_result)
        elif selection == 4:
            self.Platelets = int(new_result)
        elif selection == 5:
            self.Creatinine = float(new_result)
        elif selection == 6:
            self.Sodium = int(new_result)
        


class Patient:
    def __init__(self, Patient_ID, Characteristics, Test_results):
        self.Patient_ID = Patient_ID
        self.Characteristics = Characteristics
        self.Test_results = Test_results
        
    def printRecord(self):
        """
        

        Returns
        -------
        Returns a patient object based on user input.

        """
        print("DOB, Sex at Birth, Smoker: ", self.Characteristics)
        anemia = self.Test_results.Anemia
        diabetes = self.Test_results.Diabetes
        hbp = self.Test_results.High_BP
        pL = self.Test_results.Platelets
        creat = self.Test_results.Creatinine
        sod = self.Test_results.Sodium
        print("Anemia Diabetes High Blood Pressure Platelets Creatinine Sodium")
        print(anemia,"    ",diabetes,"      ",hbp,"                 ",pL,"  ",creat,"      ",sod)
        

def databaseManagement(x):
    """
    

    Parameters
    ----------
    x : Loads the patient file and forms it into a dictionary.

    Returns
    -------
    patient_dictionary : Returns a formatted dictionary wiht patients loaded.

    """
    pfr = x.readlines()
    patient_dictionary = {}
    count = 0
    for i in pfr:
        i = i.split("\t")
        if count >=1:
            if i[2] == "0":
                sex = "F"
                creat = float(i[8][0:3])
                ID = int(i[0])
                temp_test = Tests(ID, int(i[4]), int(i[5]), int(i[6]), int(i[7]), creat, int(i[9]))
                temp_patient = Patient(ID,(int(i[1]),sex,int(i[3])) ,temp_test)
                patient_dictionary[ID] = temp_patient
            elif i[2] == "1":
                sex = "M"
                creat = float(i[8][0:3])
                ID = int(i[0])
                temp_test = Tests(ID, int(i[4]), int(i[5]), int(i[6]), int(i[7]), creat, int(i[9]))
                temp_patient = Patient(ID,(int(i[1]),sex,int(i[3])) ,temp_test)
                patient_dictionary[ID] = temp_patient
        else:
            count += 1
    return patient_dictionary

def add_patient(x):
    """
    

    Parameters
    ----------
    x : Takes in a dictionary.

    Returns
    -------
    Returns the dictionary with a patient added based on inputs.

    """
    patient_dictionary = x
    print("Enter the patients year of birth, sex, whether the patient smokes")
    dob = int(input("DOB:"))
    sex = int(input("Sex at birth (1 for male, 0 for female):"))
    if sex == 0:
        sex = "F"
    elif sex == 1:
        sex = "M"
    smoker = int(input("Smoker (1 for smoker; 0 for non-smoker):"))
    print("Enter Test Results")
    anemia = int(input("Anemia (1/0):"))
    diabetes = int(input("Diabetes (1/0):"))
    hbp = int(input("High Blood Pressure (1/0):"))
    pL = int(input("Platelet level:"))
    cL = float(input("Creatinine level:"))
    sL = int(input("Sodium level:"))
    pID = len(patient_dictionary) + 1
    tests = Tests(pID, anemia, diabetes, hbp, pL, cL, sL)
    patient = Patient(pID, (dob,sex,smoker), tests)
    patient_dictionary[pID] = patient



def remove_patient(x):
    """
    

    Parameters
    ----------
    x : Takes in a patient dictionary file.

    Returns
    -------
    Returns the same dictionary with a specified patient removed.

    """
    patient_dictionary = x
    print("Enter the ID of the patient you would like to delete from the Database")
    patient = int(input("ID Number:"))
    del patient_dictionary[patient]
    
    

def modify_tests(x):
    """
    

    Parameters
    ----------
    x : Takes in a patient dictionary.

    Returns
    -------
    Returns the patient dictionary with a specified patient modified.

    """
    patient_dictionary =x
    print("Enter the ID of the patient and the test result you would like to modify\n")
    patient = int(input("Patient ID Number:\n"))
    print("Test Selection: Enter 1 for Anemia/2 for Diabetes/3 for High Blood Pressure/4 for Platelets/5 for Creatinine/6 for Sodium\n")
    selection = int(input("Enter your selection now:\n"))
    new_result = input("Enter the new test result:\n")
    patient_dictionary[patient].Test_results.modifyResults(selection,new_result)