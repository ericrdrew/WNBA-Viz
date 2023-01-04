# -*- coding: utf-8 -*-
"""
Created on Tue Aug 30 20:02:42 2022
WNBA VIZZIES
@author: ericd
"""
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.offsetbox import OffsetImage, AnnotationBbox
import matplotlib.ticker as mtick

########################### WNBA EFFICIENCY PLOT#################################################
#read in team data
#Source: https://www.basketball-reference.com/wnba/years/2022.html
data = pd.read_csv('teamData.csv')
data.head()

#set image paths
data['path'] = 'C:/Users/ericd/OneDrive - North Carolina State University/Desktop/WNBA Viz/LogosHeadshots/'+ data['Team']  + '.png'


### ORTG/DRTG PLOTS
#create plot area
fig, ax = plt.subplots()

#set plot size
fig.set_size_inches(7,5)


#add images
def getImage(path):
    return OffsetImage(plt.imread(path), zoom=0.03, alpha=1)

#new plot
fig, ax = plt.subplots(figsize=(6, 4), dpi=600)
ax.scatter(data['ORtg'], data['DRtg'], color='white')
ax.set_title('WNBA Team Offensive/Defensive Efficiencies, 2022 Season', size=10)
ax.set_xlabel('Offensive Rating')
ax.set_ylabel('Defensive Rating')
plt.axhline(y=103.8, color = 'black', linestyle='dashed', alpha=.5)
plt.axvline(x=103.8, color='black', linestyle='dashed', alpha=.5)    
plt.ylim(112,96)

#average line labels
fig.text(.715, .525, 'League Average DRtg', size=5, alpha=0.5)
fig.text(.475,.14, 'League Average ORtg', size=5, alpha=0.5, rotation=90)

#quadrant labels
fig.text(.58, .85, 'Good Offense, Good Defense', size=7)
fig.text(.2,.85, 'Bad Offense, Good Defense', size=7)
fig.text(.58, .14, 'Good Offense, Bad Defense', size=7)
fig.text(.2,.14, 'Bad Offense, Bad Defense', size=7)

#source/name
fig.text(0.03,.02, 'Source: https://www.basketball-reference.com/wnba/years/2022.html', size=4)
fig.text(.03,.04, 'Created By: Eric Drew',size=4)


for index, row in data.iterrows():
    ab = AnnotationBbox(getImage(row['path']), (row['ORtg'], row['DRtg']), frameon=False)
    ax.add_artist(ab)



