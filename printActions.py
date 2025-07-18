import databaseManagement

def all_records(x):
    """
    

    Parameters
    ----------
    x : Takes in a patient dictionary.

    Returns
    -------
    Returns every record from the patient dictionary.

    """
    patient_dictionary = x
    for i in patient_dictionary:
        print("Patient Record of Patient #" + str(i))
        print("DOB, Sex at Birth, Smoker: ", patient_dictionary[i].Characteristics)
        print("Anemia Diabetes High Blood Pressure Platelets Creatinine Sodium")
        anemia = patient_dictionary[i].Test_results.Anemia
        diabetes = patient_dictionary[i].Test_results.Diabetes
        hbp = patient_dictionary[i].Test_results.High_BP
        pL = patient_dictionary[i].Test_results.Platelets
        creat = patient_dictionary[i].Test_results.Creatinine
        sod = patient_dictionary[i].Test_results.Sodium
        print(anemia,"    ",diabetes,"      ",hbp,"                 ",pL,"  ",creat,"      ",sod)


def view_record(x):
    """
    

    Parameters
    ----------
    x : Takes in a patient dictionary.

    Returns
    -------
    Returns an element of the patient dictionary based on user input.

    """
    patient_dictionary = x
    patient = int(input("Please enter the id of the patient whose record you would like to see:"))
    print("Patient Record of Patient # " + str(patient))
    patient_dictionary[patient].printRecord()


def view_test(x):
    """
    

    Parameters
    ----------
    x : Takes in a patient dictionary.

    Returns
    -------
    Returns an element of the test class based on user input.

    """
    patient_dictionary = x
    patient = int(input("Please enter the id of the patient you are treating:\n"))
    print("What test results you would like to view?\n")
    result = int(input("Enter 1 for Anemia/2 for Diabetes/3 for High Blood Pressure/4 for Platelets/5 for Creatinine/6 for Sodium\n"))
    pt = patient_dictionary[patient]
    pt.Test_results.printResults(result,patient)