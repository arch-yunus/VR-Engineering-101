# Modül 4: Ağ ve Güvenlik (Security by Design)

Çok oyunculu (multiplayer) veya tele-operasyon (ROS2) tabanlı VR sistemlerinde veri akışı genelde TCP yerine **UDP** üzerinden yapılır. Bunun sebebi UDP'nin paket kontrolü yapmayarak düşük gecikme sağlamasıdır. Ancak bu durum güvenlik açıklarına yol açar.

## Teorik Altyapı
- **UDP Snapshot**: Sunucunun oyunculara (veya başlığa) her karede dünyanın o anki halini "fotoğraf (snapshot)" gibi göndermesidir.
- **Paket Kaybı & Jitter**: UDP'de paketlerin sırası karışabilir veya yolda kaybolabilir. Bunu istemci tarafında "Interpolation" ve "Extrapolation" (tahminleme) ile çözeriz.
- **Spoofing & Replay Attacks**: Şifrelenmemiş UDP paketleri ağda dinlenebilir, değiştirilebilir veya aynı paket tekrar gönderilerek hile yapılabilir (örneğin eski bir konuma ışınlanma).

## Laboratuvar (Pratik Uygulamalar)
`labs/` klasöründeki dosyaları çalıştırarak aşağıdaki kavramları pratik edebilirsiniz:

1. `01_udp_snapshot_simulator.py`: Ağ gecikmesi, paket kaybı ve sıra bozulmasını simüle eden bir ağ laboratuvarı.
2. `02_secure_avatar_sync.py`: Paketleri basitçe imzalayarak hileli verileri (ör. Spoofing veya Replay) engelleyen güvenlik konsepti.
