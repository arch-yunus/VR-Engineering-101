import time
import random

def profile_latency():
    print("--- Motion-to-Photon Latency (Gecikme) Profiler ---")
    print("İdeal bir VR sisteminde toplam gecikme 20ms altında olmalıdır.\n")
    
    # 10 Karelik (Frame) bir analiz
    for frame in range(1, 11):
        print(f"Kare (Frame) {frame} İşleniyor...")
        
        # 1. Sensör Okuma Süresi (IMU)
        sensor_ms = random.uniform(1.0, 3.0)
        
        # 2. Oyun Motoru / Fizik Güncellemesi (CPU)
        logic_ms = random.uniform(4.0, 8.0)
        
        # 3. GPU Render Süresi (Çizim)
        render_ms = random.uniform(6.0, 14.0)
        
        # 4. Ekran Yenileme Gecikmesi (Display Scanout)
        display_ms = 4.0 # Sabit 4ms varsayalım
        
        total_ms = sensor_ms + logic_ms + render_ms + display_ms
        
        status = "BAŞARILI" if total_ms < 20.0 else "DÜŞÜK KALİTE (Gecikme Hissedilir!)"
        
        print(f"  -> Sensör: {sensor_ms:.1f}ms | Mantık: {logic_ms:.1f}ms | Render: {render_ms:.1f}ms | Ekran: {display_ms:.1f}ms")
        print(f"  -> Toplam: {total_ms:.1f}ms [{status}]\n")
        
        time.sleep(0.3)

if __name__ == "__main__":
    profile_latency()
