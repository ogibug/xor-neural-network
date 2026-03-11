# XOR Problemi ve Yapay Sinir Ağları

Bu projede XOR probleminin tek katmanlı perceptron ve çok katmanlı yapay sinir ağı ile çözümü incelenmiştir.

## Amaç

XOR probleminin doğrusal olarak ayrılabilir olmadığını göstermek ve çok katmanlı sinir ağlarının doğrusal olmayan problemleri çözebildiğini ortaya koymak.

## Dosyalar

xor_perceptron.py → Tek katmanlı perceptron denemesi  
xor_mlp.py → Gizli katmanlı sinir ağı çözümü  
rapor.md → Deney raporu  

## XOR Veri Seti

| x1 | x2 | y |
|----|----|---|
| 0 | 0 | 0 |
| 0 | 1 | 1 |
| 1 | 0 | 1 |
| 1 | 1 | 0 |

## Kullanım

```bash
python xor_perceptron.py
python xor_mlp.py