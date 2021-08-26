import pandas as pd
import random
import csv
import statistics as st
import plotly.figure_factory as ff 
import plotly.graph_objects as go 
df=pd.read_csv('https://raw.githubusercontent.com/whitehatjr/datasets/master/interventions_data/School1.csv')
# df=pd.read_csv('https://raw.githubusercontent.com/whitehatjr/datasets/master/studentMarks.csv')
data=df['Math_score'].tolist()
# fig=ff.create_distplot([data],['Mathscore'],show_hist=False)
# fig.show()
# mean1=st.mean(data)
# stdev=st.stdev(data)
# print('mean of population ',mean1)
# print('standard deviation of population ',stdev)

def random_set_of_mean(counter):
    dataset = []
    for i in range(0, counter):
        random_index= random.randint(0,len(data)-1)
        value = data[random_index]
        dataset.append(value)
    mean = st.mean(dataset)
    return mean
meanlist=[]
for i in range (0,1000):
    set_of_means=random_set_of_mean(100)
    meanlist.append(set_of_means)
mean=st.mean(meanlist)
stdev=st.stdev(meanlist)
print('mean of sampling',mean)
print('standard deviation of sampling',stdev)

first_stdev_start,first_stdev_end=mean-stdev,mean+stdev
sec_stdev_start,sec_stdev_end=mean-(stdev*2),mean+(stdev*2)
third_stdev_start,third_stdev_end=mean-(stdev*3),mean+(stdev*3)
df=pd.read_csv('https://raw.githubusercontent.com/whitehatjr/datasets/master/data1.csv')
data=df['Math_score'].tolist()
mean_of_sample=st.mean(data)
print(mean_of_sample)

# fig=ff.create_distplot([meanlist],['StudentMarks'],show_hist=False)
# fig.add_trace(go.Scatter(x=[mean,mean],y=[0,0.2],mode='lines',name='mean'))
# fig.add_trace(go.Scatter(x=[mean_of_sample,mean_of_sample],y=[0,0.2],mode='lines',name='samplingmean'))
# fig.add_trace(go.Scatter(x=[first_stdev_end,first_stdev_end],y=[0,0.2],mode='lines',name='standard deviation one end'))
# fig.add_trace(go.Scatter(x=[sec_stdev_end,sec_stdev_end],y=[0,0.2],mode='lines',name='standard deviation second end'))
# fig.add_trace(go.Scatter(x=[third_stdev_end,third_stdev_end],y=[0,0.2],mode='lines',name='standard deviation third end'))
# fig.show()
zscore=(mean_of_sample-mean)/stdev
print(zscore)

df=pd.read_csv('https://raw.githubusercontent.com/whitehatjr/datasets/master/data2.csv')
data=df['Math_score'].tolist()
mean_of_sample=st.mean(data)
print(mean_of_sample)

# fig=ff.create_distplot([meanlist],['StudentMarks'],show_hist=False)
# fig.add_trace(go.Scatter(x=[mean,mean],y=[0,0.2],mode='lines',name='mean'))
# fig.add_trace(go.Scatter(x=[mean_of_sample,mean_of_sample],y=[0,0.2],mode='lines',name='samplingmean'))
# fig.add_trace(go.Scatter(x=[first_stdev_end,first_stdev_end],y=[0,0.2],mode='lines',name='standard deviation one end'))
# fig.add_trace(go.Scatter(x=[sec_stdev_end,sec_stdev_end],y=[0,0.2],mode='lines',name='standard deviation second end'))
# fig.add_trace(go.Scatter(x=[third_stdev_end,third_stdev_end],y=[0,0.2],mode='lines',name='standard deviation third end'))
# fig.show()
zscore=(mean_of_sample-mean)/stdev
print(zscore)

df=pd.read_csv('https://raw.githubusercontent.com/whitehatjr/datasets/master/data3.csv')
data=df['Math_score'].tolist()
mean_of_sample=st.mean(data)
print(mean_of_sample)

# fig=ff.create_distplot([meanlist],['StudentMarks'],show_hist=False)
# fig.add_trace(go.Scatter(x=[mean,mean],y=[0,0.2],mode='lines',name='mean'))
# fig.add_trace(go.Scatter(x=[mean_of_sample,mean_of_sample],y=[0,0.2],mode='lines',name='samplingmean'))
# fig.add_trace(go.Scatter(x=[first_stdev_end,first_stdev_end],y=[0,0.2],mode='lines',name='standard deviation one end'))
# fig.add_trace(go.Scatter(x=[sec_stdev_end,sec_stdev_end],y=[0,0.2],mode='lines',name='standard deviation second end'))
# fig.add_trace(go.Scatter(x=[third_stdev_end,third_stdev_end],y=[0,0.2],mode='lines',name='standard deviation third end'))
# fig.show()
zscore=(mean_of_sample-mean)/stdev
print(zscore)



