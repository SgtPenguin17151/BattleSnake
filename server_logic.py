import random, Board, moveLogic, time, paranoid

def choose_move(data: dict) -> str:
  Board.resetGameBoard()
  Board.resetFood()

  height = data["board"]["height"]
  snakes = data["board"]["snakes"]
  food = data["board"]["food"]

  for snake in snakes:
    if snake["id"] == data["you"]["id"]:
      mySnake = snake
  print(data["you"] == mySnake)

  Board.fillGameBoard(snakes, food, height)

  enemies = snakes[:]
  for ids, s in enumerate(enemies):
    if s["id"] == data["you"]["id"]:
      enemies.pop(ids)
    
  possible_moves = moveLogic.generateMoves(Board.getBoard(),data["you"],enemies)

  boardCopy = Board.getBoard()[:]
  bestMove = possible_moves[0]

  if data['turn'] >= 3:
    if len(possible_moves) > 1:
      paranoid.timer = time.time()
      start = time.time()
      depth = 2
      while (time.time() - start) < 0.38:
        result = (paranoid.paranoid(float('-inf'), float('inf'), depth, "Max", boardCopy,
                                    boardCopy, snakes, snakes, "initial",
                                    mySnake))
        if (time.time() - start) < 0.4:
          bestMove = result[1]
          depth += 1
      else:
        print("Broken")
        print(result)
        print(possible_moves)
        bestMove = random.choice(possible_moves)

  print(
    f"{data['game']['id']} MOVE {data['turn']}: {bestMove} picked from all valid options in {possible_moves}"
  )
  return bestMove
