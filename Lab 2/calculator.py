def display_current_value():
    #displays the current value
    print("Current value:", current_value)


def undo():
    #Restores the previous value that apperared on the screen
    global last_value, current_value
    update(last_value)

def update(new_value):
    #stores 2 variables (last value and current values) used in the undo process
    global current_value, last_value
    last_value = current_value
    current_value = new_value


def add(to_add):
    #adds to_add to the value in the calculator
    global current_value
    update(current_value + to_add)


def subtract(to_sub):
    #Subtracts to_sub from the value in the calculator
    global current_value
    update(current_value - to_sub)


def mult(to_mult):
    #multiplies the current value in the calculator by to_mult
    global current_value
    update(current_value * to_mult)


def div(to_div):
    #divides the current value in the calculator by to_div
    global current_value
    update(current_value / to_div) #encountered issue is with decimals
                            #it needs to change to float for it to work -- which it does -- can be seen in the workspace



def memory():
    # This function saves the value indicated
    global current_value
    global save
    save = current_value


def recall():
    #prints out the saved value in the calculator
    print("Saved value:", save)


if __name__ == '__main__':
    current_value = 0
    save = 0
    last_value = current_value
    print("Welcome to the calculator program.\nCurrent value:", current_value)

    add(5)
    memory()
    subtract(2)
    display_current_value()
    recall()
    undo()
    display_current_value()
    undo()
    display_current_value()
    mult(10)
    display_current_value()
    undo()
    undo()
    display_current_value()
    undo()
    undo()
    undo()
    display_current_value()
    recall()