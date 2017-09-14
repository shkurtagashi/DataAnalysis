#Step 1 - Preparing EDA.csv for other steps - EDA_Raw.csv including timestamp as well
from EDA import *
import pandas

edaPath ='/Users/shkurtagashi/Desktop/PhD/Energieinformatik17/DataAnalysis/Data/10.09/EDA.csv'
edaTimePath = '/Users/shkurtagashi/Desktop/PhD/Energieinformatik17/DataAnalysis/Data/10.09/EDA_Raw.csv'


generate_eda_time_file(edaPath, edaTimePath)

info = pandas.read_csv(str(os.path.join("/Users/shkurtagashi/Desktop/PhD/Energieinformatik17/DataAnalysis/Data/10.09/", 'information.csv')))
print info