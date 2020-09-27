##MWD Credit
#Mahad Adeel, 24/9/20

## -- PERSONAL COMMENT (TO TEACHER) --

#Hello Sir,
#
#I decided to leave a personal comment here just to give some context on what's going on in my mind. I figured it may be important to you as my teacher.
#I love Computer Science and always have at a young age, I'm sure anyone in DC who studies it must have that passion for the subject,
#so I won't bore you on the details.
#
#What I do want to say however is that I honestly feel like the transition to the new school has somewhat demoralised me. This solution feels like only a fraction
#of the effort I could've put in and I'm not satisfied at all with the outcome. I come from a background in my old school where I was always the shining example of how
#to make robust, efficient and excellent code, however with the move and some anxities I don't believe I've translated it very well here.
#
#I've done what I could in my current state but I can't say I've given a full honest effort despite everything because I don't entirely feel that fuel that keeps me
#going in Computer Science, which really sucks since I have a deep love and appreciation for the subject. This code however feels somewhat incompetent, particularly
#around the Generate CC Number function which completely fell apart when attempting to reverse-engineer the algorithm. I'm rather disappointed in myself but don't have
#much opportunity to take a step back and improve it with how long and tedious it took me and that I have so much busy work to do.
#
#I know it probably seems like I'm demanding your pity but I'm really not, I'm genuinely somewhat let down with myself and feel like I could've done better. I have
#high standards for myself I feel I have to reach but they seem to be at a distance just out of my grasp.
#
#I want to try my best, I hope I can live up to myself.
#
#I don't have much to say besides that really. I hope at the very least this program is functional, I've done some testing of my own and it hasn't seemed to collapse
#yet. At least I have that. Anyways, I shall leave the rest of the speaking to the program itself.
#
#UPDATE: 27/9/2020 - I want to also reference my result from the Data Structures Test. I should've done so much better and the quality from that test was very poor.
#Once again I'm really let down with myself for the marks I got. I'm not requesting to be pardoned for my result but I want to apologise for not giving my full
#effort into learning the topic. Much of what I revised slipped out of my mind, I have the capability to have gotten full marks but my results speak for themselves.
#I feel demoralised, it's stopping me from giving my everything.

## -- MAIN BODY AND PERITHERAL FUNCTIONS --

#Main Function - Called upon at start, root of the program
def main():
    #An option is chosen from the Menu Function
    chosenMenuOption = menu()
    if chosenMenuOption == 1:
        #If the user chooses 'Check My Card', that appropriate Function is initiated
        checkMyCard()
    elif chosenMenuOption == 2:
        #If the user chooses 'Import Numbers to Check', that appropriate Function is initiated
        importNumbersToCheck()
    elif chosenMenuOption == 3:
        #If the user chooses 'Generate a Valid CC Number', that appropriate Function is initiated
        generateValidCCNumber()
    else:
        #If the user chooses to 'Quit Program', that appropriate Function is initiated
        return quitMenu()
        #If quitMenu() is True, the program continues to loop. If quitMenu() is False, the program does not loop.
    #If the user does not choose Quit, True is returned to runOnLoop so the program loops
    return True

#Run On Loop Function - Calls a function to run on loop
def runOnLoop(function):
    #'loop' is set as True so the loop is initiated
    loop = True
    while loop:
        #'loop' is defined as True or False, determined by the function returning one or the other value to determine whether to loop or not
        #If 'loop' is True, the function loops. If 'loop' is False, the loop exits.
        loop = function()

#Integer Input Function - Called upon to input an Integer and only an Integer
def intInput(prompt):
    #Try/Except and While Loop as validation to ensure an integer is input
    valid = False
    while not valid:
        try:
            #An integer input is prompted
            userInput = int(input(prompt))
            valid = True
        except:
            #If the input is not an integer, the system requests an integer input
            print("Enter an valid number")
    return userInput

#Return Message Function - Prints out a Statement saying how the code will return to the main menu
def returnMessage():
    print("Returning to Main Menu...")

## -- MAIN MENU --

#Menu Function - Displays and allows the user to select from the Main Menu
def menu():
    #Four menu options are presented: Check My Card, Import Numbers to Check, Generate a Valid CC Number and Quit
    print("Enter the Number of the Menu Option you would like to proceed with:")
    print("1. Check my Card\n2. Import Numbers to Check\n3. Generate a Valid CC Number\n4. Quit")
    #The user chooses an Input from one of these options
    chosenMenuOption = intInput("Enter one of the displayed numbers: ")
    #The chosen option is then returned to where the function was called
    return chosenMenuOption

## -- CHECK MY CARD --

