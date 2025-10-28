import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)

from sklearn import preprocessing
from sklearn.naive_bayes import GaussianNB


# Data lists
weather = ['Sunny','Sunny','Overcast','Rainy','Rainy','Rainy','Overcast',
           'Sunny','Sunny', 'Rainy','Sunny','Overcast','Overcast','Rainy']
temp = ['Hot','Hot','Hot','Mild','Cool','Cool','Cool','Mild','Cool','Mild',
        'Mild','Mild','Hot','Mild']
play = ['No','No','Yes','Yes','Yes','No','Yes','No','Yes','Yes','Yes','Yes',
        'Yes','No']


# 2. Encoding Features:
le = preprocessing.LabelEncoder()
weather_encoded = le.fit_transform(weather)
print(weather_encoded)
# Output:-
temp_encoded = le.fit_transform(temp)
label = le.fit_transform(play)
print("Temp:", temp_encoded)
print("Play:", label)
features = list(zip(weather_encoded, temp_encoded))


# Note: These lines are redundant but kept as per your original code
X = weather_encoded
Y = temp_encoded
features = list(zip(X, Y))
print(features)
features = list(zip(weather_encoded, temp_encoded)) # This line is also redundant


# 3. Generating Model:
model = GaussianNB()
model.fit(features, label)
predicted = model.predict([[0, 2]])
print("Predicted Value:", predicted)