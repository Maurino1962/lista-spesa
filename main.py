import streamlit as st
from database import get_product_list

st.set_page_config(page_title="La Mia Spesa", page_icon="🛒")

st.title("🛒 Lista della Spesa")

# Carichiamo i prodotti dal database.py
if 'prodotti_totali' not in st.session_state:
    st.session_state.prodotti_totali = get_product_list()

if 'lista_spesa' not in st.session_state:
    st.session_state.lista_spesa = []

# Interfaccia per aggiungere prodotti
prodotto_scelto = st.selectbox("Cerca un prodotto da aggiungere:", [""] + st.session_state.prodotti_totali)

if st.button("Aggiungi alla lista") and prodotto_scelto != "":
    if prodotto_scelto not in st.session_state.lista_spesa:
        st.session_state.lista_spesa.append(prodotto_scelto)
        st.success(f"{prodotto_scelto} aggiunto!")
    else:
        st.warning("Il prodotto è già in lista.")

st.divider()

# Visualizzazione lista
st.subheader("Da comprare:")
if not st.session_state.lista_spesa:
    st.info("La lista è vuota.")
else:
    for i, voce in enumerate(st.session_state.lista_spesa):
        col1, col2 = st.columns([0.8, 0.2])
        col1.write(f"• {voce}")
        if col2.button("Elimina", key=f"del_{i}"):
            st.session_state.lista_spesa.pop(i)
            st.rerun()

if st.button("Svuota tutta la lista"):
    st.session_state.lista_spesa = []
    st.rerun()
