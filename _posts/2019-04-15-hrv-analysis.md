---
title: "HRV Analysis"
date: 2019-04-15
tags: [Projects]
---

#please see link for code and jupyter notebook
[Project Link](https://github.com/cullinap/hrv_analysis/blob/master/hrv_data_exploration-Copy1.ipynb)

# Heart Rate Variability Analysis


```python

SUBJECTS = data.sheet_names
CONDITIONS = data_df.Condition.unique()

def calculate_mean_rmssd(condition,subject):
    return data_df[(data_df.Condition==condition) & (data_df.subject==subject)].RMSSD.mean()

def generate_means(conditions,subjects):
    output={}
    
    for subject in subjects:
        m = tuple(calculate_mean(condition,subject) for condition in conditions)
        output[subject] = m
    
    return output

def generate_scatter(value,value_range):
    [plt.scatter(SUBJECTS, [elem[i] for elem in value.values()]) for i in range(value_range)]
    plt.show()
'''