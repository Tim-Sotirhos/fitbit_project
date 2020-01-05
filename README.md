# README: fitbit_project Time Series Project

***Goal Overview:*** Create a predictive model to predict the missing next two weeks of data in December based on the acquired fitbit data.

## Table of Contents

- [Installation](#installation)
- [Organization](#organization)
- [Planning](#planning)
- [Dictionary](#dictionary)

## Installation

Instructions on setting up the fitbit time series project and necessary steps to successfully run on any computer. 

- Make a clone of this repository click [here](https://github.com/Tim-Sotirhos/fitbit_project)
- Ensure you've installed the following: Python 3.7, pandas, scikit-learn, statsmodels, and numpy.
- To run the model, follow along inside the repository, there are a number of .CSV files, several .py files, and an .ipynb file. Following the flow of the .ipynb file will result in a .CSV file with predictions for the next two weeks worth of data using time series modeling.

## Organization

`fitbit_project.ipynb` pipeline:

_**Acquisition**_
- Acquire from fitbit data .CSV files representing 255 days of data covering April - December 2018

_**Preperation**_
- Handle column names, remove comma seperators in numbers, change data types from objects to integers, convert date columns to date data type, and avoid overcomplications

_**Exploration**_
- Vizualize distributions for early discoveries

_**Modeling**_
- Sample data into train and test data frames using percent split and create 3 models (last observed, simple average, and moving average) with train data

_**Evaluation**_
- Analyize evaluation metrics, select best performing forecast method, and predict based on train data

**Important:** 
To reporduce this time series project please follow along with the fitbit_project notebook [open](https://github.com/Tim-Sotirhos/fitbit_project/blob/master/fitbit_project.ipynb).

There is no env.py file required for this repository.

## Planning

### Goals:

1. Analyze different activity variables to build a model to predict missing data 
2. Discover highlights from exploration phase, vizualizations, and other investigative findings
3. Summarize the data

### fitbit data:

* Activity data that includes information about calories, steps, minutes active, etc. in 2018.
* Includes dates for each record in 2018.

## Dictionary

### Data Dictionary

**date:** data frame index

**calories_burned:** amount of calories burned for the date record

**steps:** amount of steps recoded throughout the date record

**distance:** distance traveled in miles

**floors:** measured by changes in elevation

**minutes_sedentary:** minutes with no activity

**minutes_lightly_active:** minutes with low-intensity activity

**minutes_farily_active:** minutes with moderate-intensity activity

**minutes_very_active:** minutes with high-intensity activity

**activity_calories:** Calories burned while active

**`* Note:`** all variables must be a data type of: Float64 or int64 and the indexed date column must be a datetime object for time series analysis.