"""
NAME: Michael Schroeder
DATE: 1/29/2026
CLASS: 1051
SECTION: N/A

"""

# TODO: Fix frog string
"    __   ___.--'_`."
"   ( _`.'. -   'o` )"
"   _\\.'_'      _.-'"
"  ( \\`. )    //\\`"
"   \\_`-'`---'\\__,"
"    \\`        `-\\"

# TODO: Fix sheep string
"         __  _"
"     .-:'  `; `-._"
"    (_,           )"
"  ,'o\"(            )>"
" (__,-'            )"
"    (             )"
"     `-'._.--._.-'"
"        |||  |||"


def frog(): # TODO: implement frog()
    """
    Returns ASCII art of a frog

    Parameters:
        None
    
    Returns:
        String representing ASCII art of a frog
    """

    frog_string = (
    "    __   ___.--'_`.\n"
    "   ( _`.'. -   'o` )\n"
    "   _\\.'_'      _.-'\n"
    "  ( \\`. )    //\\`\n"
    "   \\_`-'`---'\\__,\n"
    "    \\`        `-\\\n"
    )
    return frog_string

def sheep():  # TODO: implement sheep()    
    """
    Returns ASCII art of a sheep

    Parameters:
        None
    
    Returns:
        String representing ASCII art of a sheep
    """

    sheep_string = (
    "         __  _\n"
    "     .-:'  `; `-._\n"
    "    (_,           )\n"
    "  ,'o\"(            )>\n"
    " (__,-'            )\n"
    "    (             )\n"
    "     `-'._.--._.-'\n"
    "        |||  |||\n"
    )
    return sheep_string

def cow(): # This function is already implemented!
    """
    Returns ASCII art of a cow
    
    Parameters:
        None
    
    Returns:
        String representing ASCII art of a cow
    """

    cow_string = (
        "           __n__n__\n"
        "    .------`-\\00/-'\n"
        "   /  ##  ## (oo)\n"
        "  / \\## __   ./\n"
        "     |//YY \\|/\n"
        "     |||   |||\n"     
    ) 
    return cow_string
    
# This function is already implemented!
def animal_n_times(func, n):
    """
    Returns a string animal ASCII art n number of times
        Example: with a horse() function, animal_n_times(horse, 3) would return a string of 3 horses.
    
    Args:
        func: function which returns animal ASCII art
        n: integer which is the amount of ASCII art to return
        
    Returns:
        String containing the amount of ASCII art specified by n
    """
    return func * n

def farm(num_cows, num_frogs, num_sheep):
    cow_strings = animal_n_times(cow(), num_cows)
    frog_strings = animal_n_times(frog(), num_frogs)
    sheep_strings = animal_n_times(sheep(), num_sheep)
    total = cow_strings + frog_strings + sheep_strings
    return total

if __name__ == "__main__":
    print("-------- Welcome to the Ransom Farm! --------\n")
    print("Below is our comprehensive assortment of animals:\n")
    print(cow())
   
    #TODO: print frog and sheep
    print(frog())
    print(sheep())

    #TODO: Take input from the user
    print("Ol' farmer Ransom has a lot of animals!") 
    print("How many cows would you like to see? ")
    num_cows = int(input())
    print("How many frogs would you like to see? ")
    num_frogs = int(input())
    print("How many sheep would you like to see? ")
    num_sheep = int(input())
   
    #TODO: place farm here

    print(farm(num_cows, num_frogs, num_sheep))
    print("Thanks for stopping by the Ransom Farm! Come back soon!")
    
