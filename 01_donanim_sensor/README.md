# Modül 1: Donanım Mimarisi ve Sensör Füzyonu

Sanal gerçeklikte dijital objelerin yerçekimi, başımızın dönüşü ve doğrusal ivmemizi bilmesi tamamen **sensör füzyonu (sensor fusion)** sayesindedir.

## Teorik Altyapı
- **IMU (Inertial Measurement Unit)**: İvmeölçer (Accelerometer), Jiroskop (Gyroscope) ve Manyetometre içerir.
- **Drift (Sapma)**: Jiroskoplar zamanla biriken hatalar (integral alımından dolayı) üretir. Buna drift denir.
- **Kalman Filtresi**: Farklı sensörlerden gelen gürültülü veriyi, matematiksel bir modelle birleştirip "en olası" gerçek durumu (state estimation) bulmamızı sağlar.
- **Görüş Alanı (FOV - Field of View)**: Optik lensin ekrandaki pikselleri gözümüze ne kadar geniş bir açıyla iletebildiğini belirler.

## Laboratuvar (Pratik Uygulamalar)
`labs/` klasöründeki dosyaları çalıştırarak aşağıdaki kavramları pratik edebilirsiniz:

1. `01_imu_drift_simulator.py`: Jiroskop drift problemini görselleştirir.
2. `02_kalman_filter_1d.py`: 1 boyutlu ortamda gürültülü sensör okumalarından gerçek değeri bulur.
3. `03_fov_calculator.py`: Ekran boyutu ve lens mesafesi (focal length) parametrelerinden FOV değerini hesaplar.
