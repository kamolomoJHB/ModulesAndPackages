

# TODO: Decompose into functions
def print_shapes(size, degrees):
    print("* Move Forward "+str(size))
    print("* Turn Right "+str(degrees)+" degrees")

def move_square(width):
    print("Moving in a square of size "+str(width))
    for i in range(4):
        print_shapes(width, 90)

def move_rectangle(length, width):
    print("Moving in a rectangle of "+str(length)+" by "+str(width))
    for i in range(2):
        degrees = 90
        print_shapes(length,90)
        print_shapes(width,90)

def move_circle(length, degrees):
    print("Moving in a circle")
    for i in range(360):
        print_shapes(length,degrees)

def move_square_dancing(length):
    print("Square dancing - 3 squares of size 20")
    for i in range(3):
        print("* Move Forward "+str(length))
        move_square(20)

def move_crop_circles(length, degrees):
    print("Crop circles - 4 circles")
    for i in range(4):
        print("* Move Forward "+str(length))
        move_circle(1,1)

def move(): 
    '''
        >>>robot_move()
        >>>It is descriptive of the robot making movements. Clear, short and simple.
    '''
    width = 10
    move_square(width)

    length = 20
    move_rectangle(length, width)

    degrees = 1
    length = 1
    move_circle(length, degrees)

    length = 20
    move_square_dancing(length)

    move_crop_circles(length, degrees)

def robot_start():
    move()

if __name__ == "__main__":
    robot_start()
