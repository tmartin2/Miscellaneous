import pandas as pd
import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import ElasticNet
from sklearn.linear_model import Lasso
from sklearn.linear_model import SGDRegressor
from sklearn.preprocessing import normalize
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import mean_squared_error
from tensorflow import keras
from tensorflow.keras import layers


filepath = './dirty/DNNRNN_testing_medusa.csv'

df = pd.read_csv(filepath_or_buffer=filepath)

print(df)
training_data = df.iloc[:, int(0.85*len(df)):]
testing_data = df.iloc[:, :int(0.85*len(df))]

target = df.pop('predictedPower')
features = df.values

ds = tf.data.Dataset.from_tensor_slices((data[:,:4], data[:,-1].reshape(-1,1)))

ds =




# # REGRESSION TESTING
# target = data.pop('Wattage') #y
# features =data.values #X
#
#
# #features = data[['CPU_Freq']]
#
# # alt
# #target = data['Wattage']
# #features = data[['CPU_Freq','CPU_Util','Num_Proc','Num_Apps']]
#
# linear_regression = LinearRegression()
# linear_regression.fit(features, target)
# y_pred = linear_regression.predict(features)
# LR_ERROR = mean_squared_error(target, y_pred)
# print(f'LINEAR REGRESSION ERROR IS {LR_ERROR}')
# plt.title('Wattage Predictions')
# plt.plot(target, color='black', linewidth=2.0, label='Actual Wattage')
# plt.plot(y_pred, color='red', alpha=0.85, label='Predicted Wattage Li')
#
# # Normalizing Does Nothing
# #linear_regression = LinearRegression(normalize=True)
# #linear_regression.fit(features, target)
# #y_pred = linear_regression.predict(features)
# #plt.plot(y_pred, color='blue', alpha=0.75, label='Normalized Predicted Wattage')
#
# elastic_regression = ElasticNet()
# elastic_regression.fit(features, target)
# y_pred = elastic_regression.predict(features)
# plt.plot(y_pred, color='blue', alpha=0.85, label='Predicted Wattage E')
#
# lasso_regression = Lasso(tol=1e-2)
# lasso_regression.fit(features, target)
# y_pred = lasso_regression.predict(features)
# plt.plot(y_pred, color='green', alpha=0.85, label='Predicted Wattage La')
#
# features = normalize(features)
# sgd_regression = SGDRegressor(penalty='l1', max_iter=3000, learning_rate='adaptive', alpha=0.00001, verbose=1, shuffle=False)
# sgd_regression.fit(features, target)
# y_pred = sgd_regression.predict(features)
# plt.plot(y_pred, color='cyan', alpha=0.85, label='Predicted Wattage SGD')
#
# plt.legend()
# plt.show()
#
# #ERROR = mean_squared_error(targets, y_pred)


# # NN TESTING
# #file_path = 'data/cleaned_1+2.npy'
# file_path = 'data/cleaned_02.npy'
# arr = np.load(file=file_path)
#
# data = pd.DataFrame(data=arr, columns=['CPU_Freq','CPU_Util','Num_Proc','Num_Apps','Wattage'])
#
#
#
#
# #target = data.pop('Wattage')
# #normed_data = pd.DataFrame(MinMaxScaler().fit_transform(data), columns=['CPU_Freq','CPU_Util','Num_Proc','Num_Apps','Wattage'])
# #print(normed_data.shape)
#
# #target = data.pop('Wattage')
# #print(data.values)
# data = MinMaxScaler().fit_transform(data.values).reshape(len(data),5)
# print(data[:,:4].shape)
# print(data[:, -1].reshape(-1,1).shape)
# dataset = tf.data.Dataset.from_tensor_slices((data[:,:4], data[:,-1].reshape(-1,1)))
# #dataset = dataset.shuffle(buffer_size=int(len(data)*0.7), seed=1234, reshuffle_each_iteration=True)
#
# train_size = int(len(data)*0.7)
# test_size = int(len(data)*0.15)
# train_dataset = dataset.take(train_size)
# test_dataset = dataset.skip(train_size)
# val_dataset = test_dataset.skip(test_size)
# test_dataset = test_dataset.take(test_size)
#
# model = keras.Sequential(
#     [
#         layers.Dense(units=32, activation='relu', name='layer1'),
#         layers.Dense(units=64, activation='relu', name='layer2'),
#         layers.Dense(units=1, name='end'),
#     ]
# )
#
# model.compile(
#     optimizer='adam',
#     loss='mse',#tf.keras.losses.MeanSquaredError(reduction="auto", name="mean_squared_error"),
#     metrics=['mse']
# )
#
#
# model.fit(
#     x=train_dataset,
#     epochs=20,
#     validation_data=val_dataset,
#     verbose=1,
#     callbacks=[tf.keras.callbacks.EarlyStopping(patience=5)],
#     shuffle=False,
# )
#
# model.evaluate(
#     x=test_dataset,
#     verbose=1,
#     callbacks=[tf.keras.callbacks.EarlyStopping(patience=5)],
# )
#
# model.save(
#     filepath='/tmp/trained_on_cleaned_02',
# )
# del model
#
# model = keras.models.load_model('/tmp/trained_on_cleaned_02')
#
# file_path = 'data/cleaned_1+2.npy'
# arr = np.load(file=file_path)
# data = pd.DataFrame(data=arr, columns=['CPU_Freq','CPU_Util','Num_Proc','Num_Apps','Wattage'])
# x = data.pop('Wattage')
# y = data.values
#
# #actual = data['Wattage']
# #print(f'UNSCALED ACTUAL: {actual}')
# #data = MinMaxScaler().fit_transform(data.values).reshape(len(data),5)
# dataset = tf.data.Dataset.from_tensor_slices((y, x))
#
# predictions = model.predict(
#     x=dataset,
#     verbose=1,
# )
#
# #actual_vals = data[:,-1].reshape(-1,1)
# #print(f'RESCALED ACTUAL: {actual_vals}')
#
# plt.plot(x, color='red', label='Scaled Actual')
# plt.plot(predictions, color='blue', label='Scaled Predictions')
# plt.legend()
# plt.show()
