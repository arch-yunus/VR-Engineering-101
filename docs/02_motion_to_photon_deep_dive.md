# Derinlemesine Analiz: Motion-to-Photon Gecikmesi (M2P Latency)

Kafanızı çevirdiğiniz an ile (Motion), bu hareketin ekranda yeni bir piksel olarak gözünüze ulaşması (Photon) arasında geçen süreye **Motion-to-Photon (M2P) Latency** denir.

İdeal bir VR sisteminde bu süre **20 milisaniyenin (ms)** altında olmalıdır. 

## Neden 20ms?
İnsan beyni, gözünden gelen görsel veri ile iç kulağından gelen denge verisini eşleştirir. Eğer görsel veri 20ms'den daha geç gelirse, beyin "Zehirlendim, halüsinasyon görüyorum" tepkisi verir ve kusma refleksi (Motion Sickness) tetiklenir.

## 20ms'nin Anatomisi (Nasıl Harcanır?)

1. **Sensör Okuma ve Filtreleme (1-2 ms):**
   Gözlüğün içindeki IMU (Jiroskop ve İvmeölçer) 1000Hz (saniyede 1000 kere) hızında okunur. Bu ham veri Kalman Filtresi ile gürültüden arındırılır.

2. **Oyun Mantığı ve Fizik (4-6 ms):**
   CPU, kullanıcının yeni kafasının pozisyonuna göre oyun içindeki diğer objelerin yerini hesaplar. Raycast'ler atılır, çarpışmalar (collisions) tespit edilir.

3. **Render - GPU (7-10 ms):**
   En ağır kısımdır. Gözlükteki iki ekran (sağ ve sol göz) için sahne iki kere çizilir. Çözünürlük genelde 4K'ya yakındır. GPU'nun bu süreyi aşmaması için Foveated Rendering veya Level of Detail (LOD) teknikleri hayati önem taşır.

4. **Warping / Asynchronous TimeWarp (1-2 ms):**
   Kare ekrana basılmadan hemen önce, eğer son 10ms içinde kafamız biraz daha döndüyse, çizilmiş kare GPU tarafından hafifçe "kaydırılarak" (warp) son kafa pozisyonuna uydurulur. Bu, hayat kurtaran bir VR tekniğidir.

5. **Display Scanout (2-3 ms):**
   Piksellerin fiziksel olarak OLED veya LCD ekranda yanıp ışık üretme süresidir.
