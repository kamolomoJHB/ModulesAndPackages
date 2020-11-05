"""
TODO: [You can either work from this skeleton], or you can build on your solution for Toy Robot 2 exercise.
"""

# list of valid command names
valid_commands = ['off', 'help', 'forward', 'back', 'right', 'left', 'sprint', 'replay']

command_to_run = []

# variables tracking position and direction
position_x = 0
position_y = 0
directions = ['forward', 'right', 'back', 'left']
current_direction_index = 0

# area limit vars
min_y, max_y = -200, 200
min_x, max_x = -100, 100
###StartMyStuff

#history variables
history_list = []
movement_history_list = []

#count variables
silent_count = 0
iter_count = 0

#int_range variables
range_holder = ()

def is_int_range(int_range):
    """
    Tests if value is a valid integer range or not
    :param value: a range to test
    :return: True if it is a valid int range
    """
    global range_holder, iter_count
    range_holder = ()
    if "-" in int_range:
        int_range_values = int_range.split('-')
        if is_int(int_range_values[0]) and is_int(int_range_values[1]):
            if (int_range_values[0] > int_range_values[1]):
                range_holder = (int_range_values[0], int_range_values[1])
                iter_count = int(int_range_values[0]) - int(int_range_values[1])
                return True
    return False

def do_replay(robot_name, reversed, silent, n, m):
    """
    Replays (re-executes) previously executed commands depending on the param.s
    If reversed==True ==(-1), commands are executed in reverse
    If silent==True, commands executed without showing command output
    If n or n and m, only specified n,m commands will be executed
    """
    global silent_count, iter_count, movement_history_list, range_holder
    range_holder = ()
    if silent == True:
        if n == None and m == None:
            silent_count = len(movement_history_list)
        elif not n == None and not m == None:
            silent_count = n-m
        elif not n == None and m == None:
            silent_count = n
    else:
        silent_count = 0
    num_commands = len(movement_history_list)
    if isinstance(n, int) == True:
        num_commands = n 
    if isinstance(m, int) == True:
        num_commands = n-m
    if not n == None:
        # Not REVERSED
        if reversed == 1 and m == None:
            n = len(movement_history_list) - n
        elif reversed == 1 and not m == None:
            n = len(movement_history_list)- n
            m = len(movement_history_list) - m
        # REVERSED
        if reversed == -1 and m == None:    
            n = n-1
        elif reversed == -1 and not m == None:    
            n, m = m, n
            n = n - 1
            m = m -1
    for each_command in movement_history_list[n:m:reversed]:
        handle_command(robot_name, each_command.lower())
    if silent == True and reversed == 1: #silent, not reversed
        return True, ' > '+robot_name+' replayed ' + str(num_commands)+' commands silently.'
    if silent == True and reversed == -1: #silent AND reversed
        return True, ' > '+robot_name+' replayed ' + str(num_commands)+' commands in reverse silently.'
    if silent == False and reversed == -1: #not silent, but reversed
        return True, ' > '+robot_name+' replayed ' + str(num_commands)+' commands in reverse.'
    if silent == False and reversed == 1: #not silent, not reversed
        return True, ' > '+robot_name+' replayed ' + str(num_commands)+' commands.'

def record_history(command):
    """
    Records the commands executed by the robot.
    Last executed command = last item in history_list (global variable)
    """
    (command_name, arg) = split_command_input(command)
    if command_name in ('forward', 'back', 'left', 'right', 'sprint'):
        movement_history_list.append(command)
    history_list.append(command)
###
def get_robot_name():
    name = input("What do you want to name your robot? ")
    while len(name) == 0:
        name = input("What do you want to name your robot? ")
    return name

def get_command(robot_name):
    """
    Asks the user for a command, and validate it as well
    Only return a valid command
    """
    prompt = ''+robot_name+': What must I do next? '
    command = input(prompt)
    while len(command) == 0 or not valid_command(command):
        output(robot_name, "Sorry, I did not understand '"+command+"'.")
        command = input(prompt)
    record_history(command.lower())
    return command.lower()

def split_command_input(command):
    """
    Splits the string at the first space character, to get the actual command, as well as the argument(s) for the command
    :return: (command, argument)
    """
    args = command.split(' ', 1)
    if len(args) > 1:
        return args[0], args[1]
    return args[0], ''

def is_int(value):
    """
    Tests if the string value is an int or not
    :param value: a string value to test
    :return: True if it is an int
    """
    global range_holder, iter_count
    try:
        int(value)
        range_holder = (value)
        iter_count = value
        return True
    except ValueError:
        return False

