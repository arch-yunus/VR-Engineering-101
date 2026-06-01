# VR Tehdit Modeli Sablonu

Bu sablon, cok kullanicili VR veya sensor verisi isleyen bir prototipte guvenlik
varsayimlarini erken yakalamak icin kullanilir.

## Varliklar

- Kullanici pozisyonu ve hareket gecmisi
- Bakis yonu ve odaklanma verisi
- El/kol hareketleri
- Oturum kimligi
- Sahne state'i ve etkileşim olaylari

## Guven Sinirlari

| Sinir | Risk | Kontrol |
| --- | --- | --- |
| Client -> Server | Sahte pose veya hiz degeri | Imza, rate limit, fiziksel sinir kontrolu |
| Server -> Client | Manipule edilmis snapshot | Paket dogrulama, sequence kontrolu |
| Log sistemi | Hassas hareket verisinin saklanmasi | Veri azaltma, maskeleme, retention limiti |

## Kotuye Kullanim Senaryolari

- Replay: Eski ama gecerli bir paket yeniden gonderilir.
- Spoofing: Client imkansiz hizda hareket bildirir.
- Privacy leak: Bakis verisi amac disi davranis analizine donusur.
- Denial of comfort: Jitter veya sahte hareket kullanicida rahatsizlik yaratir.

## Minimum Savunmalar

- Monoton sequence number.
- Paket imzasi veya oturum anahtarina bagli MAC.
- Hiz/ivme siniri.
- Hassas telemetri icin varsayilan kapali loglama.
