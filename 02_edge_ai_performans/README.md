# Modül 2: Edge-AI ve Performans

Sanal gerçeklik cihazları, bulut sunucularına bağımlı kalmadan **kendi içlerinde (On-Premise / Edge)** karmaşık işlemleri yapabilmelidir. Yüksek çözünürlük, yapay zeka modelleri ve düşük gecikme bir araya geldiğinde donanım darboğazları oluşur.

## Teorik Altyapı
- **Foveated Rendering**: İnsan gözünün sadece odaklandığı noktayı net (fovea bölgesi), çevreyi ise bulanık (çevresel vizyon) görmesinden ilham alır. GPU gücünü sadece bakılan noktada yüksek çözünürlüğe harcamaktır.
- **Motion-to-Photon Latency**: Kullanıcının kafasını çevirdiği an (motion) ile bu değişimin ekrana yansıdığı an (photon) arasındaki gecikmedir. VR için altın kural <20ms olmasıdır.
- **Model Budama (Pruning) & Kuantizasyon**: Yapay zeka modellerinin (ör. el takibi) gözlüğün kısıtlı işlemcisinde çalışabilmesi için 32-bit'ten 8-bit'e sıkıştırılmasıdır.

## Laboratuvar (Pratik Uygulamalar)
`labs/` klasöründeki dosyaları çalıştırarak aşağıdaki kavramları pratik edebilirsiniz:

1. `01_foveated_tile_planner.py`: Ekranı bölgelere (tile) bölerek, bakış açısına göre hangi bölgelerin yüksek, hangi bölgelerin düşük çözünürlükte çizileceğini belirleyen algoritma simülatörü.
2. `02_latency_profiler.py`: Motion-to-photon gecikmesinin hangi aşamalarda (sensör okuma, render, ağ) oluştuğunu inceleyen simülasyon profil aracı.
