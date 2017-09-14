import matplotlib.pyplot as plt
import csv
from datetime import *
from datetime import timedelta
import os
from pylab import *
from WriteExcel import twoColumnCSV




# This function extracts EDA values from the csv file.
# The input of the function is the path of the file.
def eda_extraction(str):
    eda = [];

    with open(str, 'rt') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')

        for row in spamreader:
            eda.append(', '.join(row))
    return eda


# This function generates the time for each EDA value based on the first timestamp and the sampling rate.
# First timestamp is the first row in EDA.csv file
# Sampling rate is the second row in EDA.csv file
def time_extraction(eda):
    i = 0;
    time = [];
    for i in range(len(eda)):
        time.append(datetime.datetime.fromtimestamp(float(eda[0])) + timedelta(
            minutes=float((i / 4.0) / 60)))  # the time is expressed in minutes
    return time


# This function extracts the indeces of the time list that corresponds to the defined time interval
def interval(time, beg, en):
    j = 0;
    interv = [];

    for j in range(len(time)):
        if time[j] == beg:
            beginning = j

        if time[j] == en:
            end = j

    interv = [beginning, end]
    return interv


# This function extracts EDA values from the new csv files. It's created only for TESTING purposes in the end.
def eda_extraction2(str):
    eda = [];

    with open(str, 'rt') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
        next(spamreader)

        for row in spamreader:
            eda.append(''.join(row[1]))
    return eda


# This function extracts Time values from the new csv files.
# i.e csv file has columns Time, EDA_Normalized, it extracts only Time
# def time_extraction2(str):
#     time = [];

#     with open(str, 'rt') as csvfile:
#         spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
#         next(spamreader)

#         for row in spamreader:
#             time.append(float(row[0])
#     return time

# To divide the EDA_Normalized in to two parts (PART1 -from beginning to break_beg- and PART2 from break_end to end)
# edaframe -- is EDA_Normalized csv converted into a pandas DataFrame
# start --  is the starting time of the PART (e.g beginning for PART1 and break_end for PART2)
# end -- is the ending time of the PART (e.g break_beg for PART1 and end for PART2)
# dir_final -- is the directory where we want to store the PARTx.csv
# path_final -- is the final part of the path e.g "PART1.csv"

def part_div(edaframe, start, end, dir_final, path_final):
    time = edaframe['time']  # extract the time from the dataframe
    interv = interval(time, start, end)  # extract the interval of interest from the time
    part = edaframe[interv[0]:interv[1]]  # extract the EDA and the time values related to the interval of interest
    part.to_csv(str(os.path.join(dir_final, path_final)), index=False)

# To create a sheet with the extracted features (e.g mean, std, num.of.peaks and average amplitude of peaks)
# dir_part -- is the directory where the PARTx.csv is stored
# path_part -- is the final part of the path e.g "PART1.csv"
# end -- is the ending time of the PART (e.g break_beg for PART1 and end for PART2)
# dir_final -- is the directory where we want to store the sheet
# path_final -- is the final part of the path e.g "PART1_Features .csv"



def generate_eda_time_file(edaPath, edaTimePath):
    # 1. Extract EDA values from CSV file
    edaRawValues = eda_extraction(edaPath)

    # 2. Generate Time values based on the first timestamp
    edaRawTime = time_extraction(edaRawValues)

    # Deleting the first two values from EDA and last two for Time
    del edaRawValues[0]
    del edaRawValues[0]

    del edaRawTime[len(edaRawTime)-1]
    del edaRawTime[len(edaRawTime)-1]

    #Generating new EDA file with Time values
    twoColumnCSV(edaTimePath, edaRawTime, edaRawValues)
