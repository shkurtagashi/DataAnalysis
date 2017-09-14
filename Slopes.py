#Libraries

def calculateSlope(y):
    avgSlope = 0
    allSlopes = 0

    for i in range(0, len(y)-1):  # iterate through all pts not at boundaries
        slope = y[i+1]-y[i]
        allSlopes = allSlopes + slope
    avgSlope = allSlopes/len(y)
    return avgSlope

def windowingSlope(data, window_size, stride):
    result_wind = [calculateSlope(data[i:i+window_size]) for i in range(0, len(data), stride)
                   if i+window_size <= len(data) ]
    return result_wind

def windowsSlope(data,window_size,stride):
    wind = [(data[i:i+window_size]) for i in range(0, len(data), stride)
                   if i+window_size <= len(data) ] #I made a little change here in the condition "<=" because it wasnt including the last window
    return wind