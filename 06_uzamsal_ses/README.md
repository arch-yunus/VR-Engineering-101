# Modül 6: Uzamsal Ses ve Akustik (Spatial Audio)

Sanal bir dünyada inandırıcılığı (immersion) artırmanın en kritik yollarından biri sesin uzamsal (3D) olarak doğru hesaplanmasıdır. Sesin sadece stereo sağ/sol gelmesi yeterli değildir; sesin nereden geldiği, mesafesi ve objelere çarpıp çarpılmadığı beynimizi gerçekliğe ikna eden unsurlardır.

## Teorik Altyapı
- **HRTF (Head-Related Transfer Function)**: Kafamızın şekli, kulak kepçemizin yapısı nedeniyle ses dalgalarının kulak zarına ulaşana kadar nasıl değişime uğradığını modellediğimiz matematiksel bir transfer fonksiyonudur. Gerçekçi 3D ses bu formülle üretilir.
- **ITD (Interaural Time Difference)**: Sesin sağ kulağa sol kulaktan (veya tam tersi) birkaç milisaniye daha erken ulaşmasıdır. Beynimiz yönü bu şekilde tayin eder.
- **ILD (Interaural Level Difference)**: Kafamızın sesi bloke etmesi (head shadowing) nedeniyle bir kulağa gelen sesin şiddetinin diğerine göre daha az olmasıdır.
- **Doppler Etkisi**: Bize yaklaşan bir objenin ses dalgalarının sıkışması (frekans artışı/ince ses) ve bizden uzaklaşan objenin dalgalarının seyrekleşmesi (frekans düşüşü/kalın ses) olayıdır.

## Laboratuvar (Pratik Uygulamalar)
`labs/` klasöründeki dosyaları çalıştırarak aşağıdaki kavramları pratik edebilirsiniz:

1. `01_doppler_effect_sim.py`: Sanal ortamda bize hızla yaklaşan ve uzaklaşan bir objenin (örneğin bir yarış arabası) yaydığı ses frekansının değişimini hesaplar.
2. `02_hrtf_binaural_panning.py`: Ses kaynağının açısından (azimuth) yola çıkarak ITD (Gecikme) ve ILD (Şiddet) farklarını kabaca modelleyen simülasyon.
