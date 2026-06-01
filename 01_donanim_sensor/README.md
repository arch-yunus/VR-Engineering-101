# Modul 1: Donanim ve Sensor Mimarisi

## Hedef

Bir VR basliginin fiziksel sinirlarini ve sensor verisinin neden ham haliyle
kullanilamayacagini anlamak.

## Ana Kavramlar

- HMD optigi: lens distorsiyonu, FOV, IPD, ekran cozunurlugu.
- IMU: ivmeolcer, jiroskop, manyetometre, bias ve drift.
- Sensor fuzyonu: complementary filter, Kalman fikri, zaman damgasi uyumu.
- Haptik: PWM, frekans, siddet, insan algisi ve guvenli calisma araligi.

## Lab

```bash
python 01_donanim_sensor/labs/imu_complementary_filter.py
```

Lab, sentetik IMU verisinden roll acisini tahmin eder ve jiroskop drift'inin
ivmeolcerle nasil dengelendigini gosterir.

## Kontrol Listesi

- IMU verisinde bias neden olusur?
- Complementary filter'da alpha artarsa hangi sensor daha baskin olur?
- HMD'de refresh rate ve motion sickness arasindaki iliski nedir?