def valid_command(command):
    """
    Returns a boolean indicating if the robot can understand the command or not
    Also checks if there is an argument to the command, and if it a valid int or valid int_range
    """
    """
{replay}	
		{n}
		{n-m}
		{silent}	
				{n}
				{n-m}
		{reversed}	
				{n}
				{n-m}
				{silent}
						{n}
						{n-m}
    
	{n}     ==*
	{n-m}   ==*
    {silent}==*
    """
    (command_name, arg1) = split_command_input(command.lower())
    if command_name == 'replay':
        (sub_arg1_1, sub_arg1_2) = split_command_input(arg1)
        (sub_arg1_2, sub_arg1_3) = split_command_input(sub_arg1_2)
        sub_arg_list = [sub_arg1_1, sub_arg1_2, sub_arg1_3]
        sub_arg_list = sorted(sub_arg_list, key=len) #To always put numbers at the end of list
        sub_arg1_1 = sub_arg_list[2]
        sub_arg1_2 = sub_arg_list[1]
        sub_arg1_3 = sub_arg_list[0]
        if (is_int(sub_arg1_3) or is_int_range(sub_arg1_3) or (sub_arg1_3=='')) and sub_arg1_2 == 'silent' and sub_arg1_1 == 'reversed':###replay_reversed_silent_(*)
            command_to_run.append(sub_arg1_1)
            command_to_run.append(sub_arg1_2)
            if not sub_arg1_3 == '':
                command_to_run.append(sub_arg1_3)
        elif (is_int(sub_arg1_2) or is_int_range(sub_arg1_2) or (sub_arg1_2=='')) and sub_arg1_1 == 'reversed' and (sub_arg1_3 == ''):###replay_reversed_(*)
            command_to_run.append(sub_arg1_1)
            if not sub_arg1_2 == '':
                command_to_run.append(sub_arg1_2)
        elif (is_int(sub_arg1_2) or is_int_range(sub_arg1_2) or (sub_arg1_2=='')) and sub_arg1_1 == 'silent' and sub_arg1_3=='':###replay_silent_(*)
            command_to_run.append(sub_arg1_1)
            if not sub_arg1_2 == '':
                command_to_run.append(sub_arg1_2)
        elif (is_int(sub_arg1_1) or is_int_range(sub_arg1_1) or (sub_arg1_1=='')) and sub_arg1_2 == '' and sub_arg1_3=='':###replay_(*)
            if not sub_arg1_1 == '':
                command_to_run.append(sub_arg1_1)
        else:
            return False
        arg1 = command_to_run
    if isinstance(arg1, list) and command_name.lower() in valid_commands:
        return True
    return command_name.lower() in valid_commands and (len(arg1) == 0 or is_int(arg1) or arg1 == 'silent' or arg1 == 'reversed' or arg1 == 'reversed silent')

def output(name, message):
    print(''+name+": "+message)

def do_help():
    """
    Provides help information to the user
    :return: (True, help text) to indicate robot can continue after this command was handled
    """
    return True, """I can understand these commands:
OFF  - Shut down robot
HELP - provide information about commands
FORWARD - move forward by specified number of steps, e.g. 'FORWARD 10'
BACK - move backward by specified number of steps, e.g. 'BACK 10'
RIGHT - turn right by 90 degrees
LEFT - turn left by 90 degrees
SPRINT - sprint forward according to a formula
REPLAY - re-executes robot's movements in sequence
REPLAY SILENT - re-executes robot's movements in sequence but only outputs final position   e.g replay silent (run all previous movement commands)
                                                                                            e.g. replay silent 2 (2 previous movement commands)
REPLAY REVERSED - re-executes robot's movements in reverse sequence e.g. 'replay reversed 2' (2 commands in reverse)
"""

def show_position(robot_name):
    print(' > '+robot_name+' now at position ('+str(position_x)+','+str(position_y)+').')

def is_position_allowed(new_x, new_y):
    """
    Checks if the new position will still fall within the max area limit
    :param new_x: the new/proposed x position
    :param new_y: the new/proposed y position
    :return: True if allowed, i.e. it falls in the allowed area, else False
    """
    return min_x <= new_x <= max_x and min_y <= new_y <= max_y

