import streamlit as st
import qrcode
from io import BytesIO
import uuid
from PIL import Image
from gtts import gTTS
import base64

def generate_qr(data):
    qr = qrcode.QRCode(version=1,box_size=10,border=4)
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black",back_color="white")
    return img


st.title("0 Metro Ticket Booking System with QR code + Auto Voice")
stations = ["Ameerpet","Miyapur","LB Nagar","KPHB","JNTU"]
name = st.text_input("Passenger Name")
source = st.selectbox("Source Station",stations)
destination = st.selectbox("Destination Station",stations)
no_tickets = st.number_input("Number of Tickets",min_value=1, value=1)
price_per_ticket=30
total_amount = no_tickets*price_per_ticket
st.info(f" Total Amount:{total_amount}")

if st.button("Book Ticket"):
    if name.strip()=="":
        st.error("Please enter  passenger name.")
    elif source == destination:
            st.errror("Source and Destination cannot be the same")
    else:
         booking_id = str(uuid.uuid4())[:8]
         qr_data =(
             f"BookingID: {booking_id}\n"
             f"Name: {name}\nFrom: {source}\nTo: {destination}\n Tickets:{no_tickets}"
             )
         qr_img = generate_qr(qr_data)
         buf = BytesIO()
         qr_img.save(buf, format="PNG")
         qr_bytes = buf.getvalue()
         st.success("Ticket Booked Succesfully!")
         st.write("### Ticket Details")
         st.write(f"**Bookinf ID:**{booking_id}")
         st.write(f"*Passenger:* {name}")
         st.write(f"*From:* {source}")
         st.write(f"*To:* {destination}")
         st.write(f"*Tickets:* {no_tickets}")
         st.write(f"*amount paid:* {total_amount}")
         st.image(qr_bytes,width=250)
