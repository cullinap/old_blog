---
title: "NYC Taxi Analysis"
date: 2019-01-01
tags: [Projects]
---

#please see link for code and jupyter notebook
[Project Link](https://github.com/cullinap/NYC-taxi-analysis)

# Analysis of NYC Taxi Trip Data

The NYC Taxi and Limousine Commission (TLC) collects data on such as pick-up/drop-off times, pick-up/drop-off locations, data on payment types, number of passengers, and passenger count amount other fields. TLC posts this information by month and year on the following website: (https://www1.nyc.gov/site/tlc/about/tlc-trip-record-data.page)

The website provides a month-by-month breakdown of taxi data from yellow taxis, green taxis, and For-Hire Vehicles (FHV). FHV's consist of community cars, black cars, luxury limos, and high-volume for-hire services. Addtionally, the data is broken down by year and month. Because there is an enourmous amount of data we will start our analysis with yellow taxis in August of 2018.


```python

	manhattan_pu = merged_pu.loc[merged_pu['borough'] == 'Manhattan'] #sort by only Manhattan trips
	manhattan_do = merged_do.loc[merged_do['borough'] == 'Manhattan']

	fig, (ax1, ax2) = plt.subplots(ncols=2, sharex=True, sharey=True, figsize=(15,10))

	manhattan_pu.plot(ax=ax1, column='PULocationID', cmap='Reds', linewidth=0.8, edgecolor='0.8')
	manhattan_do.plot(ax=ax2, column='DOLocationID', cmap='Reds', linewidth=0.8, edgecolor='0.8', legend=True)
	ax1.axis('off')
	ax1.set_title('Aug: Manhattan pick-ups', fontdict={'fontsize': '25', 'fontweight' : '3'})
	ax2.axis('off')
	ax2.set_title('Aug: Manhattan drop-offs', fontdict={'fontsize': '25', 'fontweight' : '3'})
	plt.show()
'''