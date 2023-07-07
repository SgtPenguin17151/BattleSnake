import copy, RouteFinder

gameBoard = []
height = 11
width = 11
foodLocation = []


def fillGameBoard(snakes, food, boardHeight):
  global gameBoard, foodLocation

  for snake in snakes:
    headx = (snake["head"]["x"])
    heady = (boardHeight - 1) - (snake["head"]["y"])
    gameBoard[heady][headx] = "sh"
    for bodyPiece in snake["body"][1:]:
      bodyx = bodyPiece["x"]
      bodyy = (boardHeight - 1) - bodyPiece["y"]
      if gameBoard[bodyy][bodyx] == "x":
        gameBoard[bodyy][bodyx] = "sb"
        if snake["body"][-1]["x"] == bodyPiece["x"] and snake["body"][-1][
            "y"] == bodyPiece["y"]:
          gameBoard[bodyy][bodyx] = "st"
  for f in food:
    foodLocation.append(f)
    foodx = f["x"]
    foody = (boardHeight - 1) - f["y"]
    gameBoard[foody][foodx] = "f"


def getNumberOfFreeSquares(board, xcoOrd, ycoOrd):
  freeSquares = 0
  length = len(board) - 1
  if ycoOrd != length:
    if board[(length - ycoOrd) - 1][xcoOrd] == "x" or board[(length - ycoOrd) -
                                                            1][xcoOrd] == "f":
      freeSquares += 1

  if ycoOrd != 0:
    if board[(length - ycoOrd) + 1][xcoOrd] == "x" or board[(length - ycoOrd) +
                                                            1][xcoOrd] == "f":
      freeSquares += 1

  if xcoOrd != length:
    if board[length - ycoOrd][xcoOrd + 1] == "x" or board[length -
                                                          ycoOrd][xcoOrd +
                                                                  1] == "f":
      freeSquares += 1

  if xcoOrd != 0:
    if board[(length - ycoOrd)][xcoOrd - 1] == "x" or board[length -
                                                            ycoOrd][xcoOrd -
                                                                    1] == "f":
      freeSquares += 1

  return freeSquares


def updateSnakes(board, snake, move, index, consumedFood):
  global height, width
  updatedSnake = copy.copy(snake)
  secondLast = updatedSnake["body"][-2]
  headx = updatedSnake["head"]["x"]
  heady = updatedSnake["head"]["y"]

  if move == "up" and heady != len(board) - 1:
    newHead = {"x": headx, "y": heady + 1}
  if move == "down" and heady != 0:
    newHead = {"x": headx, "y": heady - 1}

  if move == "left" and headx != 0:
    newHead = {"x": headx - 1, "y": heady}

  if move == "right" and headx != len(board) - 1:
    newHead = {"x": headx + 1, "y": heady}

  if not consumedFood:
    updatedSnake["head"] = newHead
    updatedSnake["body"].insert(0, newHead)
    updatedSnake["body"].pop(-1)
    updatedSnake["health"] -= 1

  else:
    updatedSnake["health"] = 100
    updatedSnake["head"] = newHead
    updatedSnake["body"].insert(0, newHead)
    updatedSnake["body"].pop(-1)
    updatedSnake["body"].insert(-1, secondLast)
  length = len(updatedSnake["body"])
  updatedSnake["length"] = length

  return updatedSnake


