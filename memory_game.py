import time #Required to pause the program
from IPython.display import clear_output #Required to clear the output
import pdb #Required to debug line by line[pdb.set_trace()]
import random as rand #Required to shuffle the lists
import string #Required to create the character list
from os import system, name #Required to clear the output (Windows only)

class Memory_game:
    """A Simple memory game. Memorize letter pairs. You will be given 10 chances to find 8 pairs to win the game.
    
    Inputs:
    User enters two numbers
    
    Returns:
    Puzzle grid
    
    Sample run:
        Checks if the letter beneath the number matches, cards remain turned
        t	h	j	j
        t	h	a	a
        k	g	x	m
        g	m	x	k

        1	2	3	4
        5	6	7	8
        9	10	11	12
        13	14	15	16

        Round 1
        Enter two numbers between 1 and 16: 1 5
        t	2	3	4
        t	6	7	8
        9	10	11	12
        13	14	15	16

        Round 2
        Enter two numbers between 1 and 16: 9 10

        Retry

        t	2	3	4
        t	6	7	8
        k	g	11	12
        13	14	15	16
        
        t	2	3	4
        t	6	7	8
        9	10	11	12
        13	14	15	16

        Round 3
        Enter two numbers between 1 and 16:"""
    
    def __init__(self):
        self.usr_input = []

        ##creating a-z list

        char = []

        for i in range(26):
            char.append(string.ascii_letters[i])

        ##creating random list from char[]

        rand_char = []
        hold = []

        for i in range(8):
            hold = rand.choice(char)
            char.remove(hold)
            rand_char.append(hold)
            rand_char.append(hold)

        #pdb.set_trace()

        ##Further shuffling and creating the final random list
        master_char = []
        hold = []

        while True:
            hold = rand.sample(rand_char,1)
            for i in hold:
                master_char.append(i)
                rand_char.remove(i)
                hold = rand.sample(rand_char,1)
            if len(rand_char) == 1:
                break
        for i in hold:
                master_char.append(i)
        
        ##The below list can be used for testing purposes
        #master_char = ['a','a','b','b','c','c','d','d','e','e','f','f','g','g','m','m']
        
        ##Keeping a copy of the main list
        master_char_hold = master_char.copy()

        ##Creating number list for the second grid
        num = []
        for i in range(1,17):
            num.append(i)
            
        ##Converting number list to character list
        num_char = []
        for i in num:
            num_char.append(str(i))
    
        self.master_char_hold = master_char_hold
        self.num_char = num_char
        self.chances = 1
        
        ##Initiating the play_game() function to start the game
        self.play_game()
        
    def play_game(self): 
        """Takes numeric inputs and checks if selected cards match and then will turn the cards if true"""
        #Displaying the initial letter grid
        self.display(self.master_char_hold)
        
        ##10 second pause
        for i in range(5):
            print('Time Elapsed: '+ str(i),end = '\r', flush = True)
            time.sleep(1)
        
        ##Clearing the letter grid
        #clear_output() -- jupyter notebook
        self.clear()

        ##Displaying the number grid to mask the letter grid
        self.display(self.num_char)
        
        while self.check():
            print('\nRound %d'%self.chances)
            
            ##Accepting inputs from the user
            usr_input = input('Enter two numbers between 1 and 16: ')
            
            #pdb.set_trace()
            #checker = []
            ##Validating the user inputs and exception handling
            try:
                if len(usr_input.split()) == 2 and 0 < int(usr_input.split()[0]) < 17 and 0 < int(usr_input.split()[1]) < 17 and int(usr_input.split()[0])!=int(usr_input.split()[1]):
            
                    usr_list = usr_input.split()

                    new_usr_list = []

                    for i in usr_list:
                        i = int(i)
                        new_usr_list.append(i)

                    checker = []

                    for j in new_usr_list:
                        checker.append(self.master_char_hold[j-1])

                    ##Clearing the letter grid
                    #clear_output()
                    self.clear()

                    ##Placeholder
                    num_char_hold = self.num_char.copy()
                    
                    ##Checking if the user selected cards match or not
                    if checker[0] == checker[1] and self.num_char.count(checker[0]) != 2:

                        ##Adding the user inputs
                        for i in range(2):
                            self.num_char[new_usr_list[i]-1] = checker[i]

                        self.display(self.num_char)
    
                    else:
                        #Check if the input is repeating
                        if self.num_char.count(checker[0]) == 2 and self.num_char.count(checker[1]) == 2:
                            print('\nPlease enter a pair not already matched\n')
                            self.chances -= 1
                        
                        ##Adding the user inputs
                        for i in range(2):
                            self.num_char[new_usr_list[i]-1] = checker[i]

                        self.display(self.num_char)
                        
                        print('Try Again')

                        #2-second pause
                        time.sleep(2)

                        self.num_char = num_char_hold.copy()

                        ##Clearing the letter grid
                        #clear_output()
                        self.clear()

                        self.display(self.num_char)

                    self.chances += 1
                    
                elif usr_input == 'quit':
                    print('Thank You')
                    break
                    
                else:
                    print('\nPlease enter two valid different numbers(1-16)')

            #Exception handling for different cases
            except ValueError as e:
                print('\nPlease enter two valid different numbers(1-16) ValueError')
            except IndexError as e:
                print('\nPlease enter two valid different numbers(1-16) IndexError')
            #This is for any other exception
            except Exception as e:
                print(e,'Please enter two valid different numbers(1-16)')
            
            
    def display(self,grid_list):
        """Defines the stucture of the grid"""
        print('Grid:\n')
        print('Type (quit) to exit the game')
        for i in range(4):
            print("\t".join(grid_list[(i*4):(i*4+4)]))


    def check(self):
        """Checks the total number of turns and the status of the game"""
        if self.chances >= 11:
            print('\nToo bad! You lost the game.')
            return False
        elif self.master_char_hold == self.num_char:
            print('\nYou Won!')
            return False
        else:
            return True

    def clear(self):
        """This function is specific to windows command-line to clear the screen"""
        _ = system('cls')
        
#To initiate the function:    
if __name__ == '__main__':
    Memory_game()