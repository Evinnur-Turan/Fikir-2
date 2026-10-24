import pandas as pd
import numpy as np

class TabloKararMotoru:
    """
    Veri yapısını ve kalitesini inceleyen, en uygun tablo türünü seçen
    ve o tabloyu oluşturmak için gerekli Python/Pandas kodunu üreten uzman sistem.
    """
    def __init__(self, df):
        self.df = df
        self.satir, self.sutun = df.shape
        self.sayisal = df.select_dtypes(include=[np.number]).columns.tolist()
        self.kategorik = df.select_dtypes(include=['object', 'category']).columns.tolist()
        self.tarih = df.select_dtypes(include=['datetime', 'timedelta', 'datetimetz']).columns.tolist()
        self.boolean = df.select_dtypes(include=['bool']).columns.tolist()
        
    def veri_skorlamasi(self):
        """Verinin mimari özelliklerine göre ağırlıklı puanlama yapar."""
        skorlar = {
            'Trend_Tablosu': 0,
            'Pivot_Tablo': 0,
            'KPI_Skor_Karti': 0,
            'Korelasyon_Matrisi': 0,
            'Filtrelenebilir_Matris': 0
        }
        
        if len(self.tarih) >= 1:
            skorlar['Trend_Tablosu'] += 55 
            
        if self.satir <= 10:
            skorlar['KPI_Skor_Karti'] += 40
        else:
            skorlar['Filtrelenebilir_Matris'] += 20
            
        if len(self.kategorik) >= 1 and len(self.sayisal) >= 1:
            for col in self.kategorik:
                essiz_orani = self.df[col].nunique() / self.satir
                if essiz_orani < 0.5: 
                    skorlar['Pivot_Tablo'] += 45
                    
        if len(self.sayisal) >= 3:
            skorlar['Korelasyon_Matrisi'] += 30
            if len(self.kategorik) == 0: 
                skorlar['Korelasyon_Matrisi'] += 25
                
        if len(self.boolean) >= 2:
            skorlar['Filtrelenebilir_Matris'] += 15
                
        return skorlar

    def rapor_yazdir(self):
        """Tüm modülleri birleştirerek analiz, kalite raporu ve kod üretimini basar."""
        skorlar = self.veri_skorlamasi()
        en_iyi_format = max(skorlar, key=skorlar.get)
        
        toplam_eksik = self.df.isnull().sum().sum()
        toplam_hucre = self.satir * self.sutun
        eksik_orani = (toplam_eksik / toplam_hucre) * 100 if toplam_hucre > 0 else 0
        
        print("=" * 70)
        print("🤖 AI TABLO KARAR MOTORU v3.0 - OTOMATİK KOD ÜRETİM MODÜLÜ")
        print("=" * 70)
        print(f"📊 Veri Yapısı: {self.satir} Satır | {self.sutun} Sütun")
        print(f"🧬 Tipler: Sayısal({len(self.sayisal)}) | Kategorik({len(self.kategorik)}) | Tarih({len(self.tarih)}) | Mantıksal({len(self.boolean)})")
        print("-" * 70)
        
        print("⚠️ VERİ KALİTE RAPORU:")
        if toplam_eksik == 0:
            print("  ✅ Mükemmel! Veri setinde hiç eksik (NaN) değer bulunamadı.")
        else:
            print(f"  ❌ UYARI: Veride toplam {toplam_eksik} hücre eksik (Genel Oran: %{eksik_orani:.1f}).")
        
        print("-" * 70)
        print(f"🧠 EN DOĞRU GÖSTERİM SEÇİMİ: >>> {en_iyi_format.replace('_', ' ')} <<<")
        print("-" * 70)
        
        t_col = self.tarih if self.tarih else 'Tarih'
        k_col = self.kategorik if self.kategorik else 'Kategori'
        s_cols_str = str(self.sayisal)
        
        kodlar = {
            'Trend_Tablosu': f"# 💻 TREND TABLOSU KODU:\ndf_trend = df.sort_values(by='{t_col}')\ndisplay(df_trend)",
            'Pivot_Tablo': f"# 💻 PIVOT TABLO KODU:\npivot = df.pivot_table(index='{k_col}', values={s_cols_str}, aggfunc='sum')\ndisplay(pivot)",
            'KPI_Skor_Karti': f"# 💻 SKOR KARTI KODU:\nprint(df.sum())",
            'Korelasyon_Matrisi': "# 💻 ISI HARİTASI KODU:\nprint(df.corr(numeric_only=True))",
            'Filtrelenebilir_Matris': "# 💻 MATRİS KODU:\ndisplay(df.head(10))"
        }
        
        print("🚀 BU GÖSTERİM İÇİN HAZIRLANAN PANDAS KODUNUZ:")
        print(kodlar[en_iyi_format])
        print("=" * 70)

# --- DENEME ALANI ---
simule_veri = pd.DataFrame({
    'Siparis_Tarihi': pd.date_range(start='2026-01-01', periods=5),
    'Musteri_Segmenti': ['Kurumsal', 'Bireysel', 'Bireysel', 'Kurumsal', 'Eğitim'],
    'Tutar_USD': [100, 200, 300, 400, 500]
})

motor = TabloKararMotoru(simule_veri)
motor.rapor_yazdir()
