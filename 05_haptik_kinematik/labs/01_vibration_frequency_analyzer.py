import math
import time

def simulate_haptic_feedback(material_type):
    materials = {
        "TAHTA": {"freq": 60, "amplitude": 0.8, "duration": 0.15},
        "CAM": {"freq": 250, "amplitude": 0.4, "duration": 0.05},
        "SÜNGER": {"freq": 20, "amplitude": 0.2, "duration": 0.3}
    }
    
    if material_type not in materials:
        print("Bilinmeyen materyal!")
        return
        
    mat = materials[material_type]
    print(f"\n--- Haptik Simülasyon: {material_type} ---")
    print(f"Frekans (Hz): {mat['freq']}, Genlik (Güç): {mat['amplitude']}, Süre (Sn): {mat['duration']}")
    
    # Frekansı görselleştirmek için basit bir dalga çizdirimi
    wave_length = 40
    print("Sinyal Dalgası (Controller'a gönderilen titreşim motoru verisi):")
    
    for i in range(20):
        # Basit sinüs dalgası simülasyonu
        # Yüksek frekans = daha sık dalga
        val = math.sin(i * (mat['freq'] / 50.0)) * mat['amplitude']
        
        # Sinyali ASCII ile ekrana çiz
        spaces = int((val + 1) * wave_length / 2) # -1 ile 1 arasını 0 ile wave_length arasına map et
        print(" " * spaces + "*")
        time.sleep(0.02)
        
    print("Dokunma hissi başarıyla iletildi.")

def main():
    print("=== Haptik Frekans (Titreşim) Analizörü ===")
    print("Sanal gerçeklikte kumandanın LRA motoru, dokunulan objeye göre farklı frekanslar üretir.\n")
    
    simulate_haptic_feedback("TAHTA")
    time.sleep(1)
    simulate_haptic_feedback("CAM")
    time.sleep(1)
    simulate_haptic_feedback("SÜNGER")

if __name__ == "__main__":
    main()
