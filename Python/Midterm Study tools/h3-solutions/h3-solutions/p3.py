# Python Programming.
# Homework 3, problem 3
# Instructor: Dr. Ionut Cardei
# Do not distribute.

# Modified: with Human class

# Copyright 2017, 2013, 2011 Pearson Education, Inc., W.F. Punch & R.J.Enbody
"""Predator-Prey Simulation
   four classes are defined: animal, predator, prey, and island
   where island is where the simulation is taking place,
   i.e. where the predator and prey interact (live).
   A list of predators and prey are instantiated, and
   then their breeding, eating, and dying are simulted.
"""
import random
import time
import pylab

class Island (object):
    """Island
       n X n grid where zero value indicates not occupied."""
    def __init__(self, n, prey_count=0, predator_count=0, human_count=0):
        '''Initialize grid to all 0's, then fill with animals
        '''
        # print(n,prey_count,predator_count)
        self.grid_size = n
        self.grid = []
        for i in range(n):
            row = [0]*n    # row is a list of n zeros
            self.grid.append(row)
        self.init_animals(prey_count,predator_count, human_count)

    # new method:
    def init_species(self, animal_count, animal_class):
        ''' Put count  animals of class animal_class on the island at random locations.
        precondition: count >= 0
        '''
        count = 0
        # while loop continues until prey_count unoccupied positions are found
        while count < animal_count:
            x = random.randint(0,self.grid_size-1)
            y = random.randint(0,self.grid_size-1)
            if not self.animal(x,y):
                new_animal = animal_class(island=self,x=x,y=y)
                count += 1
                self.register(new_animal)
        
    # refactored this method, as it repeated code and that is bad style:
    # (refactoring in class Island is not required by the homework. It is demonstrated here for education.)
    def init_animals(self,prey_count, predator_count, human_count):
        ''' Put some initial animals on the island
        '''
        self.init_species(prey_count, Prey)
        self.init_species(predator_count, Predator)
        self.init_species(human_count, Human)


    def clear_all_moved_flags(self):
        ''' Animals have a moved flag to indicated they moved this turn.
        Clear that so we can do the next turn
        '''
        for x in range(self.grid_size):
            for y in range(self.grid_size):
                if self.grid[x][y]:
                    self.grid[x][y].clear_moved_flag()
        
    def size(self):
        '''Return size of the island: one dimension.
        '''
        return self.grid_size

    def register(self,animal):
        '''Register animal with island, i.e. put it at the 
        animal's coordinates
        '''
        x = animal.x
        y = animal.y
        self.grid[x][y] = animal

    def remove(self,animal):
        '''Remove animal from island.'''
        x = animal.x
        y = animal.y
        self.grid[x][y] = 0

    def animal(self,x,y):
        '''Return animal at location (x,y)'''
        if 0 <= x < self.grid_size and 0 <= y < self.grid_size:
            return self.grid[x][y]
        else:
            return -1  # outside island boundary

    def __str__(self):
        '''String representation for printing.
           (0,0) will be in the lower left corner.
        '''
        s = ""
        for j in range(self.grid_size-1,-1,-1):  # print row size-1 first
            for i in range(self.grid_size):      # each row starts at 0
                if not self.grid[i][j]:
                    # print a '.' for an empty space
                    s+= "{:<2s}".format('.' + "  ")
                else:
                    s+= "{:<2s}".format((str(self.grid[i][j])) + "  ")
            s+="\n"
        return s

    # refactored counting: repeating code with minor variation cries for it:
    def count_species(self, animal_class):
        ''' count all the animal of a given class on the island'''
        count = 0
        for x in range(self.grid_size):
            for y in range(self.grid_size):
                animal = self.animal(x,y)
                if animal and (type(animal) == animal_class):   # can't use isinstance here
                    count+=1
        return count
    


    def count_prey(self):
        ''' count all the prey on the island'''
        return self.count_species(Prey)

    def count_predators(self):
        ''' count all the predators on the island'''
        return self.count_species(Predator)

    def count_humans(self):
        ''' count all the humans on the island'''
        return self.count_species(Human)



