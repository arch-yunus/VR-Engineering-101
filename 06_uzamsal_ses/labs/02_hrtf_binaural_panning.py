import math
import time

def simulate_hrtf_cues(azimuth_degrees, head_radius_cm=8.75, speed_of_sound_cm_s=34300):
    """
    Azimuth: Kaynağın yatay açısı (0=Tam ön, 90=Tam sağ, -90=Tam sol)
    ITD (Interaural Time Difference): Sesin bir kulağa diğerinden daha erken gelmesi.
    ILD (Interaural Level Difference): Baş gölgesi nedeniyle şiddetin düşmesi.
    """
    azimuth_rad = math.radians(azimuth_degrees)
    
    # Basitleştirilmiş Woodworth Model (ITD için)
    # T = (r / v) * (sin(theta) + theta)
    itd_seconds = (head_radius_cm / speed_of_sound_cm_s) * (math.sin(abs(azimuth_rad)) + abs(azimuth_rad))
    itd_ms = itd_seconds * 1000
    
    # Sol ve sağ için gecikme (Hangi kulak sese daha yakın?)
    delay_left = itd_ms if azimuth_degrees > 0 else 0
    delay_right = itd_ms if azimuth_degrees < 0 else 0
    
    # ILD: Sesin şiddetinin düşmesi. Açılara göre basit bir logaritmik uydurma
    # Ses tam karşıdan (0) geliyorsa düşüş 0, arkadan geliyorsa veya yandaysa değişir.
    ild_db = abs(math.sin(azimuth_rad)) * 8.0 # Kabaca 8 dB maksimum fark
    
    vol_left_db = -ild_db if azimuth_degrees > 0 else 0
    vol_right_db = -ild_db if azimuth_degrees < 0 else 0
    
    return delay_left, delay_right, vol_left_db, vol_right_db

def main():
    print("=== HRTF Binaural İşaretleri Simülatörü (ITD & ILD) ===")
    print("VR oyunlarında, bir objenin nerede olduğunu anlamamız için oyun motoru sesleri")
    print("her iki kulağa (sol ve sağ) milisaniye farkı ve ses şiddeti farkıyla yollar.\n")
    
    angles = [
        {"desc": "Tam Önümüzden", "deg": 0},
        {"desc": "Tam Sağımızdan", "deg": 90},
        {"desc": "Tam Solumuzdan", "deg": -90},
        {"desc": "Hafif Sağımızdan", "deg": 30}
    ]
    
    for angle in angles:
        print(f"\n--- Ses Kaynağı: {angle['desc']} (Açı: {angle['deg']}°) ---")
        dl, dr, vl, vr = simulate_hrtf_cues(angle['deg'])
        
        print("SOL KULAK:")
        print(f"  Gecikme (ITD): {dl:.3f} ms")
        print(f"  Şiddet Kaybı (ILD): {vl:.1f} dB")
        
        print("SAĞ KULAK:")
        print(f"  Gecikme (ITD): {dr:.3f} ms")
        print(f"  Şiddet Kaybı (ILD): {vr:.1f} dB")
        time.sleep(1)

if __name__ == "__main__":
    main()
