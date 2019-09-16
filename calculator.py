def check_HDL(HDL_result):
    if HDL_result >= 60:
        return "Normal"
    elif 40 <= HDL_result <60:
        return "Borderline low"
    else:
        return "low"

def check_LDL(LDL_result):
    if LDL_result < 130:
        return "Normal"
    elif 130 <= LDL_result <160:
        return "Borderline high"
    elif 160 <= LDL_result <190:
        return "High"
    else:
        return "Very high"

def cholesterol_interface():
    print("Cholesterol check")
    chol_input = input("Enter your cholesterol test result(__=__): ")
    chol_data = chol_input.split("=")
    if chol_data[0] == "HDL":
        result = check_HDL(int(chol_data[1]))
    elif chol_data[0] == "LDL":
        result = check_LDL(int(chol_data[1]))
    print("Your {} cholesterol level is: {}". format(chol_data[0],result))

def interface():
    print("My calculator program")
    keep_running = True
    while keep_running:
        print("Option: ")
        print("9 - Quit")
        print("1 - Check cholesterol results")
        choice = input("Enter your choice: ")
        if choice == '9':
            keep_running = False
        elif choice == '1':
            cholesterol_interface()
    return

if __name__ == "__main__":
    interface()