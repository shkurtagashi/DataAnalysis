#Libraries
import pandas
from pandas import DataFrame # In order to write into the .csv file we can use the pandas module
import os
from pylab import *


def features_sheet(dir_part, path_part, dir_final, path_final):
    # Compute the features from PART1
    part = pandas.read_csv(str(os.path.join(dir_part, path_part)))  # read the PART we're interesting in
    EdaPart = part['EDA_Normalized']  # read the EDA from the PART we're interesting in
    # Mean
    mean = np.mean(EdaPart)
    # Std
    std = np.std(EdaPart)
    # Number of peaks
    indices = indexes(EdaPart, thres=0.01, min_dist=4)
    x = indices
    y = [EdaPart[j] for j in indices]
    numpeak = len(y)

    # Average Amplitude of peaks
    avpeak = np.mean(y)

    # Create the feature sheet and store it
    data = {'Mean': [mean], 'Standard deviation': [std], 'Number of peaks': [numpeak],
            'Average peaks amplitude': [avpeak]}
    frame = DataFrame(data)
    frame.to_csv(str(os.path.join(dir_final, path_final)), index=False)

# To create a sheet with the correlation (e.g participants, correlation)
# dir_part -- is the directory where the PARTx.csv is stored
# teacher_path_part -- is the final part of the path for teacher e.g "PART1.csv"
# student_path_part -- is the final part of the path for student e.g "PART1.csv"
# file_path_part -- is the name of the file 'PARTx.csv'
# dir_final -- is the directory where we want to store the sheet
# path_final -- is the final part of the path e.g "Correlation_T006_R_PART1.csv"
