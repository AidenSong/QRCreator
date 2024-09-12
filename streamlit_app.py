import streamlit as st
import qrcode
from PIL import Image
from io import BytesIO

# 타이틀 설정
st.title("QR 코드 생성기")

# 사용자로부터 입력받기
data = st.text_input("QR 코드로 변환할 텍스트 또는 URL을 입력하세요:")

# 버튼 클릭 시 QR 코드 생성
if st.button("QR 코드 생성"):
    if data:
        # QR 코드 생성
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(data)
        qr.make(fit=True)

        # 이미지 생성
        img = qr.make_image(fill='black', back_color='white')

        # 이미지 표시
        st.image(img)

        # 이미지 다운로드 기능 추가
        buf = BytesIO()
        img.save(buf)
        byte_im = buf.getvalue()
        st.download_button(
            label="QR 코드 이미지 다운로드",
            data=byte_im,
            file_name="qrcode.png",
            mime="image/png"
        )
    else:
        st.warning("텍스트나 URL을 입력해주세요.")

# Footer
st.write("QR 코드 생성기 © 2024")
