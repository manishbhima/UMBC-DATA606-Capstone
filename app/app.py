from flask import Flask, request, render_template

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report
from sklearn.svm import SVC
from xgboost import XGBClassifier
from sklearn.neighbors import KNeighborsClassifier

df = pd.read_csv('water_potability.csv')
df.shape
df.head()
df.tail()
#Finding null values
df.isna().sum()
#Dropping the null values
df = df.dropna()

app = Flask(__name__)


@app.route('/')
@app.route('/home', methods=['GET', 'POST'])
def home():
    return render_template('index.html')

X = df.iloc[:, :-1].values
y = df.iloc[:, -1].values
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=0)
import pickle

# Load the StandardScaler object
with open('standard_scaler.pkl', 'rb') as f:
    sc = pickle.load(f)
# sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

classifier = SVC(C=5.0, kernel='rbf', random_state=42, gamma='scale', probability=True, shrinking=True,
                 decision_function_shape='ovr', tol=0.1)
classifier.fit(X_train, y_train)
#ph,Hardness,Solids,Chloramines,Sulfate,Conductivity,Organic_carbon,Trihalomethanes,Turbidity,Potability
# Define Flask route
@app.route('/predict', methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        ph = request.form.get('ph')
        hardness = request.form.get('hardness')
        solids = request.form.get('solids')
        chlor = request.form.get('chlor')
        sulfate = request.form.get('sulfate')
        cond = request.form.get('cond')
        orga = request.form.get('orga')
        tri = request.form.get('tri')
        tub = request.form.get('tub')

        # Check if any of the form inputs are None
        if None in [ph, hardness, solids, chlor, sulfate, cond, orga, tri, tub]:
            # Handle missing values appropriately
            return "Please fill in all fields"

        # Convert to float if not None
        ph = float(ph)
        hardness = float(hardness)
        solids = float(solids)
        chlor = float(chlor)
        sulfate = float(sulfate)
        cond = float(cond)
        orga = float(orga)
        tri = float(tri)
        tub = float(tub)
        X = df.iloc[:, :-1].values
        y = df.iloc[:, -1].values
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=0)
        import pickle

        # Load the StandardScaler object
        with open('standard_scaler.pkl', 'rb') as f:
            sc = pickle.load(f)
        # sc = StandardScaler()
        X_train = sc.fit_transform(X_train)
        X_test = sc.transform(X_test)

        classifier = SVC(C=5.0, kernel='rbf', random_state=42, gamma='scale', probability=True, shrinking=True,
                        decision_function_shape='ovr', tol=0.1)
        classifier.fit(X_train, y_train)
        input_features = [[ph, hardness, solids, chlor, sulfate, cond, orga, tri, tub]]
        input_features = sc.transform(input_features)  # Transform input features
        print("#########################################")
        prediction = classifier.predict(input_features)
        print("#########################################",prediction)
        if prediction[0]==1:
            prediction_result="Good Quality - 1"
        else:

            prediction_result="NOT Good Quality - 0"
        print("#########################################",prediction_result)
        return render_template('output.html', predicted_result=prediction_result)
    else:
        return render_template('index.html',predicted_result=None)

@app.route('/visual', methods=['GET', 'POST'])
def visual():
    import seaborn as sns
    #Checking for the Outliers
    df.boxplot(figsize = (15,6))
    plt.show()

    #Plotting the count for the potability column
    colors = ["#ff9999", "#66b3ff"]
    ax = sns.countplot(x="Potability", data=df, palette=colors, saturation=0.7)
    plt.xticks(ticks=[0, 1], labels = ["Not Potable", "Potable"])
    plt.show()

    #plotting the distribution of the water
    d = pd.DataFrame(df["Potability"].value_counts())

# Rename the count column to match the expected 'values' parameter
    d.rename(columns={"Potability": "count"}, inplace=True)

    # Plot the pie chart
    fig = px.pie(d, values="count", names=["Not Potable", "Potable"], hole=0.35, opacity=0.8,
                labels={"label": "Potability", "count": "Number of Samples"})
    fig.update_layout(title=dict(text="Pie Chart of Potability Feature"))
    fig.update_traces(textposition="outside", textinfo="percent+label")
    fig.show()

    #Finding the potability of the water according to the ph value
    sns.swarmplot(x='Potability', y='ph', data=df, palette='pastel')

    #Plotting the correlation between Potability and other  factors afftecing it
    import seaborn as sns
    plt.figure(figsize=(10, 10))
    sns.heatmap(df.corr(), annot= True, cmap='twilight')

    sns.pairplot(df, hue="Potability")
    plt.show()

    sns.scatterplot(x = df['ph'], y = df['Potability'])
    plt.show()

    #Plotting the factors affecting the potability of the water
    df.hist(column='Hardness', by='Potability')
    plt.show()

    df.hist(column='ph', by='Potability')
    plt.show()

    plt.rcParams['figure.figsize'] = [7,7]
    sns.distplot(df['Potability'])
    plt.show

    plt.figure(figsize=(15, 8))
    plt.suptitle('Feature Distribution by Potability class', weight = 'bold')
    for i, col in enumerate(df.columns[:-1]):
        plt.subplot(2, 5, i + 1)
        sns.violinplot(x='Potability', y=col, data=df, palette='pastel')
    plt.tight_layout(pad=0.5, w_pad=0.7, h_pad=1.0)
    plt.show()

    plt.figure(figsize=(15, 8))
    plt.suptitle('Feature Distribution by Potability class', weight = 'bold')
    for i, col in enumerate(df.columns[:-1]):
        
        plt.subplot(2, 5, i + 1)
        sns.boxplot(x='Potability', y=col, data=df, palette='viridis')
    plt.tight_layout(pad=0.5, w_pad=0.7, h_pad=1.0)
    plt.show()


    return render_template('index.html')

if __name__=="__main__":
    app.run(debug=True)