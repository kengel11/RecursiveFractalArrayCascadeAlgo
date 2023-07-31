import tensorflow as tf
import numpy as np

# Define the number of inputs, hidden layers, and outputs
n_inputs = X_train.shape[1]
n_hidden1 = 32
n_hidden2 = 64
n_outputs = 2

# Define the model
model = tf.keras.models.Sequential([
    tf.keras.layers.Dense(n_hidden1, activation='relu', input_shape=(n_inputs,)),
    tf.keras.layers.Dense(n_hidden2, activation='relu'),
    tf.keras.layers.Dense(n_outputs, activation='softmax')
])

# Compile the model
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

# Train the model
model.fit(X_train, y_train, epochs=10, batch_size=32)

# Evaluate the model
model.evaluate(X_test, y_test)

# Use the model to make predictions
y_probs = model.predict(X_test)


