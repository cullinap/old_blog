---
title: "Predicting Molecular Coupling"
date: 2019-03-15
tags: [Projects]
---

# please see link for code and jupyter notebook
[Project Link](https://github.com/cullinap/predicting-molecular-coupling/blob/master/SVM_model-Copy1.ipynb)

# Predicting Molecular Coupling


```python
#logistic regression
lr_clf = LogisticRegression(random_state=1, solver='newton-cg', multi_class='multinomial')
lr_clf.fit(atom_scalar,type_coupling)

plot_decision_regions(X=X.values, y=type_coupling, clf=lr_clf, legend=7)
plt.show()
```

<img src="{{ site.url }}{{ site.baseurl }}/images/logistic-regression.png" alt="">