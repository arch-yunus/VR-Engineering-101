import math

def calculate_2d_ik(target_x, target_y, upper_arm_length, lower_arm_length):
    """
    Omuz(0,0) noktasında sabit. El (target_x, target_y) noktasında.
    Geriye kalan Dirsek açısı (Elbow) ve Omuz açısını (Shoulder) Kosinüs teoremi ile buluruz.
    """
    # Omuzdan ele olan uzaklık
    distance_to_target = math.sqrt(target_x**2 + target_y**2)
    
    # Ulaşılmazlık kontrolü
    if distance_to_target > (upper_arm_length + lower_arm_length):
        print(f"Hedef (X:{target_x}, Y:{target_y}) çok uzak! Kol yetişmiyor.")
        return None, None
        
    if distance_to_target < abs(upper_arm_length - lower_arm_length):
        print(f"Hedef (X:{target_x}, Y:{target_y}) çok yakın! Anatomik olarak imkansız.")
        return None, None
        
    # Kosinüs teoremi: c^2 = a^2 + b^2 - 2ab*cos(C)
    # Dirsek açısı
    cos_angle_elbow = (upper_arm_length**2 + lower_arm_length**2 - distance_to_target**2) / (2 * upper_arm_length * lower_arm_length)
    angle_elbow = math.acos(cos_angle_elbow)
    
    # Omuz açısı hesaplaması için iki parçalı açı
    angle_base = math.atan2(target_y, target_x)
    cos_angle_shoulder_part = (upper_arm_length**2 + distance_to_target**2 - lower_arm_length**2) / (2 * upper_arm_length * distance_to_target)
    angle_shoulder = angle_base - math.acos(cos_angle_shoulder_part)
    
    # Radyandan dereceye çevir
    return math.degrees(angle_shoulder), math.degrees(angle_elbow)

def main():
    print("=== Ters Kinematik (IK) Simülatörü ===")
    print("VR oyunlarında sadece kaskın ve ellerin pozisyonunu biliyoruz.")
    print("Tüm vücudun geri kalanını (Kollar, bacaklar) IK matematiği ile tahmin ediyoruz.\n")
    
    upper_arm = 30.0 # cm (Omuz - Dirsek)
    lower_arm = 25.0 # cm (Dirsek - El)
    
    print(f"Kol Uzunlukları: Üst Kol = {upper_arm}cm, Alt Kol = {lower_arm}cm\n")
    
    targets = [
        {"x": 10, "y": 40},  # Normal ulaşılabilir bir nokta
        {"x": 40, "y": 40},  # Yetişmesi zor
        {"x": 60, "y": 10},  # Çok uzak, yetişmez
    ]
    
    for target in targets:
        print(f"-> El (Controller) Hedefi: X={target['x']}, Y={target['y']}")
        shoulder_deg, elbow_deg = calculate_2d_ik(target['x'], target['y'], upper_arm, lower_arm)
        
        if shoulder_deg is not None:
            print(f"   [BAŞARILI] Avatar Render Ediliyor: Omuz Açısı: {shoulder_deg:.1f}°, Dirsek İç Açısı: {elbow_deg:.1f}°\n")
        else:
            print("   [HATA] Model pozu çözülemedi.\n")

if __name__ == "__main__":
    main()
