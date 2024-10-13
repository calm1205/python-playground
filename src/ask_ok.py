def ask_ok(prompt, retries = 3, reminder="input yes or no"):
    """
    Keep prompting the user until the user inputs 'yes' or 'no'.
    """

    i = 0
    while i < retries:
        user_input = input(prompt + "\n=> ")
        if user_input in ('y', 'ye', 'yes'):
            return True
        if user_input in ('n', 'no', 'nop', 'nope'):
            return False
        print(reminder, "\n")
        i += 1
    else:
        print("You have exceeded the number of retries.")
        return False

ask_ok("Do you really want to quit?") # Do you really want to quit?yes