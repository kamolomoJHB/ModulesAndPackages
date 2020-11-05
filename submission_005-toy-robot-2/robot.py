"""This is a test"""

def move_robot(steps_move, robot_xy, current_dir):
    if current_dir == 0:
        new_robot_xy = (robot_xy[0]+int(steps_move), robot_xy[1])
    elif current_dir == 180:
        new_robot_xy = (robot_xy[0]-int(steps_move), robot_xy[1])
    elif current_dir == 90:
        new_robot_xy = (robot_xy[0], robot_xy[1] + int(steps_move))
    else:
        new_robot_xy = (robot_xy[0], robot_xy[1] - int(steps_move))
    return new_robot_xy

def sprint_robot(steps):
    if steps == 1:
        return steps
    else:
        return steps + sprint_robot(steps - 1)

def is_robot_in_safe_zone(robot_name, robot_xy, xy_before_moving):
    if (robot_xy[0] > 100) or (robot_xy[0] < -100) or (robot_xy[1] > 200) or (robot_xy[1] < -200):
        print(str(robot_name) + ": Sorry, I cannot go outside my safe zone.")
        print(" > " + str(robot_name) + " now at position "+ str(xy_before_moving).replace(" ", "") +"." )
        return False
    else:
        return True

def sprint_command(robot_name, steps, robot_xy):
    for i in range(steps, 0,-1):
        print(" > " + str(robot_name) +" moved forward by " + str(i) + " steps.")
    print(" > " + str(robot_name) + " now at position "+ str(robot_xy).replace(" ", "") +".")    

def left_command(robot_name, robot_xy):
    turn_left = " > " + str(robot_name) + " turned left.\n > " + str(robot_name) + " now at position "+ str(robot_xy).replace(" ", "") +"."
    return print(turn_left)

def right_command(robot_name, robot_xy):
    turn_right = " > " + str(robot_name) + " turned right.\n > " + str(robot_name) + " now at position "+ str(robot_xy).replace(" ", "") +"."
    return print(turn_right)

def backward_command(robot_name, steps, robot_xy):
    move_back = " > " + str(robot_name) +" moved back by " + str(steps) + " steps.\n > " + str(robot_name) + " now at position "+ str(robot_xy).replace(" ", "") +"."
    return print(move_back)

def forward_command(robot_name, steps, robot_xy):
    move_forward = " > " + str(robot_name) +" moved forward by " + str(steps) + " steps.\n > " + str(robot_name) + " now at position "+ str(robot_xy).replace(" ", "") +"."
    return print(move_forward)

def help_command():
    valid_commands_output = """I can understand these commands:
OFF  - Shut down robot
HELP - provide information about commands
FORWARD - moves robot forward
BACK - moves robot backward
RIGHT - turns robot right
LEFT - turns robot left
SPRINT - sprints robot forward
"""
    return print(valid_commands_output)

def valid_command(command):
    steps = ""
    if command in ("OFF", "HELP", "RIGHT", "LEFT") :
        return True
    if ("BACK " in command):
        steps = command.replace("BACK ", "")
    if ("FORWARD " in command):
        steps = command.replace("FORWARD ", "")
    if ("SPRINT " in command):
        steps = command.replace("SPRINT ", "")
    if steps.isdigit() == True:
        return True
    else:
        return False

def get_command(robot_name, robot_xy, current_dir):
    """
    Gets command from user
    """
    input_command = input(robot_name + ": What must I do next? ")
    #print("1rin")
    valid_command(input_command.upper())
    if valid_command(input_command.upper()) == True: 
        #print("in2run")
        #print(str(input_command))
        if input_command.upper() in("OFF"):
            print(robot_name+ ": Shutting down..")
            exit
        elif input_command.upper() in("HELP"):
            help_command()
            get_command(robot_name, robot_xy, current_dir)
        elif "FORWARD " in input_command.upper():
            steps_forward = input_command.upper().strip("FORWARD ")
            new_robot_xy = move_robot(steps_forward, robot_xy, current_dir)
            
            safe_zone = is_robot_in_safe_zone(robot_name, new_robot_xy, robot_xy)
            if safe_zone == True:
                forward_command(robot_name, steps_forward, new_robot_xy)
                get_command(robot_name, new_robot_xy, current_dir)
            else:
                get_command(robot_name, robot_xy, current_dir)
            
        elif "BACK " in input_command.upper():
            steps_back = input_command.upper().strip("BACK ")
            new_robot_xy = move_robot((-1)*int(steps_back), robot_xy, current_dir)

            safe_zone = is_robot_in_safe_zone(robot_name, new_robot_xy, robot_xy)
            if safe_zone == True:
                backward_command(robot_name, steps_back, new_robot_xy)
                get_command(robot_name, new_robot_xy, current_dir)
            else:
                get_command(robot_name, robot_xy, current_dir)

        elif input_command.upper() in "RIGHT":
            right_command(robot_name, robot_xy)
            if current_dir in(270,180,90):
                #right_command(robot_name, robot_xy)
                get_command(robot_name, robot_xy, current_dir -90)
            else:
                get_command(robot_name, robot_xy, 270)
        elif input_command.upper() in "LEFT":
            left_command(robot_name, robot_xy)
            if current_dir in(0,90,180):
                #left_command(robot_name, robot_xy)
                get_command(robot_name, robot_xy, current_dir +90)
            else:
                get_command(robot_name, robot_xy, 0)
        elif "SPRINT " in input_command.upper():
            steps_sprint = input_command.upper().strip("SPRINT ")
            total_steps_sprint = sprint_robot(int(steps_sprint))
            new_robot_xy = move_robot(int(total_steps_sprint), robot_xy, current_dir)
            safe_zone = is_robot_in_safe_zone(robot_name, new_robot_xy, robot_xy)
            if safe_zone == True:
                sprint_command(robot_name, int(steps_sprint), new_robot_xy)
                get_command(robot_name, new_robot_xy, current_dir)
            else:
                get_command(robot_name, robot_xy, current_dir)
    else:
        print(robot_name + ": Sorry, I did not understand '" + input_command.capitalize() + "'." )
        get_command(robot_name, robot_xy, current_dir)

def get_robot_name():
    """
    Gets input from user: name of robot
    """
    robot_name = input("What do you want to name your robot? ")
    print(robot_name.upper() + ": Hello kiddo!")
    return robot_name.upper()

def robot_start():
    """This is the entry function, do not change"""
    robot_name = get_robot_name()
    get_command(robot_name, (0,0), 90)
    pass


if __name__ == "__main__":
    robot_start()