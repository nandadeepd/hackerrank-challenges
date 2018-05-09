def group(numbers, groupLen):
  for i in range(0, len(numbers), groupLen):
    val = numbers[i:i + groupLen]
    if len(val) == groupLen:
      yield tuple(val)

def solution(A, E):
    # write your code in Python 3.6
    
    # reshaping the nodes with their edges
    groups = group(E, 2)
    # count longest path with same labels
    counter = 0
    for eachNodePair in groups:
        labelFrom, labelTo = A[eachNodePair[0] - 1], A[eachNodePair[1] - 1]
        if labelFrom == labelTo:
            counter += 1
    return counter 
