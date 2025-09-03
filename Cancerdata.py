# Write a Python class that:
# - Computes the ECDF $\hat{F}_N(x)$
# - Has a method to compute any quantile without using Numpy
# - Has a method to compute the **Interquartile Range (IQR)** -- the .25 quantile and the .75 quantile, which brackets 50% of the data -- and the **whiskers**: $\pm 1.5 \times \text{IQR}$ from the edges of the IQR
	#paramers = df and column name 
	def IQR(): #add parameters that will be passed 

	    
	    import numpy as np
	    import pandas as pd
	    #import data file 
	    fileP = 'metabric.csv'
	    df = pd.read_csv(fileP)
	    df.head()

	    #get interquartile range
	    Q1 = df['Age at Diagnosis'].quantile(0.25) #change this 
	    Q3 = df['Age at Diagnosis'].quantile(0.75) #change this 
	    IQR = Q3 - Q1

	    #whisker info 
	    left_whisker= Q1 - 1.5 * IQR
	    right_whisker = Q3 + 1.5 * IQR
	    return IQR, left_whisker, right_whisker
# - Has a method to compute a five-number summary/boxplot: the whiskers, the minimum and maximum, the IQR and the median
# - Compare your answers with `sns.boxplot`; making a boxplot yourself is kind of a pain, but you could make a 5-number summary visualization
# - Anything outside the whiskers is an **outlier**; write a method that returns a Boolean vector indicating if the observations are outliers

