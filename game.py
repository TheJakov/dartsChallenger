from random import randint
from colorama import Fore
from colorama import Back
from colorama import Style
import os

class game:

    playGame = True
    numberOfRounds = 0

    # Each challange has its own text, value to add to score if completed and
    # a value to decrease the score if not completed.
    #
    # EPIC - no score decreasing upon not completing the challenge
    # LEGENDARY - gives points and after that doubles total points (HARD)
    # UNLUCKY - 0 points for completing, but 25 for not completing
    challengesList = [
        ["[EPIC] (3 darts) Score more than 60 points.", 15, 0],
        ["[EPIC] (3 darts) Score less than 7 points - each dart MUST hit the target.", 15, 0],
        ["(3 darts) Score any number of points between 20 and 30, including those numbers" +
         " - each dart MUST hit the target.", 10, 2],
        ["(1 dart) You must hit even number.", 10, 5],
        ["(1 dart) You must hit odd number.", 10, 5],
        ["(2 darts) Sum of two darts must be an even number - each dart MUST hit the target.", 8, 3],
        ["(2 darts) Sum of two darts must be an odd number - each dart MUST hit the target.", 8, 3],
        ["(5 darts) You must hit BULLSEYE !", 30, 4],
        ["[LEGENDARY] (1 dart) You must hit BULLSEYE ! (30 points, but then doubles total points)", 30, 0],
        ["[LEGENDARY] (2 darts) You must hit number 7 two times. (15 points, but then doubles total points)", 15, 0],
        ["(2 darts) You must hit one even and one odd number.", 15, 3],
        ["[UNLUCKY] (2 darts) You must hit two numbers in range 11-16. (BULLSEYE is not included)", 0, 25],
        ["(3 darts) You must hit two number neighbours. (e.g. 5 and 6, 18 and 17)", 12, 4]
    ]

    @staticmethod
    def printWelcome():
        game.clearScreen()
        print("Welcome to the Darts Challenger game!" +
              "\nGame rules are following: " +
              "\n\n 1) You will be given a challenge and your target is to complete it." +
              "\n 2) If successful, you will be given points or even lose them if not!" +
              "\n 3) Each challenge has it's own unique awarding and/or punishing system for their completion and/or failure." +
              "\n 4) Player with most points, after playing selected number of rounds, is the winner!" +
              "\n 5) Good luck, steady hands and have fun!")
    
    @staticmethod
    def clearScreen():
        os.system('cls')

    @staticmethod
    def generateChallengeId():
        #seed(randint(0, 10))
        value = randint(0, (len(game.challengesList)-1))
        return value

    @staticmethod
    def playRound(gameRound):
        for player in playerHelper.playerList:
            game.clearScreen()
            game.printScore()
            print(f"\nRound: {gameRound} - {player[0]} playing")
            indeksGenerated = game.generateChallengeId()

            print(Fore.YELLOW)
            print(f"\nChallenge: {game.challengesList[indeksGenerated][0]}\n\n")
            print(Style.RESET_ALL)

            if game.HeCompleted(player[0]):
                player[1] += game.challengesList[indeksGenerated][1]
                if "LEGENDARY" in game.challengesList[indeksGenerated][0]:
                    player[1] *= 2
            else:
                player[1] -= game.challengesList[indeksGenerated][2]
                if player[1] < 0:
                    player[1] = 0
    
    @staticmethod
    def startGame():
        for gameRound in range(1, game.numberOfRounds + 1):
            game.playRound(gameRound)

    @staticmethod
    def selectRounds():
        msg = input("\nNumber of rounds (1-16): ")
        if msg.isnumeric():
            if int(msg) >= 1 and int(msg) <= 16:
                game.numberOfRounds = int(msg)
                return
            else:
                print("Number of rounds must be in range 1-16.")
            playerHelper.getPlayers()
        else:
            print("Invalid input.")
            playerHelper.getPlayers()

    @staticmethod
    def printScore():
        print(Back.BLACK)
        header = "\n PLAYER".ljust(16) + "SCORE".ljust(7)
        print(header)
        for player in playerHelper.playerList:
            print(f" {player[0].ljust(15)} {str(player[1]).ljust(5)}")
        print(Style.RESET_ALL)

    @staticmethod
    def ResetScores():
        for player in playerHelper.playerList:
            player[1] = 0

    @staticmethod
    def playSomeMore():
        game.clearScreen()
        game.printScore()
        print("\nDo you want to play again ?")
        print("1) Yes")
        print("2) No")
        msg = input("\nYour choice: ")
        if msg == "1":
            game.playGame = True
            game.ResetScores()
        elif msg == "2":
            game.playGame = False
        else:
            print("Invalid option.\n")
            game.playSomeMore()

    @staticmethod
    def HeCompleted(playerName):
        print(f"{playerName} completed challenge successfully ?")
        print("1) Yes")
        print("2) No")
        msg = input("\nYour choice: ")
        if msg == "1":
            return True
        elif msg == "2":
            return False
        else:
            print("Invalid option.\n")
            game.HeCompleted(playerName)


class playerHelper:

    playerList = []

    @staticmethod
    def getPlayers():
        msg = input("\nNumber of players (1-10): ")
        if msg.isnumeric():
            if int(msg) >= 1 and int(msg) <= 10:
                playerHelper.getPlayerNames(msg)
                return
            else:
                print("Number of players must be in range 1-10.")
            playerHelper.getPlayers()
        else:
            print("Invalid input.")
            playerHelper.getPlayers()

    @staticmethod
    def getPlayerNames(playerNum):
        for i in range(1, int(playerNum)+1):
            playerName = input(f"{i}. player name: ")
            playerHelper.playerList.append([playerName, 0])