class Animal(object):
    def __init__(self, island, x=0, y=0, s="A"):
        '''Initialize the animal's and their positions
        '''
        self.island = island
        self.name = s
        self.x = x
        self.y = y
        self.moved=False
            
    def position(self):
        '''Return coordinates of current position.
        '''
        return self.x, self.y

    def __str__(self):
        return self.name
    
    def check_grid(self,type_looking_for=int):
        ''' Look in the 8 directions from the animal's location
        and return the first location that presently has an object
        of the specified type. Return 0 if no such location exists
        '''
        # neighbor offsets
        offset = [(-1,1),(0,1),(1,1),(-1,0),(1,0),(-1,-1),(0,-1),(1,-1)] 
        result = 0
        for i in range(len(offset)):
            x = self.x + offset[i][0]  # neighboring coordinates
            y = self.y + offset[i][1]
            if not 0 <= x < self.island.size() or \
               not 0 <= y < self.island.size():
                continue
            if type(self.island.animal(x,y))==type_looking_for:
                result=(x,y)
                break
        return result

    def move(self):
        '''Move to an open, neighboring position '''
        if not self.moved:
            location = self.check_grid(int)
            if location:
                # print('Move, {}, from {},{} to {},{}'.format( \
                #       type(self),self.x,self.y,location[0],location[1]))
                self.island.remove(self)   # remove from current spot
                self.x = location[0]       # new coordinates
                self.y = location[1]
                self.island.register(self) # register new coordinates
                self.moved=True
                
    def breed(self):
        ''' Breed a new Animal.If there is room in one of the 8 locations
        place the new Prey there. Otherwise you have to wait.
        '''
        if self.breed_clock <= 0:
            location = self.check_grid(int)
            if location:
                self.breed_clock = self.breed_time
                # print('Breeding Prey {},{}'.format(self.x,self.y))
                the_class = self.__class__
                new_animal = the_class(self.island,x=location[0],y=location[1])
                self.island.register(new_animal)

    def clear_moved_flag(self):
        self.moved=False



class Prey(Animal):
    def __init__(self, island, x=0,y=0,s="O"):
        Animal.__init__(self,island,x,y,s)
        self.breed_clock = self.breed_time
        # print('Init Prey {},{}, breed:{}'.format(self.x, self.y,self.breed_clock))
           
    def clock_tick(self):
        '''Prey only updates its local breed clock
        '''
        self.breed_clock -= 1
        # print('Tick Prey {},{}, breed:{}'.format(self.x,self.y,self.breed_clock))

class Predator(Animal):
    def __init__(self, island, x=0,y=0,s="X"):
        Animal.__init__(self,island,x,y,s)
        self.starve_clock = self.starve_time
        self.breed_clock = self.breed_time
        # print('Init Predator {},{}, starve:{}, breed:{}'.format( \
        #       self.x,self.y,self.starve_clock,self.breed_clock))

    def clock_tick(self):
        ''' Predator updates both breeding and starving
        '''
        self.breed_clock -= 1
        self.starve_clock -= 1
        # print('Tick, Predator at {},{} starve:{}, breed:{}'.format( \
        #       self.x,self.y,self.starve_clock,self.breed_clock))
        if self.starve_clock <= 0:
            # print('Death, {} at {},{}'.format(type(self).__name__, self.x,self.y))
            self.island.remove(self)     # this also applies to Humans

    def eat(self):
        ''' Predator looks for one of the 8 locations with Prey. If found
        moves to that location, updates the starve clock, removes the Prey
        '''
        if not self.moved:
            location = self.check_grid(Prey)
            if location:
                # print('Eating: pred at {},{}, prey at {},{}'.format( \
                #       self.x,self.y,location[0],location[1]))
                self.island.remove(self.island.animal(location[0],location[1]))
                self.island.remove(self)
                self.x=location[0]
                self.y=location[1]
                self.island.register(self)
                self.starve_clock=self.starve_time
                self.moved=True


