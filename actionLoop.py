import databaseManagement as dM
import printActions as pA
import statisticsActions as sA




patient_file = open("/Users/jasonfinkle/Desktop/Advanced Coding/patients-database-tab.txt", "r")

patient_dictionary = dM.databaseManagement(patient_file)





choice = 0
opt_1 = "Enter 1 to add a patient to the database\n\n"
opt_2 = "2 to delete a patient from the database\n\n"
opt_3 = "3 to modify a patient's test result\n\n"
opt_4 = "4 to print all the patient's records\n\n"
opt_5 = "5 to print a single patient's record\n\n"
opt_6 = "6 to print a single patient's test result\n\n"
opt_7 = "7 to print a statistic\n\n"
opt_8 = "8 to exit the program\n"

while choice != 8:
    print(opt_1,opt_2,opt_3,opt_4,opt_5,opt_6,opt_7,opt_8)
    choice = int(input("Enter your choice now:\n"))
    
    if choice == 1:
        dM.add_patient(patient_dictionary)
    elif choice == 2:
        dM.remove_patient(patient_dictionary)
    elif choice == 3:
        dM.modify_tests(patient_dictionary)
    elif choice == 4:
        pA.all_records(patient_dictionary)
    elif choice == 5:
        pA.view_record(patient_dictionary)
    elif choice == 6:
        pA.view_test(patient_dictionary)
    elif choice == 7:
        sA.statistics(patient_dictionary)


