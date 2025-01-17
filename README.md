# Spylogger & RavixR00T


**SpyLogger**, kullanıcının klavye tuşlarını kaydeden ve ekran görüntülerini alan bir Python uygulamasıdır. Bu araç, etik kullanım ve güvenlik araştırmaları amacıyla tasarlanmıştır. Lütfen yalnızca izin aldığınız sistemlerde kullanın. Bu yazılım, kötüye kullanım amaçlı kullanılmamalıdır.

## Özellikler

- Klavye tuşlarını kaydeder.
- Ekran görüntüleri alır.
- Telegram üzerinden logları raporlar.
- Kullanıcı dostu ve basit yapı.

## Gereksinimler

Python 3.x sürümünü ve aşağıdaki bağımlılıkları kurmanız gerekmektedir:

- `requests`
- `pynput`
- `Pillow`
- `cryptography`

Bu bağımlılıkları kurmak için `requirements.txt` dosyasını kullanabilirsiniz:

```bash
pip install -r requirements.txt

Kullanım

    Başlatma: Uygulama başlatıldığında, Telegram bot token'ınızı ve chat ID'nizi girmeniz istenecektir. Bu bilgileri girerek uygulamanın çalışmasına başlayabilirsiniz.

    Loglama: Uygulama, arka planda çalışarak klavye tuşlarını kaydeder ve ekran görüntüleri alır. Elde edilen loglar, belirttiğiniz Telegram botuna gönderilecektir.

    Telegram İstemcisi: Bot token ve chat ID bilgilerini Telegram botunuzdan edinin. Bunun için BotFather ile yeni bir bot oluşturabilirsiniz.

Lisans

Bu proje MIT lisansı altında lisanslanmıştır. Daha fazla bilgi için LICENSE dosyasına bakabilirsiniz.
Yasal Uyarı

Bu yazılım yalnızca etik kullanım için tasarlanmıştır. Yasalara aykırı kullanım, kullanıcıya ait olacaktır. Lütfen yalnızca izinli sistemlerde ve ortamda kullanın.
Bağlantılar

    GitHub: https://github.com/RavixR00T/SpyLogger

