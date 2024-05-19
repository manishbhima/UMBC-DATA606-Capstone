# 1. PROJECT TITLE - WATER QUALITY 
- Prepared for UMBC Data Science Master Degree Capstone by Dr Chaoji (Jay) Wang - SPRING 2024 Semester
- Author: Manish Bhima
- GitHub : https://github.com/manishbhima
- Linkedin : www.linkedin.com/in/manish-bhima
## 2. BACKGROUND
  - Constructing Sustainable Smart Water Supply systems are facing serious challenges all around the world with the fast expansion of modern cities. Water quality is 
     influencing our life ubiquitously and prioritizing all the urban management.

  - Research Questions:
    - How accurately can machine learning models predict the quality of urban water based on various features such as pH, sulfates, solids, hardness.
    - Which features contribute the most to the prediction of quality of water?
    - What recommendations can be made based on the model's outputs?


## 3. DATA
Description : 

1. Data Source : *[Kaggle](https://www.kaggle.com/code/imakash3011/water-quality-prediction-7-model/input)*. :link:

2. Data Size : 513 KB

3. Data Shape
   > - Number of columns =  10
   > - Number of rows    = 3276
4. Column Description:
    > - ph: pH of 1. water (0 to 14).
    > - Hardness: Capacity of water to precipitate soap in mg/L.
    > - Solids: Total dissolved solids in ppm.
    > - Chloramines: Amount of Chloramines in ppm.
    > - Sulfate: Amount of Sulfates dissolved in mg/L
    > - Conductivity: Electrical conductivity of water in μS/cm.
    > - Organic_carbon: Amount of organic carbon in ppm.
    > - Trihalomethanes: Amount of Trihalomethanes in μg/L.
    > - Turbidity: Measure of light emiting property of water in NTU.
    > - Potability: Indicates if water is safe for human consumption. Potable -1 and Not potable -0
 5. Target Variable: Potability(Boolean)
 6. Feature Predictors : 'pH', ‘Hardness', ‘Solids’, ‘Chloramines', ‘Sulfate', ‘Conductivity ‘, ‘Trihalomethanes', and ‘Turbidity' can be used as variables for predicting machine learning models. These variables represent categorical features, and depending on the nature of your predictive task, they can be valuable predictors for your model.

## 4. Data Exploration and Visualizations
#### Distribution of portability
![image](https://github.com/manishbhima/UMBC-DATA606-Capstone/blob/main/docs/Picture1.png)
#### Pie Chart of portability feature
![image](https://github.com/manishbhima/UMBC-DATA606-Capstone/blob/main/docs/Picture2.png)
#### Distribution of portability of water with pH values
![image](https://github.com/manishbhima/UMBC-DATA606-Capstone/blob/main/docs/Picture3.png)
#### Correleation Heatmap
![image](https://github.com/manishbhima/UMBC-DATA606-Capstone/blob/main/docs/Picture4.png)
#### Pairplot of portability class
![image](https://github.com/manishbhima/UMBC-DATA606-Capstone/blob/main/docs/Picture5.png)
#### Scatterplot portability with ph values
![image](https://github.com/manishbhima/UMBC-DATA606-Capstone/blob/main/docs/Picture6.png)
#### Desnsity plot of portability
![image](https://github.com/manishbhima/UMBC-DATA606-Capstone/blob/main/docs/Picture7.png)
#### Feature distribution of portability class
![image](https://github.com/manishbhima/UMBC-DATA606-Capstone/blob/main/docs/Picture8.png)
#### Feature distribution of portability class
![image](https://github.com/manishbhima/UMBC-DATA606-Capstone/blob/main/docs/Picture9.png)



## 5. Model Building
- In this project, machine learning techniques are applied to analyze and predict quality of water based on various factors.
- By leveraging machine learning algorithms, we can build predictive models that estimate health insurance charges based on factors such as pH,sulfates , hardness, trihalomethanes, turbides, chloramines and solids.
- These predictive models can help us in prerdicting whether the given water is potable for drinking or not.
- Data preprocessing is a critical step in machine learning workflows to ensure data compatibility with models.
- Standardization and encoding techniques are applied to handle numerical and categorical features, respectively.
- This step ensures that the data is in a suitable format for model training.


Classification models used in this project are:

- **Random Forest Classifier** : Random Forest Classifier is an ensemble learning method used for classification tasks in machine learning. It constructs multiple decision trees during training and outputs the class that is the mode of the classes (classification) or mean prediction (regression) of the individual trees. Random Forest is effective because it reduces overfitting by averaging the predictions of multiple trees and utilizes the wisdom of crowds to make robust predictions. The accuracy of the model is found to be 70%.

- **Support Vector Classifier** : SVC stands for Support Vector Classifier, which is a type of support vector machine (SVM) used for classification tasks. It aims to find the hyperplane that best separates data points into different classes. Unlike other SVM variants like Support Vector Regression (SVR), which is used for regression tasks, SVC focuses specifically on classification. SVC's ability to handle complex classification problems efficiently while maintaining high performance makes it a significant choice in various machine learning applications. The accuracy of the model is found to be 71%. Because of the highest accuracy of 71% we choose SVC as the preferred choice of classifier for training the model.
  
- **XGB Classifier** : XGBoost, short for Extreme Gradient Boosting, is a powerful machine learning algorithm that belongs to the boosting family. It combines the advantages of both bagging and boosting techniques, utilizing an ensemble of weak learners (decision trees) to create a strong learner. XGBoost's versatility, scalability, and effectiveness make it a go-to choice for many data scientists and machine learning practitioners. The accuracy of the model is found to be 67%.


## 6.Deployment Using Flask

- Flask web application utilizes a pre-trained machine learning model to predict the water potability based on user input. 
- Users input the pH, hardness , solids, chloramines,sulfate, conductivity, organic carbon, trihalomethanes, turbidity values through a simple web form. This data is then transmitted to a pre-trained machine learning model, which utilizes water quality data to make predictions. 
- The model predicts water potablity based on the information provided.

![image](https://github.com/manishbhima/UMBC-DATA606-Capstone/blob/main/docs/Picture10.png)



## 7. Conclusion

- My analysis involved robust data preprocessing and model building, utilizing Random Forest Classifier, XGBoost Classifier, and Support Vector Classifier.
- The developed models demonstrated strong predictive performance in estimating water potability, with the SVC Model exhibiting exceptional accuracy.
- Implications- Water quality prediction projects play a crucial role in safeguarding public health, preserving the environment, optimizing resource utilization, shaping policies, and fostering community participation in water management.
- In conclusion, our machine learning model demonstrates promising capabilities in predicting water quality parameters. By leveraging advanced algorithms and robust data sets, we've achieved significant accuracy in forecasting water quality, empowering stakeholders to make informed decisions and take proactive measures to ensure safe and sustainable water resources for communities and ecosystems alike.
