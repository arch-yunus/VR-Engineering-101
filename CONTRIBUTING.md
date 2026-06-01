# Katki Rehberi

Bu repo uygulamali bir muhendislik defteri gibi buyuyecek: her katki okunabilir,
calistirilabilir ve olculebilir olmali.

## Degisiklik Turleri

- **Lab:** Tek kavrami gosteren kucuk, calistirilabilir ornek.
- **Not:** Tasarim karari, matematik aciklamasi, sistem analizi veya kaynak ozeti.
- **Arac:** Repo kalitesini, veri uretimini veya ogrenme akisini iyilestiren script.
- **Proje:** Birden fazla modulun birlestigi capstone gorevi.

## Kabul Kriterleri

- Komutlar Windows PowerShell ve POSIX shell icin makul sekilde belgelenmeli.
- Python lab'lari mumkunse standart kutuphane ile calismali.
- Her yeni modul README'si su bolumleri icermeli: hedef, kavramlar, lab, kontrol listesi.
- Performans iddialari sayisal hedef veya olcum yontemiyle desteklenmeli.
- Guvenlik konularinda gercek sistemlere zarar verecek exploit kodu eklenmemeli.

## Stil

- Dosya ve klasor adlarinda kucuk harf, rakam ve alt cizgi kullanin.
- Uzun teoriyi `docs/` altina, calisan ornekleri `labs/` altina koyun.
- Lab'lar calistiginda kisa ve yorumlanabilir cikti uretmeli.

## PR Kontrol Listesi

```bash
python scripts/validate_repo.py
python scripts/learning_path.py
```

PR aciklamasinda sunlari belirtin:

- Neyi ogretiyor veya hangi problemi cozuyor?
- Hangi komutlarla dogrulandi?
- Hangi varsayimlar veya sinirlar var?
