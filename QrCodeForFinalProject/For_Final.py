import qrcode

# QR koduna dönüştürülecek link
link = "https://lucid.app/lucidspark/38e09080-49a1-40bc-8865-cf2ad0c95562/edit?viewport_loc=8%2C281%2C4740%2C2484%2C0_0&invitationId=inv_afd9ead3-54bc-4c71-a151-64097f01ee20"

# QR kodu oluşturma
qr = qrcode.QRCode(
    version=1,  # Versiyon (QR kod karmaşıklığını belirler; 1 en basiti)
    error_correction=qrcode.constants.ERROR_CORRECT_L,  # Hata düzeltme seviyesi
    box_size=10,  # QR kod kutularının boyutu
    border=4,  # Kenar boşluğu (varsayılan 4)
)
qr.add_data(link)
qr.make(fit=True)

# QR kodu görüntüsü oluşturma
img = qr.make_image(fill_color="black", back_color="white")

# QR kodunu bir dosyaya kaydetme
img.save("qr_code.png")

print("QR kodu başarıyla oluşturuldu ve 'qr_code.png' olarak kaydedildi!")
