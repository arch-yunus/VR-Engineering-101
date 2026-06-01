import math

class Quaternion:
    def __init__(self, w, x, y, z):
        self.w = w
        self.x = x
        self.y = y
        self.z = z

    def __mul__(self, other):
        """İki kuaterniyonun çarpımı (Rotasyonların birleştirilmesi)"""
        w = self.w * other.w - self.x * other.x - self.y * other.y - self.z * other.z
        x = self.w * other.x + self.x * other.w + self.y * other.z - self.z * other.y
        y = self.w * other.y - self.x * other.z + self.y * other.w + self.z * other.x
        z = self.w * other.z + self.x * other.y - self.y * other.x + self.z * other.w
        return Quaternion(w, x, y, z)
        
    def __str__(self):
        return f"[{self.w:.2f}, {self.x:.2f}i, {self.y:.2f}j, {self.z:.2f}k]"

def euler_to_quaternion(roll, pitch, yaw):
    """Euler açılarını (radyan) Kuaterniyona çevirir."""
    cy = math.cos(yaw * 0.5)
    sy = math.sin(yaw * 0.5)
    cp = math.cos(pitch * 0.5)
    sp = math.sin(pitch * 0.5)
    cr = math.cos(roll * 0.5)
    sr = math.sin(roll * 0.5)

    w = cr * cp * cy + sr * sp * sy
    x = sr * cp * cy - cr * sp * sy
    y = cr * sp * cy + sr * cp * sy
    z = cr * cp * sy - sr * sp * cy

    return Quaternion(w, x, y, z)

def main():
    print("--- Uzamsal Matematik: Quaternion (Kuaterniyon) Temelleri ---")
    print("VR sistemlerinde kafa rotasyonu Euler açıları (X,Y,Z) yerine Kuaterniyonlar (w,x,y,z) ile tutulur.\n")
    
    # Sadece Y ekseninde (Yaw) 90 derece dönme
    q1 = euler_to_quaternion(0, 0, math.radians(90))
    print(f"90 Derece Yaw Dönüşü (q1): {q1}")
    
    # Sadece X ekseninde (Pitch) 45 derece dönme
    q2 = euler_to_quaternion(math.radians(45), 0, 0)
    print(f"45 Derece Pitch Dönüşü (q2): {q2}")
    
    # Rotasyonları Birleştirme (Çarpım)
    # Önce Yaw (Sağa bak), sonra Pitch (Yukarı bak)
    q_combined = q1 * q2
    print(f"\nBirleştirilmiş Dönüş (q1 * q2): {q_combined}")
    print("\nSonuç: Kuaterniyon çarpımı, matris çarpımından daha az CPU harcar ve Gimbal Lock sorununu (eksen kilitlenmesi) çözer.")

if __name__ == "__main__":
    main()
