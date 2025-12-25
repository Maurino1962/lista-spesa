import streamlit as st
from database import get_product_list
from fpdf import FPDF

# 1. Configurazione base (Titolo e Icona della scheda browser)
st.set_page_config(
    page_title="La Mia Spesa", 
    page_icon="logo.png",
    layout="centered"
)

# 2. CODICE PER FORZARE L'ICONA SU ANDROID E IPHONE
# Questo comunica al telefono di usare il tuo logo.png quando aggiungi l'app alla Home
st.markdown(f"""
    <head>
        <link rel="manifest" href="https://raw.githubusercontent.com/Maurino1962/lista-spesa/main/manifest.json">
        <link rel="apple-touch-icon" href="https://raw.githubusercontent.com/Maurino1962/lista-spesa/main/logo.png">
        <meta name="mobile-web-app-capable" content="yes">
        <meta name="apple-mobile-web-app-status-bar-style" content="black">
    </head>
""", unsafe_allow_html=True)

# 3. Visualizzazione Logo Centrale nell'interfaccia
try:
    col1, col2, col3 = st.columns([1, 1, 1])
    with col2:
        st.image("logo.png", width=150)
except:
    st.markdown("<h1 style='text-align: center;'>🛒</h1>", unsafe_allow_html=True)

st.markdown("<h1 style='text-align: center;'>Lista della Spesa</h1>", unsafe_allow_html=True)

# 4. Caricamento prodotti dal database
prodotti_db = get_product_list()

if 'lista' not in st.session_state:
    st.session_state.lista = []

# 5. Area di inserimento
st.write("### Aggiungi Prodotti")
prodotto_scelto = st.selectbox("Cerca un prodotto:", [""] + prodotti_db)

if st.button("Aggiungi alla lista ➕", use_container_width=True):
    if prodotto_scelto and prodotto_scelto != "":
        if prodotto_scelto not in st.session_state.lista:
            st.session_state.lista.append(prodotto_scelto)
            st.rerun()

st.write("---")

# 6. Visualizzazione della lista corrente
st.subheader("Da comprare:")
if not st.session_state.lista:
    st.info("La lista è vuota.")
else:
    for i, voce in enumerate(st.session_state.lista):
        c1, c2 = st.columns([0.85, 0.15])
        c1.write(f"✅ {voce}")
        if c2.button("❌", key=f"del_{i}"):
            st.session_state.lista.pop(i)
            st.rerun()

    st.write("---")

    # 7. Funzione per creare il PDF (gestisce anche caratteri speciali)
    def crea_pdf(lista):
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", 'B', 16)
        pdf.cell(200, 10, txt="La Mia Lista della Spesa", ln=True, align='C')
        pdf.ln(10)
        pdf.set_font("Arial", size=12)
        for item in lista:
            # Pulisce il testo per evitare errori nel file PDF
            item_clean = item.encode('latin-1', 'ignore').decode('latin-1')
            pdf.cell(200, 10, txt=f"- {item_clean}", ln=True)
        return pdf.output(dest='S').encode('latin-1')

    # 8. Tasti di azione finale (PDF e Svuota)
    pdf_data = crea_pdf(st.session_state.lista)
    st.download_button(
        label="📥 Scarica Lista in PDF", 
        data=pdf_data, 
        file_name="lista_spesa.pdf", 
        mime="application/pdf", 
        use_container_width=True
    )
    
    if st.button("🗑️ Svuota tutta la lista", use_container_width=True):
        st.session_state.lista = []
        st.rerun()