#Check My Card Function - Called upon from the Main Menu to see if a Credit Card Number is Valid
def checkMyCard():
    #A subprocess is done to get the Card Number. This is processed as a String
    cardNumber = getCardNumber()
    #This Card Number is then validated
    validateCardNumber(cardNumber)
    #The user is then returned to the Main Menu
    returnMessage()

#Get Card Number - A Process to retrieve and validate a series of integers as a Credit Card number
def getCardNumber():
    #A Validation Loop is set until the card input is valid
    invalid = True
    while invalid:
        #The user is prompted to input their Credit Card details
        cardNumber = input("Enter your Card Number\nIt must be 16 digits in length\nLeave no spaces\n")
        if cardNumber.isnumeric() and len(cardNumber) == 16:
            #A Card Number has to be all-numeric and 16 digits in length. If this is the case for the input, it is deemed valid
            invalid = False
        else:
            #If the input is invalid, an error message is displayed
            print("Please Re-Enter an Appropriate Card Number\nMake sure all digits are only numbers 0 to 9 and the length is 16 Digits")
    #The Card Number is then Returned to where the process was called
    return cardNumber

#Validate Number - A process which states whether a Card Number is valid or not
def validateCardNumber(cardNumber):
    #The number is processed through Luhn's Algorithm
    if validByLuhnAlgorithm(cardNumber):
        #If the algorithm returns True, the card is Valid
        print("This Credit Card Number is Valid")
    else:
        #If the algorithm returns False, the card is Invalid
        print("This Credit Card Number is Invalid")

#Valid By Luhn Algorithm Function - Returns True or False depending on whether a Credit Card Number follows Luhn's Algorithm
def validByLuhnAlgorithm(inputNumbers):
    #The digitSummation variable is assigned as 0, defined as an integer, in preparation for all following calculations
    digitSummation = 0
    for i in range(0,15,2): #The loop indexes from 0 to 14 in steps of 2. This will select every other number until the second-last
        #The appropriate number is selected from the series and multiplied by 2. List Comprehension is then used to separate those to digits.
        number = int(inputNumbers[i])*2
        digits = [int(digit) for digit in str(number)]
        #Those sum of these digits are then added onto the total summation
        digitSummation += sum(digits)
    ##COULD THIS PROCESS BE REDUCED TO A SINGLE LIST COMPREHENSION?

    #Then the remaining digits are added on to the summation using List Comprehension
    digitSummation += sum([int(inputNumbers[i]) for i in range(1,16,2)])
    #The final digit of this summation is checked to be 0
    if str(digitSummation)[-1] == '0':
        #If the last digit is 0, True is returned
        return True
    #If the last digit is not 0, False is returned
    return False

## -- IMPORT NUMBERS TO CHECK --

#Import Numbers To Check Function - Called upon from the Main Menu to see if each series from an imported set of Credit Card numbers are valid or not
def importNumbersToCheck():
    #The file is opened by being given the File Path
    file = retrieveFile()
    #Due to a high risk of error messages from processing the File Data, a Try/Except statement is initiated
    #This file data is processed and the Card Numbers are recieved
    cardNumbers = processFileNumbers(file)
    #These numbers are then checked
    checkNumbers(cardNumbers)
    #Finally a statement is presented indicating the user is returning to the Main Menu
    returnMessage()

#Retrieve File Path Function - Validates and returns an inputted file from a given path
def retrieveFile():
    #A validation loop is set up until the contents of a file are retrieved
    invalid = True
    while invalid:
        try:
            #The user is prompted to enter a file path and name of the txt file. The input is taken a Raw String
            filePath = input(r"Enter the Path and Name of the .txt File you are looking for: ")
            #Finally the program attempts to open the file. If successful, the validation loop is closed.S
            fileContents = open(filePath,'r').read()
            invalid = False
        except:
            #If the file cannot be located, the user is prompted to re-enter
            print("File cannot be found. Enter a valid File Path and Name")
    ##HOW CAN THIS VALIDATION LOOP BE COMPRESSED INTO A SINGLE FUNCTION? IS THAT POSSIBLE?

    #Once an appropriate file is read, the contents are returned
    return fileContents

#Process File Numbers Function - Processes the data from a string taken from a file in order to extract the desired Card Numbers
def processFileNumbers(fileData):
    #A list is declared to store the Numbers
    numbersRetrieved = []
    #Each line of the file data is processed individually
    for i in fileData.split('\n'):
        try:
            #The first 16 characters of that file are taken
            sequence = i[0:16]
            if sequence.isnumeric():
                #If all the characters are numbers, that data is registered
                numbersRetrieved.append(sequence)
        except:
            #If the index is out of bounds, that line of data is ignored
            pass
    #When every line is processed, the data is returned
    return numbersRetrieved

#Check Numbers Function - Processes a list of card numbers one at a time and states whether each of them are valid or not
def checkNumbers(listOfData):
    #Each value is Validated one at a time
    for i in listOfData:
        print("Validating",i)
        validateCardNumber(i)