def doMove(move, snake, board, index, snakes):
  global height, width
  gameBoard = copy.deepcopy(board)
  consumedFood = False
  isPlayerDead = False
  survived = True
  updatedSnakes = copy.deepcopy(snakes)
  tail = snake["body"][-1]
  secondLast = snake["body"][-2]
  headx = snake["head"]["x"]
  heady = snake["head"]["y"]
  deadIndexs = []

  if move == "up":
    if not heady == height - 1:
      if gameBoard[(height - heady) - 2][headx] == "sh":
        gameBoard, updatedSnakes, survived, isPlayerDead, deadIndexs = calculateHeadCollision(
          gameBoard, snakes, index, move)
      if survived:
        if gameBoard[(height - heady) - 2][headx] == "f":
          consumedFood = True
        if not consumedFood:
          if not gameBoard[((height - tail["y"]) - 1)][tail["x"]] == "sh":
            gameBoard[((height - tail["y"]) - 1)][tail["x"]] = "x"
          gameBoard[(height - secondLast["y"]) - 1][secondLast["x"]] = "st"

        gameBoard[(height - heady - 1)][headx] = "sb"
        gameBoard[(height - heady) - 2][headx] = "sh"
        updatedSnake = updateSnakes(gameBoard, snake, move, index,
                                    consumedFood)
        if deadIndexs != []:
          if index > deadIndexs[0]:
            index -= 1
          if len(deadIndexs) == 2:
            if index + 1 > deadIndexs[1]:
              index -= 1
        newSnakes = copy.deepcopy(updatedSnakes)
        if updatedSnake["health"] <= 0:
          newBoard = removeSnake(gameBoard, updatedSnake)
          newSnakes.pop(index)
          if index == 0:
            isPlayerDead = True
          deadIndexs = [index]
          return newBoard, newSnakes, False, isPlayerDead, deadIndexs

        newSnakes.pop(index)
        newSnakes.insert(index, updatedSnake)
        return gameBoard, newSnakes, survived, isPlayerDead, deadIndexs
      else:
        return gameBoard, updatedSnakes, survived, isPlayerDead, deadIndexs

  if move == "down":
    if not heady == 0:
      if gameBoard[(height - heady)][headx] == "sh":
        gameBoard, updatedSnakes, survived, isPlayerDead, deadIndexs = calculateHeadCollision(
          gameBoard, snakes, index, move)
      if survived:
        if gameBoard[(height - heady)][headx] == "f":
          consumedFood = True
        if not consumedFood and not heady == 0:
          if not gameBoard[(height - tail["y"]) - 1][tail["x"]] == "sh":
            gameBoard[(height - tail["y"]) - 1][tail["x"]] = "x"
          gameBoard[(height - secondLast["y"]) - 1][secondLast["x"]] = "st"
        gameBoard[(height - heady) - 1][headx] = "sb"
        gameBoard[(height - heady)][headx] = "sh"
        updatedSnake = updateSnakes(gameBoard, snake, move, index,
                                    consumedFood)
        if deadIndexs != []:
          if index > deadIndexs[0]:
            index -= 1
          if len(deadIndexs) == 2:
            if index + 1 > deadIndexs[1]:
              index -= 1
        newSnakes = copy.deepcopy(updatedSnakes)

        if updatedSnake["health"] <= 0:
          newBoard = removeSnake(gameBoard, updatedSnake)
          newSnakes.pop(index)
          if index == 0:
            isPlayerDead = True
          deadIndexs = [index]
          return newBoard, newSnakes, False, isPlayerDead, deadIndexs

        newSnakes.pop(index)
        newSnakes.insert(index, updatedSnake)
        return gameBoard, newSnakes, survived, isPlayerDead, deadIndexs
      else:
        return gameBoard, updatedSnakes, survived, isPlayerDead, deadIndexs

  if move == "left":
    if not headx == 0:
      if gameBoard[(height - heady) - 1][headx - 1] == "sh":
        gameBoard, updatedSnakes, survived, isPlayerDead, deadIndexs = calculateHeadCollision(
          gameBoard, snakes, index, move)
      if survived:
        if gameBoard[(height - heady) - 1][headx - 1] == "f":
          consumedFood = True
        if not consumedFood:
          if not gameBoard[(height - tail["y"]) - 1][tail["x"]] == "sh":
            gameBoard[(height - tail["y"]) - 1][tail["x"]] = "x"
          gameBoard[(height - secondLast["y"]) - 1][secondLast["x"]] = "st"
        gameBoard[((height - heady) - 1)][headx - 1] = "sh"
        gameBoard[((height - heady) - 1)][headx] = "sb"
        updatedSnake = updateSnakes(gameBoard, snake, move, index,
                                    consumedFood)
        if deadIndexs != []:
          if index > deadIndexs[0]:
            index -= 1
          if len(deadIndexs) == 2:
            if index + 1 > deadIndexs[1]:
              index -= 1
        newSnakes = copy.deepcopy(updatedSnakes)

        if updatedSnake["health"] <= 0:
          newBoard = removeSnake(gameBoard, updatedSnake)
          newSnakes.pop(index)
          if index == 0:
            isPlayerDead = True
          deadIndexs = [index]
          return newBoard, newSnakes, False, isPlayerDead, deadIndexs

        newSnakes.pop(index)
        newSnakes.insert(index, updatedSnake)
        return gameBoard, newSnakes, survived, isPlayerDead, deadIndexs
      else:
        return gameBoard, updatedSnakes, survived, isPlayerDead, deadIndexs

  if move == "right":
    if not headx == width - 1:
      if gameBoard[(height - heady) - 1][headx + 1] == "sh":
        gameBoard, updatedSnakes, survived, isPlayerDead, deadIndexs = calculateHeadCollision(
          gameBoard, snakes, index, move)
      if survived:
        if gameBoard[(height - heady) - 1][headx + 1] == "f":
          consumedFood = True
        if not consumedFood:
          if not gameBoard[(height - tail["y"]) - 1][tail["x"]] == "sh":
            gameBoard[(height - tail["y"]) - 1][tail["x"]] = "x"
          gameBoard[(height - secondLast["y"]) - 1][secondLast["x"]] = "st"
        gameBoard[((height - heady) - 1)][headx + 1] = "sh"
        gameBoard[((height - heady) - 1)][headx] = "sb"
        updatedSnake = updateSnakes(gameBoard, snake, move, index,
                                    consumedFood)
        if deadIndexs != []:
          if index > deadIndexs[0]:
            index -= 1
          if len(deadIndexs) == 2:
            if index + 1 > deadIndexs[1]:
              index -= 1
        newSnakes = copy.deepcopy(updatedSnakes)

        if updatedSnake["health"] <= 0:
          newBoard = removeSnake(gameBoard, updatedSnake)
          newSnakes.pop(index)
          if index == 0:
            isPlayerDead = True
          deadIndexs = [index]
          return newBoard, newSnakes, False, isPlayerDead, deadIndexs

        newSnakes.pop(index)
        newSnakes.insert(index, updatedSnake)
        return gameBoard, newSnakes, survived, isPlayerDead, deadIndexs
      else:
        return gameBoard, updatedSnakes, survived, isPlayerDead, deadIndexs

  if move == "none":
    gameBoard = removeSnake(gameBoard, snake)
    updatedSnakes.remove(snake)
    if index == 0:
      isPlayerDead = True
    deadIndexs = [index]
    survived = False

  return gameBoard, updatedSnakes, survived, isPlayerDead, deadIndexs


