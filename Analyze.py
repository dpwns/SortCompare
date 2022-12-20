import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import os
import dataframe_image as dfi

# Load Data
N_list=[100,200,500,1000,2000,3000,4000,5000]
SortingType = ["Quick 1", "Quick 2", "Quick 3", "Heap"]
result_List = []
data_List = [[] for _ in range(len(N_list))]
for i in range(len(N_list)):
    result_List.append(pd.read_csv("N"+str(N_list[i])+"/Result.csv"))
    for j in range(4):
        data_List[i].append(pd.read_csv("N"+str(N_list[i])+"/SortType"+str(j)+".csv"))
    for j in range(4):
        data_List[i][j]['Type'] = SortingType[j]

# Check Dirctory
if not os.path.isdir(os.getcwd()+"/Analyze"):
    os.mkdir("Analyze")


if not os.path.isdir(os.getcwd()+"/Analyze/Average"):
    os.mkdir("Analyze/Average")


if not os.path.isdir(os.getcwd()+"/Analyze/StandardDeviation"):
    os.mkdir("Analyze/StandardDeviation")


if not os.path.isdir(os.getcwd()+"/Analyze/Compare"):
    os.mkdir("Analyze/Compare")

if not os.path.isdir(os.getcwd()+"/Analyze/Compare/Best"):
    os.mkdir("Analyze/Compare/Best")

if not os.path.isdir(os.getcwd()+"/Analyze/Compare/Worst"):
    os.mkdir("Analyze/Compare/Worst")


if not os.path.isdir(os.getcwd()+"/Analyze/Swap"):
    os.mkdir("Analyze/Swap")

if not os.path.isdir(os.getcwd()+"/Analyze/Swap/Best"):
    os.mkdir("Analyze/Swap/Best")

if not os.path.isdir(os.getcwd()+"/Analyze/Swap/Worst"):
    os.mkdir("Analyze/Swap/Worst")


if not os.path.isdir(os.getcwd()+"/Analyze/Time"):
    os.mkdir("Analyze/Time")

if not os.path.isdir(os.getcwd()+"/Analyze/Time/Best"):
    os.mkdir("Analyze/Time/Best")

if not os.path.isdir(os.getcwd()+"/Analyze/Time/Worst"):
    os.mkdir("Analyze/Time/Worst")


dataType = ['Time','Swap','Compare']

for i in range(len(N_list)):
    temp = pd.concat([data_List[i][j] for j in range(4)])
    
    # Save graph
    for dataTypeName in dataType:
        plt.clf()
        ax = sns.stripplot(data=temp,x='Type',y=dataTypeName,size=1)
        plt.title = "N"+str(N_list[i])
        plt.savefig("Analyze/"+dataTypeName+"/"+dataTypeName+"_N"+str(N_list[i])+".png")
    print("N"+str(N_list[i])+" graph finished")
    
    # Worst Case
    for dataTypeName in dataType:
        worstDict = {'Time':[],'Swap':[],'Compare':[]}
        worstIndex=[]
        for j in range(4):
            temp = data_List[i][j].loc[data_List[i][j][dataTypeName].idxmax()]
            worstDict['Time'].append(temp['Time'])
            worstDict['Swap'].append(temp['Swap'])
            worstDict['Compare'].append(temp['Compare'])
            worstIndex.append(temp['Type'])
            
            worstDataframe = pd.DataFrame(data=worstDict,index=worstIndex)
            
            dfi.export(worstDataframe, "./Analyze/"+dataTypeName+"/Worst/N"+str(N_list[i])+"WorstCase.png")
    print("N"+str(N_list[i])+" worst case finished")
    
    # Best Case
    for dataTypeName in dataType:
        bestDict = {'Time':[],'Swap':[],'Compare':[]}
        bestIndex=[]
        for j in range(4):
            temp = data_List[i][j].loc[data_List[i][j][dataTypeName].idxmin()]
            bestDict['Time'].append(temp['Time'])
            bestDict['Swap'].append(temp['Swap'])
            bestDict['Compare'].append(temp['Compare'])
            bestIndex.append(temp['Type'])
            
            bestDataframe = pd.DataFrame(data=bestDict,index=bestIndex)
            
            dfi.export(bestDataframe, "./Analyze/"+dataTypeName+"/Best/N"+str(N_list[i])+"BestCase.png")
    print("N"+str(N_list[i])+" best case finished")
    
    # Average
    AvrDict = {'Time':[],'Swap':[],'Compare':[]}
    avrIndex=[]
    for j in range(4):
        for dataTypeName in dataType:
            AvrDict[dataTypeName].append(sum(data_List[i][j][dataTypeName]) / len(data_List[i][j][dataTypeName]))
        avrIndex.append(data_List[i][j]['Type'][0])
    avrDataframe = pd.DataFrame(data=AvrDict,index=avrIndex)
    dfi.export(avrDataframe, "./Analyze/Average/N"+str(N_list[i])+"Average.png")
    print("N"+str(N_list[i])+" average finished")
    
    # Standard Deviation
    StdDict = {'Time':[],'Swap':[],'Compare':[]}
    stdIndex=[]
    for j in range(4):
        for dataTypeName in dataType:
            StdDict[dataTypeName].append(np.std(data_List[i][j][dataTypeName]))
        stdIndex.append(data_List[i][j]['Type'][0])
    avrDataframe = pd.DataFrame(data=StdDict,index=stdIndex)
    dfi.export(avrDataframe, "./Analyze/StandardDeviation/N"+str(N_list[i])+"StandardDeviation.png")
    print("N"+str(N_list[i])+" standard deviation finished")