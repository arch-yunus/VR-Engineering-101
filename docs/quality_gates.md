# Kalite Kapilari

Bu repo icin kalite, sadece kodun calismasi degil; ogrenme degerinin ve sistem
varsayimlarinin acik olmasidir.

## Dokumantasyon

- Her modulun hedefi ve kontrol listesi var.
- Her lab'in calistirma komutu var.
- Yeni teknik terimler `docs/glossary.md` dosyasina ekleniyor.

## Kod

- Lab'lar kucuk ve tek sorumluluklu.
- Standart Python kutuphanesi tercih ediliyor.
- Komut ciktilari kisa, okunabilir ve deterministik.

## Performans

- FPS yerine frame time ve motion-to-photon gecikmesi konusuluyor.
- p95/p99 gibi tail latency metrikleri tasarim notlarinda belirtiliyor.

## Guvenlik

- Kimlik, pozisyon, bakis ve el hareketi verisi hassas kabul ediliyor.
- Ag ornekleri zarar verici exploit degil, savunma ve dogrulama odakli.
