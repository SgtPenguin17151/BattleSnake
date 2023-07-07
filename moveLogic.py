import Board

stateMap = {}

def avoid_self(my_head,snakes,possible_moves,index):
  currentSnake = snakes[index]
  if currentSnake["body"][1]['x'] == my_head["x"] + 1 and my_head["y"] == currentSnake['body'][1]["y"] and "right" in possible_moves:
    possible_moves.remove("right")
  if currentSnake["body"][1]['x'] == my_head["x"] -1 and  my_head["y"] == currentSnake['body'][1]["y"] and "left" in possible_moves:
    possible_moves.remove("left")
  if currentSnake["body"][1]['y'] == my_head["y"] + 1 and  my_head["x"] == currentSnake['body'][1]["x"] and "up" in possible_moves:
    possible_moves.remove("up")
  if currentSnake["body"][1]['y'] == my_head["y"] - 1 and    my_head["x"] == currentSnake['body'][1]["x"] and "down" in possible_moves:
    possible_moves.remove("down")
  return possible_moves

def avoid_other_snakes(my_head, enemy_snake,possible_moves):

    for s in enemy_snake:
      current_snake = s["body"][:-1]
      for snake_body in current_snake:
          if my_head["x"] == snake_body["x"] + 1 and my_head[
                  "y"] == snake_body["y"] and "left" in possible_moves:
              possible_moves.remove("left")
          if my_head["x"] == snake_body["x"] - 1 and my_head[
                  "y"] == snake_body["y"] and "right" in possible_moves:
              possible_moves.remove("right")
          if my_head["y"] == snake_body["y"] + 1 and my_head[
                  "x"] == snake_body["x"] and "down" in possible_moves:
              possible_moves.remove("down")
          if my_head["y"] == snake_body["y"] - 1 and my_head[
                  "x"] == snake_body["x"] and "up" in possible_moves:
              possible_moves.remove("up")
    return possible_moves


def avoid_walls(my_head, width, height,possible_moves):
    if my_head["x"] == width - 1 and "right" in possible_moves:
        possible_moves.remove("right")
    if my_head["x"] == 0 and "left" in possible_moves:
        possible_moves.remove("left")
    if my_head["y"] == 0 and "down" in possible_moves:
        possible_moves.remove("down")
    if my_head["y"] == height - 1 and "up" in possible_moves:
        possible_moves.remove("up")
    return possible_moves

def checkForHeadCollision(my_snake,snakes,possible_moves,board):
  newMoves = possible_moves[:]
  for s in snakes:
    if s["id"] == my_snake["id"]:
      continue

    if "left" in newMoves:
      if (s["head"]["y"] - 1 == my_snake["head"]["y"] or s["head"]["y"] + 1 == my_snake["head"]["y"] or s["head"]["y"] == my_snake["head"]["y"]) and ((s["head"]["x"] == my_snake["head"]["x"]-2) or my_snake["head"]["x"] - 1 == s["head"]["x"]):
        if(len(my_snake["body"]) <= len(s["body"])):
          newMoves.remove("left")

    if "right" in newMoves: 
      if (s["head"]["y"] - 1 == my_snake["head"]["y"] or s["head"]["y"] + 1 == my_snake["head"]["y"] or s["head"]["y"] == my_snake["head"]["y"] ) and ((s["head"]["x"] == my_snake["head"]["x"]+2) or my_snake["head"]["x"] + 1 == s["head"]["x"]):
        if(len(my_snake["body"]) <= len(s["body"])):
          newMoves.remove("right")

    if "down" in newMoves:
      if (s["head"]["y"] + 2 == my_snake["head"]["y"] or s["head"]["y"] + 1 == my_snake["head"]["y"] ) and ((s["head"]["x"] == my_snake["head"]["x"]+1) or my_snake["head"]["x"]-1 == s["head"]["x"] or my_snake["head"]["x"] == s["head"]["x"]):

        if(len(my_snake["body"]) <= len(s["body"])):
          newMoves.remove("down")

    if "up" in newMoves:
      if (s["head"]["y"] - 2 == my_snake["head"]["y"] or s["head"]["y"] - 1 == my_snake["head"]["y"]) and ((s["head"]["x"] == my_snake["head"]["x"]+1) or my_snake["head"]["x"]-1 == s["head"]["x"] or my_snake["head"]["x"] == s["head"]["x"] ):
        if(len(my_snake["body"]) <= len(s["body"])):
          newMoves.remove("up")

  if newMoves == []:
    return possible_moves

  return newMoves


def generateMoves(board,snake,enemies):
  global stateMap
  moves = ["left","up","down","right"]
  moves = avoid_other_snakes(snake["head"],enemies,moves)
  moves = avoid_walls(snake["head"],Board.getWidth(),Board.getHeight(),moves)
  moves = checkForHeadCollision(snake,enemies,moves,board)
  if str(board) in stateMap:
      bestMove = stateMap[str(board)]
      if bestMove in moves and len(moves) > 1:
          moves.remove(bestMove)
          moves[0] = bestMove

  return moves