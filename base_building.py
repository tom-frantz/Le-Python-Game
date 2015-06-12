#
#        Test of what base building should look like
#
#          Start with basic perimeter to define where you can build shit
#
#            y xxxxxxxxxxx y
#            x             x
#            x             x
#            x             x
#            x             x
#            y xxxxxxxxxxx y
#
#         Then use resources collected in looting to build walls, doors and other defensive entities
#            Walls represented by another text based message e.g [ { | \ / . ! : -
#               -----------
#             y xxxxxxxxxxx y
#            |x             x|
#            |x             x|
#            |x             x|
#            |x             x|
#            |y xxxxxxxxxxx y|
#              -------------
#
#   As you continue to expand you will attract attention of zombies   represented with a text based entity
#      If you get to the point where your base is cramped and you need to expand your perimeter
#      you will need to clear zombies from that area and make flatten the area out, this will cost ammo and building
#      supplies.     once you do that, the base perimeter will be expanded in one of two ways
#      the first way will simply increase the area of the perimeter on all sides E.G
#
#            y xxxxxxxxxxxxxxxxxxxxxx y
#            x                        x
#            x                        x
#            x                        x
#            x                        x
#            x                        x
#            x                        x
#            x                        x
#            y xxxxxxxxxxxxxxxxxxxxxx y
#
#   The second way will make a new perimeter the same size of the first next to the current one on the side chosen
#
#            y xxxxxxxxxxx y
#            x             x
#            x             x
#            x             x
#            x             x
#            y xxxxxxxxxxx y
#            x             x
#            x             x
#            x             x
#            x             x
#            y xxxxxxxxxxx y
#
#   Any walls that were put in place before this will be kept as interior walls
#
#
# As we continue building this we will need to make is easy to replicate this code wise,
# I'm think we use the method but with white space double that in each direction plus the space between them
# This way we can display the zombies and surrounding areas in a basic form until we implement a UI and visuals
#
#
#
#
#
#
#            y xxxxxxxxxxx y
#            x             x
#            x             x
#            x             x
#            x             x
#            y xxxxxxxxxxx y
#
#
#
#
#
#
# This somehow aligns when printed
base = ('''            y xxxxxxxxxxx y
            x             x
            x             x
            x             x
            x             x
            y xxxxxxxxxxx y ''')
print(base)
