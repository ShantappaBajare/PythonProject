#call all the functions from both animal and bird modules

# approach1
# import animal
# import bird
#
# animal.fly()
# animal.color()
#
# bird.color()
# bird.fly()

#approach2
# from animal import *
# from bird import *  # by default python will take the latest import where both functions are same name
#
# fly()
# color()

#  To overcome this issue we need to do
from animal import *
fly()
color()

from bird import *
fly()
color()