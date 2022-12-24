import streamlit as st
import base64

st.title("Esta es la aventura de Navidad! 🎄")

points = 0

st.write("### Responde a las preguntas y podrás ganar fabulosos premios! 🎁")

def displayPDF(file):
    # Opening file from file path
    with open(file, "rb") as f:
        base64_pdf = base64.b64encode(f.read()).decode('utf-8')

    # Embedding PDF in HTML
    pdf_display = F'<iframe src="data:application/pdf;base64,{base64_pdf}" width="700" height="500" type="application/pdf"></iframe>'

    # Displaying File
    st.markdown(pdf_display, unsafe_allow_html=True)

displayPDF("attachments/k50valid until  22022023.pdf")