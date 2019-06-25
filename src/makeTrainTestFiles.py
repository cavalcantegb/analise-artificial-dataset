import pandas as pd
from sklearn.model_selection import StratifiedShuffleSplit

nomePasta = 'HT107'

filename=r'C:\Users\caval\Documents\ufc\analise-desempenho\projeto\src\dataset\{}\2017\Merged_HT101.csv'.format(nomePasta)


df = pd.read_csv(filename)

X = df.iloc[:, 1 :-1]
y = df.iloc[:,-1]


i_train, i_test = next(StratifiedShuffleSplit(n_splits=1, train_size=0.80, test_size=0.20).split(X, y))

#i_train, i_test = next(StratifiedShuffleSplit(n_splits=1).split(X, y))

X_train, X_test, y_train, y_test = X.loc[i_train], X.loc[i_test], y[i_train], y[i_test]

# X_train = X.loc[i_train]
# X_test = X.loc[i_test]
# y_train = y[i_train]
# y_test = y[i_test]

with open(r'C:\Users\caval\Documents\ufc\analise-desempenho\projeto\src\dataset\{}\train\X_train.txt'.format(nomePasta),'w') as file:
  for i, row in X_train.iterrows():
    line = ' '.join(map(str, row)) + '\n'
    print(line)
    file.write(line)

with open(r'C:\Users\caval\Documents\ufc\analise-desempenho\projeto\src\dataset\{}\test\X_test.txt'.format(nomePasta),'w') as file:
  for i, row in X_test.iterrows():
    line = ' '.join(map(str, row)) + '\n'
    file.write(line)

with open(r'C:\Users\caval\Documents\ufc\analise-desempenho\projeto\src\dataset\{}\train\y_train.txt'.format(nomePasta),'w') as file:
  for row in y_train:
    line = str(row) + '\n'
    file.write(line)

with open(r'C:\Users\caval\Documents\ufc\analise-desempenho\projeto\src\dataset\{}\test\y_test.txt'.format(nomePasta),'w') as file:
  for row in y_test:
    line = str(row) + '\n'
    file.write(line)