def update_position(steps):
    """
    Update the current x and y positions given the current direction, and specific nr of steps
    :param steps:
    :return: True if the position was updated, else False
    """
    global position_x, position_y
    new_x = position_x
    new_y = position_y

    if directions[current_direction_index] == 'forward':
        new_y = new_y + steps
    elif directions[current_direction_index] == 'right':
        new_x = new_x + steps
    elif directions[current_direction_index] == 'back':
        new_y = new_y - steps
    elif directions[current_direction_index] == 'left':
        new_x = new_x - steps

    if is_position_allowed(new_x, new_y):
        position_x = new_x
        position_y = new_y
        return True
    return False

def do_forward(robot_name, steps):
    """
    Moves the robot forward the number of steps
    :param robot_name:
    :param steps:
    :return: (True, forward output text)
    """
    if update_position(steps):
        return True, ' > '+robot_name+' moved forward by '+str(steps)+' steps.'
    else:
        return True, ''+robot_name+': Sorry, I cannot go outside my safe zone.'

def do_back(robot_name, steps):
    """
    Moves the robot forward the number of steps
    :param robot_name:
    :param steps:
    :return: (True, forward output text)
    """
    if update_position(-steps):
        return True, ' > '+robot_name+' moved back by '+str(steps)+' steps.'
    else:
        return True, ''+robot_name+': Sorry, I cannot go outside my safe zone.'

def do_right_turn(robot_name):
    """
    Do a 90 degree turn to the right
    :param robot_name:
    :return: (True, right turn output text)
    """
    global current_direction_index
    current_direction_index += 1
    if current_direction_index > 3:
        current_direction_index = 0
    return True, ' > '+robot_name+' turned right.'

def do_left_turn(robot_name):
    """
    Do a 90 degree turn to the left
    :param robot_name:
    :return: (True, left turn output text)
    """
    global current_direction_index
    current_direction_index -= 1
    if current_direction_index < 0:
        current_direction_index = 3
    return True, ' > '+robot_name+' turned left.'

def do_sprint(robot_name, steps):
    """
    Sprints the robot, i.e. let it go forward steps + (steps-1) + (steps-2) + .. + 1 number of steps, in iterations
    :param robot_name:
    :param steps:
    :return: (True, forward output)
    """
    if steps == 1:
        return do_forward(robot_name, 1)
    else:
        (do_next, command_output) = do_forward(robot_name, steps)
        print(command_output)
        return do_sprint(robot_name, steps - 1)

def handle_command(robot_name, command):
    """
    Handles a command by asking different functions to handle each command.
    :param robot_name: the name given to robot
    :param command: the command entered by user
    :return: `True` if the robot must continue after the command, or else `False` if robot must shutdown
    """
    global silent_count, command_to_run, range_holder, iter_count
    (command_name, arg) = split_command_input(command)
    if command_name == 'replay':
        if not len(command_to_run) == 0:
            if 'reversed' in command_to_run:
                reversed = -1
            else:
                reversed = 1
            if 'silent' in command_to_run:
                silent = True
            else:
                silent = False
            if len(range_holder) == 2:
                n = range_holder[0]
                m = range_holder[1]
                n = int(n)
                m = int(m)
            else:
                n = None
                m = None
            
            if len(range_holder) == 1:
                n = range_holder[0]
                n = int(n)

            (do_next, command_output) = do_replay(robot_name, reversed, silent, n, m)
        else:
            (do_next, command_output) = do_replay(robot_name, 1, False, None, None) 
    if command_name == 'off':
        movement_history_list = []
        return False
    elif command_name == 'help':
        (do_next, command_output) = do_help()
    elif command_name == 'forward':
        (do_next, command_output) = do_forward(robot_name, int(arg))
    elif command_name == 'back':
        (do_next, command_output) = do_back(robot_name, int(arg))
    elif command_name == 'right':
        (do_next, command_output) = do_right_turn(robot_name)
    elif command_name == 'left':
        (do_next, command_output) = do_left_turn(robot_name)
    elif command_name == 'sprint':
        (do_next, command_output) = do_sprint(robot_name, int(arg))
    if silent_count == 0:
        if command == 'help':
            print(command_output)
        else:
            print(command_output)
            show_position(robot_name)
    else:
        silent_count = silent_count -1
    return do_next

def robot_start():
    """This is the entry point for starting my robot"""
    global position_x, position_y, current_direction_index
    global movement_history_list, command_to_run, range_holder
    robot_name = get_robot_name()
    output(robot_name, "Hello kiddo!")
    position_x = 0
    position_y = 0
    current_direction_index = 0
    command_to_run = []
    movement_history_list = []
    range_holder = ()
    command = get_command(robot_name)
    while handle_command(robot_name, command.lower()):
        command = get_command(robot_name)
    output(robot_name, "Shutting down..")

if __name__ == "__main__":
    robot_start()
