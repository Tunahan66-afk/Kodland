ucaklar = {
            "F4F<Croshair": "WW2 Uçağı.",
            "F4<Phantom PHANTOM": "Soğuksavaş`ta kullanılan jet avcı uçağı.",
            "X-43A":"Nasanın deneysel bir hipersonik uçak projesidir.Dünyanın En hızlı uçağı.Km/h=11.000",
            "Su-27<Flanker":"Manevrası ve silahları güçlü jet avcı uçağı.",
            "SR-71<Blackbird":"Dünyanın en hızlı savaş uçağı.Gözlem için kullanılmıştır.",
            "F-14<Tomcat":"En sevdiğim savaş jeti.",
            "Jas39<Gripen":"Çok maksatlı savaş jeti.",
            "Messerschmitt<Bf-109":"WW2`de en fazla üretilen uçak.",
            "Lancaster MK1":"WW2`de en yüksek kiloda bomba taşıyan uçak.  9.979,03 kg  ",
            "Harrier GR1":"V/STOL kalkış özellikli bir uçaktır.Dikey kalkış ve iniş."
            
            }

ucak = input("Hangi uçağı aruyorsunuz ? (hepsini büyük harflerle yazın!): ")

if ucak in ucaklar.keys():
    print(ucaklar[ucak])
    # Kelime eşleşiyorsa ne yapmalıyız?
else:
    print("Yazdığınız uçak vurulup tüştü.")
    # Kelime eşleşmiyorsa ne yapmalıyız?
