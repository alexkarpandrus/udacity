#!/usr/bin/env python
# game.py - simple game to demonstrate classes and objects
from classes import *

DIRECTIONS = {
    "r": "right",
    "l": "left",
    "d": "down",
    "u": "up"
}

if __name__ == '__main__':

    print """Welcome to 'Hello, Class' game
    Available commands are:
    r - move right
    l - move left
    u - move up
    d - move down
    a - attack
    gps - print location
    x - exit

    There is a Bug 2 steps to the right from you.
    You should probably do something about it!
    """

    # initializing some entities

    #campus = World(100, 100)
    student = Player(10, 10)
    engineer1 = Wizard(35, 13)
    engeneer2 = Wizard(15,21)
    bug1 = Enemy(15, 10)
    bug2 = Enemy(13, 10)
    fountains = Fountains((random.randint(1,world.width-1)), (random.randint(1,world.height-1)), (random.randint(1,10)))

    statusbar.set_character(student)
    world.print_map()

    while True:
        c = raw_input("You > ")

        if c == "x":
            break
        elif c in DIRECTIONS:
            student.move(DIRECTIONS[c])
            bug1.act(student, DIRECTIONS)
        elif c == "gps":
            statusbar.set_status("Your GPS location: %i %i" % (student.x, student.y))
            statusbar.set_status("Bug GPS location: %i %i" % (bug1.x, bug1.y))
        elif c == "a":
            enemies = student.get_alive_enemies(1)
            if enemies:
                student.attack(enemies[0])
                enemies[0].act(student, DIRECTIONS)
        else:
            statusbar.set_status("Unknown command. 'x' to exit game")

        statusbar.show()
        world.print_map()


