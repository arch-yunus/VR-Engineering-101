import hashlib
import time

# Secret Key (Sadece sunucu ve istemci bilir)
SECRET_KEY = "vr_super_secret_key"

def sign_packet(data, sequence_number):
    """Veriyi ve sıra numarasını birleştirip hash oluşturur."""
    payload = f"{data}|{sequence_number}|{SECRET_KEY}"
    signature = hashlib.sha256(payload.encode()).hexdigest()
    return signature

def process_packet_on_server(data, seq_num, signature, last_seq_num):
    print(f"\nSunucuya paket geldi: Veri='{data}', Seq={seq_num}")
    
    # 1. Replay Attack Kontrolü (Eski paket mi?)
    if seq_num <= last_seq_num:
        print("  [GÜVENLİK İHLALİ] Eski paket tespit edildi (Replay Attack!). REDDEDİLDİ.")
        return False, last_seq_num
        
    # 2. İmza Doğrulama (Veri değiştirilmiş mi?)
    expected_signature = sign_packet(data, seq_num)
    if signature != expected_signature:
        print("  [GÜVENLİK İHLALİ] İmza geçersiz (Spoofing!). REDDEDİLDİ.")
        return False, last_seq_num
        
    print("  [BAŞARILI] Paket güvenli. Avatar pozisyonu güncellendi.")
    return True, seq_num

def main():
    print("--- Secure Avatar Sync (Güvenli Paket İmzası) Simülasyonu ---")
    last_processed_seq = 0
    
    # 1. Normal, güvenli paket
    data1 = "AvatarX=10.5,Y=2.0"
    seq1 = 101
    sig1 = sign_packet(data1, seq1)
    success, last_processed_seq = process_packet_on_server(data1, seq1, sig1, last_processed_seq)
    
    # 2. Replay Attack (Hacker aynı paketi tekrar gönderiyor)
    success, last_processed_seq = process_packet_on_server(data1, seq1, sig1, last_processed_seq)
    
    # 3. Spoofing Attack (Hacker veriyi değiştirdi ama imzayı uydurmaya çalıştı)
    data2 = "AvatarX=999.0,Y=999.0" # Hileli lokasyon
    seq2 = 102
    sig2 = "fake_signature_123"
    success, last_processed_seq = process_packet_on_server(data2, seq2, sig2, last_processed_seq)

if __name__ == "__main__":
    main()
