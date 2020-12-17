import pandas as pd
import tensorflow as tf
import numpy as np
import itertools as it
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

# concatenate the separate files
dir = './data2/'
df1 = pd.read_csv(dir+'DNNRNN_testing_medusa_Media.csv')
df2 = pd.read_csv(dir+'DNNRNN_testing_medusa_webSearch.csv')
df3 = pd.read_csv(dir+'DNNRNN_testing_medusa.csv')

df = pd.concat([df1, df2, df3], axis=0, ignore_index=True)
df = df.dropna()

# these are relatively uninformative, as seen in linear regression
labels_to_drop = [
    'timeStamp',
    'systemTime1Sec',
    'ioWaitTime1Sec',
    'percentVirtualMemory',
    'networkBytesSent',
    'networkBytesReceived',
    'networkConnections',
    'systemCalls',
    'cacheMemoryUsedBytes',
    'swapMemoryUsedBytes',
    'swapMemoryOutBytes',
    'swapMemoryInBytes',
    'ioReadBytes',
    'ioWriteBytes',
    'predictedPower'
]
df = df.drop(columns=labels_to_drop, axis=1)

# shuffle dataframe
df = df.sample(frac = 1)

# split into training and testing data
training_data = df.iloc[:int(0.85*len(df)), :]
testing_data = df.iloc[int(0.85*len(df)):, :]

# training target and features
trn_target = training_data.pop('whatsupPower')
trn_features = training_data.values

# normalized training features
trn_norm_features = MinMaxScaler().fit_transform(trn_features)

# ? is just using trn_target the same as trn_target.values in this case

# training dataset
trn = tf.data.Dataset.from_tensor_slices((trn_norm_features, trn_target))

# create validation dataset and edit size of training dataset
trn_ds_size = int(len(training_data)*0.7)
sample_tst_ds_size = int(len(training_data)*0.15)

trn_ds = trn.take(trn_ds_size)
sample_tst_ds = trn.skip(trn_ds_size)
val_ds = sample_tst_ds.skip(sample_tst_ds_size)
sample_tst_ds = sample_tst_ds.take(sample_tst_ds_size)

# build the model
# model = keras.Sequential(
#     [
#         # layers.Dense(units=64, input_dim=9, activation='relu', name='layer1'),
#         # layers.Dense(units=64, activation='relu', name='layer2'),
#         # layers.Dense(units=1, name='end'),
#
#         layers.Dense(units=32, activation='relu'),
#         layers.Dense(units=16, activation='relu'),
#         layers.Dense(units=32, activation='relu'),
#         layers.Dense(units=8,activation='relu'),
#         layers.Dense(1)
#     ]
# )

# model.compile(
#     optimizer=tf.keras.optimizers.Adam(learning_rate=0.00001),
#     loss='mean_absolute_error',
#     metrics=['mean_absolute_error'],
# )

# ALTERNATE METHOD
# model.compile(
#     optimizer='adam',
#     loss=tf.keras.losses.MeanSquaredError(reduction="auto", name="mean_squared_error"),
#     metrics=['mse']
# )

# model.fit(
#     x=trn_ds,
#     epochs=200,
#     validation_data=val_ds,
#     verbose=1,
#     callbacks=[tf.keras.callbacks.EarlyStopping(patience=10)],
#     shuffle=False,
# )

# evaluate the model
# model.evaluate(
#     x=sample_tst_ds,
#     verbose=1,
#     callbacks=[tf.keras.callbacks.EarlyStopping(patience=10)],
# )

# testing target and features
tst_target = testing_data.pop('whatsupPower')
tst_features = testing_data.values

# testing normalized features
tst_norm_features = MinMaxScaler().fit_transform(tst_features)

# testing dataset
tst_ds = tf.data.Dataset.from_tensor_slices((tst_norm_features, tst_target))

# save the current model and delete it, reinstantiating later with the saved weights
# model.save(
#     filepath='/tmp/DNNRNN_testing_medusa01',
# )
# del model

# reinstantiate saved weights
model = keras.models.load_model('/tmp/DNNRNN_testing_medusa01')

# make predictions on test values
predictions = model.predict(
    x=tst_ds,
    verbose=1,
)

actual_values = tst_target.values.tolist()
predicted_values = list(it.chain.from_iterable(predictions.tolist()))

total = []
total.extend(actual_values)
total.extend(predicted_values)
max_val = max(total)

ax = plt.axes()
ax.set_xlim([0, max_val+10])
ax.set_ylim([0, max_val+10])

for index, a in enumerate(actual_values):
    offset = abs(a - predicted_values[index])
    plt.scatter(a, predicted_values[index], c='red')

plt.title('Predicted and Actual Energy Consumption in Watts')
plt.xlabel('ACTUAL VALUE')
plt.ylabel('PREDICTED VALUE')
plt.legend()
plt.show()


# # REGRESSION TESTING
target = data.pop('Wattage') #y
features =data.values #X
#
#
# #features = data[['CPU_Freq']]
#
# # alt
#target = data['Wattage']
# features = data[['CPU_Freq','CPU_Util','Num_Proc','Num_Apps']]
#
#linear_regression = LinearRegression()
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


# NN TESTING
#file_path = 'data/cleaned_1+2.npy'
file_path = 'data/cleaned_02.npy'
arr = np.load(file=file_path)

data = pd.DataFrame(data=arr, columns=['CPU_Freq','CPU_Util','Num_Proc','Num_Apps','Wattage'])




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
