## What is Machine Learning?

#### Artificial Intelligence
* A huge set of tools for making computers behave intelligently.

* Machine learning is the most prevalent subset of AI. A set of tools for making inferences and predictions from data.

#### Defining machine learning: what can it do?
* Predict future events
	* Will it rain tomorrow?
  	* Yes (75% probability)
* Infer the causes of events and behaviors
	* Why does it rain?
  	* Time of the year, humidity levels, temperature, location, etc.
* Infer patterns
	* What are the different types of weather conditions?
  	* Rain, sunny, overcast, fog, etc

#### Defining machine learning: how does it work?
* Interdisciplinary mix of statistics and computer science
* Ability to learn without being explicitly programmed
* Learn patterns from existing data and applies it to new data
* Relies on high-quality data

#### Data science
* Data science is about making discoveries and creating insights from data.
* Machine learning is often an important tool for data science work

#### Machine learning model
A statistical representation of a real-world process based on data.

#### Types of Machine Learning
1. Reinforcement learning - It is used for deciding sequential actions, like a robot deciding its path or its next move in a chess game
2. Supervised learning
3. Unsupervised learning

#### Training data
* Training data: existing data to learn from
* Training a model: when a model is being built from training data
	* Can take nanoseconds to weeks

#### Supervised learning training data
|Age|Sex| Cholesterol | Cigarettes per day | Family history of heart disease | Chest pain type | Blood sugar | Heart disease |
|---|---|-------------|--------------------|---------------------------------|-----------------|-------------|---------------|
|55|M|221|5|True|Typical angina| 118 | True|
|50|F|196|0|False|non-anginal pain|98|False|

The target varaible is Heart disease because this is what we want to predict. The values are labels for True or False. The labels can be numbers or categories.
Each row is an observation or examples that our model will learn from. We should get as many as possible.

The columns such as age, sex, cholesterol, etc are features. Features are different pieces of information that might help predict the target.

#### After training
The features are inputted and the models outputs its prediction.

#### Supervised vs unsupervised learning
* Supervised learning
	* Training data is "labeled". For e.g. True/False was labels in Heart disease

* Unsupervised learning
	* Training data only has features (No labels)
  * Useful for:
  	* Anomaly detection
    * Clustering e.g. dividing data into groups
  * In reality, data doesn't always come with labels
  	* Requires manual labor to label
    * Labels are unknown
  * No labels: model is unsupervised and finds its own pattern. 
  * e.g. Think of millions of data coming from self deriving car. This is case where unsupervised model shines.
  
#### Machine Learning Workflow

##### Our scenario
* Our datasets: New York City property sales from 2015-2019
  * Square feet
  * Neighborhood
  * Year built
  * Sale price
  * And more!
* Our target: Sale price

There are multiple steps in machine learning workflow.

Raw data >> 1. Extract Features >> 2. Split dataset (Train dataset and Test dataset) >> 3. Train model >> 4. Evaluate

#### Summary:
* Extract features
	* Choosing features and manuplating the dataset
* Split dataset
	* Train and test dataset
* Train model
	* Input train dataset into a machine learning model
* Evaluate
	* If desired performance isn't reached: tune the model and repeat the step 3