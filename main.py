from ingest import ingest_from_file
from mars import Mars
from robot import Robot


def deploy_robots(mars, robots):
    """
    Deploys the robots onto their adventure.
    Robots attempt to carry out their orders in sequence
    :param mars - The euclidean surface with edges the robots traverse
    :param robots - List of robots we'll attempt to fulfil the instructions of
    :return: All robots after instructions carried out
    """
    for robot in robots:
        # No point instructing those poor, doomed robots
        if robot.is_lost:
            continue

        # Carry out each instruction sequentially
        for instruction in robot.movement_instructions:
            _do_instruction(robot, mars, instruction)

    return robots


def _do_instruction(robot, mars, instruction):
    """
    Attempts to carry out the instruction given on the current
    robot with the current state of Mars, which can mutate to give
    different results for later robots
    :param robot - The robot we're currently carrying out instructions on
    :param mars - The Mars euclidean plane we're acting in
    :param instruction - The instruction we will attempt to execute
    :return: Robot and Mars, updated as a necessary as a result of instruction
    """
    # Separate out the available actions
    turn_instructions = ('L', 'R')
    move_instructions = ('F')

    if instruction in turn_instructions:
        robot.turn(instruction)

    if instruction in move_instructions:
        # For now we assume we only go forwards but we could pass the
        # instruction to enable backwards, hop, or other fantastic abilities
        robot, mars = _move_robot(robot, mars)

    return robot, mars


def _move_robot(robot, mars):
    """
    Attempts to move the robot forward. Attempts to move the
    rover one step forward. If the rover goes to move off the edge
    and there isn't a scent left by a martyr rover before it, it will
    lurch into the abyss and be LOST. If the rover is about to move into
    the abyss but has a scent to warn it, it will double check that the
    abyss isn't coming up, and if it is, it will ignore the current instruction
    Otherwise, it will move forward as expected
    """
    start_x, start_y = robot.current_x, robot.current_y
    finish_x, finish_y = robot.look_forward()
    forward_exists = mars.location_exists(finish_x, finish_y)
    in_scented_tile = mars.location_is_scented(start_x, start_y)

    if not forward_exists and in_scented_tile:
        return robot, mars

    if not forward_exists:
        mars.add_scented_location(start_x, start_y)
        robot.move_forward()
        robot.is_lost = True
        return robot, mars

    robot.move_forward()
    return robot, mars


def _display_results(robots):
    """
    A utility method that nicely formats and prints state of robots
    :param robots - The robots we want to display
    """
    for robot in robots:
        result = "{0} {1} {2} {3}".format(
            robot.current_x,
            robot.current_y,
            robot.current_orientation,
            "LOST" if robot.is_lost else '',
            )

        print result

if __name__ == '__main__':
    max_coordinates, robots_config = ingest_from_file('instructions.txt')
    mars = Mars(**max_coordinates)
    robots = [Robot(**robot_config) for robot_config in robots_config]

    deployed_robots = deploy_robots(mars=mars, robots=robots)
    _display_results(robots=deployed_robots)
