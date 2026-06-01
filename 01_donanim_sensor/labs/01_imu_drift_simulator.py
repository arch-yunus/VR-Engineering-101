import math
import random
import time

def simulate_imu_drift():
    print("--- IMU Drift (Sapma) Simülasyonu ---")
    print("Sabit duran bir VR gözlüğünün jiroskop sensörü verisi okunuyor...")
    
    true_angle = 0.0
    estimated_angle = 0.0
    drift_rate = 0.05 # Saniyede 0.05 derece sapma
    dt = 1.0 # 1 saniyelik zaman adımları
    
    for step in range(1, 11):
        # Gerçekte cihaz sabit (0 rotasyon)
        # Ancak jiroskop gürültü ve sabit bir bias (drift) üretir.
        gyro_noise = random.uniform(-0.01, 0.01)
        gyro_reading = drift_rate + gyro_noise
        
        # İntegrasyon (Açı = Açı + Açısal_Hız * Zaman)
        estimated_angle += gyro_reading * dt
        
        print(f"Saniye {step}: Gerçek Açı = {true_angle:.2f}°, Sensör Tahmini = {estimated_angle:.2f}° (Hata: {estimated_angle - true_angle:.2f}°)")
        time.sleep(0.3)
        
    print("\nSonuç: Sadece jiroskop kullanılarak yönelim hesaplandığında, zamanla oluşan küçük hatalar birikerek büyük sapmalara (drift) yol açar.")
    print("Bunu çözmek için İvmeölçer ve Manyetometre verileri Kalman veya Madgwick filtreleriyle jiroskop verisiyle birleştirilir (Sensor Fusion).")

if __name__ == "__main__":
    simulate_imu_drift()
