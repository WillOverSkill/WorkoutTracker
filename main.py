# main executable file for workout tracker


def create_workout(name: str, sets: int, reps: int):
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

    Returns
    -------
    new_dict : dict
        Dictionary containing the attributes of the workout
    
    Raises
    ------
    TypeError
        If input variables are not the expected types (str, int, int)
    '''

    if not isinstance(name, str):
        raise TypeError("name is not a string")
    
    if not isinstance(sets, int):
        raise TypeError("sets is not an integer")
    
    if not isinstance(reps, int):
        raise TypeError("reps is not an integer")
    
    new_dict = {
        "name": name,
        "sets": sets,
        "reps": reps
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
            name = str(input("Input name of workout: "))
            sets = int(input("Input number of sets: "))
            reps = int(input("Input number of reps: "))
            workout_list.append(create_workout(name, sets, reps))
        
        if user_in == 2:
            print(workout_list)

    print("Thanks for using the workout tracker.")
    return

if __name__ == "__main__":
    main()