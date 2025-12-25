import streamlit as st
from database import get_product_list

# 1. Configurazione dell'icona e del titolo (apparirà sul Desktop e sul telefono)
st.set_page_config(page_title="La Mia Spesa", page_icon="🛒")

# 2. Titolo principale dell'app
st.title("🛒 Lista della Spesa")

# 3. Caricamento dei prodotti dal tuo database (suddivisi per categoria)
prodotti_db = get_product_list()

# Inizializzazione della lista nella memoria del browser
if 'lista' not in st.session_state:
    st.session_state.lista = []

# 4. Area di selezione del prodotto
st.write("### Seleziona prodotti")
prodotto_scelto = st.selectbox(
    "Cerca un prodotto dalla tua lista Excel:", 
    [""] + prodotti_db,
    help="Inizia a scrivere il nome del prodotto o della categoria"
)

if st.button("Aggiungi alla lista"):
    if prodotto_scelto and prodotto_scelto not in st.session_state.lista:
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
        if col2.button("Elimina", key=f"del_{i}"):
            st.session_state.lista.pop(i)
            st.rerun()

    st.write("---")
    # Tasto per ricominciare da capo
    if st.button("🗑️ Svuota tutta la lista"):
        st.session_state.lista = []
        st.rerun()
