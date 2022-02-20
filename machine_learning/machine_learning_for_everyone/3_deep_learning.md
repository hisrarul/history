
## Deep Learning


#### Computer Vision
Helps computers see and understand the content of digital images.


#### Applications of Computer Vision
* Facial recognition
* Self-driving vehicles
* Automatic detection of tumors in CT scans


#### The process
In a bar you strike up a conversation with someone who turns out to be a data scientist at the self-driving car department of Tesla. They start talking about one of the deep learning models they built a while ago. It was able to classify images of vehicles as cars or trucks. You discuss the process and find out they used a neural network to build the model.

Can you place the steps that happen inside a neural network in the right order?

* The car images are transformed to numbers
* The pixel intensities are fed into a neural network
* Neurons will learn to detect edges
* Neurons will learn to more complex objects like wheels, doors, and windows
* Neurons will learn to detect shapes of vehicles
* The image is classified as a car or a truck


#### Natural Language Processing
The ability for computers to understand the meaning of human language


#### Bag of words: n-grams

That book is not great

| Word | Count |
|++++++|+++++++|
| That | 1 |
| book | 1 |
| is | 1 |
| not | 1 |
| great | 1 |


2-gram (bi-gram)

| Word | Count |
|------|-------|
| That book | 1 |
| book is | 1 |
| is not | 1 |
| not great | 1 |


#### Bag of words: limitations

Word embeddings
* Create features that group similar words
* Features have a mathematical meaning


#### Language translation

Applications of LT
* Language translation
* Chatbots
* Personal assistants
* Sentiment analysis


#### Deep learning
* Two types of learning
	* Computer vision
  * Natural language processing
* Why deep learning?
	* Complex problems
  * Automatic feature extraction
  * Lots of data


#### Sentiment analysis
Sentiment Analysis is a Natural Language Processing methodology for quantifying how positive or negative the emotion expressed by a segment of text is. It is often used for automatically categorizing customer feedback messages or product reviews.

Below are four reviews of the movie "The Last Jedi":

1. I really agree with this comment "Great film, one of the best Star Wars films."
2. Worst star wars movie ever made. It disrespected the force and everything we love.
3. A fun exciting, visually striking movie with a great score, great characters, and great action. The Last Jedi is very well directed, but very messy.
4. This movie was a pointless, ugly, and plot-hole-riddled mess. All it served to do was crush all hope and destroy everything that remained of the Original Trilogy.


#### Computer vision, NLP, Traditional machine learning

| Computer Vision | NLP | Traditional Machine Learning |
|-----------------|-----|------------------------------|
| Searching for images on Google | Parsing all tweets about an artist's latest album to get a feeling for the sentiment toward it | Clustering pre-paid telecom customers to identify patterns in terms of money spent in recharing, sending SMS, and browsing the internet. |
| Building an application that takes pictures of all the items passing on a conveyor belt and detecting any defects | Google Home understanding that you have asked it to turn on the lights. | Predicting the temperature in New York tomorrow. |
| | Auto-complete predicting the word you are typing while texting. | |


#### Bag of words
In the field of Natural Language Processing, n-grams are a foundational way to make features from text. n-grams count the sequence of words and n indicates how many word(s) a sequence contains. For example, 2-grams, count the occurrence of two-word sequences.

In this exercise, you can input text and see what are the top 1-gram, 2-gram, and 3-gram features based on occurrence. If you're not sure what to enter, try some of these restaurant reviews:

The food was not great and the service could be faster.

I've seen a lot of bad reviews about this place, but it was not that bad. You get what you pay for!

Which of the following statements is true?
* As you increase the value of n, the occurrences of n-grams decreases.
* This makes sense because individual words are less unique than sequences of words. This bag of words is powerful for how simple it is. However it does have its limitation, so it's common to combine it with other techniques (like word embeddings) when building a natural language processing model.


#### Limits of Machine learning
* Data quality in ML

    Garbage in ---> Machine learning model ---> Garbage out

* Garbage in garbage out
* Output quality depends on input quality


#### Example - How it can go horribly wrong
1. Amazon's gender-biased recruiting tool
	* Preferred men because it learned from historic data when more men were hired
  * It downgraded resumes that
  	* contain the word "women"
    * implied the applicant was female
    

2. Microsoft's AI chatbot


#### Beware
* Don't blindly trust your model
* Awareness is key
* Pay attention to your data

A machine learning model is only as good as the data you give it.


#### Quality assurance
* High quality data requires:
	* Data analysis
  * Review of outliers
  * Domain expertise
  * Documentation
  

#### Explainability
Input ---> Machine learning model ---> Output

* Transparency to increase trust. clarity, and understanding
* Use cases: business adoption, regulatory oversight, minimizing bias


#### Explainable AI
| Black box | Explainable AI |
|-----------|----------------|
| Problems with complex inputs like large quantities of text or images require a deep learning approach and can be considered black boxes | Problems where it is helpful to know why the algorithm chose a particular classification should be tackled with Explainable AI |
| Deep learning | Traditional machine learning |
| Better for "What?" | Better for "Why?" |
| Highly accurate predictions | Understandable by humans |
| Extract information from medical journal articles | Provide a list of likely diagnoses, given a set of facts about a patient |
| Classify images from mammograms as cancerous or non-cancerous | Predict whether or not a nurse is likely to quit within the next month |


#### Example: Explainable AI
1. Prediction: Will the patient get diabetes?
2. Inference: Why will this happen?


#### Example: Inexplicable AI
1. Prediction only: Which letter is this likely to be?