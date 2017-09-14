#Libraries
import csv
import pandas
from pandas import DataFrame # In order to write into the .csv file we can use the pandas module
from scipy.stats.stats import pearsonr
import os
from scipy.spatial.distance import euclidean
from fastdtw import fastdtw
from pylab import *

# This function computes the Pearson correlation between two variables sig1 and sig2
# beg, en -- beginning and end of the session
# time1, time2 -- extracted times for both signals
# sig1, sig2 -- normalized signals for two participants
# interval1, interval2 -- indeces of defined time interval for both signals
# strin1, strin2 -- name of the two participants (i.e T006_R and S046)
def corr_bar(beg, en, time1, time2, sig1, sig2, interval1, interval2, strin1,
             strin2):  # sig1 and sig2 should be the normalized signal
    sess = session(beg, en)  # list of 4 min sessions in the timeslot beg-end
    timestamp = []
    corr = []
    init1 = []
    init2 = []
    sig1 = map(lambda x: float(x), sig1)
    sig2 = map(lambda x: float(x), sig2)

    sig1 = list(sig1)
    sig2 = list(sig2)
    for i in range(len(sess)):
        ses = sess[i]  # i-th timeslot
        indices1 = interval(time1, ses[0], ses[1])  # indices of the timeslot related to the beg and end
        indices2 = interval(time2, ses[0], ses[1])  # indices are different if are extracted from time1 or time2
        init1.append(indices1[0])  # list of timestamp of the timeslot'beginning
        init2.append(indices2[0])
        corr.append(pearsonr(sig1[indices1[0]:indices1[1]], sig2[indices2[0]:indices2[
            1]]))  # pearson correlation between the two signals in each timeslot
        timestamp.append(ses[0])
    # initt1.append(indicest1)
    df2 = pandas.DataFrame(corr, timestamp, columns=['correlation coefficient', 'p-value'])
    plt.figure()
    df2.plot.bar(title='Pearson Correlation between' + ' ' + strin1 + ' &' + strin2)


def correlation_sheet(dir_part, teacher_path_part, student_path_part, file_path_part, dir_final, path_final):
    # Compute the features from PART1
    partT = pandas.read_csv(
        str(os.path.join(dir_part, teacher_path_part, file_path_part)))  # read the T_PART we're interesting in
    partS = pandas.read_csv(
        str(os.path.join(dir_part, student_path_part, file_path_part)))  # read the S_PART we're interesting in

    EdaPartT = partT['EDA_Normalized']  # read the EDA from the PART we're interesting in
    EdaPartS = partS['EDA_Normalized']  # read the EDA from the PART we're interesting in

    # Correlation
    correlation = pearsonr(EdaPartT, EdaPartS)

    # Create the feature sheet and store it
    data = {'Value of Correlation': [correlation], 'Participants': [teacher_path_part + "_" + student_path_part]}

    frame = DataFrame(data)

    fileToSave = str(os.path.join(dir_final, path_final))
    if (os.path.exists(fileToSave)):
        fileToOpen = open(fileToSave, "a")
        #         fileToOpen.write(frame)
        fwriter = csv.writer(fileToOpen, delimiter=',', quotechar=' ', quoting=csv.QUOTE_MINIMAL)
        fwriter.writerow(["{},{}".format(teacher_path_part + "_" + student_path_part, '"' + str(correlation) + '"')]);
    else:
        frame.to_csv(str(os.path.join(dir_final, path_final)), index=False)


def dtw_correlation_sheet(dir_part, teacher_path_part, student_path_part, file_path_part, dir_final, path_final):
    partT = pandas.read_csv(
        str(os.path.join(dir_part, teacher_path_part, file_path_part)))  # read the T_PART we're interesting in
    partS = pandas.read_csv(
        str(os.path.join(dir_part, student_path_part, file_path_part)))  # read the S_PART we're interesting in

    EdaPartT = partT['EDA_Normalized']  # read the EDA from the PART we're interesting in
    EdaPartS = partS['EDA_Normalized']  # read the EDA from the PART we're interesting in

    # Correlation
    #     correlation = pearsonr(EdaPartT, EdaPartS)
    distance, path = fastdtw(EdaPartT, EdaPartS, dist=euclidean)

    # Create the feature sheet and store it
    data = {'Distance': [distance], 'Participants': [teacher_path_part + "_" + student_path_part], }
    dtwPath = {'Wraping path': [path]}

    frame = DataFrame(data)
    framePath = DataFrame(dtwPath)

    #     framePath.to_csv(str(os.path.join(dir_final,"Path" + student_path_part + path_final)), index=False)

    fileToSave = str(os.path.join(dir_final, path_final))

    if (os.path.exists(fileToSave)):
        fileToOpen = open(fileToSave, "a")
        #         fileToOpen.write(frame)
        fwriter = csv.writer(fileToOpen, delimiter=',', quotechar=' ', quoting=csv.QUOTE_MINIMAL)
        fwriter.writerow(["{},{}".format(str(distance), teacher_path_part + "_" + student_path_part)]);
    else:
        frame.to_csv(str(os.path.join(dir_final, path_final)), index=False)


def theSumOfPositiveElements(correlationCoefs):
    positiveSum = 0
    negativeSum = 0

    for x in correlationCoefs:
        if x > 0:
            positiveSum = positiveSum + x
        elif x <= 0:
            negativeSum = negativeSum + abs(x)

    result = positiveSum / negativeSum  # result of the sum of positive correlations/negative corr
    result = np.log(result)  # natural logarithmic transformation of the result because of the skew inherent in ratios

    return result