def calculateHeadCollision(board, snakeList, index, move):
  snakes = copy.deepcopy(snakeList)
  snake1 = snakes[index]
  snake2 = []
  survived = True
  playerDead = False

  if move == "up":
    headx = snake1["head"]["x"]
    heady = snake1["head"]["y"] + 1
  if move == "down":
    headx = snake1["head"]["x"]
    heady = snake1["head"]["y"] - 1
  if move == "left":
    headx = snake1["head"]["x"] - 1
    heady = snake1["head"]["y"]
  if move == "right":
    headx = snake1["head"]["x"] + 1
    heady = snake1["head"]["y"]
  if move == "none":
    newSnakes = snakes[:]
    newSnakes.pop(index)
    boardCopy = board[:]
    for bodyPiece in snakes[index]["body"]:
      boardCopy[len(board) - bodyPiece['y'] - 1][bodyPiece['x']] = 'x'
    if index == 0:
      playerDead = True
    survived = False
    deadIndexs = [index]
    return boardCopy, newSnakes, survived, playerDead, deadIndexs

  i = 0
  for snake in snakes:
    if snake["head"]["x"] == headx and snake["head"]["y"] == heady:
      snake2 = snake
      snake2Index = i
      break
    i += 1
  isTie = False

  if len(snake1["body"]) == len(snake2["body"]):
    isTie = True

  if not isTie:
    if len(snake1["body"]) < len(snake2["body"]):
      smaller_snake = snake1
      smallSnakeIndex = index
    if len(snake1["body"]) > len(snake2["body"]):
      smaller_snake = snake2
      smallSnakeIndex = snake2Index

  if isTie:
    survived = False
    # both snakes from board
    newSnakes = snakes[:]
    newSnakes.pop(index)
    tempIndex = snake2Index
    if index < snake2Index:
      snake2Index -= 1
    newSnakes.pop(snake2Index)

    boardCopy = board[:]
    boardCopy = removeSnake(boardCopy, snakes[index])
    boardCopy = removeSnake(boardCopy, snakes[tempIndex])
    playerDead = True
    survived = False
    deadIndexs = [index, tempIndex]
    return boardCopy, newSnakes, survived, playerDead, deadIndexs
  else:
    # remove smaller snake from board and snakes list
    newSnakes = snakes[:]
    newSnakes.pop(smallSnakeIndex)
    boardCopy = board[:]
    boardCopy = removeSnake(boardCopy, smaller_snake)
    if smallSnakeIndex == 0:
      playerDead = True
    if smallSnakeIndex == index:
      survived = False
    deadIndexs = [smallSnakeIndex]
    return boardCopy, newSnakes, survived, playerDead, deadIndexs


