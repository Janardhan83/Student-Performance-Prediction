import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score , root_mean_squared_error
import warnings
warnings.filterwarnings('ignore')
import pickle
class MUL:
    def __init__(self , data):
        self.df = pd.read_csv(data)
    def exploration(self):
        print('first 5 rows :\n')
        print(self.df.head(5))
        print('data set shape :\n')
        print(self.df.shape)
        print('checking null values :')
        print(self.df.isnull().sum())
    def preprocessing(self):
        self.df['Extracurricular Activities'] = self.df['Extracurricular Activities'].map({'Yes': 1, 'No': 0})
        print('\n ========== data preprocessing ========')
        self.x =self.df.iloc[:,:-1]
        self.y=self.df.iloc[:,-1]
        print('independent shape',self.x.shape)
        print('dependent shape', self.y.shape)
    def spliting(self):
        self.xtrain , self.xtest ,self.ytrain,self.ytest = train_test_split(self.x,self.y, test_size=0.25,random_state=42)
        print(f'xtrain shape :{self.xtrain.shape} and ytrain shape :{self.ytrain.shape}')

    def model_building(self):
        self.lir = LinearRegression()
        self.lir.fit(self.xtrain,self.ytrain)
        print('---------- train performance --------------')
        print(f'r2 score is :{r2_score(self.ytrain , self.lir.predict(self.xtrain))}')
        print(f'root_mean_squared_error is :{root_mean_squared_error(self.ytrain , self.lir.predict(self.xtrain))}')

    def testing(self):
        print('---------- test performance --------------')
        print(f'r2 score is :{r2_score(self.ytest, self.lir.predict(self.xtest))}')
        print(f'root_mean_squared_error is :{root_mean_squared_error(self.ytest, self.lir.predict(self.xtest))}')
    def sample_prediction(self , user):
        print('user input prediction is :')
        print(self.lir.predict(user))

    def pickle_file(self):

        with open('s_mlr.pkl','wb') as f:
            pickle.dump(self.lir , f)
            print('pickel file ok')



if __name__ == "__main__":
    obj=MUL('Student_Performance.csv')
    obj.exploration()
    obj.preprocessing()
    obj.spliting()
    obj.model_building()
    obj.testing()
    obj.sample_prediction([[7,99,1,9,1]])
    obj.pickle_file()





