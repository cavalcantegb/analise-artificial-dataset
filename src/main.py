import numpy as np
from knnDtw import KnnDtw
from sklearn.metrics import classification_report, confusion_matrix
import matplotlib.pyplot as plt
from sklearn.externals import joblib
import time

pasta = 'HT104'

X_train_file = open('dataset/{}/train/X_train.txt'.format(pasta), 'r')
y_train_file = open('dataset/{}/train/y_train.txt'.format(pasta), 'r')
X_test_file = open('dataset/{}/test/X_test.txt'.format(pasta), 'r')
y_test_file = open('dataset/{}/test/y_test.txt'.format(pasta), 'r')

X_train = []
X_test = []
y_train = []
y_test = []

# Mapping table for classes
labels = {1:'DYING', 2:'NOT DYING', 3:'PRETTY OKAY'}

for x in X_train_file:
    X_train.append([float(ts) for ts in x.split()])

for y in y_train_file:
    y_train.append(int(y.rstrip('\n')))

for x in X_test_file:
    X_test.append([float(ts) for ts in x.split()])

for y in y_test_file:
    y_test.append(int(y.rstrip('\n')))

# Convert to numpy for efficiency
X_train = np.array(X_train)
y_train = np.array(y_train)
X_test = np.array(X_test)
y_test = np.array(y_test)

start = time.time()
neighbours = 2
clf = KnnDtw(n_neighbors=neighbours, max_warping_window=10)
clf.fit(X_train, y_train)
label, proba = clf.predict(X_test)
end = time.time()

print("Tempo total: {}s".format(end-start) )
print("Número de Vizinhos = {}\n".format(neighbours))

# print(classification_report(label, y_test, target_names=[l for l in labels.values()]))

# conf_mat = confusion_matrix(label, y_test)

# fig = plt.figure(figsize=(3,3))
# width = np.shape(conf_mat)[1]
# height = np.shape(conf_mat)[0]

# sr = 100*np.sum(np.diag(conf_mat))/np.sum(conf_mat)

# n_neighbors = clf.n_neighbors

# print('Parâmetros Utilizados:')
# print(f'Número de Vizinhos = {n_neighbors}\n')

# print(f'Taxa de Acerto: {sr:0.2f}%')
# print(f'Matriz de Confusão: \n {conf_mat}')