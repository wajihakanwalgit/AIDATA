
import tensorflow as tf
from tensorflow.keras import layers, models
import matplotlib.pyplot as plt

(x_train, y_train), (x_test, y_test) = tf.keras.datasets.mnist.load_data()
x_train, x_test = x_train / 255.0, x_test / 255.0
model = models.Sequential([

    layers.Flatten(input_shape=(28, 28)),

    layers.Dense(128, activation='relu'),

    layers.Dense(10, activation='softmax')

])

model.compile(optimizer='adam',

              loss='sparse_categorical_crossentropy',

              metrics=['accuracy'])

model.fit(x_train, y_train, epochs=5)
est_loss, test_acc = model.evaluate(x_test, y_test)

print(f"Test accuracy: {test_acc}")

predictions = model.predict(x_test)

num_images = 25  # Change this number if you want to display more or fewer images

plt.figure(figsize=(10, 10))

for i in range(num_images):

    plt.subplot(5, 5, i + 1)

    plt.xticks([])

    plt.yticks([])

    plt.grid(False)

    plt.imshow(x_test[i], cmap=plt.cm.binary)

   

    # Get the predicted label for the image

    predicted_label = predictions[i].argmax()

    true_label = y_test[i]

   

    # Color the label blue if correct, red if incorrect

    color = 'blue' if predicted_label == true_label else 'red'

    plt.xlabel(f"Pred: {predicted_label}\nTrue: {true_label}", color=color)


plt.tight_layout()

plt.show()