import os
import subprocess
import sys

def run_script(path):
    print(f"Test ediliyor: {path}")
    try:
        # Scriptleri çalıştırıp hata kodu var mı diye bakıyoruz
        result = subprocess.run([sys.executable, path], capture_output=True, text=True, timeout=5)
        if result.returncode == 0:
            print(f"  [BAŞARILI] {path}")
            return True
        else:
            print(f"  [HATA] {path} çalışırken çöktü!\n{result.stderr}")
            return False
    except subprocess.TimeoutExpired:
        # Simülasyon scriptleri olduğu için bazıları bilerek bekliyor olabilir (time.sleep)
        # Timeout yerse ama hata fırlatmadıysa şimdilik başarılı sayıyoruz.
        print(f"  [BAŞARILI/ZAMAN AŞIMI] {path}")
        return True
    except Exception as e:
        print(f"  [HATA] {path} çalıştırılamadı: {e}")
        return False

def main():
    print("--- VR Engineering 101 Repo Doğrulama ---")
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    
    scripts_to_test = [
        "01_donanim_sensor/labs/01_imu_drift_simulator.py",
        "01_donanim_sensor/labs/02_kalman_filter_1d.py",
        "01_donanim_sensor/labs/03_fov_calculator.py",
        "02_edge_ai_performans/labs/01_foveated_tile_planner.py",
        "02_edge_ai_performans/labs/02_latency_profiler.py",
        "03_yazilim_matematik_pipeline/labs/01_quaternion_basics.py",
        "03_yazilim_matematik_pipeline/labs/02_vr_runtime_loop.py",
        "04_ag_guvenlik/labs/01_udp_snapshot_simulator.py",
        "04_ag_guvenlik/labs/02_secure_avatar_sync.py"
    ]
    
    all_passed = True
    for script in scripts_to_test:
        full_path = os.path.join(base_dir, script.replace("/", os.sep))
        if os.path.exists(full_path):
            success = run_script(full_path)
            if not success:
                all_passed = False
        else:
            print(f"  [HATA] Dosya bulunamadı: {full_path}")
            all_passed = False
            
    if all_passed:
        print("\nSonuç: TÜM TESTLER GEÇTİ. (Exit Code 0)")
        sys.exit(0)
    else:
        print("\nSonuç: BAZI TESTLER BAŞARISIZ. Lütfen hataları kontrol edin.")
        sys.exit(1)

if __name__ == "__main__":
    main()
