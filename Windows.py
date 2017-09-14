#Libraries
from scipy.spatial.distance import euclidean
from fastdtw import fastdtw

# Returns an array of results of the function fun, computed over windows of length  = window_size.
# stride is the overlapping step.See the example to understand how it works.
# if you want no overlapping windows stride = window_size
def windowing(data,fun,window_size,stride):
    result_wind = [fun(data[i:i+window_size]) for i in range(0, len(data), stride)
                   if i+window_size < len(data) ]
    return result_wind


def windowingForCorrelations(dataSet1, dataSet2, fun, window_size, stride):
    results = [fun(dataSet1[i:i+window_size], dataSet2[i:i+window_size]) for i in range(0, len(dataSet1), stride)
                   if i+window_size < len(dataSet1) ]
    return results


# Returns an array of chunks, computed over windows of length  = window_size.
# stride is the overlapping step.See the example to understand how it works.
# if you want no overlapping windows stride = window_size
def windows(data,window_size,stride):
    wind = [(data[i:i+window_size]) for i in range(0, len(data), stride)
                   if i+window_size < len(data) ]
    return wind


def windowingForDTW(dataSet1, dataSet2, window_size, stride):
    distance = [fastdtw(dataSet1[i:i+window_size], dataSet2[i:i+window_size], dist=euclidean) for i in range(0, len(dataSet1), stride)
                   if i+window_size < len(dataSet1) ]
    return distance
