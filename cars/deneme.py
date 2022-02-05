# class User():
    
#     sayac_kullanici = 0 #? Bu cur yazilis birbasa class icinde yazilis class attribute gedir
    
#     #initden evvel class sonra yazilan funksiyalar daha cox classmethod deye seslenilir
    
#     #!ShowActiveUser =>@classmethod decorator
#     @classmethod
#     def display_active_users(cls):
#         print('{} tane aktiv kullanici var'.format(cls.sayac_kullanici))
    
#     @classmethod
#     def create_user_classmethod(cls,data_user):
#         ad,soyad,yas = data_user.split(',')
#         return cls(ad,soyad,yas)  #Burdaki cls yaradilan user objectini bildirir ele bilki self kimidir amma cls yazanda ilk parametresine funksiyani bu funksiya classmethod funksiyasi olur
#         #Burdaki cls ele User Classidir yeni ele bilki bele olur => #!User(ad,soyad,yas) seklinde bu curde yazilnada bildiyimiz kimi yeni bir user yaratmag mumkunudur yeni classdan nesne toretmek,yeni return cls(ad,soyad,yas) verende avtomatik olarag __init__ isleyir
        
#     def __init__(self,ad,soyad,yas):
#         self.ad = ad
#         self.soyad = soyad
#         self.yas = yas
#         User.sayac_kullanici+=1
        
#     def bilgilerGoster(self):
#         return 'kullanicinin ismi {} ve soyismi {}'.format(self.ad,self.soyad)
    
#     def logOut(self):
#         User.sayac_kullanici-=1
#         print(f"{self.ad} kullanici programdan cikis yapti")

# User.display_active_users()
# # user_1 = User('riad','elimemmedov',20)
# # user_2 = User('tural','veliyev',16)
# # user_3 = User('kenan','suleymanov',25)
# # user_1.logOut()
# #User.display_active_users()

# user_4 = User.create_user_classmethod("Kamran,Ismayolov,25")
# print(user_4.ad)
# print(user_4.soyad)
# print(user_4.yas)
# print(user_4.bilgilerGoster())
# User.display_active_users()



#!Inheritance

# class User():
#     def __init__(self,name,surname,age):
#         self.name = name
#         self.surname = surname
#         self.age = age
        
    
# class Student(User):
#     def __init__(self,name,surname,age,nomremekteb):
#         super().__init__(name,surname,age)#ve ya super yerine birbasa => User.__init__() formasindada yaza bilersen
#         self.nomremekteb = nomremekteb
        
#     def bilgilver(self):
#         print('Bilgiver Calisti')
        
# st1 = Student('riad','elimemmedov',20,5)
# print(st1.name)
# print(st1.surname)
# print(st1.age)
# print(st1.nomremekteb)
# st1.bilgilver()#cunki return ile deyeri dondermemisemki print yazim eger return ile deyeri geri donsem o zaman print yazmaliyams


#!Ozel Metodlarin Istifasi Classlarda

# class Urun():
#     def __init__(self,urunKodu,urunAdim,urunFiyati):
#         self.urunKodu = urunKodu
#         self.urunAdim = urunAdim
#         self.urunFiyati = urunFiyati
    
#     def bilgerverUrun(self):
#         return f"{self.urunKodu} olan urunun adi:{self.urunAdim} ve ismi:{self.urunFiyati} dir"
    
#     #?burda ise metodlari istifade edek meselen => __len__ bu cur metodlara special class methodlar deyilir yeni ozel metodlar deyilir
#     def __len__(self):
#         return len(self.urunAdim)
    
#     def __str__(self):#eger class icinde bi funksiya yazirsansa self olmalidir ilk parametresi mutleq,eger yoxdursa ve istifade etmek isteyirsense amma bu zaman @staticmethodlardan istifade etmelisen
#         return f"{self.urunKodu} {self.urunAdim}"
    
#     def __repr__(self):
#         return f"{self.urunKodu} {self.urunAdim}"
    
#     def __del__(self):
#         print('Urun Silindi')
        
    
# urun1 = Urun('545353','armud',5)
#print(len(urun1))#eger yuxarida => __len__ funksiyasini yazmagsaydig Class bize icaze vermir len istifade etmeye __len__ sayesinden ise istfiade ede bildik
#print(str(urun1))#gedib yuxarida yazilan __str__ funksiyani isledecek str(urun1) adli kod 
#print(repr(urun1))
#del(urun1)
#?Ve Ya
#print(urun1.__str__())
# print(urun1.__len__())
#print(urun1.__repr__())
# urun1.__del__() => bu formada 2 defe yazacag ekrana bir defe sildiyi deyeri donderir 2 cide ise oz funksiyasindaki print isleidir deyesen
#*Ve ya
#del urun1

#!Pyhontdaki => Iterable ve Iteratorlar
#?Iterable => listeler ola biler meselen => sayilar = [1,2,3,4,5]
#?Iterator => tam ededler ola biler 


sayilar =  [1,2,3,4,5]
# for i in sayilar:
#     print(i)#burda bir iterable isledir yeni => __next__ metodu isledir burda
    
#*Oz iterable imizi yaag
iterablenesne = iter(sayilar)
# print(next(iterablenesne))
# print(next(iterablenesne))
# print(next(iterablenesne))
# print(next(iterablenesne))
# print(next(iterablenesne))
# print(next(iterablenesne))

# while True:
#     try:
#         print(next(iterablenesne))#her next isleyende bir addim ireli atilir ele bil
#     except StopIteration as e:#as vasitesile adini deyisdimki xetanin uzun olmasin
#         break


#!Indi ise oz => Iteratorumuzu yazag
# class PowTo:
#     def __init__(self,max_number=0):
#         self.max_number = max_number
    
#     def __iter__(self):
#         self.n = 0
#         return self #bura qanun kimidir PowTo geri donmelidirki uzerine yazsin diger deyerleri yoxsa xeta verecek python  #self burda PowTo dur
    
#     def __next__(self):
#         if self.n <= self.max_number:
#             result = 2 ** self.n
#             self.n+=1
#             return result
#         else:
#             raise StopIteration
# nesne = PowTo(3)

# i = iter(nesne)
# print(next(i))

# class Sayac():
#     def __init__(self,start,stop):
#         self.start = start
#         self.stop = stop
        
#     def __iter__(self):
#         return self
    
#     def __next__(self):
#         if self.start <= self.stop:
#             x = self.start
#             self.start+=1
#             return x#her artan start deyerini ekrana yazmag ucun bu cur yoldan istifade etdim
#         else:
#             raise StopIteration

# sayac_result = Sayac(2,5)
# a = iter(sayac_result)
# for i in a:
#     print(i)
