# Modul 2: Edge-AI ve Performans Optimizasyonu

## Hedef

VR sistemlerinde performansi tek bir FPS sayisi yerine uc uca gecikme zinciri
olarak modellemek.

## Ana Kavramlar

- Motion-to-photon latency: sensor, prediction, render, compositor, display.
- Foveated rendering: bakis noktasina yakin bolgeye daha yuksek kalite ayirma.
- Edge model optimizasyonu: pruning, quantization, batching ve thermal budget.
- Profiling: p95/p99 gecikme, frame pacing, dropped frame.

## Lab

```bash
python 02_edge_ai_performans/labs/latency_budget.py
python 02_edge_ai_performans/labs/foveated_tile_planner.py
```

## Kontrol Listesi

- 90 Hz hedefte frame butcesi kac milisaniyedir?
- p95 gecikme neden ortalamadan daha onemlidir?
- Goz takip verisi gec gelirse foveated rendering hangi artefaktlari uretebilir?
