 # Calculating Cronbach's Alpha using Python

Cronbach’s alpha is a measure of internal consistency, that is, how closely related a set of items are as a group. More information about this: https://stats.idre.ucla.edu/spss/faq/what-does-cronbachs-alpha-mean/

The code assumes that you already have uploaded your data in Azure ML, and that you have imported into Python. More information: https://gist.github.com/lauramar17/0fd5ea81be217a7ccd39cacaba7397b9.js

Method: 
It takes an unlimited number of parameters for the questions that you want to calculate its internal consistency. 

To run:

    CronbachAlpha2([<datasetname>['<columnname>']])
 
## Example

    CronbachAlpha2([frame['Q27'],frame['Q28'],frame['Q29']])
              
   Note: "frame' is the name of the dataset, and the 'Q27' is the name of column.