import streamlit as st
from database import get_product_list

# 1. Configurazione dell'icona e del titolo per il browser
st.set_page_config(
    page_title="La Mia Spesa", 
    page_icon="logo.png",  # <--- MODIFICA EFFETTUATA: Ora usa il tuo logo!
    layout="centered"
)

# --- LOGO PROFESSIONALE ---
# Carica "logo.png" dalla cartella principale di GitHub
try:
    col_logo1, col_logo2, col_logo3 = st.columns([1, 1, 1])
    with col_logo2:
        st.image("logo.png", width=150)
except:
    st.markdown("<h1 style='text-align: center;'>🛒</h1>", unsafe_allow_html=True)

# 2. Titolo principale dell'app
st.markdown("<h1 style='text-align: center;'>Lista della Spesa</h1>", unsafe_allow_html=True)

# 3. Caricamento dei prodotti dal tuo database
prodotti_db = get_product_list()

# Inizializzazione della lista nella memoria del browser (Session State)
if 'lista' not in st.session_state:
    st.session_state.lista = []

# 4. Area di selezione del prodotto
st.write("### Seleziona prodotti")
prodotto_scelto = st.selectbox(
    "Cerca un prodotto dalla tua lista:", 
    [""] + prodotti_db,
    help="Inizia a scrivere il nome del prodotto"
)

# Pulsante per aggiungere con icona
if st.button("Aggiungi alla lista ➕", use_container_width=True):
    if prodotto_scelto and prodotto_scelto != "":
        if prodotto_scelto not in st.session_state.lista:
            st.session_state.lista.append(prodotto_scelto)
            st.rerun()

st.write("---")

# 5. Visualizzazione della lista "Da comprare"
st.subheader("Da comprare:")

if not st.session_state.lista:
    st.info("La lista è vuota. Seleziona qualcosa sopra per iniziare!")
else:
    # Mostra ogni prodotto con un tasto per eliminarlo
    for i, voce in enumerate(st.session_state.lista):
        col1, col2 = st.columns([0.85, 0.15])
        col1.write(f"✅ {voce}")
        # Tasto X per eliminare il singolo elemento
        if col2.button("❌", key=f"del_{i}"):
            st.session_state.lista.pop(i)
            st.rerun()

    st.write("---")
    # Tasto per ricominciare da capo
    if st.button("🗑️ Svuota tutta la lista", use_container_width=True):
        st.session_state.lista = []
        st.rerun()
