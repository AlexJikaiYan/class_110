import plotly.express as px
import pandas as pd
import plotly.figure_factory as pf
import statistics as st
import random as ran
import plotly.graph_objects as go
import csv 
df=pd.read_csv("newdata.csv")
data=df["average"].tolist()
populationmean=st.mean(data)
populationmedian=st.median(data)
populationmode=st.mode(data)
print("mean:",populationmean,"median:",populationmedian,"mode:",populationmode)
def randomsetmean(counter):
    dataset=[]
    for i in range(0,counter):
        randomindex=ran.randint(0,len(data)-1)
        value=data[randomindex]
        dataset.append(value)
        mean=st.mean(dataset)
    return mean
def showfigure(meanlist):
    df=meanlist
    mean=st.mean(df)
    figure=pf.create_distplot([df],["average"],show_hist=False)
    figure.add_trace(go.Scatter(x=[mean,mean],y=[0,1]))
    figure.show()
def setup():
    meanlist=[]
    for i in range(0,1000):
        setupmean= randomsetmean(100)
        meanlist.append(setupmean)
    showfigure(meanlist)
    mean=st.mean(meanlist)
    print(mean)
setup()
def standarddeviation():
    meanlist=[]
    for i in range(0,1000):
        setupmean=randomsetmean(100)
        meanlist.append(setupmean)
    stdevmeanlist=st.stdev(meanlist)
    print(stdevmeanlist)
standarddeviation()


    



