import random
import time

def simulate_udp_network():
    print("--- UDP Snapshot (Paket) Simülatörü ---")
    print("Oyun sunucusu saniyede 20 kere (20 tick) dünyanın durumunu gönderiyor.\n")
    
    total_packets = 20
    received_packets = []
    
    # 1. Aşama: Paketleri gönder ve ağ gecikmesi/kaybı uygula
    for seq_num in range(1, total_packets + 1):
        # %10 Paket Kaybı İhtimali
        if random.random() < 0.10:
            print(f"Sunucu -> [X] Paket {seq_num} Yolda Kayboldu!")
            continue
            
        # Jitter (Gecikme dalgalanması) Simülasyonu
        arrival_time = time.time() + random.uniform(0.01, 0.1)
        received_packets.append((seq_num, arrival_time))
        
    print("\nİstemci Paketleri İşliyor...\n")
    
    # 2. Aşama: İstemciye ulaşan paketleri varış zamanına göre sırala
    received_packets.sort(key=lambda x: x[1])
    
    last_seq = 0
    for seq, arr_time in received_packets:
        if seq < last_seq:
            print(f"İstemci <- Paket {seq} ALINDI AMA ESKİ! (Sıra Dışı - Out of Order) -> ÇÖPE ATILIYOR.")
        else:
            print(f"İstemci <- Paket {seq} İşlendi.")
            last_seq = seq
            
    print("\nSonuç: VR'da UDP kullanırken, sıra dışı veya eksik paketleri istemci tarafında mantıklı bir şekilde (Interpolation) doldurmak gerekir.")

if __name__ == "__main__":
    simulate_udp_network()
