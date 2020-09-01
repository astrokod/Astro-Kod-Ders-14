import p5
from random import randint
# Gerekli içe aktarmalar yapıldı

# Genişlik ve Yükseklik için global değişkenler oluşturuldu
width, height = 800, 500

# toplara dında, global, bir dizi değişken oluşturuldu
toplar = []


# Top sınıfı oluşturuldu
class Top:
    # Constactor (işna edici) metod
    def __init__(self, x, y, v_x, v_y, r):
        # bu metod x, y, v_x, v_y ve r değerlerini zorunlu olarak alır
        # Böylece bu sınıftan bir (instance/object)
        # obje oluşturulurken bu bilgiler istenir
        # self kavramı ise kendine (Top sınıfına) bir referanstır
        self.x = x
        self.y = y
        self.v_x = v_x
        self.v_y = v_y
        self.r = r


    def ciz(self):
        """Bu metod, ekrana self.x ve self.'de self.r çapında bir daire çizer"""
        p5.circle((self.x, self.y), self.r)

    def hareket_et(self):
        """Bu metod, self.x ve self.y değerini,
        sırasıyla self.v_x ve self.v_y'ye göre değiştiriyor"""
        self.x += self.v_x
        self.y += self.v_y

    def sek(self):
        """Bu metod, şimdiki konumun ekranın dışında olup olmadığını kontrol edilr
        Ekranın dışında olması durumunda hızı değerimizin yönünü değiştiriyor"""
        if self.x <= self.r/2 or self.x >= width - self.r/2:
            self.v_x *= -1

        if self.y <= self.r/2 or self.y >= height - self.r/2:
            self.v_y *= -1


def setup():
    # toplar değişkenini değiştirabilmek için global anahtar kelimesi kullanıldı
    global toplar
    # widthxheight ebatlarında bir pencere oluşturuldu
    p5.size(width, height)

    # toplar dizi değişkeninin içine 20 adet Top objesi yerleştiriliyor
    for _ in range(20):
        # Konum, Hız ve çap değerleri rastgele seçiliyor
        toplar.append(Top(randint(5, width - 5), randint(5, height - 5),
                          randint(-7, 7), randint(-7, 7),
                          randint(5, 10)))


def draw():
    # Arka alanı siyaha boya
    p5.background(0)

    # toplar dizid eğişkeni içerisinde bir iterasyon yap
    # Böylece sırasıyla:
    # toplar[0], toplar[1], ..., toplar[8], toplar[9], top değişkenine atanır
    # top değikeni aslında bir Top objesi barındırıyor
    for top in toplar:
        # top'u çiz
        top.ciz()
        # top'u haret ettir
        top.hareket_et()
        # top ekranın kenarına geldiyse, topu sektir
        top.sek()


# Bu script çalıştırıldığunda aşağıdakileri yap
# Böylece import edildiğinde işlem yapılmaz
if __name__ == "__main__":
    # p5'i çalıştır
    p5.run()
