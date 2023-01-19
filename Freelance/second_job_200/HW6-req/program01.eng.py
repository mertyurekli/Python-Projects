#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
You have just been hired at a video game software house, and you have
to render the snake game on an image by saving the final image of the
snake's path and returning the length of the snake.
Implement the generate_snake function that takes as input a path to an
image file, which is the starting image "start_img". The image can
contain black background pixels, obstacle for the snake as red pixels
and finally food as orange pixels. The snake must be drawn in green.
In addition, you must draw in gray the trail that the snake leaves onto
its path. The function also takes as input the initial snake position,
"position" as a list of two integers X and Y. The commands of the
player on how to move the snake in the video game are available in a
string "commands."  The function must save the final image of the
snake's path to the path "out_img," which is passed as the last input
argument to the function. In addition, the function must return the
length of the snake at the end of the game.

Each command in "commands" corresponds to a cardinal sign, followed by
a space. The possible cardinal signs are:

| NW | N | NE |
| W  |   |  E |
| SW | S | SE |

corresponding to one-pixel snake movements such as:

| up-left     | up     | up-right     |
| left        |        | right        |
| bottom-left | bottom | bottom-right |

The snake moves according to the commands; in the case the snake
eats food, it increases its size by one pixel.

The snake can move from side to side of the image, horizontally and
vertically, this means that if the snake crosses a side of the image,
it will appear again from the opposite side.
The game ends when the commands are over or the snake dies. The snake
dies when:
- it hits an obstacle
- it hits itself, so it cannot pass over itself
- crosses itself diagonally. As an examples, a 1->2->3->4 path like the
  one below on the left is not allowed; while the one on the right is
  OK.

  NOT OK - diagonal cross        OK - not a diagonal cross
       | 4 | 2 |                    | 1 | 2 |
       | 1 | 3 |                    | 4 | 3 |

For example, considering the test case data/input_00.json
the snake starts from "position": [12, 13] and receives the commands
 "commands": "S W S W W S W N N W N N N N N W N"
generates the image in visible in data/expected_end_00.png
and returns 5 since the snake is 5 pixels long at the
end of the game.

NOTE: Analyze the images to get the exact color values to use.

