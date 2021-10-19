# Author: <Kelvin Delarosa>
# Assignment #6 - Battleship
# Date due: 2020-12-04
# I pledge that I have completed this assignment without
# collaborating with anyone else, in conformance with the
# NYU School of Engineering Policies and Procedures on
# Academic Misconduct.

import random

### DO NOT EDIT BELOW (with the exception of MAX_MISSES) ###

HIT_CHAR = 'x'
MISS_CHAR = 'o'
BLANK_CHAR = '.'
HORIZONTAL = 'h'
VERTICAL = 'v'
MAX_MISSES = 20
SHIP_SIZES = {
    "carrier": 5,
    "battleship": 4,
    "cruiser": 3,
    "submarine": 3,
    "destroyer": 2
}
NUM_ROWS = 10
NUM_COLS = 10
ROW_IDX = 0
COL_IDX = 1
MIN_ROW_LABEL = 'A'
MAX_ROW_LABEL = 'J'


def get_random_position():
    """Generates a random location on a board of NUM_ROWS x NUM_COLS."""

    row_choice = chr(
                    random.choice(
                        range(
                            ord(MIN_ROW_LABEL),
                            ord(MIN_ROW_LABEL) + NUM_ROWS
                        )
                    )
    )

    col_choice = random.randint(0, NUM_COLS - 1)

    return (row_choice, col_choice)


def play_battleship():
    """Controls flow of Battleship games including display of
    welcome and goodbye messages.

    :return: None
    """

    print("Let's Play Battleship!\n")

    game_over = False

    while not game_over:

        game = Game()
        game.display_board()

        while not game.is_complete():
            pos = game.get_guess()
            result = game.check_guess(pos)
            game.update_game(result, pos)
            game.display_board()

        game_over = end_program()

    print("Goodbye.")

### DO NOT EDIT ABOVE (with the exception of MAX_MISSES) ###



class Ship:

    def __init__(self, name, start_position, orientation):
        """Creates a new ship with the given name, placed at start_position in the
        provided orientation. The number of positions occupied by the ship is determined
        by looking up the name in the SHIP_SIZE dictionary.

        :param name: the name of the ship
        :param start_position: tuple representing the starting position of ship on the board
        :param orientation: the orientation of the ship ('v' - vertical, 'h' - horizontal)
        :return: None
        """
        self.name = name

        self.sunk = False


        self.positions= {}
        starting_row = start_position[ROW_IDX]
        starting_column = start_position[COL_IDX]


        positions_occupied = SHIP_SIZES[name]
        if orientation == VERTICAL:
            for i in range(positions_occupied):
                self.positions[(chr((ord(starting_row)+i)), starting_column)] = False

        if orientation == HORIZONTAL:
            for i in range(positions_occupied):
                self.positions[((starting_row), (starting_column + i) )] = False









