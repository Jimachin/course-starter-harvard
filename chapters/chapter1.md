---
title: 'Chapter 1 : Introduction to Linear Regression'
description:
  'In this initial chapter you will archive the basic about Linear Regression.' 
prev: null
next: /chapter2/
type: chapter
id: 1
---

<exercise id="1" title="Linear Regression Basics" type="slides">
    <slides source="chapter1_01_introduction"></slides>
</exercise>

<exercise id="2" title="Getting Started">

The Linear Regression Models are used for : 

<choice>
<opt text="Answer 1">This is not correct either.</opt>
<opt text="Approximate the dependency relationship between a dependent variable Y, the independent variables X." correct="true">Good job!</opt>
<opt text="Answer 3">This is not correct either.</opt>
</choice>

</exercise>

<exercise id="3" title="Describe your data">

- Load data from data file `data.csv` using pandas
- Examine the `DataFrame`. How many points?

<codeblock id="01_03"> 
Pandas read csv file data go to https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_csv.html
<br> 
A great method to describe the dataframe is .describe() 
</codeblock>

</exercise>

<exercise id="4" title="Draw x vs y">
The goal here is produce a plot like this :

<div style="text-align:center">
    <img src="./visual_representation.png" 
    alt="Visual representation of the data generates in this example" 
    width="40%">
</div>

- Rename the columns of your Data Frame.
- Plot the data in a graphic of x vs y.

<codeblock id="01_04">---Hints---</codeblock>

</exercise>

<exercise id="5" title="Estimate the Linear Model">

- Guess &beta;<sub>0</sub> and &beta;<sub>1</sub> and make predictions with your model.
- Calculate the MSE for your model.

<codeblock id="01_05">---Hints---</codeblock>

</exercise>

<exercise id="6" title="Analize the MSE">

- Set beta0 = 2.2 and examine all models for beta1 = 0,3 in increments of 0.1

<codeblock id="01_06">---Hints---</codeblock>

</exercise>