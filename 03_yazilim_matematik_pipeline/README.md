# Modül 3: Yazılım, Matematik ve Pipeline

Donanımdan alınan ham verinin anlamlı bir 3B dünyaya dönüşmesi için ileri seviye uzamsal matematik ve sağlam bir sistem mimarisi (render loop) gereklidir.

## Teorik Altyapı
- **Gimbal Lock (Euler Açıları)**: 3B dönüşümlerde (X, Y, Z eksenlerinde dönme) iki eksenin çakışması sonucu bir serbestlik derecesinin (degree of freedom) kaybedilmesidir.
- **Quaternion (Kuaterniyon)**: Gimbal Lock problemini çözen, 4 boyutlu (w, x, y, z) kompleks sayı tabanlı dönme matematiğidir. VR'da rotasyonlar daima Kuaterniyonlar ile hesaplanır.
- **VR Runtime Loop**: Klasik oyun motoru döngüsünden farklı olarak, VR sistemleri `Oda tahmini (Pose Prediction) -> Simülasyon -> Render -> Ekrana basma` şeklinde sıkı bir sıralama izler.

## Laboratuvar (Pratik Uygulamalar)
`labs/` klasöründeki dosyaları çalıştırarak aşağıdaki kavramları pratik edebilirsiniz:

1. `01_quaternion_basics.py`: Quaternion kullanımını, rotasyon hesaplamalarını ve Gimbal Lock'tan nasıl kaçınıldığını gösteren basit script.
2. `02_vr_runtime_loop.py`: Temel bir HMD render döngüsünü taklit eder (Pose update, rendering, sync).
