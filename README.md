# Raspberry Pi Control Server

## English

Server that provides access to the Raspberry pi card via wifi. With this server you can easily control your raspberr pi card. You can customize the codes according to your request or according to your job. You can also make changes easily thanks to clearly written code.

## Getting Started

### Prerequisites

The necessary items for the server are available in the file, but you can install the libraries that are used against the possible situation as follows.

```
pip install socket

pip install python-handler-socket

pip install RPi.GPIO

pip install smbus2
```

### Installing


For installation, the administrator will first turn on the server from the computer. Here the user name and password will come up as the default user name: "admin" password: "123" is the form.
After logging in successfully, we will ask you to enter host and port information. You must enter the local ip address of the server computer as a host. By default, the port address is set to "8585".

Example:
```
Host=192.168.1.54
port=8585
```

After completing these operations, the order will be made via the raspberry pi card. In this section, we need to make small changes on the codes. Replace the IP address of the "client.py" file against the host variable.

```
host="192.168.1.54"
```

And at the end of the process, you can now run the "client.py" file through the terminal.
```
python /directory/client.py
```
If you received a successful message from the server computer, everything went fine.

## Authors

* **Ahmed Demirezen** - *Initial work* - [feezx1](https://github.com/feezx1)

## Acknowledgments

* Thank you to Kutalmış Köroğlu for helping me customize the program.

# Raspberry Pi Control Server

## Türkçe

Raspberry pi kartına wifi üzerinden erişim imkanı tanıyan sunucu. Bu sunucu ile raspberry pi kartınızı kolay bir şekilde kontrol edebilirsiniz. Kodları isteğinize göre veya kullanıcağınız işe göre özelleştirebilirsiniz. Anlaşılır bir şekilde yazılmış kodlar sayesinde de değişiklikleri kolay bir şekilde yapabilirsiniz. 

## Kullanım Kılavuzu

### Ön Şartlar

Sunucu için gerekli öğeler dosyanın içerisinde mevcut ama olası duruma karşı kullanılan kütüphanelerin kurulumunu aşağıdaki gibi yapabilirsiniz.

```
pip install socket

pip install python-handler-socket

pip install RPi.GPIO

pip install smbus2
```

### Kurulum

Kurulum için ilk olarak yönetici bilgisayardan sunucu açmak olacaktır. Burada karşınıza kullanıcı adı ve şifre çıkacaktır bunlar varsayılan olarak kullanıcı adı:"admin" şifre:"123" şeklindedir.
Başarılı bir şekilde giriş yaptıktan sonra bizden host ve port bilgilerini girmemizi isteyecektir. Burada host olarak sunucu bilgisayarın yerel ip adresini girmeniz gerekmektedir. Varsayılan olarak port adresi "8585" olarak ayarlıdır bunu isteğinize göre yapılandırabilirsiniz.

Örneğin:
```
Host=192.168.1.54
port=8585
```

Bu işlemleri tamamladıktan sonra sıra raspberry pi kartı üzerinden yapılacak olan ayarlara. Bu kısımda kodlar üzerinde küçük değişiklik yapmamız gerekmekte. "client.py" dosyasındaki host değişkenin karşısında yazan ip adresini sunucu ip adresi ile değiştirmek.

Örneğin:
```
host="192.168.1.54"
```

Ve sonunda işlemler tamam artık "client.py" dosyasını terminal üzerinden çalıştırabilirsiniz.
```
python /dizin/client.py 
```
Eğer sunucu bilgisayardan bağlantı başarılı şeklinde mesaj aldıysanız herşey yolunda gitmiş demektir.

## Yazarlar

* **Ahmed Demirezen** - *İlk İş* - [feezx1](https://github.com/feezx1)

## Emeği Geçenler

* Programı özelleştirmemde yardımcı olan Kutalmış Köroğlu'na Teşekkür ederim.

