# xor_mlp.py

import numpy as np

np.random.seed(42)

# XOR veri seti
X = np.array([
    [0, 0],
    [0, 1],
    [1, 0],
    [1, 1]
], dtype=float)

y = np.array([
    [0],
    [1],
    [1],
    [0]
], dtype=float)

# Aktivasyon fonksiyonu: sigmoid
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def sigmoid_derivative(x):
    return x * (1 - x)

# Ağ yapısı
input_neurons = 2
hidden_neurons = 2
output_neurons = 1

# Ağırlıklar
W1 = np.random.uniform(size=(input_neurons, hidden_neurons))
b1 = np.random.uniform(size=(1, hidden_neurons))

W2 = np.random.uniform(size=(hidden_neurons, output_neurons))
b2 = np.random.uniform(size=(1, output_neurons))

learning_rate = 0.5
epochs = 10000

for epoch in range(epochs):
    # Forward propagation
    hidden_input = np.dot(X, W1) + b1
    hidden_output = sigmoid(hidden_input)

    final_input = np.dot(hidden_output, W2) + b2
    final_output = sigmoid(final_input)

    # Hata
    error = y - final_output

    # Backpropagation
    d_output = error * sigmoid_derivative(final_output)
    error_hidden = d_output.dot(W2.T)
    d_hidden = error_hidden * sigmoid_derivative(hidden_output)

    # Ağırlık güncelleme
    W2 += hidden_output.T.dot(d_output) * learning_rate
    b2 += np.sum(d_output, axis=0, keepdims=True) * learning_rate

    W1 += X.T.dot(d_hidden) * learning_rate
    b1 += np.sum(d_hidden, axis=0, keepdims=True) * learning_rate

    if epoch % 1000 == 0:
        loss = np.mean(np.square(error))
        print(f"Epoch {epoch}: Loss = {loss:.6f}")

print("\nMLP Tahminleri:")
for i in range(len(X)):
    hidden = sigmoid(np.dot(X[i], W1) + b1)
    output = sigmoid(np.dot(hidden, W2) + b2)
    pred = 1 if output[0][0] >= 0.5 else 0
    print(f"Girdi: {X[i].astype(int)} -> Tahmin: {pred}, Olasılık: {output[0][0]:.4f}, Gerçek: {int(y[i][0])}")

print("\nSonuç:")
print("Gizli katman içeren çok katmanlı sinir ağı XOR problemini başarıyla öğrenmiştir.")