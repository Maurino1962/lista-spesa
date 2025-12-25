# database.py

def get_product_list():
    """
    Ritorna la lista completa dei 215 prodotti per l'app della spesa.
    """
    products = [
        # --- FRUTTA E VERDURA (40) ---
        "Mela", "Banana", "Arancia", "Pera", "Limone", "Kiwi", "Fragola", "Uva", "Melone", "Anguria",
        "Pomodori", "Insalata", "Carota", "Cipolla", "Aglio", "Patate", "Zucchine", "Melanzane", "Peperoni", "Spinaci",
        "Broccoli", "Cavolfiore", "Asparagi", "Finocchi", "Sedano", "Fagiolini", "Piselli", "Zucca", "Cetrioli", "Ravanelli",
        "Funghi", "Prezzemolo", "Basilico", "Rosmarino", "Salvia", "Mirtilli", "Lamponi", "Pesca", "Albicocca", "Susina",
        
        # --- LATTICINI E UOVA (30) ---
        "Latte Intero", "Latte Parzialmente Scremato", "Yogurt Bianco", "Yogurt Frutta", "Burro", "Uova (6 pz)", "Uova (10 pz)",
        "Parmigiano Reggiano", "Pecorino", "Mozzarella", "Ricotta", "Mascarpone", "Stracchino", "Gorgonzola", "Panna da cucina",
        "Panna da montare", "Formaggio a fette", "Provola", "Asiago", "Certosa", "Emmental", "Philadelphia", "Latte di Soia",
        "Latte di Mandorla", "Margarina", "Feta", "Kefir", "Taleggio", "Fontina", "Scamorza",

        # --- CARNE E SALUMI (25) ---
        "Petto di Pollo", "Cosce di Pollo", "Macinato Bovino", "Bistecca Manzo", "Costolette Maiale", "Salsiccia",
        "Prosciutto Crudo", "Prosciutto Cotto", "Salame", "Mortadella", "Bresaola", "Speck", "Pancetta", "Wurstel",
        "Hamburger Pollo", "Hamburger Manzo", "Tacchino a fette", "Fegato", "Lonza", "Arista", "Coniglio", "Anatra",
        "Coppa", "Guanciale", "Cotechino",

        # --- PESCE (15) ---
        "Salmone Fresco", "Orata", "Branzino", "Merluzzo", "Tonno in scatola", "Sgombro", "Gamberetti", "Calamari",
        "Bastoncini di Pesce", "Filetti di Platessa", "Alici", "Polpo", "Vongole", "Cozze", "Pesce Spada",

        # --- DISPENSA E COLAZIONE (50) ---
        "Pasta Spaghetti", "Pasta Penne", "Pasta Fusilli", "Pasta Corta", "Riso Carnaroli", "Riso Basmati", "Farina 00",
        "Farina Integrale", "Zucchero Bianco", "Zucchero di Canna", "Miele", "Caffè macinato", "Capsule Caffè", "Tè",
        "Biscotti", "Frollini", "Merendine", "Cereali", "Fette biscottate", "Confettura Fragola", "Confettura Albicocca",
        "Nutella", "Crema di arachidi", "Olio EVO", "Olio di Semi", "Aceto di Vino", "Aceto Balsamico", "Sale Grosso",
        "Sale Fino", "Passata di Pomodoro", "Polpa di Pomodoro", "Legumi Ceci", "Legumi Lenticchie", "Legumi Fagioli",
        "Maionese", "Ketchup", "Senape", "Pesto", "Pane a fette", "Pane Bauletto", "Cracker", "Grissini", "Gallette di Riso",
        "Lievito per dolci", "Lievito di birra", "Cacao amaro", "Cioccolato Fondente", "Cioccolato al latte", "Noci", "Mandorle",

        # --- BEVANDE (20) ---
        "Acqua Naturale", "Acqua Frizzante", "Vino Rosso", "Vino Bianco", "Birra", "Coca Cola", "Aranciata", "Succo d'Arancia",
        "Succo di Frutta", "Acqua Tonica", "Gassosa", "Aperitivo analcolico", "Spumante", "Tè freddo Limone", "Tè freddo Pesca",
        "Bevanda Energetica", "Sciroppo di Menta", "Vino Rosato", "Birra Artigianale", "Caffè d'Orzo",

        # --- SURGELATI (15) ---
        "Pizza Surgelata", "Patatine fritte", "Spinaci surgelati", "Minestrone", "Misto funghi", "Gelato vaschetta",
        "Coni Gelato", "Sorbetto", "Lasagne pronte", "Pesce impanato", "Piselli novelli", "Zuppa pronta", "Verdure grigliate",
        "Cornetti surgelati", "Pancakes",

        # --- IGIENE E PULIZIA (20) ---
        "Carta Igienica", "Rotolone Cucina", "Detersivo Lavatrice", "Ammorbidente", "Detersivo Piatti", "Pastiglie Lavastoviglie",
        "Sgrassatore", "Detergente Pavimenti", "Candeggina", "Alcool", "Sapone Mani", "Bagnoschiuma", "Shampoo", "Balsamo",
        "Dentifricio", "Spazzolino", "Deodorante", "Schiuma da barba", "Assorbenti", "Fazzoletti di carta"
    ]
    
    return sorted(list(set(products))) # Rimuove duplicati e ordina alfabeticamente
