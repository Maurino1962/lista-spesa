import streamlit as st
from database import get_product_list
from fpdf import FPDF

# Configurazione Pagina e Icona Browser
st.set_page_config(page_title="La Mia Spesa", page_icon="logo.png")

# Visualizzazione Logo Centrale
col1, col2, col3 = st.columns([1, 1, 1])
with col2:
    st.image("logo.png", width=150)

st.markdown("<h1 style='text-align: center;'>Lista della Spesa</h1>", unsafe_allow_html=True)

# Database
prodotti_db = get_product_list()

if 'lista' not in st.session_state:
    st.session_state.lista = []

# Selezione Prodotti
st.write("### Aggiungi Prodotti")
prodotto_scelto = st.selectbox("Cerca prodotto:", [""] + prodotti_db)

if st.button("Aggiungi ➕", use_container_width=True):
    if prodotto_scelto and prodotto_scelto not in st.session_state.lista:
        st.session_state.lista.append(prodotto_scelto)
        st.rerun()

st.write("---")

# Visualizzazione Lista
st.subheader("Prodotti da acquistare:")
for i, voce in enumerate(st.session_state.lista):
    c1, c2 = st.columns([0.85, 0.15])
    c1.write(f"• {voce}")
    if c2.button("❌", key=f"del_{i}"):
        st.session_state.lista.pop(i)
        st.rerun()

st.write("---")

# Funzione per creare il PDF
def crea_pdf(lista):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", 'B', 16)
    pdf.cell(200, 10, txt="La Mia Lista della Spesa", ln=True, align='C')
    pdf.ln(10)
    pdf.set_font("Arial", size=12)
    for item in lista:
        pdf.cell(200, 10, txt=f"- {item}", ln=True)
    return pdf.output(dest='S').encode('latin-1')

# Azioni Finali
if st.session_state.lista:
    pdf_data = crea_pdf(st.session_state.lista)
    st.download_button(label="📥 Scarica Lista in PDF", data=pdf_data, file_name="lista_spesa.pdf", mime="application/pdf", use_container_width=True)
    
    if st.button("🗑️ Svuota Tutto", use_container_width=True):
        st.session_state.lista = []
        st.rerun()
