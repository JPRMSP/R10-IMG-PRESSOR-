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
    This app lets you compress JPEG/PNG images and save them to the `/content/` directory.
    - Upload an image
    - Choose the compression quality
    - Download or use the file saved in Google Colab
    """)

    uploaded_file = st.file_uploader("📤 Upload an Image", type=["jpg", "jpeg", "png"])

    if uploaded_file:
        # Save the original file to /content
        original_path = f"/content/{uploaded_file.name}"
        with open(original_path, "wb") as f:
            f.write(uploaded_file.getbuffer())
        st.success(f"✅ File uploaded and saved to: `{original_path}`")

        # Set compression quality
        quality = st.slider("🛠️ Compression Quality (lower = smaller file size)", 10, 95, 30)

        # Output path for compressed image
        filename = os.path.splitext(uploaded_file.name)[0]
        output_path = f"/content/compressed_{filename}.jpg"

        # Compress button
        if st.button("⚡ Compress Image"):
            result = compress_image(original_path, output_path, quality)
            if result:
                st.success(f"✅ Image compressed and saved to: `{output_path}`")

                # Show download button
                with open(output_path, "rb") as f:
                    st.download_button(
                        label="📥 Download Compressed Image",
                        data=f,
                        file_name=os.path.basename(output_path),
                        mime="image/jpeg"
                    )
            else:
                st.error("❌ Failed to compress image. Please try another image.")
