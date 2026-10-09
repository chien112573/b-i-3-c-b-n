#Km đầu tiên: 15.000 đồng.
#Từ km thứ 2 đến km thứ 5: 12.000 đồng/km.
#Từ km thứ 6 trở đi: 10.000 đồng/km.
#Nếu quãng đường lớn hơn 100 km, khách hàng được giảm 10% tổng tiền cước.
#Nếu km <= 0, in ra "Quang duong khong hop le".

km = float(input("Nhập số km: "))

if km <= 0:
    print("Quang duong khong hop le")
elif km <= 1:
    tien = 15000
    print("Tien cuoc:", tien, "dong")
elif km <= 5:
    tien = 15000 + (km - 1) * 12000
    print("Tien cuoc:", tien, "dong")
else:
    tien = 15000 + 4 * 12000 + (km - 5) * 10000
    print("Tien cuoc:", tien, "dong")