class Game:

    ########## DO NOT EDIT #########
    
    _ship_types = ["carrier", "battleship", "cruiser", "submarine", "destroyer"]

    def __init__(self, max_misses = MAX_MISSES):
        """ Creates a new game with max_misses possible missed guesses.
        The board is initialized in this function and ships are randomly
        placed on the board.

        :param max_misses: maximum number of misses allowed before game ends
        """

        self.ships = []
        self.guesses = []
        self.max_misses = MAX_MISSES
        self.board = {}
        self.initialize_board()
        self.create_and_place_ships()


    def initialize_board(self):
        """Sets the board to it's initial state with each position occupied by
        a period ('.') string.

        :return: None
        """

        for spot in range(ord(MIN_ROW_LABEL), ord(MAX_ROW_LABEL)+1):
            self.board[chr(spot)] = [BLANK_CHAR] * 10


    def display_board(self):
        """ Displays the current state of the board."""

        print()
        print("  " + ' '.join('{}'.format(i) for i in range(len(self.board))))
        for row_label in self.board.keys():
            print('{} '.format(row_label) + ' '.join(self.board[row_label]))
        print()

    def in_bounds(self, start_position, ship_size, orientation):
        """Checks that a ship requiring ship_size positions can be placed at start position.

        :param start_position: tuple representing the starting position of ship on the board
        :param ship_size: number of positions needed to place ship
        :param orientation: the orientation of the ship ('v' - vertical, 'h' - horizontal)
        :return status: True if ship placement inside board boundary, False otherwise
        """
        row = start_position[ROW_IDX]
        column = start_position[COL_IDX]

        if orientation == HORIZONTAL:
            for pos in range(column, column + ship_size):
                column = pos
            if column >= NUM_COLS:
                return False
            else:
                return True

        if orientation == VERTICAL:
            for pos in range(ord(row), ord(row) + ship_size):
                row = chr(pos)
            if ord(row) > ord(MAX_ROW_LABEL):
                return False
            else:
                return True


    def overlaps_ship(self, start_position, ship_size, orientation):
        """Checks for overlap between previously placed ships and a potential new ship
        placement requiring ship_size positions beginning at start_position in the
        given orientation.

        :param start_position: tuple representing the starting position of ship on the board
        :param ship_size: number of positions needed to place ship
        :param orientation: the orientation of the ship ('v' - vertical, 'h' - horizontal)
        :return status: True if ship placement overlaps previously placed ship, False otherwise
        """


        row = start_position[ROW_IDX]
        column = start_position[COL_IDX]

        if orientation == VERTICAL:
            test_range = range(ord(row), ord(row) + ship_size)
            for coordinate in test_range:
                position = (chr(coordinate), column)
                for ship in self.ships:
                    if position in ship.positions:
                        return True

        elif orientation == HORIZONTAL:
            test_range = range(column, column + ship_size)
            for coordinate in test_range:
                position = (row, coordinate)
                for ship in self.ships:
                    if position in ship.positions:
                        return True

        return False

    def place_ship(self, start_position, ship_size):
        """Determines if placement is possible for ship requiring ship_size positions placed at
        start_position. Returns the orientation where placement is possible or None if no placement
        in either orientation is possible.

        :param start_position: tuple representing the starting position of ship on the board
        :param ship_size: number of positions needed to place ship
        :return orientation: 'h' if horizontal placement possible, 'v' if vertical placement possible,
            None if no placement possible
        """
        if self.in_bounds(start_position, ship_size, VERTICAL) and not self.overlaps_ship(start_position, ship_size, VERTICAL):
            return "v"

        elif self.in_bounds(start_position, ship_size, HORIZONTAL) and not self.overlaps_ship(start_position, ship_size, HORIZONTAL):
            return "h"

        else:
            return None

    def create_and_place_ships(self):
        """Instantiates ship objects with valid board placements.

        :return: None
        """

        for ship in SHIP_SIZES.keys():
            start_point = get_random_position()
            possible_posititon = self.place_ship(start_point, SHIP_SIZES[ship])
            while possible_posititon == None:
                start_point = get_random_position()
                possible_posititon = self.place_ship(start_point, SHIP_SIZES[ship])

            self.ships.append(Ship(ship, start_point, possible_posititon))

    def get_guess(self):
        """Prompts the user for a row and column to attack. The
        return value is a board position in (row, column) format

        :return position: a board position as a (row, column) tuple
        """
        row_response = input("Enter a row: ")
        while ord(row_response) not in range(ord(MIN_ROW_LABEL), ord(MAX_ROW_LABEL) + 1):
            row_response = input("Enter a row: ")

        col_response = int(input("Enter a column: "))
        while col_response not in range(0, NUM_COLS):
            col_response = int(input("Enter a column: "))

        board_position = (row_response, col_response)

        return board_position

    def check_guess(self, position):
        """Checks whether or not position is occupied by a ship. A hit is
        registered when position occupied by a ship and position not hit
        previously. A miss occurs otherwise.

        :param position: a (row,column) tuple guessed by user
        :return: guess_status: True when guess results in hit, False when guess results in miss
        """
        sunk_status = True
        for ship in self.ships:
            if position in ship.positions and ship.positions[position] == False:
                ship.positions[position] = True
                for pos in ship.positions:
                   if ship.positions[pos] == False:
                        sunk_status = False
                if sunk_status:
                    ship.sunk = True
                    print("You sunk the {}!".format(ship.name))
                return True

        return False

    def update_game(self, guess_status, position):
        """Updates the game by modifying the board with a hit or miss
        symbol based on guess_status of position.

        :param guess_status: True when position is a hit, False otherwise
        :param position:  a (row,column) tuple guessed by user
        :return: None
        """
        if guess_status:
            self.board[position[ROW_IDX]][position[COL_IDX]] = HIT_CHAR

        else:
            self.guesses.append(position)
            if self.board[position[ROW_IDX]][position[COL_IDX]] == BLANK_CHAR:
                self.board[position[ROW_IDX]][position[COL_IDX]] = MISS_CHAR

    def is_complete(self):
        """Checks to see if a Battleship game has ended. Returns True when the game is complete
        with a message indicating whether the game ended due to successfully sinking all ships
        or reaching the maximum number of guesses. Returns False when the game is not
        complete.

        :return: True on game completion, False otherwise
        """
        ship_status = True
        for ship in self.ships:
            if not ship.sunk:
                ship_status = False

        if ship_status == True:
            print("YOU WIN!")
            return True
        elif len(self.guesses) >= MAX_MISSES:
            print("SORRY! NO GUESSES LEFT.")
            return True

        else:
            return False


    ########## DO NOT EDIT #########


def end_program():
    """Prompts the user with "Play again (Y/N)?" The question is repeated
    until the user enters a valid response (Y/y/N/n). The function returns
    False if the user enters 'Y' or 'y' and returns True if the user enters
    'N' or 'n'.

    :return response: boolean indicating whether to end the program
    """
    usr_response = input("Play again (Y/N)?")
    while usr_response not in ("Y","y","N","n"):
        usr_response = input("Play again (Y/N)?")

    if usr_response == "Y" or usr_response == "y":
        return False

    if usr_response == "N" or usr_response == "n":
       return True





def main():
    """Executes one or more games of Battleship."""

    play_battleship()
    ship = Ship("carrier", ('B', 3), 'v')
    print(ship.positions)




if __name__ == "__main__":
    main()
