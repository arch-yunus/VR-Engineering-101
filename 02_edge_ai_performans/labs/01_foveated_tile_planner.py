import math

def calculate_distance(x1, y1, x2, y2):
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

def generate_foveated_map(grid_size, gaze_x, gaze_y, fovea_radius):
    print(f"--- Foveated Rendering Tile Planner ---")
    print(f"Ekran Çözünürlüğü Grid: {grid_size}x{grid_size}")
    print(f"Bakış Noktası (Gaze): X={gaze_x}, Y={gaze_y}")
    print(f"Fovea Yarıçapı: {fovea_radius}\n")
    
    print("Kalite Haritası (H: High, M: Medium, L: Low)\n")
    
    total_pixels_saved = 0
    
    for y in range(grid_size):
        row_str = ""
        for x in range(grid_size):
            dist = calculate_distance(x, y, gaze_x, gaze_y)
            
            if dist <= fovea_radius:
                row_str += "[H] " # High quality - 100% render cost
            elif dist <= fovea_radius * 2:
                row_str += "[M] " # Medium quality - 50% render cost
                total_pixels_saved += 50
            else:
                row_str += "[L] " # Low quality - 10% render cost
                total_pixels_saved += 90
        print(row_str)
        
    total_cost_without_foveated = grid_size * grid_size * 100
    total_cost_saved = total_pixels_saved
    saving_percentage = (total_cost_saved / total_cost_without_foveated) * 100
    
    print(f"\nPerformans Kazancı: GPU işlem yükünde yaklaşık %{saving_percentage:.1f} tasarruf sağlandı.")

if __name__ == "__main__":
    # 10x10 tile grid (Örneğin her biri 100x100 pixel bloğu temsil etsin)
    generate_foveated_map(grid_size=10, gaze_x=5, gaze_y=4, fovea_radius=2)
