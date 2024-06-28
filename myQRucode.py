# import qrcode

# qr_data = 'www.naver.com'
# qr_img = qrcode.make(qr_data)

# save_path = '.\\' + qr_data + '.png'
# qr_img.save(save_path)
import qrcode

# QR 코드 데이터 설정
data = "https://www.naver.com"

# QR 코드 생성
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)

# 데이터 추가
qr.add_data(data)
qr.make(fit=True)

# QR 코드를 이미지로 변환
img = qr.make_image(fill_color="black", back_color="white")

# 이미지 저장
img.save("example_qr.png")

# 이미지 보기
img.show()
