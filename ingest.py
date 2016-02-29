import sys


def ingest_from_file(file_path):
    """
    Attemps to open a file, read its contents, valid what it finds
    and finally decodes this into friendly python data structures.
    :param file_path - Expected location of the compatible txt file.
    :return: Tuple of dictionaries containing maximum grid coordinates
        and instructions relating to each brave little rover.
    """
    try:
        with open(file_path) as f:
            instructions = f.read().splitlines()
    except (IOError, OSError):
        sys.exit('Instructions text file could not be opened! '
                 'Please ensure an instructions.txt file is available in the '
                 'project root and sufficient permissions are given.')

    # Get the maximum x and y of the Mars plane
    maximum_coordinates = extract_coordinates(instructions.pop(0))

    # Get each robot's life goal
    robots_instructions = extract_robots_instructions(instructions)

    return maximum_coordinates, robots_instructions


def extract_coordinates(coordinates_line):
    """
    Extracts the maximum x and y coordinates from a single string
    of an x and y coordinate separated by a space. The coordinate
    values must be a positice integer and cannot exceed 50
    """
    try:
        coordinates = [int(coordinate) for coordinate in coordinates_line.split(' ')]
    except ValueError:
        sys.exit('Maximum coordinates could not be interepreted as an integer!'
                 'Please check, remove any coordinate emoji, and try again.')

    # Ensure none of the coordinates exceed 50, or are negative
    if not all(0 <= coord <= 50 for coord in coordinates):
        sys.exit('Coordinates have a range of 0 to 50, '
                 'please double check your instructions and try again!')

    return {'max_x': coordinates[0],
            'max_y': coordinates[1]}


def extract_robots_instructions(instructions_lines):
    """
    Extracts n robots' initial position and movement instructions
    from multiple string lines.
    """
    robots_instruction_lines = [
        (instructions_lines[line_number], instructions_lines[line_number+1])
        for line_number
        in range(0, len(instructions_lines), 3)
    ]

    # Ensure no movement instruction set exceeds 100 moves
    if any(len(ri[1]) >= 100 for ri in robots_instruction_lines):
        sys.exit('Unfortunately you cannot have more than 100 moves per robot! '
                 'Please upgrade to Mars Robot Pro for unlimited robot moves.')

    return [_package_robot_instructions(robot_instruction_lines)
            for robot_instruction_lines
            in robots_instruction_lines]


def _package_robot_instructions(instruction_lines):
    """
    Packages two strings representing a robot's initial poin and
    movement into a friendly data structure.
    :param instruction_lines - Two string lines, initial point and
        movement instructions
    :returns: Dictionary of friendly properties describing initial point
        and movement instructions
    """
    initial_point = instruction_lines[0].split(' ')
    return {
        'initial_x': int(initial_point[0]),
        'initial_y': int(initial_point[1]),
        'initial_orientation': initial_point[2],
        'movement_instructions': instruction_lines[1],
    }
