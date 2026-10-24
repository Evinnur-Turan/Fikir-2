
# 🤖 Yapay Zeka Destekli Tablo Karar Motoru (v3.0)

Bu proje, ham bir veri setinin yapısını ve kalitesini inceleyerek **en düzgün hangi tablo formatında anlaşılacağını** otomatik olarak belirleyen kural tabanlı bir uzman sistem (Expert System) mimarisidir.

## 🚀 Özellikler
*   **Veri Mimarisi Analizi:** Verideki Sayısal, Kategorik, Tarih ve Mantıksal (Boolean) sütunları otomatik ayrıştırır.
*   **Ağırlıklı Skorlama Algoritması:** Gelişmiş kural setiyle en okunabilir tablo türünü (Trend, Pivot, KPI, Korelasyon veya Filtrelenebilir Matris) seçer.
*   **Entegre Veri Kalite Modülü (NaN Kontrolü):** Eksik verileri analiz ederek temizleme stratejisi önerir.
*   **Otomatik Kod Üretimi:** Seçilen tabloyu Kaggle/Jupyter üzerinde doğrudan çalıştıracak özelleştirilmiş Pandas kodunu dinamik olarak üretir.

## 🛠️ Nasıl Çalıştırılır?
1. `fikir2.py` dosyasındaki sınıfı (class) Kaggle Notebook'unuza veya VS Code projenize aktarın.
2. Analiz etmek istediğiniz veriyi `TabloKararMotoru(df)` şeklinde modele besleyin.
3. `motor.rapor_yazdir()` komutuyla analiz çıktısını alın.
