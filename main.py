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


def compute_list(concert_premiere_length, tracks_list):
    total_length = 0
    result = []
    # To answer to the first bonus quesiton, change the following line (for loop) to the following ones,
    # fix the "strict" parameter in filter_list to False,
    # and indent the "valid_combination" assignment line.

    # valid_combination = False
    # x = 0
    # while not valid_combination:
    #     x += 1
    for x in range(3):
        print("XXXXX ROUND {} XXXXX".format(x + 1))
        tracks_list = filter_list(tracks_list, concert_premiere_length - total_length, strict=x < 2)
        if len(tracks_list) == 0:
            print("No tracks available for the premiere.")
            return False, result
        higher_key = list(tracks_list.keys())[0]
        total_length += tracks_list[higher_key]
        result.append(higher_key)

        print()
        print("The highest track is {} with a length of {}".format(higher_key, tracks_list[higher_key]))
        del tracks_list[higher_key]
        print("The remaining tracks are: {}".format(tracks_list))
        print("The total length of the tracks is {}".format(total_length))
        print()
    valid_combination = concert_premiere_length - SET_LENGTH_TOLERANCE <= total_length <= concert_premiere_length + SET_LENGTH_TOLERANCE
    return valid_combination, result


def main():
    """
    Main function.
    :return: A boolean indicating if a valid combination was found.
    """
    concert_premiere_length = int(input("How long is the concert premiere? "))
    tracks_list = sort_list(INPUT_LIST)
    execute = True
    while execute and len(tracks_list) > 2:
        print()
        print()
        print()
        print("-----> The tracks available are: {}".format(tracks_list))

        possible, result = compute_list(concert_premiere_length, tracks_list)
        if possible:
            print("The tracks are: {}".format(result))
            return True
        tracks_list.pop(list(tracks_list.keys())[0])
    return False


if __name__ == '__main__':
    print(main())
