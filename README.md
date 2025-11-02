# 🧭 MacChanger

**MacChanger**, ağ arayüzlerinin MAC adreslerini rastgele bir şekilde değiştiren küçük ama kullanışlı bir Python aracıdır. Bu araç, gizlilik ve anonimlik amacıyla veya ağ testi senaryolarında hızlı MAC değişimi yapmak için tasarlanmıştır. Kullanıcı dostu ve platformlar arası (Linux, Windows, macOS) uyumluluk hedeflenmiştir.

---

## 🎯 Amaç ve Özellikler

Bu proje, belirli bir ağ arayüzünün mevcut MAC adresini alır, ardından rastgele yeni bir MAC adresi üretir ve bunu sisteme uygular.  
Uygulama, sistemdeki ağ bağlantısını geçici olarak devre dışı bırakır, yeni MAC adresini atar ve ardından bağlantıyı yeniden etkinleştirir.  
Bu sayede kullanıcı, ağ üzerinde farklı bir cihaz olarak görünür.

Özellikleri:

- Rastgele MAC adresi üretimi
    
- Mevcut MAC adresinin otomatik tespiti
    
- Eski ve yeni MAC adreslerinin terminalde gösterimi
    
- Basit ve minimal kod yapısı
    

---

## ⚙️ Gereksinimler

Bu program, Python 3 ile çalışır ve standart kütüphaneler dışında ek modül gerektirmez.  
Yalnızca aşağıdaki modüller kullanılmaktadır:

- `random`
    
- `subprocess`
    
- `re`
    

Bu modüller Python ile birlikte varsayılan olarak gelir.

---

## 🧩 Linux’ta Kullanım

1. Dosyayı indirin veya kopyalayın:
	git clone https://github.com/kullanici/MAC-Address-Changer.git
	cd MacChanger

2. Python dosyasına çalıştırma izni verin (isteğe bağlı):
	 chmod +x MacChanger.py

3. Programı çalıştırın:
	 sudo python3 MacChanger.py

**Not:** Kodda yer alan ağ arayüzü adı (`enp12s0`) sistemine göre değişebilir.  
Terminalde `ip link show` komutuyla ağ arayüzünü öğrenip kodun içindeki kısmı düzenleyebilirsiniz.  
Örnek: `wlan0`, `eth0`, `enp0s3` gibi.

## 🪟 Windows’ta Kullanım

Windows'ta Python ile doğrudan `ip` komutu bulunmadığı için, `MacChanger.py` doğrudan çalışmayabilir.  
Ancak aşağıdaki yöntemlerle kullanılabilir:

1. Python 3’ü [python.org](https://www.python.org/downloads/) adresinden yükleyin.
    
2. Komut satırını yönetici olarak açın.
    
3. `getmac` ve `netsh interface set address` komutlarını kullanan Windows’a özel bir sürüm hazırlayabilirsiniz.
    

> Alternatif olarak, Windows Subsystem for Linux (WSL) üzerinden Ubuntu veya Fedora kullanarak aynı komutlarla çalıştırabilirsiniz:

sudo python3 MacChanger.py

## 🍎 macOS’ta Kullanım

macOS üzerinde benzer şekilde `ifconfig` komutu kullanılır.  
Aşağıdaki adımları izleyebilirsiniz:

1. Terminali açın.
    
2. Ağ arayüzünüzü öğrenin:
	 ifconfig
	 
3. Kodun içindeki `ip link` komutlarını aşağıdakiyle değiştirin:
	 sudo ifconfig en0 ether <yeni_mac_adresi>

4. Ardından programı çalıştırın:
	 sudo python3 MacChanger.py
	 
**Not:** macOS’ta genellikle ağ arayüzü `en0` veya `en1` olarak adlandırılır.


# 🧠 Örnek Çıktı

Old MAC address: 2C:33:1A:9F:77:12
New MAC address: 9A:4E:B1:2F:93:C7

## ⚠️ Uyarılar

- MAC adresi değiştirme işlemi yönetici (root) yetkisi gerektirir.
    
- Bazı ağ arabirimleri veya sanal makineler MAC adresi değişikliğini engelleyebilir.
    
- MAC adresinizi değiştirmek bazı ağ politikalarıyla çelişebilir, bu yüzden dikkatli kullanın.
