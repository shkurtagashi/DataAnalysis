# This function generates a new csv file
    # arr -- is the array we want to write in the file
    # path -- is the place where we want to save the file
def write_excel(arr, path):
    df = DataFrame(arr)
    df.to_csv(path, sheet_name='sheet1', index=False)
    return


# This function generates a CSV file with two columns for the whole signal
# path -- is the path where the new file should be saved in String format
# list1 --  is the data that you want to put in the first column
# list2 -- is the data that you want to put in the second column
def twoColumnCSV(path, list1, list2):
    f = open(path, 'w')

    for i, j in zip(list1, list2):
        f.write(str(i) + "," + str(j) + "\n")
    f.close()

# If you want to choose interval
# def twoColumnCSV(path, list1, list2, interval):
#     f=open(path,'w')
#
#     for i,j in zip(list1[interval[0]:interval[1]], list2[interval[0]:interval[1]]):
#         f.write(str(i)+ "," + str(j) + "\n")
#     f.close()