## -- GENERATE VALID CC NUMBER --

#Generate Valid CC Number Function - Called upon from the Main Menu, generates a specified number of CC Numbers between 1 and 100
def generateValidCCNumber():
    #The user first gives the number of cards they want, between 1 and 100
    number = getNumberOfCards()
    #The list of Card Numbers is set as 0, and will be filled in with individual unique card numbers
    listOfCardNumbers = []
    #The program loops for the amount of cards that want to be generated
    for i in range(number):
        #The Card Numbers are then generated with reference to this list (to avoid duplicates)
        listOfCardNumbers.append(generateNewNumber(listOfCardNumbers))
        ##THIS SOLUTION DOES NOT WORK! THE CARDS ARE INVALID! DEBUG IF POSSIBLE
    #Afterwards, the cards are then processed and saved
    saveCardsData(listOfCardNumbers)
    returnMessage()

#Get Number Of Cards Function - Asks the user to enter a number of cards to generate between 1 and 100
def getNumberOfCards():
    #A validation loop is set to get a number
    invalid = True
    while invalid:
        #The user is prompted to enter a number between 1 and 100
        number = intInput("Enter the Number of Cards to Generate within 1 to 100: ")
        if 0 < number < 101:
            #If the number is within 1 and 100, the loop breaks
            invalid = False
        else:
            #If the number is out of range, an error displays and the user is prompted to re-enter
            print("Enter a Number between 1 and 100")
    #Once validated, the number is returned
    return number

#Generate New Number Function - Generates a new CC Number, with reference to previous ones it generates in order to prevent duplication
def generateNewNumber(existingList):
    invalid = True
    while invalid:
        #A random final summation digit that ends with 0 (between 0 and 140 in intervals of 10) is picked
        endSummation = r.choice([i for i in range(144) if i % 10 == 0])
        #The sum of the Odd Individuals is selected randomly from a valid range
        oddIntervalsSum = r.randint(0,getMaxOdd(endSummation))
        #The Odd Intervals are then randomly generated and then shuffled
        oddIntervals = generateListOfIntervals(oddIntervalsSum)
        r.shuffle(oddIntervals)
        #The Even Intervals are then randomly generated from a sum and shuffled
        evenIntervalsSum = endSummation - oddIntervalsSum
        evenIntervals = generateListOfIntervals(evenIntervalsSum)
        r.shuffle(evenIntervals)
        #The Even Intervals are then processed to what their values would be
        evenIntervals = processEvenIntervals(evenIntervals)
        #Finally the data is combined into a card which is then displayed for the user
        cardNumber = createCardNumber(oddIntervals, evenIntervals)
        #Next, it is checked whether this card number already exists within the given list
        invalid = cardNumber in existingList
        #If it is a unique value, invalid is set to False and the loop breaks as it is not within the list
    #The data is then ultimately returned for the list
    return cardNumber

#Generate Division Count Function - Counts how many times a number can be divided by 1-9 and returns as a dictionary
def generateDivisionCount(number):
    #A blank dictionary is created
    dictionary = {}
    for i in range(1,10):
        #For numbers 1 to 10, it counts how many times minimum each number divides into the given value
        dictionary[i] = number // i
    #When the final dictionary is generated, that number is returned
    return dictionary

#Get Max Odd Function - Finds the maximum value that the sum of the odd interval digits can be
def getMaxOdd(endSummation):
    #The end summation has to be checked if it is equal to 0, which is the exception for this formula
    if endSummation != 0:
        if endSummation > 70:
            #The absolute maximum number that can be generated is 72. If the end summation is greater than 72, then by default the value to return is 72
            return 72
        else:
            #The maximum value for the Odd Intervals sum is counted by subtracting 8 from the endSummation
            #This is because the minimum value for the Even Intervals would be 1 1 1 1 1 1 1 1, which would produce 8
            return endSummation - 8
    else:
        #The only value that would be appropriate for 0 would be 0
        return 0

