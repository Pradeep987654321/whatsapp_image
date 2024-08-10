import streamlit as st
import pywhatkit
import imageio as iio
import tempfile  # For creating temporary files


with open("style.css") as f:
    st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)


# Streamlit app
st.title("WhatsApp Message Sender")

# User inputs
phone_number = st.text_input("Enter Your Phone Number with Country Code (e.g., +1234567890)")
message = st.text_area("Enter Your Message")
uploaded_file = st.file_uploader("Upload an Image", type=["png", "jpg", "jpeg"])

if st.button("Send Message"):
    if phone_number and message and uploaded_file is not None:
        try:
            # Create a temporary file to save the uploaded image
            with tempfile.NamedTemporaryFile(delete=False, suffix=".png") as temp_file:
                temp_file.write(uploaded_file.read())
                temp_file_path = temp_file.name

            # Send the WhatsApp message with the image
            pywhatkit.sendwhats_image(phone_number, temp_file_path, message)
            
            st.success(f"Message sent successfully to {phone_number}!")
        except Exception as e:
            st.error(f"An error occurred: {e}")
    else:
        st.warning("Please fill out all fields and upload an image.")
