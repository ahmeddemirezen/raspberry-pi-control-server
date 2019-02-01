<h1>
  Raspberry Pi Control Server
  </h1>

<h2>
  Features//Özellikler
  </h2>  
  
<p>
  <li>You can connect to a local network and communicate with the raspberry pi on the server.//Yerel bir ağa bağlanıp sunucu üzerinden raspberry pi ile iletişim kurabilirsiniz.
  </li>
  <li>The source code is clearly written and changes can be made by the user.//Kaynak kodlardaki açık şekilde yazılmış olup değişiklikler kullanıcı tarafından yapılabilir.
  </li>
  </p>
<h2>
Directions For Use//Kullanım Talimatları
</h2>
<p>
  <li>First we open the server.py file from the computer we will manage.//İlk olarak server.py dosayasını yöneteceğimiz bilgisayardan açıyoruz.</li>
  <li>The user name and password will be asked by default, the user name "admin" password is also "123".//Karşımıza kullanıcı adı ve şifre sorulacak varsayılan olarak kullanıcı adı "admin" şifre de "123". </li>
  <code><span>def kontrol(self):<br>
        if (self.e1.get() == "ahmed" and self.e2.get() == "528"):  <br>
            print "\nGiris Basarili"<br>
            self.kontrol_birimi = 1<br>
            pencere.destroy()<br>
        else:<br>
            print "\nKullanici Adi veya Sifre Hatali !!!<br>"</span></code>
  <li>Test</li>
  <li></li>
  <li></li>
</p>
