import pandas as pd
# Load the dataset
df = pd.read_csv("C:/Users/ali_a/Desktop/Ete2018/CreditCardPrediction/TrainData/train_ali_124.csv")
df.rename(columns = {'Default':'default'}, inplace=True)
'''
df = df.drop(["PERIODID_MY"],axis=1)
df  =df.iloc[:11900]
df = df.drop(df.columns[2:15],axis=1)
df = df.drop(df.columns[346:352],axis=1)
'''
df.head()


# Let's see if there are empty values.

print(df.isnull().sum())

print(df.shape)
