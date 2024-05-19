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


