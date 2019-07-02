---
title: "Knapsack Algorithm"
date: 2019-06-01
tags: [Projects]
---

#please see link for code and jupyter notebook
[Project Link](https://github.com/cullinap/knapsack-algorithm)

# Solving the Multi-Dimensional Knapsack Problem using Python

The knapsack problem seeks to optimize a paramenter given a constraint. In this case, given a backpack with a certain capacity what is the optimal value while maximizing weight and volume (or two other parameters).

```python

	def knap_sack(a,b,i):
    if i == 0:
        result = max(0,(values[i] if state_1[a]<=max_weight and state_2[b]<=max_volume \
            and state_1[a]>=weights[i] and state_2[b]>=volumes[i] else -9999.99))
        
    elif state_1[a] < weights[i] or state_2[b] < volumes[i]:
        result = knap_sack(state_1[a],state_2[b],i-1)
    else:
        tmp3 = knap_sack(state_1[a],state_2[b],i-1)
        tmp4 = values[i] + knap_sack(state_1[a]-weights[i],state_2[b]-volumes[i],i-1)
        result = max(tmp3, tmp4)
    return result
'''
