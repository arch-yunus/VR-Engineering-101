# Proje Havuzu (Bitirme Projeleri - Capstone)

Bu dosya, repoyu "okuma listesi" olmaktan cikarip gercek bir VR muhendisligi
atolyesine donusturecek gorevleri toplar. 

Asagida, temel modulleri tamamlayan ogrencilerin (veya katkimda bulunmak isteyenlerin) ele alabilecegi gercek dunya (real-world) seviyesindeki projeler yer almaktadir.

## TRL 1-2: Kavram Kanitlari

| Proje | Modul | Cikti |
| --- | --- | --- |
| IMU drift defteri | Donanim/Sensor | Drift, bias ve filtre notlari |
| FOV hesaplayici | Donanim/Sensor | Lens/display parametrelerinden FOV tahmini |
| Quaternion kartlari | Matematik | Carpim, ters, normalizasyon ornekleri |

## TRL 3-4: Calisan Prototipler

| Proje | Modul | Cikti |
| --- | --- | --- |
| Motion-to-photon profiler | Performans | CSV girdisinden latency raporu |
| Foveated tile planner | Edge-AI | Bakis noktasina gore tile kalite haritasi |
| UDP snapshot simulator | Ag | Siralama, jitter ve kayip simulasyonu |
| Ters Kinematik 3D | Haptik/Kinematik | Python ile 3 Eklemli (Omuz, Dirsek, Bilek) IK Cözücüsü |
| HRTF Panning Filter | Ses | Gerçek bir wav dosyasını açıya göre filtreleyen script |

## TRL 5+: Sistem Entegrasyonu (Capstone Projeleri)

| Proje | Modul | Cikti |
| --- | --- | --- |
| Mini VR runtime loop | Pipeline | Pose update, simulation, render sirasi |
| Secure avatar sync | Ag/Guvenlik | Paket imzasi, replay korumasi, rate limit |
| ROS2 VR Digital Twin | ROS2 | ROS2 uzerinden yayinlanan `joint_states` verisini alip ekrana yazdiran veya cizen entegrasyon |
| Ses-Haptik Senkronizasyonu | Ses/Haptik | Objeye carpma aninda ayni anda hem HRTF ses hem de ilgili LRA titresim profilini ureten birlesik modul |

## Onceliklendirme

1. Once olculebilir lab.
2. Sonra dokumantasyon.
3. En son genis entegrasyon.

Her proje, README'de anlatilan kalite kapilarindan gecmelidir.
