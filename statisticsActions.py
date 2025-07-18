def statistics(x):
    """
    

    Parameters
    ----------
    x : Takes in a dictionary

    Returns
    -------
    Returns statistics based on calculations made on elements of the dictionary.

    """
    patient_dictionary = x
    male_count = 0
    female_count = 0
    male_anemia = 0
    female_anemia = 0
    male_diabetes = 0
    female_diabetes = 0
    
    for i in patient_dictionary:
        if patient_dictionary[i].Characteristics[1] == "F":
            female_count += 1
            female_anemia += patient_dictionary[i].Test_results.Anemia
            female_diabetes += patient_dictionary[i].Test_results.Diabetes
        else:
            male_count += 1
            male_anemia += patient_dictionary[i].Test_results.Anemia
            male_diabetes += patient_dictionary[i].Test_results.Diabetes
    m_anemia_stat = round((male_anemia/male_count) * 100,1)
    m_diabetes_stat = round((male_diabetes/male_count) * 100,1)
    f_anemia_stat = round((female_anemia/female_count) * 100,1)
    f_diabetes_stat = round((female_diabetes/female_count) * 100,1)
    
    print("The percentage of women who have anemia is " +str(f_anemia_stat) + "%\n")
    print("The percentage of men who have anemia is "+str(m_anemia_stat) +"%\n") 
    print("The percentage of women who have diabetes is " +str(f_diabetes_stat)+"%\n")
    print("The percentage of men who have diabetes is " +str(m_diabetes_stat)+"%\n")