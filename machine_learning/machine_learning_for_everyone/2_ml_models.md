## Machine learning models
There are two types of machine learning
* Supervised learning
* Unsupervised learning


#### Supervised learning
Supervised learning is basically a labeling machine. It takes an observation, and assigns a label to it.
There are two flavors of supervised learning:
* classification
* regression


#### Classification
* Classification = assigning a category
	* Will this customer stop its subscription?
  	* Yes, No
  * Is this mole cancerous?
  	* Yes, No
  * What kind of wine is that?
  	* Red, White, Rose
  * What flower is that?
  	* Rose, Tulip, Carnation, Lily

Note: We feed the model observations.

	* Regression = assigning a continuous variable
  	* How much will this stock be worth?
    * What is this exoplanet's mass?
    * How tall will this child be as an adult?


#### Classification vs regression
* Regression = continuous
	* Any value within a finite (height) or infinite (time) interval
  	* 20 deg F, 20.1 deg F, 20.01 deg F

* Classification = category
	* One of few specific values
  	* Cold, Mild, Hot


#### Unsupervised learning
* Unsupervised learning = no target column
	* No guidance
  * Look at the whole dataset
  * Tries to detect patterns
* Unsupervised learning focus on clustering, anomaly detection, association.
	* Clustering consists in identifying groups in your dataset. The observations in these groups share stronger similarities with members of other groups. For e.g. finding cat and dogs in a group 


#### Unsupervised learning are categorized:
1. Clustering
2. Association
3. Anomaly detection


#### Clustering models
Clustering consists of identifying groups in your datasets. The observations in these groups share stronger similarity with members of their group.

* K Means
	* Specify the number of clusters
* DBSCAN (density-based spatial clustering of applications with noise)
	* Don't require you to specify the number of cluster in advance
  * Specify what constitute a cluster


#### Detecting outliers
* Anomaly detection = detecting outliers
* Outliers = observations that differ from the rest


#### Some anomaly detection use cases
* Discover devices that fail faster or last longer
* Discover fraudsters that manage trick the system
* Discover patients that resist a fatal disease


#### Association
Let's end with association, which consists in finding relationships between observations. In other words, it's about finding events that happen together.
It's often used for market basket analysis, which is just a fancy expression to state "Which objects are brought together?"
For example, people who buy jam are likely to buy bread, people who buy beer are likely to buy peanuts, etc.


#### Supervised vs Unsupervised
| Supervised | Unsupervised |
|------------|--------------|
|Based on customer information (sign up date, ordering frequency, age, martial status), predict their yearly spending amount. | Based on customer information (sign up date, ordering frequency, age, martial status, spending income), find segments of customers.|
|Based on stock information (open value, highest value, lowest value, close value for each day), predict its future value. | Based on email information (sender topic), find groups of emails by theme. |
|Based on email features (sender, topic, ratio uppercased letter, proportion of 'money' term), predict if an email is spam or not.| Based on customer's purchase history, find which items they are likely to be interested in next. |


#### Overfitting
* Performs great on training data
* Performs poorly on testing data
* Model memorized training data and can't generalize learning to new data

That's why we need to split data into two data sets. 

#### Accurancy
* Accurancy = correctly classified observations / all observations e.g. 48/50 = 96% accurancy

#### Confusion matrix
A confusion matrix is a table that is often used to describe the performance of a classification model (or "classifier")
on a set of test data for which the true values are known.

#### Sensitivity
* sensitivity = true positives / true positives + false negatives

#### Specificity
* specificity = true negatives / true negatives + false positives

#### root mean square error
Root Mean Square Error (RMSE) is the standard deviation of the residuals (prediction errors).


#### QA

| True | False |
|------|-------|
| Assessing an unsupervised learning model's performance is trickier and depends on your original objectives. | Accuracy is always an informative and useful metric |
| Confusion matrices are used to evaluate classification performance. | A false negative is a value that was predicted as positive, when it's actually negative. |
| A False positive is a value that was predicted as positive, when it's actually negative. | |


#### Improving performance
There are several options:
1. Dimensionality reduction
2. Hyperparameter tuning
3. Ensemble methods


#### Dimensionality reduction
It is essentially means reducing the number of features. Example
* Irrelevance: some features don't carry information
* Correlation: some features carry similar information
	* Keep only one feature
  	* e.g. height and shoe size are highly correlated ----> height (keep only the height)
  * Collapse multiple features into the underlying feature
  	* e.g. height and weight ----> Body mass index

    
#### Hyperparameter tuning
Depending on dataset, different hyperparameter values will give better or inferior results. e.g. genre dataset and instrument settings


#### SVM algorithm hyperparameters
* kernel: "linear" --> "poly"
* C
* degree
* gamma
* shrinking
* coef0
* tol


#### Ensemble methods

* For classification
	* The three main classes of ensemble learning methods are bagging, stacking, and boosting. It is important to both have a detailed understanding of each method
  	and to consider them on your predictive modeling project.

* For regression
	* The goal of ensemble regression is to combine several models in order to improve the prediction accuracy in learning problems with a numerical target variable.
  	The process of ensemble learning can be divided into three phases: the generation phase, the pruning phase, and the integration phase.


| Hyperparameter Tuning | Dimensionality Reduction | Ensemble Methods |
|-----------------------|--------------------------|------------------|
| Write a script to try 3 different values of three different hyperparameters of your SVM, and keep the configuration that yieldsthe best results. | Run an analysis to identify the four main features that give the best predictions, and get rid of the others. | Use the most common prediction from an SVM, a K-Means and a Decision Tree model to assign a category to an observation |
| While training a Decision Tree, change the minimum count of observations for what constitutes a branch. | On a dataset of running sessions of assess a treadmill's longevity, with duration, speed, inclination, remove the column "calories_burned". | Use the average prediction from a Linear regression, a K-Means and a Decision Tree model to assign a category to an observation |



#### Deep learning

Deep learning uses an algorithm called neural networks which is loosely inspired by biological neural networks.

* AKA: Neural networks
  * Basic unit: neurons (nodes)
* Special area of Machine learning
* Require more data than traditional machine learning
* Best when inputs are images or text

Example:- Predicting box office revenue

* Neural networks are much higher
* Deep learning: neural network with many neurons
* Can solve complex problems

#### When to use deep learning?
* Lots of data
* Access to processing power
* Lack of domain knowledge
* Complex problems
  * Computer vision
  * Natural language processing


#### Question and Answer

| True | False |
|------|-------|
| More complex problems like image classification can be solved much faster by deep learning than by traditional machine learning | The number of neurons is a neural network is limited. |
| When there is lack of domain knowledge and you are not sure of the exact features that need to be used, you should use deep learning | Deep learning is always preferred over traditional machine learning |
| Deep learning is a subfield of machine learning concerned with algorithms inspired by the human brain called neural networks. | You have to figure out the higher-level features yourself while training the data |

