import random
import time

class KalmanFilter1D:
    def __init__(self, process_variance, estimated_measurement_variance):
        self.process_variance = process_variance # Süreç (sistem) gürültüsü
        self.estimated_measurement_variance = estimated_measurement_variance # Ölçüm (sensör) gürültüsü
        self.posteri_estimate = 0.0 # Tahmin edilen değer (başlangıç)
        self.posteri_error_estimate = 1.0 # Tahmin hatası (başlangıç)

    def update(self, measurement):
        # 1. Tahmin (Predict)
        priori_estimate = self.posteri_estimate
        priori_error_estimate = self.posteri_error_estimate + self.process_variance

        # 2. Güncelleme (Update)
        blending_factor = priori_error_estimate / (priori_error_estimate + self.estimated_measurement_variance)
        self.posteri_estimate = priori_estimate + blending_factor * (measurement - priori_estimate)
        self.posteri_error_estimate = (1 - blending_factor) * priori_error_estimate

        return self.posteri_estimate

def simulate_kalman():
    print("--- 1 Boyutlu Kalman Filtresi Simülasyonu ---")
    print("Sensörden gelen gürültülü 1D konum verisi filtreleniyor...\n")
    
    kf = KalmanFilter1D(process_variance=1e-5, estimated_measurement_variance=0.1)
    true_position = 10.0
    
    for i in range(1, 16):
        # Sensör okuması (Gerçek konum + Gürültü)
        noise = random.gauss(0, 0.5)
        measurement = true_position + noise
        
        # Filtreleme
        filtered_position = kf.update(measurement)
        
        print(f"Adım {i:02d} | Gerçek: {true_position:.2f} | Ölçüm (Gürültülü): {measurement:.2f} | Filtrelenmiş: {filtered_position:.2f}")
        time.sleep(0.2)

if __name__ == "__main__":
    simulate_kalman()