#Generate List Of Intervals Function - Generates a list of 8 random digits which add up into the Sum
def generateListOfIntervals(_sum):
    #Intervals is declared as a blank list to be filled, and the division dictionary finds the possible divisors
    intervals = []
    divisionDict = generateDivisionCount(_sum)
    for i in range(9,0,-1):
        for x in range(divisionDict[i]):
            #A sum is generated with minimal numbers, prioritising the largest ones, starting from 9 and going to 1
            if sum(intervals) + i <= _sum:
                intervals.append(i)
    #These large numbers then can be broken down into smaller ones
    #A loop is set on repeat until 8 digits have been created
    while len(intervals) < 8:
        if all(i < 2 for i in intervals):
            for i in range(8-len(intervals)):
                #If all the internal values are 1 or 0, the rest are filled out as 0s
                intervals.append(0)
        else:
            #Otherwise, a random number is selected to be split
            numToSplit = r.choice(intervals)
            #There is also the random low chance the rest of the digits will be filled with 0
            zeroFillChance = r.randint(1,100)
            if zeroFillChance > 2:
                if numToSplit > 1:
                    #The bigger number is removed from the list and split into 2 randomly-sized pieces
                    #The smaller pieces add up to the bigger number
                    #From then the smaller pieces are added in place of the bigger number, keeping the same sum but adding a digit
                    intervals.remove(numToSplit)
                    numToSubtract = r.randint(1,numToSplit)
                    intervals.append(numToSubtract)
                    intervals.append(numToSplit - numToSubtract)
            else:
                #There is a 2% chance the rest of the digits will all be set as 0
                #This is an unlikely shortcut to make it less predictable
                for i in range(8-len(intervals)):
                    intervals.append(0)
    return intervals
    ##THE VARIATION FROM THIS SOLUTION IS POOR. RESULTS VARY UNEVENLY. THIS IS A SIMPLE AND RUSHED SOLUTION. IMPROVEMENT URGENTLY REQUIRED!

#Process Even Intervals Function - Processes the given list of Even Intervals and swaps out their values to their appropriate halves
def processEvenIntervals(evenIntervals):
    #This key is established to replace values appropriately. Furthermore an empty list is set to contain the processed data
    processDictionary = {0: 0, 1: 5, 2: 1, 3: 6, 4: 2, 5: 7, 6: 3, 7: 8, 8: 4, 9: 9}
    newEvenIntervals = []
    for i in evenIntervals:
        #Each value from the old list is ran through the key, and the output of the key is added to the new list
        #This is done for every value in the list
        newEvenIntervals.append(processDictionary[i])
    #Finally the new values are returned to where required
    return newEvenIntervals

#Create Card Number Function - Creates the number of the card through combining the odd and even intervals
def createCardNumber(odds, evens):
    #The Card String is set as blank to be filled
    cardString = ''
    for i in range(0,8):
        #Every value in the odds and evens is added one at a time to the Card String
        cardString += str(odds[i])
        cardString += str(evens[i])
    #When complete, the Card String is returned
    return cardString

def saveCardsData(inputdata):
    #The save data is formatted onto a single continuous string so it is easier to display and save
    saveDataString = ''
    for i in inputdata:
        saveDataString += i + '\n'
    print(saveDataString)
    #The data is saved in the current working directory under the name "CARDS" and a time stamp
    saveFileName = "CARDS {}.txt".format(dt.datetime.today().strftime('%Y-%m-%d %H;%M;%S'))
    saveFile = open(saveFileName,'w')
    saveFile.write(saveDataString)
    saveFile.close()
    #An appropriate message is displayed once the data is saved
    print("Finished Saving Data as",saveFileName)

## -- QUIT MENU --

#Quit Menu Function - Called upon from Main Menu for the user to choose to quit the program or not
def quitMenu():
    #The user is prompted to enter 'Y' to confirm to Quit
    if confirm("Are you sure you would like to Quit? Enter 'Y' to Quit\n"):
        #If they enter 'Y', an appropriate message is given and False is returned
        print("Quitting Program...")
        return False
    #If they don't enter 'Y', True is returned
    return True

## -- PACKAGE CALLING AND PROGRAM INITIATION --

import random as r
#Random Module used for generating valid CC Numbers
import datetime as dt
#Datetime Module for Saving Data with DMY, HMS

confirm = lambda prompt='': True if input(prompt).upper() == 'Y' else False
#Confirm Lambda Function to allow for Y and N inputs

#The program is initiated with a permanent loop in case a Keyboard Interrupt is detected
mainProgramLoop = True
while mainProgramLoop:
    try:
        #Given that there are no Keyboard Interrupts, the Main Process runs on loop until closed
        runOnLoop(main)
        mainProgramLoop = False
    except KeyboardInterrupt:
        #If a Keyboard Interrupt is detected, the user is asked to confirm if they want to quit the program
        try:
            #The user is prompted whether they want to actually quit, or reboot the program
            print("The program has been interrupted\n(Unsaved Work has been Lost)")
            if not confirm("Enter Y to return to Main Menu. Otherwise the program will Quit\n"):
                #If the user confirms they want to quit the program, the loop is broken
                print("Quitting Program...")
                mainProgramLoop = False
            else:
                #If the user doesn't want to quit, the program is rebooted
                print("Rebooting program...\n\n")
        except KeyboardInterrupt:
            #If a second Keyboard Interrupt is registered, the program is Force Quit
            print("Force Quitting program...")
            mainProgramLoop = False
