import time
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    clear_screen()
    print("=========================================================")
    print("🌌 VR ENGINEERING 101: INTERAKTIF OGRENME ASISTANI 🌌")
    print("=========================================================\n")
    print("Sanal gerçekliğin temellerini öğrenmeye hoş geldin!\n")
    print("Hangi konuya odaklanmak istersin?")
    print("1. Donanım ve Sensörler (IMU, Drift, Kalman)")
    print("2. Performans ve Edge-AI (Foveated Rendering, Latency)")
    print("3. Uzamsal Matematik (Quaternion, Render Loop)")
    print("4. Ağ ve Güvenlik (UDP, Replay Attacks)")
    print("5. Çıkış\n")
    
    choice = input("Seçiminiz (1-5): ")
    
    clear_screen()
    if choice == '1':
        print("--- Modül 1: Donanım ve Sensör Füzyonu ---")
        print("Tavsiye edilen laboratuvarlar:")
        print("  python 01_donanim_sensor/labs/01_imu_drift_simulator.py")
        print("  python 01_donanim_sensor/labs/02_kalman_filter_1d.py")
        print("\nMini Soru: Sensör verilerindeki birikimli hataya ne denir?")
        ans = input("Cevabınız: ").lower()
        if "drift" in ans or "sapma" in ans:
            print("Harika! Doğru bildin.")
        else:
            print("Cevap 'drift' veya 'sapma' olmalıydı.")
            
    elif choice == '2':
        print("--- Modül 2: Performans ve Edge-AI ---")
        print("Tavsiye edilen laboratuvarlar:")
        print("  python 02_edge_ai_performans/labs/01_foveated_tile_planner.py")
        print("  python 02_edge_ai_performans/labs/02_latency_profiler.py")
        print("\nMini Soru: VR'da 'Motion-to-Photon' gecikmesi ideal olarak kaç ms'nin altında olmalıdır?")
        ans = input("Cevabınız: ")
        if "20" in ans:
            print("Tebrikler! 20ms standart bir eşiktir.")
        else:
            print("Hedef genelde 20ms'nin altıdır.")
            
    elif choice == '3':
        print("--- Modül 3: Uzamsal Matematik ---")
        print("Tavsiye edilen laboratuvarlar:")
        print("  python 03_yazilim_matematik_pipeline/labs/01_quaternion_basics.py")
        print("  python 03_yazilim_matematik_pipeline/labs/02_vr_runtime_loop.py")
        print("\nMini Soru: Euler açılarındaki eksen kilitlenmesi sorununa ne ad verilir?")
        ans = input("Cevabınız: ").lower()
        if "gimbal" in ans or "gimbal lock" in ans:
            print("Mükemmel! Kuaterniyonlar bu yüzden var.")
        else:
            print("Cevap 'Gimbal Lock' olmalıydı.")
            
    elif choice == '4':
        print("--- Modül 4: Ağ ve Güvenlik ---")
        print("Tavsiye edilen laboratuvarlar:")
        print("  python 04_ag_guvenlik/labs/01_udp_snapshot_simulator.py")
        print("  python 04_ag_guvenlik/labs/02_secure_avatar_sync.py")
        print("\nMini Soru: Çok oyunculu VR oyunlarında veri iletimi için genelde TCP mi UDP mi kullanılır?")
        ans = input("Cevabınız: ").upper()
        if "UDP" in ans:
            print("Doğru! Düşük gecikme için UDP tercih edilir.")
        else:
            print("Cevap UDP olmalıydı.")
            
    elif choice == '5':
        print("Çıkış yapılıyor. VR yolculuğunda başarılar!")
        
    else:
        print("Geçersiz seçim.")

if __name__ == "__main__":
    main()
