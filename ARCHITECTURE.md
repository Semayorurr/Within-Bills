# Within-Bills Projesi Teknik Mimarisi
## Proje Amacı
Kullanıcıların yüklediği fatura/fiş görsellerinden OCR ile veri çekip, bu verileri yapılandırılmış düzenli bir tablo formatına dönüştürmek.

## Teknoloji Yığını (Tech Stack)
- **Arayüz (Frontend):** Streamlit (Python)
- **Arka Plan (Backend):** Python
- **Veri Çıkarımı (OCR / AI):** Tesseract / EasyOCR veya Vision API
- **Veri İşleme:** Pandas

## Veri Akışı (Pipeline)
1. Kullanıcı arayüz üzerinden fatura görselini yükler.
2. Görsel OCR motoruna iletilir ve metinler okunur.
3. Model; Satıcı Adı, Tarih, Vergi No ve Toplam Tutar gibi anahtar verileri ayıklar.
4. Çıkarılan veriler bir Pandas DataFrame'ine aktarılır ve ekranda tablo olarak gösterilir.