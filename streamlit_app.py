import streamlit as st
import qrcode
from PIL import Image
from io import BytesIO

# 페이지 제목
st.title("QR 코드 생성기")

# 사용자 입력을 받는 필드
input_data = st.text_input("QR 코드에 포함할 데이터를 입력하세요:")

# QR 코드 생성
if input_data:
    qr = qrcode.QRCode(
        version=1, 
        error_correction=qrcode.constants.ERROR_CORRECT_L, 
        box_size=10, 
        border=4
    )
    qr.add_data(input_data)
    qr.make(fit=True)

    # QR 코드 이미지를 생성
    img = qr.make_image(fill="black", back_color="white")

    # 이미지 메모리에 저장
    buffer = BytesIO()
    img.save(buffer)
    buffer.seek(0)

    # 이미지 출력
    st.image(img, caption="생성된 QR 코드", use_column_width=True)

    # 이미지 다운로드 버튼
    st.download_button(
        label="QR 코드 다운로드",
        data=buffer,
        file_name="qr_code.png",
        mime="image/png"
    )
