# main executable file for workout tracker

import datetime

def create_workout(name: str, sets: int, reps: int, date: datetime.date = datetime.date.today(), num: int = 1):
    '''
    Method to create a workout

    Parameters
    ----------
    name : str
        name of the workout
    sets : int
        number of sets
    reps : int
        number of reps
    date : datetime.date
        date of workout
    num : int
        workout session number on single day

    Returns
    -------
    new_dict : dict
        Dictionary containing the attributes of the workout
    
    Raises
    ------
    TypeError
        If input variables are not the expected types (str, int, int)
    '''

    try:
        name = str(name)
    except:
        raise TypeError("name is not a string")
    
    try:
        sets = int(sets)
    except:
        raise TypeError("sets is not an integer")
    
    try:
        reps = int(reps)
    except:
        raise TypeError("reps is not an integer")
    
    if not isinstance(date, datetime.date):
        raise TypeError("date is not a datetime.date object")
    
    try:
        num = int(num)
    except:
        raise TypeError("num is not an integer")

    new_dict = {
        "name": name,
        "sets": sets,
        "reps": reps,
        "date": date,
        "num": num
    }

    return new_dict

def main():

    print("Welcome to the workout tracker:")

    workout_list = []

    while(True):
        print("Input 2 to display current workouts, 1 to create workout, or 0 to quit")

        user_in = int(input())

        if user_in == 0:
            break
        
        if user_in == 1:
            name = input("Input name of workout: ")
            sets = input("Input number of sets: ")
            reps = input("Input number of reps: ")
            workout_list.append(create_workout(name, sets, reps))
        
        if user_in == 2:
            print(workout_list)

    print("Thanks for using the workout tracker.")
    return

if __name__ == "__main__":
    main()