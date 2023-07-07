import Board,moveLogic,copy,itertools,time
timer = 0
def paranoid(alpha, beta, depth, turn, oldBoard,currentBoard,oldSnakes,currentSnakes,prevMove,mySnake):
  bestMove = prevMove

  #Depth is 0 return the evaluation
  if depth == 0 or mySnake == []:  
    if mySnake == []:
      return float('-inf'),prevMove
    myEval = Board.evaluate(currentBoard, mySnake, currentSnakes)
    return myEval,prevMove

  #Is max turns
  if turn == "Max":
    bestScore = float("-inf")
    if time.time() - timer > 0.38:
      score = Board.evaluate(currentBoard,mySnake,currentSnakes)
      if score > bestScore:
        return(score,bestMove)
      else:
        return bestScore,bestMove
    turn = "min"
    moves = moveLogic.generateMoves(oldBoard,mySnake,oldSnakes)
    #if max has no moves return negative inf
    if moves == []:
      return float("-inf"),prevMove
    #loop through each move of max player and continue search
    for move in moves:
      copyOfMe = copy.deepcopy(mySnake)
      boardCopy = copy.deepcopy(currentBoard)
      newBoard,newSnakes,survived,isPlayerDead,deadIndex = Board.doMove(move,copyOfMe,boardCopy,0,currentSnakes)
      if survived:
        v,newMove = paranoid(alpha,beta,depth-1,turn,oldBoard,newBoard,oldSnakes,newSnakes,move,newSnakes[0])
        bestScore = max(bestScore,v)
        if bestScore == v:
          bestMove = move
        if bestScore >= beta:
          return bestScore,move
        alpha = max(alpha,bestScore)
      else:
        return float("-inf"),prevMove
  else:
    #is mins turn
    bestScore = float("inf")
    if time.time() - timer > 0.38:
      score = Board.evaluate(currentBoard,mySnake,currentSnakes)
      if score < bestScore:
        return(score,bestMove)
      else:
        return bestScore,bestMove
    enemies = oldSnakes[1:]
    turn = "Max"
    moves = []
    #generate possible moves for each minimizing snake

    for s in enemies:
      possible_moves = ["left","up","down","right"]
      possible_moves = moveLogic.generateMoves(oldBoard, s, oldSnakes)
      moves += [possible_moves]
      if possible_moves == []:
        currentBoard = Board.removeSnake(currentBoard, s)
        currentSnakes.remove(s)
    if moves == [[]]:
      return float("inf"),prevMove
      
    #create cartesian product
    moveList = itertools.product(*moves)

    #start looping through moveSets
    for moveSet in moveList:
      index = 0
      newBoard =copy.deepcopy(currentBoard)
      newSnakes = copy.deepcopy(currentSnakes)
      playerDies = False
    
      for move in moveSet:
        copyOfCurrent = copy.deepcopy(currentSnakes[index+1])
        newBoard,newSnakes,survived,isPlayerDead,deadIndexs = Board.doMove(move,copyOfCurrent,newBoard,index+1,newSnakes)
        if len(newSnakes) != len(currentSnakes):
          index -= (len(currentSnakes) - len(newSnakes) + 1 )
        if isPlayerDead == True:
          playerDies = True
        index +=1
      if playerDies:
        return(float('-inf'),prevMove)
      else:
        if time.time() - timer > 0.38:
          score = Board.evaluate(currentBoard,mySnake,currentSnakes)
          if score < bestScore :
            return(score,bestMove)
          else:
            return bestScore,bestMove
        if len(newSnakes) != 1:
          v,newMove = paranoid(alpha,beta,depth-1,turn,newBoard,newBoard,newSnakes,newSnakes,prevMove,mySnake)
        else:
          return(float("inf"),prevMove)
      bestScore = min(bestScore,v)
      beta = min(beta,bestScore)
      if bestScore <= alpha:
        return bestScore, prevMove
      if beta == bestScore:
        bestMove = newMove


  return bestScore,bestMove

