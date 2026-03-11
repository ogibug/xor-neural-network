# XOR Problemi Deney Raporu

## 1 Amaç

Bu deneyin amacı XOR probleminin yapay sinir ağları açısından önemini incelemek ve tek katmanlı perceptron ile çok katmanlı sinir ağları arasındaki farkı göstermektir.

## 2 Teorik Bilgi

XOR problemi doğrusal olarak ayrılabilir değildir. Bu nedenle tek katmanlı perceptron algoritması XOR problemini çözemez. Ancak gizli katman içeren çok katmanlı sinir ağları doğrusal olmayan karar sınırları oluşturabildiği için bu problemi öğrenebilir.

## 3 Uygulama

Bu çalışmada Python kullanılarak iki model uygulanmıştır:

1 Tek katmanlı perceptron  
2 Gizli katmanlı çok katmanlı sinir ağı

Tek katmanlı model XOR problemini öğrenememiştir.  
Çok katmanlı model ise doğru çıktıları üretmiştir.

## 4 Veri Seti

| x1 | x2 | y |
|----|----|---|
|0|0|0|
|0|1|1|
|1|0|1|
|1|1|0|

## 5 Sonuç

Deney sonucunda XOR probleminin doğrusal ayrılabilir olmadığı görülmüştür. Bu nedenle tek katmanlı perceptron algoritması problemi çözememiştir. Gizli katman içeren çok katmanlı sinir ağı ise problemi başarıyla öğrenmiştir.