class Human(Predator):
    def __init__(self, island, x=0, y=0, s="H"):
        super().__init__(island,x,y,s)
        self.starve_clock = self.starve_time
        self.breed_clock = self.breed_time
        self.hunt_clock = self.hunt_time

        ##print("****", isinstance(self,Predator))
        
        # print('Init Human {},{}, starve:{}, breed:{}'.format( \
        #       self.x,self.y,self.starve_clock,self.breed_clock))

    def clock_tick(self):
        ''' Human updates breeding, starving, and hunting timers.
        '''
        super().clock_tick()   # relies on superclass for breeding and starving

        self.hunt_clock -= 1
        # will reset when reaching 0. A human must hunt&kill Predators or will starve.

        
    def eat(self):
        """
            Humans don't eat Prey, like their superclass. Override and do nothing.
        """
        return

        
    def hunt(self):
        # print('Tick, Human at {},{} starve:{}, breed:{}, hunt:{}'.format( \
        #       self.x,self.y,self.starve_clock,self.breed_clock, self.hunt_clock))
##        if not self.moved and self.hunt_clock <= 0:
        if not self.moved and self.hunt_clock <= 0:
            # print('Human: hunt at {},{}'.format(self.x,self.y))

            # Human hunts Predaors periodically. If not now, must wait for next interval.
            self.hunt_clock = self.hunt_time
            location = self.check_grid(Predator)
            if location:
                # can hunt
                print("Human.hunt(): x,y={} predator at {}".format(self.x, self.y, location))
                self.island.remove(self.island.animal(location[0],location[1]))
                self.island.remove(self)
                self.x=location[0]
                self.y=location[1]
                self.island.register(self)
                self.moved=True
                # Humans hunt and "eat" Predators, so we do this:
                self.starve_clock = self.starve_time


###########################################
def main(predator_breed_time=10, predator_starve_time=6, initial_predators=15, \
         prey_breed_time=3, initial_prey=50, \
         size=10, ticks=1000,
         human_breed_time=50, human_starve_time=20, human_hunt_time=10, initial_humans=10):
    ''' main simulation. Sets defaults, runs event loop, plots at the end
    '''

    random.seed(2)    # it's better to have repeatable results and use the same seed for each simulation
    
    # initialization values
    Human.breed_time = human_breed_time
    Human.starve_time = human_starve_time
    Human.hunt_time = human_hunt_time
    
    Predator.breed_time = predator_breed_time
    Predator.starve_time = predator_starve_time
    Prey.breed_time = prey_breed_time

    # for graphing
    predator_list=[]
    prey_list=[]
    human_list = []

    tick_list = []
    
    # make an island
    isle = Island(size,initial_prey, initial_predators, initial_humans)
    print(isle)

    # event loop. 
    # For all the ticks, for every x,y location.
    # If there is an animal there, try eat, move, breed and clock_tick
    for i in range(ticks):
        # important to clear all the moved flags!
        isle.clear_all_moved_flags()
        for x in range(size):
            for y in range(size):
                animal = isle.animal(x,y)
                if animal:
                    if isinstance(animal, Human):
                        animal.hunt()
                    if isinstance(animal,Predator):
                        animal.eat()
                    animal.move()
                    animal.breed()
                    animal.clock_tick()

        # record info for display, plotting
        prey_count = isle.count_prey()
        predator_count = isle.count_predators()
        human_count = isle.count_humans()
        
        # to stop when prey are gone:
        #if prey_count == 0:
        #    print('Lost the Prey population. Quiting.')
        #    break
        #if predator_count == 0:
        #    print('Lost the Predator population. Quitting.')
        #    break
        

        # Actually, it is more informative to stop when everybody is gone:
        if prey_count == predator_count == human_count == 0:
            break

        tick_list.append(i)    # for plotting
        
        prey_list.append(prey_count)
        predator_list.append(predator_count)
        human_list.append(human_count)
        
        # print out every 10th cycle, see what's going on
        if 0 == i % 10:
            print("time={} prey={} predators={} humans={}".format(i, prey_count, predator_count, human_count))
        # print the island, hold at the end of each cycle to get a look
#        print('*'*20)
#        print(isle)
#        ans = input("Return to continue")


    print(isle)


    pylab.plot(tick_list, predator_list, label="Predators")
    pylab.plot(tick_list, prey_list, label="Prey")
    pylab.plot(tick_list, human_list, label="Humans")
    pylab.legend(loc="best", shadow=True)
    pylab.title("pop ({}, {}, {}), breed ({}, {}, {}), starve ({}, {}), hunt {}"
                .format(initial_prey, initial_predators, initial_humans, prey_breed_time, predator_breed_time,
                        human_breed_time, predator_starve_time, human_starve_time, human_hunt_time))
    pylab.show()
