class Mars(object):
    """
    Mars! Normally an spheroid, but today, Mars is represented as a
    euclidean plane composed of integer grid locations.
    Fun Mars Fact: In the next 20-40mil years, Mars will develop a ring.
    """
    def __init__(self, max_x, max_y):
        self.max_x = max_x
        self.max_y = max_y
        self.min_x, self.min_y = 0, 0
        self.scented_locations = []

    def location_exists(self, x, y):
        """
        Checks whether a coordinate pair exists in this instance.
        :param x: x coordinate to check
        :param y: y coordinate to check
        :return: True if location exists, else false
        """
        return self.max_x >= x >= 0 and self.max_y >= y >= 0

    def location_is_scented(self, x, y):
        """
        Checks whether a location has has been 'scented' by doomed robot
        :param x: x coordinate to check
        :param y: y coordinate to check
        :return: True if scented, else false
        """
        return [x, y] in self.scented_locations

    def add_scented_location(self, x, y):
        """
        Denotes an area as 'scented' by adding it the scented areas list
        :param x: x coordinate to add
        :param y: y coordinate to add
        """
        self.scented_locations.append([x, y])
