ucaklar = {
            "F4F": "WW2 Uçağı",
            "F4 PHANTOM": "Soğuksavaş`ta kullanılan jet avcı"
            }

ucak = input("Hangi uçağı aruyorsunuz ? (hepsini büyük harflerle yazın!): ")

if ucak in ucaklar.keys():
    print(ucaklar[ucak])
    # Kelime eşleşiyorsa ne yapmalıyız?
else:
    print("Yazdığınız uçak vurulup tüştü.")
    # Kelime eşleşmiyorsa ne yapmalıyız?
