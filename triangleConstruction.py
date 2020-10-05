import math

height = input(" Height : ")
height = int(height)

# calculate base's length
length = (2 * height) - 1

print(" Length : " + str(length))

# concept : each layer contains white spaces and stars
#           # of white spaces + # of stars = base's length

# iterate through layers

positions = []
# define as None because it has no data available now
position_center = None
position_left = None
position_right = None

for layer in range(0, height):
    # on the top of trigatle
    # find position of a star in the top of triangle 
    # It will be at the center of the base

    # define a variable to record center position of the top layer
    # which is important for calculating the postions of stars in
    # the next layer

    # top layer
    if (layer == 0) :     
        positions_in_layer = []
        marked_position = math.ceil(length / 2)
        print(" => Layer " + str(layer + 1) + " from the top : star's position = " + str(marked_position))
        position_counter = 0
        while(position_counter < length):
            if(position_counter == (marked_position - 1)):
                positions_in_layer.extend("*")
            else:
                positions_in_layer.extend(" ")
            position_counter += 1
        
        position_center = marked_position
        print(positions_in_layer)

        positions.append(positions_in_layer)

        position_left = position_center - 1
        position_right = position_center + 1

    # base layer
    elif (layer == (height - 1)):
        positions_in_layer = []
        print(" => Layer " + str(layer + 1) + " from top : Base layer")

        position_counter = 0
        while(position_counter < length):
            positions_in_layer.extend("*")
            position_counter += 1
        print(positions_in_layer)

        positions.append(positions_in_layer)

    # other layers
    else:
        # we need to know 2 positions which are left and right positions
        # concept : position will be shifted to the left and right by 1 from the upper layer
        # position_left = position_center - 1
        # position_right = position_center + 1
        print(" => Layer " + str(layer + 1) + " from top : stars' positions : left = " + str(position_left) + " right = " + str(position_right))

        positions_in_layer = []
        position_counter = 0

        while(position_counter < length):
            if(position_counter == (position_left - 1)) or (position_counter == (position_right - 1)):
                positions_in_layer.extend("*")
            else:
                positions_in_layer.extend(" ")
            position_counter += 1
        print(positions_in_layer)
        positions.append(positions_in_layer)

        position_left -= 1
        position_right += 1










