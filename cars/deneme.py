class User():
    
    sayac_kullanici = 0 #? Bu cur yazilis birbasa class icinde yazilis class attribute gedir
    
    #initden evvel class sonra yazilan funksiyalar daha cox classmethod deye seslenilir
    
    #!ShowActiveUser =>@classmethod decorator
    @classmethod
    def display_active_users(cls):
        print('{} tane aktiv kullanici var'.format(cls.sayac_kullanici))
    
    @classmethod
    def create_user_classmethod(cls,data_user):
        ad,soyad,yas = data_user.split(',')
        return cls(ad,soyad,yas)  #Burdaki cls yaradilan user objectini bildirir ele bilki self kimidir amma cls yazanda ilk parametresine funksiyani bu funksiya classmethod funksiyasi olur
        #Burdaki cls ele User Classidir yeni ele bilki bele olur => #!User(ad,soyad,yas) seklinde bu curde yazilnada bildiyimiz kimi yeni bir user yaratmag mumkunudur yeni classdan nesne toretmek,yeni return cls(ad,soyad,yas) verende avtomatik olarag __init__ isleyir
        
    def __init__(self,ad,soyad,yas):
        self.ad = ad
        self.soyad = soyad
        self.yas = yas
        User.sayac_kullanici+=1
        
    def bilgilerGoster(self):
        return 'kullanicinin ismi {} ve soyismi {}'.format(self.ad,self.soyad)
    
    def logOut(self):
        User.sayac_kullanici-=1
        print(f"{self.ad} kullanici programdan cikis yapti")

User.display_active_users()
# user_1 = User('riad','elimemmedov',20)
# user_2 = User('tural','veliyev',16)
# user_3 = User('kenan','suleymanov',25)
# user_1.logOut()
#User.display_active_users()

user_4 = User.create_user_classmethod("Kamran,Ismayolov,25")
print(user_4.ad)
print(user_4.soyad)
print(user_4.yas)
print(user_4.bilgilerGoster())
User.display_active_users()

