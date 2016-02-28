class Robot(object):
    """
    Contains the spatial state of the robot as it bravely around mars,
    as well as methods to update those states.
    Fun Rover Fact: Curiousity carries 12 million people's names in a chip on its 'back'.
    """
    def __init__(self, initial_x, initial_y, initial_orientation, movement_instructions):
        self.current_x = initial_x
        self.current_y = initial_y
        self.current_orientation = initial_orientation
        self.movement_instructions = movement_instructions

    def move_forward(self):
        """
        Moves our intrepid little rover forward 1 coordinate
        :return: Updated x, y coordinates of rover
        """
        # In most languages, this would likely be a switch
        # statement, but python has chosen not to include one
        # due to its "one and only one way of doing something" philosophy
        if self.current_orientation == 'N':
            self.current_y += 1
        if self.current_orientation == 'E':
            self.current_x += 1
        if self.current_orientation == 'S':
            self.current_y -= 1
        if self.current_orientation == 'W':
            self.current_x -= 1
        return self.current_x, self.current_y

    def turn(self, direction):
        """
        Lets turn the rover! The rover can be on one of four compass
        orientations, and turning left or right can be thought of as going
        left or right on a clock. Therefore if you go left from E, you get N,
        and if you 'overflow' on either side, you simply wrap round, e.g.
        right from W would return to N
        :param direction - The direction, 'L' or 'R', we'd like to turn
        :return: Updated orientation
        """
        orientations = ('N', 'E', 'S', 'W')
        current_orientation_index = orientations.index(self.current_orientation)

        if direction == 'L':
            current_orientation_index -= 1
            if current_orientation_index < 0:
                current_orientation_index += 4
        if direction == 'R':
            current_orientation_index += 1
            if current_orientation_index > 3:
                current_orientation_index -= 4

        self.current_orientation = orientations[current_orientation_index]
        return self.current_orientation
