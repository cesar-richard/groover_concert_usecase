INPUT_LIST = dict(stairway_to_heaven=8, una_mattina=4, track1=1, track2=2, track3=3, track4=4, track5=5, track6=6,
                  track7=7, track8=8, track9=9)
SET_LENGTH_TOLERANCE = 5  # Bonus: set tolerence for set length


def filter_list(tracks_list, goal_length, strict=True):
    """
    Filter the list of tracks to only those that are under a max length.
    :param strict: should the list be filtered to only those tracks that are exactly the goal length?
    :param tracks_list: list of tracks
    :param goal_length: Length limit
    :return: A new list of tracks that are under the length limit
    """
    if strict:
        return {k: v for k, v in tracks_list.items() if v < goal_length + SET_LENGTH_TOLERANCE}
    return {k: v for k, v in tracks_list.items() if v <= goal_length + SET_LENGTH_TOLERANCE}


def sort_list(tracks_list):
    """
    Initialize the data structure for the tracks.
    :param tracks_list: list of tracks
    :return: A dictionary of tracks with their lengths
    """
    return dict(sorted(tracks_list.items(), key=lambda x: x[1], reverse=True))


def main():
    """
    Main function.
    :return: A boolean indicating if a valid combination was found.
    """
    concert_premiere_length = int(input("How long is the concert premiere? "))
    tracks_list = sort_list(INPUT_LIST)
    # TODO: Add the computation of the tracks


if __name__ == '__main__':
    print(main())
