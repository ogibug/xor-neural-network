# xor_perceptron.py

import numpy as np

# XOR veri seti
X = np.array([
    [0, 0],
    [0, 1],
    [1, 0],
    [1, 1]
])

y = np.array([0, 1, 1, 0])

# perceptron parametreleri
weights = np.zeros(2)
bias = 0.0
learning_rate = 0.1
epochs = 20

def step_function(x):
    return 1 if x >= 0 else 0

print("Tek Katmanlı Perceptron - XOR Problemi\n")

for epoch in range(epochs):
    total_error = 0
    for i in range(len(X)):
        linear_output = np.dot(X[i], weights) + bias
        y_pred = step_function(linear_output)

        error = y[i] - y_pred
        total_error += abs(error)

        weights += learning_rate * error * X[i]
        bias += learning_rate * error

    print(f"Epoch {epoch+1}: Toplam Hata = {total_error}")

print("\nEğitim Sonrası Tahminler:")
for i in range(len(X)):
    pred = step_function(np.dot(X[i], weights) + bias)
    print(f"Girdi: {X[i]} -> Tahmin: {pred}, Gerçek: {y[i]}")

print("\nSonuç:")
print("Tek katmanlı perceptron XOR problemini tam olarak öğrenemez.")