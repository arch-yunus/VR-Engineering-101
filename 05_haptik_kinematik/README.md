# Modül 5: Haptik Geri Bildirim ve Kinematik

Sanal gerçeklikte sadece görmek ve duymak yetmez; fiziksel dünyanın direncini (force feedback), dokusunu (texture) ve kendi bedenimizin hareketlerini (kinematics) de hissetmemiz gerekir.

## Teorik Altyapı
- **Haptik Aktüatörler (ERM, LRA, VCM)**: Klasik telefon titreşim motorları (ERM) yerine, sanal dünyadaki objelerin dokusunu simüle etmek için daha hassas olan LRA (Linear Resonant Actuator) ve Ses Bobini Motorları (VCM) kullanılır.
- **Titreşim Frekansları**: Ahşap bir masaya vurmak düşük frekanslı tok bir his (örn. 50-80 Hz) yaratırken, cama vurmak yüksek frekanslı keskin bir his (örn. 200-250 Hz) yaratır.
- **Ters Kinematik (Inverse Kinematics - IK)**: Sadece ellerimizin nerede olduğunu bildiğimizde (kumanda takibi), dirseklerimizin ve omuzlarımızın doğal olarak nerede olması gerektiğini hesaplayan matematik dalıdır. Tüm VR oyunlarında karakterin kolunu bükmesi bu sayede olur.

## Laboratuvar (Pratik Uygulamalar)
`labs/` klasöründeki dosyaları çalıştırarak aşağıdaki kavramları pratik edebilirsiniz:

1. `01_vibration_frequency_analyzer.py`: Sanal objelere dokunulduğunda üretilmesi gereken haptik frekans sinyallerini analiz eden simülatör.
2. `02_inverse_kinematics_arm.py`: Omuz sabitken sadece elin (hedef noktanın) pozisyonu bilindiğinde dirsek açısını hesaplayan basit trigonometrik IK simülatörü.
