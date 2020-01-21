from game import game, playerHelper

game.printWelcome()
playerHelper.getPlayers()

while game.playGame:

    game.selectRounds()
    game.startGame()
    game.playSomeMore()


