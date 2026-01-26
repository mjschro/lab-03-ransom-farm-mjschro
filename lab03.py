# TODO: Something should go up here...

# TODO: Fix frog string
"    __   ___.--'_`."
"   ( _`.'. -   'o` )"
"   _\.'_'      _.-'"
"  ( \`. )    //\`"
"   \_`-'`---'\__,"
"    \`        `-\"

# TODO: Fix sheep string
"         __  _"
"     .-:'  `; `-._"
"    (_,           )"
"  ,'o"(            )>"
" (__,-'            )"
"    (             )"
"     `-'._.--._.-'"
"        |||  |||"


def frog(): # TODO: implement frog()
    pass

def sheep():  # TODO: implement sheep()    
    pass
    
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

if __name__ == "__main__":
   print("-------- Welcome to the Ransom Farm! --------\n")
   print("Below is our comprehensive assortment of animals:\n")
   print(cow())
   
   #TODO: print frog and sheep
   
   #TODO: Take input from the user
   # print("Ol' farmer Ransom has a lot of animals!") 
   # print("How many cows would you like to see? ")
   # print("How many frogs would you like to see? ")
   # print("How many sheep would you like to see? ")
   
   #TODO: place farm here
   
   # print("Thanks for stopping by the Ransom Farm! Come back soon!")
    
