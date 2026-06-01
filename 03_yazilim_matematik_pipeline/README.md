# Modul 3: Yazilim, Matematik ve Pipeline

## Hedef

3B rotasyonlari, render dongusunu ve runtime mimarisini hata uretmeyecek kadar
net bir zihinsel modelle kavramak.

## Ana Kavramlar

- Vektorler, matrisler, koordinat sistemleri.
- Quaternion: normalizasyon, carpim, ters, slerp fikri.
- Render loop: input, prediction, simulation, render submission.
- C++ runtime: bellek sahipligi, cache locality, thread sorumluluklari.

## Lab

```bash
python 03_yazilim_matematik_pipeline/labs/quaternion_playground.py
```

## Kontrol Listesi

- Gimbal lock neden Euler acilarinda gorulur?
- Quaternion carpim sirasi neden onemlidir?
- Runtime loop'ta pose prediction hangi asamada yapilmalidir?
