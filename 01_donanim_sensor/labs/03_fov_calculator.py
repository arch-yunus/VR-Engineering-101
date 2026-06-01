import math

def calculate_fov(sensor_width_mm, focal_length_mm):
    """
    Kamera/Gözlük lensi için temel FOV (Görüş Alanı) hesaplaması.
    FOV = 2 * arctan(sensor_genisligi / (2 * odak_uzakligi))
    """
    fov_rad = 2 * math.atan(sensor_width_mm / (2 * focal_length_mm))
    fov_deg = math.degrees(fov_rad)
    return fov_deg

def main():
    print("--- VR FOV (Görüş Alanı) Hesaplayıcı ---")
    print("HMD (Head Mounted Display) tasarımlarında FOV, ekran genişliği ve lensin odak uzaklığına bağlıdır.")
    
    # Örnek değerler
    screens = [
        {"name": "Eski Nesil (ör. Oculus DK1)", "width_mm": 149.7, "focal_length_mm": 40},
        {"name": "Modern Standart (Göz başına)", "width_mm": 60.0, "focal_length_mm": 35},
        {"name": "Ultra Geniş Pimax Serisi (Göz başına)", "width_mm": 80.0, "focal_length_mm": 25},
    ]
    
    for screen in screens:
        fov = calculate_fov(screen["width_mm"], screen["focal_length_mm"])
        print(f"\nSistem: {screen['name']}")
        print(f"  Ekran Genişliği: {screen['width_mm']} mm, Odak Uzaklığı (Focal Length): {screen['focal_length_mm']} mm")
        print(f"  Hesaplanan Yatay FOV: {fov:.2f} derece")

if __name__ == "__main__":
    main()
