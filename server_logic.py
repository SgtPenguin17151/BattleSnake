import random, Board, moveLogic, time, paranoid


def choose_move(data: dict) -> str:
  Board.resetGameBoard()
  Board.resetFood()
  moveLogic.stateMap = {}

  height = data["board"]["height"]
  width = data["board"]["width"]
  snakes = data["board"]["snakes"]
  food = data["board"]["food"]
  my_head = data["you"]["head"]

  for snake in snakes:
    if snake["id"] == data["you"]["id"]:
      mySnake = snake
  print(data["you"] == mySnake)

  Board.fillGameBoard(snakes, food, height)

  possible_moves = ["up", "down", "left", "right"]
  possible_moves = moveLogic.avoid_other_snakes(my_head, snakes,
                                                possible_moves)
  possible_moves = moveLogic.avoid_walls(my_head, width, height,
                                         possible_moves)
  possible_moves = moveLogic.checkForHeadCollision(mySnake, snakes,
                                                   possible_moves,
                                                   Board.getBoard())

  index = 0
  for s in snakes:
    if s["id"] == data["you"]["id"]:
      snakes.pop(index)
    index += 1
  snakes.insert(0, mySnake)

  pinf = float('inf')
  ninf = float('-inf')
  boardCopy = Board.getBoard()[:]
  bestMove = random.choice(possible_moves)
  move = random.choice(possible_moves)

  if data['turn'] >= 3:
    if len(possible_moves) > 1:
      paranoid.timer = time.time()
      start = time.time()
      depth = 2
      while (time.time() - start) < 0.38:
        result = (paranoid.paranoid(ninf, pinf, depth, "Max", boardCopy,
                                    boardCopy, snakes, snakes, "initial",
                                    mySnake))
        if (time.time() - start) < 0.4:
          bestMove = result[1]
          moveLogic.stateMap[str(boardCopy)] = bestMove
          depth += 2
      if bestMove in possible_moves:
        print(result)
        move = bestMove
      else:
        print("Broken")
        print(result)
        print(possible_moves)
        move = random.choice(possible_moves)

  print(
    f"{data['game']['id']} MOVE {data['turn']}: {move} picked from all valid options in {possible_moves}"
  )
  return move
