def europaExploration(inputData): 
    if not inputData: # To check if Input Data is present
        return "Error: No input data"
    x_upper, y_upper = inputData[0].split()
    if int(x_upper) < 0 or int(y_upper) < 0: # To check if Dimensions are valid
        return "Error: Invalid Plateau Dimensions"
    if (len(inputData) - 1) % 2 != 0: # To check if the input has the correct parameters
        return "Error: Invalid number of robot lines"
    r_compass = {'N': 'E', 'W': 'N', 'E': 'S', 'S': 'W'}
    l_compass = { 'N':'W', 'W':'S', 'S':'E', 'E':'N' }
    res = []
    for i in range(1,len(inputData), 2):
        x_str, y_str, dir_str = inputData[i].split()
        pos = [int(x_str), int(y_str), dir_str]
        curr = pos[2]
        directions = inputData[i+1]
        for dir in directions:
            if dir == 'L':
                curr = l_compass[curr]
            elif dir == 'R':
                curr = r_compass[curr]
            elif dir == 'M':
                if curr == 'N':
                    pos[1]+=1
                elif curr == 'S':
                    pos[1] -=1
                elif curr == 'E':
                    pos[0]+=1
                elif curr == 'W':
                    pos[0]-=1
                if not 0<=pos[0]<=int(x_upper) or not 0<=pos[1]<=int(y_upper):  # Error scenario if the Robot goes out of bounds
                    pos[2] = 'Robot Out of Bounds'
                    res.append(pos)
                    lines = [f"{x} {y} {d}" for x, y, d in res]
                    return "\n".join(lines)
            else:
                return 'Error: Invalid Input'
            pos[2] = curr
        res.append(pos)
    lines = [f"{x} {y} {d}" for x, y, d in res]
    return "\n".join(lines)

    
    
    
if __name__ == '__main__':
    inputData = [
    "15 15",
    "1 2 N",
    "LMLMLMLMMMMMMLMRMRMRM",
    "3 3 E",
    "MMRMMRMRRM",
    "3 4 S",
    "LMLMLMLMM",
    "3 3 E",
    "MMRMMRMRRM",
    "1 2 S",
    "LMLMLMLMM",
    "3 3 E",
    "MMRMMRMRRM"
    ]
    output = europaExploration(inputData)
    print(output)
