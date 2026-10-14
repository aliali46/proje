# Proje Yönetim Sistemi

Çevrimdışı kullanım hedefiyle hazırlanmış, Python standart kütüphanesi ve SQLite kullanan tek dosyalı proje/sistem takip uygulaması. Bu depo, mevcut uygulamanın işlevlerini koruyan ve GitHub/DeepSeek ile aşamalı geliştirmeye uygun bir başlangıç paketidir.

> **Önemli:** Bu paket, uygulamanın tamamının güvenlik denetiminden geçtiği veya üretim ortamına hazır olduğu anlamına gelmez. İnternete doğrudan açmadan önce güvenlik incelemesi yapın.

## Özellikler

- Proje ve sistem kayıtları
- Aktif / pasif / arızalı durum takibi ve durum geçmişi
- Fotoğraf ve belge ekleme
- PDF ve CSV raporları
- Yönetici ve salt-okunur kullanıcı rolleri
- SQLite ile yerel veri saklama
- Sunum ekranı ve harita/akış görselleştirmesi
- Python standart kütüphanesiyle çalışma; ek Python paketi gerektirmez

## Gereksinimler

- Python 3.10 veya üstü önerilir
- Harici Python paketi gerekmez

## Yerel çalıştırma

Windows PowerShell:

```powershell
$env:DATA_DIR = "$PWD\data"
$env:UPLOAD_DIR = "$PWD\uploads"
$env:ADMIN_USERNAME = "admin"
$env:ADMIN_PASSWORD = "GUVENLI_VE_BENZERSIZ_BIR_PAROLA"
$env:VIEWER_USERNAME = "izleyici"
$env:VIEWER_PASSWORD = "BASKA_GUVENLI_BIR_PAROLA"
python app.py
```

Linux/macOS:

```bash
export DATA_DIR="$PWD/data"
export UPLOAD_DIR="$PWD/uploads"
export ADMIN_USERNAME="admin"
export ADMIN_PASSWORD="GUVENLI_VE_BENZERSIZ_BIR_PAROLA"
export VIEWER_USERNAME="izleyici"
export VIEWER_PASSWORD="BASKA_GUVENLI_BIR_PAROLA"
python app.py
```

Ardından `http://127.0.0.1:8080` adresini açın. İlk çalıştırmada kullanıcı tablosu boşsa ortam değişkenlerindeki ilk kullanıcılar oluşturulur. **Mevcut veritabanında kullanıcılar varsa bu değişkenleri değiştirmek mevcut kullanıcı parolalarını değiştirmez.** Parola değişikliği uygulama içinden yapılmalıdır.

HTTPS arkasında yayın yapılıyorsa ve TLS sonlandırması doğru yapılandırıldıysa `COOKIE_SECURE=1` ayarı oturum çerezine `Secure` niteliği ekler. Düz HTTP yerel geliştirmede bu ayarı etkinleştirmeyin.

## Veri ve yedekleme

- SQLite veritabanı: `DATA_DIR/projects.db`
- Yüklenen dosyalar: `UPLOAD_DIR`
- Git'e veritabanı, yüklemeler, sırlar veya gerçek kullanıcı verileri eklemeyin.
- Güncellemeden önce hem veritabanının hem yükleme klasörünün ayrı yedeğini alın.
- `app.py` mevcut veritabanı şemasını başlangıçta oluşturur/günceller. Şema değişiklikleri ayrı test edilmeden canlı veriye uygulanmamalıdır.

## Test

```bash
python -m py_compile app.py
python tests/smoke_test.py
```

Smoke test geçerse yalnızca temel başlatma ve sağlık kontrolü doğrulanmış olur; bu, tüm iş akışlarının tarayıcıda test edildiği anlamına gelmez.

## Harita ve sunum ekranı hakkında

Harita davranışı ve sunum animasyonları mevcut uygulama kodunda bulunur. Sunum amaçlı akış animasyonları gerçek ağ trafiği/telemetri değildir. Gerçek 81 il sınırı verisinin, dünya sınır katmanının ve tarayıcı tabanlı yakınlaştırma/gruplama davranışlarının ayrıca doğrulanması gerekir. Bunları varmış gibi göstermeyin; gerçek veri katmanı ve otomatik test eklendikçe bu bölümü güncelleyin.

## DeepSeek / başka bir kod asistanıyla geliştirme önerisi

Her değişiklikte şu kuralları verin:

1. Önce mevcut `app.py` ve şema incelensin; özellikler silinmesin.
2. Değişiklik küçük ve tek amaçlı olsun.
3. Veritabanı ve `uploads/` silinmesin, sıfırlanmasın veya yeniden adlandırılmasın.
4. Yeni özellik için test ve geri alma notu eklensin.
5. Önce ayrı dalda/klonda çalışılsın; canlı sunucuya doğrudan uygulanmasın.
6. “Test edildi” denmeden önce hangi komutların çalıştırıldığı ve hangi senaryoların doğrulandığı raporlansın.

## Lisans

Henüz lisans seçilmedi. Açık kaynak paylaşmadan önce uygun bir lisans seçin (ör. MIT) ve yalnızca size ait veya kullanım hakkınız olan dosyaları ekleyin.