def removeSnake(board, snake):
  length = len(board)
  newBoard = board[:]
  for piece in snake["body"]:
    x = piece["x"]
    y = piece["y"]
    newBoard[length - y - 1][x] = "x"
  return newBoard


def floodFill(board, xcord, ycord):
  global height, width

  area = 0
  length = width
  queue = []
  freeSquares = getNumberOfFreeSquares(board, xcord, ycord)
  if ycord != (length - 1):
    if freeSquares > 0:
      if (board[((length - 1) - ycord) - 1][xcord] == 'x'
          or board[((length - 1) - ycord) - 1][xcord] == 'f'):
        queue.append([ycord + 1, xcord])

  if ycord != 0:
    if freeSquares > 0:
      if (board[((length - 1) - ycord) + 1][xcord] == 'x'
          or board[((length - 1) - ycord) + 1][xcord] == 'f'):
        queue.append([ycord - 1, xcord])

  if xcord != (length - 1):
    if freeSquares > 0:
      if (board[((length - 1) - ycord)][xcord + 1] == 'x'
          or board[((length - 1) - ycord)][xcord + 1] == 'f'):
        queue.append([ycord, xcord + 1])

  if xcord != 0:
    if freeSquares > 0:
      if (board[((length - 1) - ycord)][xcord - 1] == 'x'
          or board[((length - 1) - ycord)][xcord - 1] == 'f'):
        queue.append([ycord, xcord - 1])

  visited = []

  while queue:
    n = queue.pop()
    if n not in visited:
      visited.append(n)
      if board[((length - n[0]) - 1)][n[1]] == "x" or board[((length - n[0]) -
                                                             1)][n[1]] == "f":
        area += 1
      # Deals with adding Right square
      if n[1] != (length - 1):
        if (board[(length - 1) - n[0]][n[1] + 1] == 'x'
            or board[(length - 1) - n[0]][n[1] + 1] == 'f'):
          queue.append([n[0], n[1] + 1])

      # Deals with adding Up square
      if n[0] != (length - 1):
        if (board[length - 1 - n[0] - 1][n[1]] == 'x'
            or board[length - 1 - n[0] - 1][n[1]] == 'f'):
          queue.append([n[0] + 1, n[1]])

      # Deals with adding Down square
      if n[0] != 0:
        if (board[(length - 1 - n[0]) + 1][n[1]] == 'x'
            or board[(length - 1 - n[0]) + 1][n[1]] == 'f'):
          queue.append([n[0] - 1, n[1]])

      # Deals with adding Left square
      if n[1] != 0:
        if (board[length - 1 - n[0]][n[1] - 1] == "x"
            or board[length - 1 - n[0]][n[1] - 1] == 'f'):
          queue.append([n[0], n[1] - 1])

  return area


