import time

def calculate_doppler(original_freq, source_velocity, observer_velocity=0, speed_of_sound=343.0):
    """
    Doppler Formülü: f' = f * ((v + vo) / (v - vs))
    v: Sesin havadaki hızı (m/s)
    vo: Gözlemcinin hızı (Bize doğruysa +, uzaklaşıyorsa -)
    vs: Kaynağın hızı (Bize doğruysa +, uzaklaşıyorsa -)
    """
    # Kaynak bize doğru geliyorsa vs pozitiftir, uzaklaşıyorsa negatiftir.
    observed_freq = original_freq * ((speed_of_sound + observer_velocity) / (speed_of_sound - source_velocity))
    return observed_freq

def main():
    print("=== Uzamsal Ses: Doppler Etkisi Simülatörü ===")
    print("VR dünyasında sana doğru hızla gelen bir sanal arabanın motor sesi inceleşir (frekansı artar).")
    print("Seni geçip uzaklaştığında ise sesi kalınlaşır (frekansı düşer).\n")
    
    base_freq = 440.0 # Örnek: A4 notası frekansı (Motor sesi gibi düşünelim)
    print(f"Orijinal Ses Frekansı: {base_freq} Hz\n")
    
    # -50 m/s hız (Uzakta, bize doğru 50m/s ile geliyor) -> +50m/s (Bizden uzaklaşıyor)
    velocities = [50, 25, 10, 0, -10, -25, -50]
    
    print("--- Araba yaklaşıyor, tam önümüzden geçiyor ve uzaklaşıyor ---")
    
    for vel in velocities:
        # Eğer vel pozitifse bize yaklaşıyor (formülde vs pozitif)
        # Eğer vel negatifse bizden uzaklaşıyor (formülde vs negatif)
        
        freq = calculate_doppler(base_freq, vel)
        
        state = ""
        if vel > 0:
            state = f"[Yaklaşıyor ({vel} m/s)]"
        elif vel == 0:
            state = "[Tam yanımızda (0 m/s)]"
        else:
            state = f"[Uzaklaşıyor ({-vel} m/s)]"
            
        print(f"{state:25} -> Duyulan Frekans: {freq:.2f} Hz")
        time.sleep(0.5)

if __name__ == "__main__":
    main()
