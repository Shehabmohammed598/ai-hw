import pandas as pd   # importing the required modules
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import train_test_split # importing the train_test_split method from sklearn
from sklearn.metrics import accuracy_score ,confusion_matrix # importing accuracy_score , the Confusion Matrix
 
# Import the data set and read by pandas  modules
df = pd.read_csv('purchasing.csv')

#df = df.drop(['Unnamed: 7'], axis=1)
df.head()

df.describe()



y = df['Purchasing']
x = df.drop(['Purchasing'], axis=1) 

# splitting the data
x_train, x_test, y_train, y_test = train_test_split(x,y, test_size= 0.20,random_state=27)

x_train
x_test
y_train
y_test 


clf = MLPClassifier(hidden_layer_sizes=(200), verbose= 10, max_iter=500, alpha=0.0001, solver='sgd', random_state=21,tol=0.000000001)
# model training
clf.fit(x_train, y_train)

# testing the model
y_pred = clf.predict(x_test)

# claculate  accuracy
accuracy_score(y_test, y_pred)

# providing actual and predicted values
cm = confusion_matrix(y_test, y_pred)

# If True, write the data value in each cell
sns.heatmap(cm, center=True)
plt.show()




