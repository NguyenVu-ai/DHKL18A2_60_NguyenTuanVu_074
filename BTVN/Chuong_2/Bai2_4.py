from xml.dom import minidom
tai_lieu = minidom.parse("C:\Users\os\OneDrive\Pictures\OneDrive\Desktop\60_DHKL18A2Hn_nguyenTuanVu_24174600074\BTVN\Chuong_2\sample.xml")
goc = tai_lieu.documentElement
print("Kết quả gốc là: ",goc.tagName)