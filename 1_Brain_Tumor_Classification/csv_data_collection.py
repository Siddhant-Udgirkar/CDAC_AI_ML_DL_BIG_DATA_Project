import os
import numpy as np
import pandas as pd
from tensorflow.keras.models import Model
from tensorflow.keras.layers import Input, Flatten, Dense, Dropout
from tensorflow.keras.applications.vgg19 import VGG19

# Load the model
base_model = VGG19(include_top=False, input_shape=(240, 240, 3))
x = base_model.output
flat = Flatten()(x)
class_1 = Dense(4608, activation='relu')(flat)
drop_out = Dropout(0.2)(class_1)
class_2 = Dense(1152, activation='relu')(drop_out)
output = Dense(2, activation='softmax')(class_2)
model_03 = Model(base_model.inputs, output)
model_03.load_weights('vgg_unfrozen.h5')

# Compile the model
model_03.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

# Assume train_data, train_labels, val_data, val_labels are already defined
# Train the model
history_01 = model_03.fit(train_data, train_labels, epochs=50, validation_data=(val_data, val_labels))

# Create a DataFrame to store the data
history_df = pd.DataFrame({
    'Epoch': list(range(1, len(history_01.history['accuracy']) + 1)),
    'Training_Accuracy': history_01.history['accuracy'],
    'Validation_Accuracy': history_01.history['val_accuracy'],
    'Training_Loss': history_01.history['loss'],
    'Validation_Loss': history_01.history['val_loss']
})

# Save the DataFrame to a CSV file
history_df.to_csv('model_training_history.csv', index=False)
