# TODO : Set opp en dobbel array med 1-8 og A-H. En annen array som inneholder bom fra motspiller
import copy

from Tile import Tile
import array

global Tiles_in_Map


def battleships_Map_Setup():
    global Tiles_in_Map
    dim1, dim2 = (8, 8)
    Tiles_in_Map = [[0 for i in range(dim1)] for j in range(dim2)]
    for x in range(dim1):
        for y in range(dim2):
            Tiles_in_Map[x][y] = Tile(x + 1, determine_Letter(y))
    # for x in range(dim1):
    #    for y in range(dim2):
    #      print(str(Tiles_in_Map[x][y].get_x_pos()) + str(Tiles_in_Map[x][y].get_y_pos()))

    setup_Ships(1)
    setup_Ships(2)
    setup_Ships(3)


def setup_Ships(length):
    list_put_ship = compute_position()
    possible_directions = compute_position_based_on_length(length, list_put_ship)


def compute_position():
    put_ship = input()
    put_ship = put_ship.upper()
    put_ship = put_ship.replace(" ", "")
    if len(put_ship) != 2:
        print("Feil lengde")
    if put_ship[0].isdigit():
        print("Første ting er tall")
    else:
        put_ship = put_ship[::-1]
    print(put_ship)
    list_put_ship = list(put_ship)
    list_put_ship[0] = int(list_put_ship[0])
    list_put_ship[1] = determine_Number(list_put_ship[1])
    return list_put_ship


def compute_east(length, east_position):
    east_position[0] = east_position[0] + length
    return east_position


def compute_west(length, west_position):
    west_position[0] = west_position[0] - length
    return west_position


def compute_north(length, north_position):
    north_position[1] = north_position[1] + length
    return north_position


def compute_south(length, south_position):
    south_position[1] = south_position[1] - length
    return south_position


def remove_illegal_placements(possible_directions):
    nr_to_remove = []
    for x in range(len(possible_directions)):
        if possible_directions[x][0] <= 0 or possible_directions[x][1] <= 0:
            nr_to_remove.append(copy.deepcopy(possible_directions[x]))

    for y in range(len(nr_to_remove)):
        print(nr_to_remove[y])


def compute_position_based_on_length(length, list_put_ship):
    possible_directions = [compute_east(length, copy.deepcopy(list_put_ship)),
                           compute_west(length, copy.deepcopy(list_put_ship)),
                           compute_north(length, copy.deepcopy(list_put_ship)),
                           compute_south(length, copy.deepcopy(list_put_ship))]
    remove_illegal_placements(possible_directions)
    print(possible_directions)
    return possible_directions


def determine_Letter(number_letter):
    if number_letter == 0:
        return "A"
    elif number_letter == 1:
        return "B"
    elif number_letter == 2:
        return "C"
    elif number_letter == 3:
        return "D"
    elif number_letter == 4:
        return "E"
    elif number_letter == 5:
        return "F"
    elif number_letter == 6:
        return "G"
    elif number_letter == 7:
        return "H"


def determine_Number(letter_number):
    if letter_number == "A":
        return 1
    elif letter_number == "B":
        return 2
    elif letter_number == "C":
        return 3
    elif letter_number == "D":
        return 4
    elif letter_number == "E":
        return 5
    elif letter_number == "F":
        return 6
    elif letter_number == "G":
        return 7
    elif letter_number == "H":
        return 8
