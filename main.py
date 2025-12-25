import streamlit as st
from database import get_product_list
from fpdf import FPDF

# 1. Configurazione base
st.set_page_config(
    page_title="La Mia Spesa", 
    page_icon="logo.png",
    layout="centered"
)

# 2. Codice per l'icona (Versione semplificata per non bloccare l'app)
st.markdown("""
    <link rel="apple-touch-icon" href="https://raw.githubusercontent.com/Maurino1962/lista-spesa/main/logo.png">
""", unsafe_allow_html=True)

# 3. Visualizzazione Logo
try:
    st.image("logo.png", width=150)
except:
    st.title("🛒 Lista della Spesa")

st.markdown("<h1 style='text-align: center;'>Lista della Spesa</h1>", unsafe_allow_html=True)

# 4. Database e Sessione
prodotti_db = get_product_list()
if 'lista' not in st.session_state:
    st.session_state.lista = []

# 5. Selezione e Aggiunta
prodotto_scelto = st.selectbox("Cerca un prodotto:", [""] + prodotti_db)

if st.button("Aggiungi ➕", use_container_width=True):
    if prodotto_scelto and prodotto_scelto not in st.session_state.lista:
        st.session_state.lista.append(prodotto_scelto)
        st.rerun()

st.write("---")

# 6. Lista prodotti
if st.session_state.lista:
    for i, voce in enumerate(st.session_state.lista):
        c1, c2 = st.columns([0.8, 0.2])
        c1.write(f"✅ {voce}")
        if c2.button("❌", key=f"del_{i}"):
            st.session_state.lista.pop(i)
            st.rerun()

    st.write("---")

    # 7. Funzione PDF
    def crea_pdf(lista):
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", 'B', 16)
        pdf.cell(200, 10, txt="La Mia Lista della Spesa", ln=True, align='C')
        pdf.ln(10)
        pdf.set_font("Arial", size=12)
        for item in lista:
            item_clean = item.encode('latin-1', 'ignore').decode('latin-1')
            pdf.cell(200, 10, txt=f"- {item_clean}", ln=True)
        return pdf.output(dest='S').encode('latin-1')

    pdf_data = crea_pdf(st.session_state.lista)
    st.download_button(label="📥 Scarica PDF", data=pdf_data, file_name="lista.pdf", mime="application/pdf", use_container_width=True)
    
    if st.button("🗑️ Svuota Tutto", use_container_width=True):
        st.session_state.lista = []
        st.rerun()