NOTE: do not import or use any other library except images.
"""

import images


def generate_snake(start_img, head_position, commands, out_img):
    snake_length = 1
    counter = 0

    # reverse head position
    head_position.reverse()
    trail_segments = [head_position]

    # split commands by space
    commands = commands.split()

    # bool to exit loop
    collision = False

    # constants
    food = (255, 128, 0)
    obstacle = (255, 0, 0)
    snake_segment = (0, 255, 0)
    snake_trail = (128, 128, 128)
    blank_pixel = (0, 0, 0)

    commands_dict = {
        'N': [-1, 0],
        'S': [1, 0],
        'E': [0, 1],
        'W': [0, -1],
        'NE': [-1, 1],
        'SE': [1, 1],
        'SW': [1, -1],
        'NW': [-1, -1],
    }
    # create image object
    image = images.load(start_img)

    for command in commands:
        head_position = [sum(x) for x in zip(head_position, commands_dict[command])]
        # Vertical
        if head_position[0] < 0:
            head_position[0] = len(image) - 1
        elif head_position[0] > len(image) - 1:
            head_position[0] = 0
        elif head_position[1] < 0:
            head_position[1] = len(image[0]) - 1
        if head_position[1] > len(image[0]) - 1:
            head_position[1] = 0
        trail_segments.append(head_position)
        # obstacle crash
        if image[head_position[0]][head_position[1]] == obstacle:
            print("Obstacle crash game over")
            trail_segments.remove(head_position)
            break

        # self crash
        if snake_length >= 2:
            for i in range(snake_length - 1):
                if trail_segments[i - snake_length] == trail_segments[-1]:
                    print("Self crash game over")
                    trail_segments.pop()
                    collision = True
                    break

            # diagonal crash
            for j in range(len(trail_segments)-3, len(trail_segments)-snake_length, -1):
                if command == 'NE':
                    if ((trail_segments[-2][0]-1, trail_segments[-2][1]) == (
                            trail_segments[j][0], trail_segments[j][1])):
                        for k in range(len(trail_segments)-3, len(trail_segments)-snake_length, -1):
                            if((trail_segments[-2][0], trail_segments[-2][1]+1) == (
                                    trail_segments[k][0], trail_segments[k][1])):
                                print("Diagonal crash game over")
                                trail_segments.pop()
                                collision = True
                                break
                elif command == 'NW':
                    if ((trail_segments[-2][0] - 1, trail_segments[-2][1]) == (
                            trail_segments[j][0], trail_segments[j][1])):
                        for k in range(len(trail_segments)-3, len(trail_segments)-snake_length, -1):
                            if((trail_segments[-2][0], trail_segments[-2][1]-1) == (
                                    trail_segments[k][0], trail_segments[k][1])):
                                print("Diagonal crash game over")
                                trail_segments.pop()
                                collision = True
                                break
                elif command == 'SE':
                    if ((trail_segments[-2][0] + 1, trail_segments[-2][1]) == (
                            trail_segments[j][0], trail_segments[j][1])):
                        for k in range(len(trail_segments)-3, len(trail_segments)-snake_length, -1):
                            if((trail_segments[-2][0], trail_segments[-2][1]+1) == (
                                    trail_segments[k][0], trail_segments[k][1])):
                                print("Diagonal crash game over")
                                trail_segments.pop()
                                collision = True
                                break
                elif command == 'SW':
                    if ((trail_segments[-2][0] + 1, trail_segments[-2][1]) == (
                            trail_segments[j][0], trail_segments[j][1])):
                        for k in range(len(trail_segments)-3, len(trail_segments)-snake_length,-1):
                            if((trail_segments[-2][0], trail_segments[-2][1]-1) == (
                                    trail_segments[k][0], trail_segments[k][1])):
                                print("Diagonal crash game over")
                                trail_segments.pop()
                                collision = True
                                break
            if collision:
                break

        if image[head_position[0]][head_position[1]] == food:
            image[head_position[0]][head_position[1]] = blank_pixel
            snake_length += 1

    for segment in trail_segments:
        if len(trail_segments) - counter <= snake_length:
            image[segment[0]][segment[1]] = snake_segment
        else:
            image[segment[0]][segment[1]] = snake_trail
        counter += 1

    images.save(image, out_img)

    return snake_length


generate_snake(start_img="./data/input_09.png", head_position=[39, 16],
               commands="SW SW SW SW SW SW SW SW SW SW SW SW SW SW SW SW SW SW SW SW SW SW SW SW SW SW SW SW SW SW SW SW SW SW SW SW SW SW SW SW SW SW SW SW SW SW SW SW SW SW SW SW SW SW SW SW SW SW SW SW SW SW SW SW SW SW SW SW NW NW NW NW NW NW NW NW NW NW NW NW NW NW NW NW NW NW NW NW NW NW NW NW NW NW NW NW NW NW NW NW NW NW NW NW NW NW NW NW NW NW NW NW NW NW NW NW NW NW NW NW NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE SE SE SE SE SE SE SE SE SE SE SE SE SE SE SE SE SE SE SE SE SE SE SE SE SE SE SE SE SE SE SE SE SE SE SE SE SE SE SE SE SE SE SE SE SE SE SE SE SE SE SE SE SE SE SE SE SE SE NE NE SE NE SE NE SE NE SE NE SE NE SE NE SE NE NE SE NE SE NE SE NE SE SE SE SE NE NE SE NE SE NE SE NE SE NE SE SE SE SE SE NE NE SE NE NE NE SE SE SE SE SW SW SW SW SW SW SW SW SW SW N N N SW N SW SW N SW N SW N SW N SW N SW N SW N SW SW SW N SW N SW SW N N N N SW N SW N SW N SW N N N N SW N SW N SW N SW N SW N SW N SW SW N SW N N N SW SW N SW SW SW SW SW SW SW SE SE SE SE SE SE SE SE SE SE NE NE NE NE NE NE NE N N N NW NW NW NW S NE NW S SW S E S NE E S NW SE NE SE SE NW S E SE E N SE S N NW E S SW NE S S S E W NE NE SE N W E S S S NE S S N S NW E SW S N NE NE N N NW SE S S SE E E S SE SW NW S SE E E NE SW NW E S S NE N N NE SE S SE NW W S S NE W NW N W S SE E S N SE S SE SE S S W N SE SW SE NW N E NE SE S SE SW N NW SE NW SW W NE W N S NW SE W S E SE NW N SE E NW W NW SW S S E W SE W NW N W SW S SE NE S S SW S SW N W S SE E NE S N SE S N NW S S S NE W S SE SE E NE E W S NE N SW S S NW S SE W E S NE E NE E SW SE W NW SW NW SE E W SE NE E SW SW E NW SE NE S NW SW W NE W E S N NE S E NE S SW S W NW W N NW SE SE E NE NE SE NE S NW W SE SE N S S NW W E NW S SW W NW W E NW S NE SE W W NW SW NE NW S NW NW SW SE SE N NE E SW N NW E SE SW NE SE NE W S NW NE NW S E S NW SE S S SE N NE N NE N W NE NE E SW NW E S S E S S NW SW N W SE S NE NE S N S E SE W NW S E NW SE S E SW SW N SW S NE NW N E SE S S S S E S S SW NW SE SW NW NW NW S E SW SE NE NE E SW W NE SE W SW S S S SW S S NE W S S SW W NW SW E N E NW W E SW SE SW NE SW SW SE E N", out_img="./output/output_end_00.png")
