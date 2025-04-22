import streamlit as st
import os
from compress import compress_image
from auth import check_password

# Set the Streamlit page config
st.set_page_config(page_title="Image Compressor", layout="centered")

# Only proceed if password is correct
if check_password():
    st.title("🔒 Image Compressor with Login")

    st.markdown("""
    This app compresses JPEG/PNG images.
    - Upload an image
    - Choose compression quality
    - Download the compressed image
    """)

    uploaded_file = st.file_uploader("📤 Upload an Image", type=["jpg", "jpeg", "png"])

    if uploaded_file:
        # Save uploaded file to the local directory
        original_path = uploaded_file.name
        with open(original_path, "wb") as f:
            f.write(uploaded_file.getbuffer())
        st.success(f"✅ File uploaded: `{original_path}`")

        # Set compression quality
        quality = st.slider("🛠️ Compression Quality (lower = more compression)", 10, 95, 30)

        # Define output path for compressed image
        filename = os.path.splitext(uploaded_file.name)[0]
        output_path = f"compressed_{filename}.jpg"

        # Compress image when button is clicked
        if st.button("⚡ Compress Image"):
            result = compress_image(original_path, output_path, quality)
            if result:
                st.success(f"✅ Image compressed and saved as `{output_path}`")

                # Download button for the user
                with open(output_path, "rb") as f:
                    st.download_button(
                        label="📥 Download Compressed Image",
                        data=f,
                        file_name=os.path.basename(output_path),
                        mime="image/jpeg"
                    )
            else:
                st.error("❌ Compression failed. Try a different image.")