def onEdge(snake, board):

  if snake["head"]["x"] == 0 or snake["head"]["x"] == len(board) - 1 or snake[
      "head"]["y"] == 0 or snake["head"]["y"] == len(board) - 1:
    return True
  return False


def hasTrapped(mySnake, eSnake, board):

  myX = mySnake["head"]["x"]
  myY = mySnake["head"]["y"]
  eX = eSnake["head"]["x"]
  eY = eSnake["head"]["x"]

  if eX == 0 and myX == 1:
    return True
  if eX == len(board) - 1 and myX == len(board) - 2:
    return True
  if eY == 0 and myY == 1:
    return True
  if eY == len(board) - 1 and myY == len(board) - 2:
    return True
  return False


def evaluate(board, snake, allSnakes):
  totalScore = 0
  headx = snake["head"]["x"]
  heady = snake["head"]["y"]
  floodfillScore = floodFill(board, headx, heady)
  myLength = len(snake["body"])
  if floodfillScore < myLength:
    totalScore -= 250
  else:
    totalScore += floodfillScore
  distToFood = RouteFinder.findClosestFood(getFood(), snake['head'])[1]
  totalScore += (len(board) - distToFood) / 2
  totalScore += myLength * 2
  if headx == 0 or headx == len(board) - 1:
    totalScore -= 30
  if heady == 0 or heady == len(board) - 1:
    totalScore -= 30
  if headx == 1 or headx == len(board) - 2:
    totalScore -= 15
  if heady == 1 or heady == len(board) - 2:
    totalScore -= 15
  if headx > len(board) / 3 and headx < len(board) - (len(board) / 3):
    totalScore += 10
  if heady > len(board) / 3 and heady < len(board) - (len(board) / 3):
    totalScore += 10
  totalScore += 4 - len(allSnakes) * 30
  distToTail = RouteFinder.findClosestFood([snake["body"][-1]],
                                           snake['head'])[1]
  totalScore += len(board) - distToTail * 1.5
  totalScore += getNumberOfFreeSquares(board, headx, heady)
  for s in allSnakes:
    if not s['id'] == snake['id']:
      totalScore -= 4 - getNumberOfFreeSquares(board, s["head"]["x"],
                                               s["head"]["y"]) * 10
      if s["head"]["x"] == 0 or s["head"]["x"] == len(board) - 1:
        totalScore += 30
      if s["head"]["y"] == 0 or s["head"]["y"] == len(board) - 1:
        totalScore += 30
      if s["head"]["x"] == 1 or s["head"]["x"] == len(board) - 2:
        totalScore += 15
      if s["head"]["y"] == 1 or s["head"]["y"] == len(board) - 2:
        totalScore += 15
      if len(s['body']) < myLength:
        totalScore += 20
        distToSnake = RouteFinder.findClosestFood([s["head"]],
                                                  snake['head'])[1]
        totalScore += (len(board) - distToSnake) * 3
      else:
        distToSnake = RouteFinder.findClosestFood([s["head"]],
                                                  snake['head'])[1]
        totalScore += (len(board) - distToSnake) * -2
        totalScore -= 15
        totalScore += (len(board) - distToFood) * 2

      floodScore = floodFill(board, s["head"]["x"], s["head"]["y"])
      if floodScore < len(s["body"]):
        totalScore += 30
      else:
        totalScore += (len(board) * len(board)) - floodScore
      if onEdge(s, board):
        totalScore += 30
      if hasTrapped(snake, s, board):
        totalScore += 50
  if snake['health'] > 70:
    totalScore += 15
  if snake['health'] < 50:
    totalScore -= 20
  return totalScore


def resetGameBoard():
  global gameBoard
  gameBoard = [['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
               ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
               ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
               ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
               ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
               ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
               ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
               ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
               ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
               ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
               ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x']]


def resetFood():
  global foodLocation
  foodLocation = []


def getBoard():
  return gameBoard


def getHeight():
  global width
  return height


def getWidth():
  global width
  return width


def getFood():
  global foodLocation
  return foodLocation


def setBoard(board):
  global gameBoard
  gameBoard = copy.deepcopy(board)


def prettyPrint(board):
  print("\n")
  for r in board:
    print(r)
