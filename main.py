from ingest import ingest_from_file


def deploy_robots(mars, robots):
    """
    Deploys the robots onto their adventure.
    Robots attempt to carry out their orders in sequence
    :param mars - The euclidean surface with edges the robots traverse
    :param robots - List of robots we'll attempt to fulfil the instructions of
    :returns: The final position of all given robots.
    """
    pass

if __name__ == '__main__':
    max_coordinates, robots_config = ingest_from_file('instructions.txt')
