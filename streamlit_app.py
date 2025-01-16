import streamlit as st
from pathlib import Path

st.markdown("<style> .stAppHeader {display:none;} ul {list-style-type: none; } </style>", unsafe_allow_html=True)

def get_file_content_as_bytes(file_path):
    with open(file_path, "rb") as file:
        return file.read()

# Pfad zur PDF-Datei
file_path = 'Lebenslauf.pdf'

st.write("")

# Lese den Inhalt der PDF-Datei als Bytes
file_bytes = get_file_content_as_bytes(file_path)


left, right = st.columns(2)
left.image("profile-pic.png", width=250)

with right:
 st.markdown("""
        <h3>Milana Bondar</h3>
        <em>Ich bin davon überzeugt, dass KI die Welt verändern wird   
        und ich möchte ein Teil davon sein.</em>  
            
        🏠 *Hertha-Firnberg-Straße7*             
        📇 *1100 Wien*            
        📱  *Mobil: +43 066 08613308*                        
         """, unsafe_allow_html=True)
 
 st.write("")

with right:
 st.download_button(
                label="📄 Download Lebenslauf",
                data=file_bytes,
                file_name=file_path,
                mime='application/pdf'
    )
with right:
 st.write("📩", "milana.bondar.79@gmail.com")


st.write("")
st.write("")        

st.header("IT-Kompetenz", anchor=False, divider="blue") 

st.markdown("""
        👩🏻‍💼 Office: Guter Umfang mit Powerpoint, Excel und Word    
        💻 Programmiersprachen:HTML, Python  
        👩🏻‍💻 Programmierung: Praktische Erfahrung in Python, Entwicklung kleine Website  
        📊 Eigene Projekte: Konzeption und Umsetzung verschiedener Projekte inklusive diese Website  
        🎒 Schule: Fach Bereich IT mit positivem Erfolg 
            """,)  

st.write("")
st.write("")

st.header("Schulbildung", anchor=False, divider="blue") 
st.markdown("🛠️ Berufspraktische Tage 1: Gesundheitszentrum Favoriten, Wien - 18./22.11.2024")

st.write("")

st.header("Sprachen", anchor=False, divider="blue") 

import streamlit as st

st.subheader("English", anchor=False)
levels = ("A1", "A2", "B1", "B2", "C1", "C2") 
levels = st.select_slider("", options=levels, value="B2")

st.subheader("German", anchor=False)
levels = ("A1", "A2", "B1", "B2", "C1", "C2") 
levels = st.select_slider("", options=levels, value="B1")

st.subheader("Ukrainian", anchor=False)
levels = ("A1", "A2", "B1", "B2", "C1", "C2") 
levels = st.select_slider("", options=levels, value="C2")

st.subheader("Russian", anchor=False)
levels = ("A1", "A2", "B1", "B2", "C1", "C2") 
levels = st.select_slider("", options=levels, value="C1")

st.write("")
st.write("")
st.write("")
st.write("")

st.header("Interessen und Hobbys", anchor=False, divider="blue") 
st.markdown("""
        💻 Programmieren (HTML, Streamlit, Python)  
        🎹 Klavier spielen (Schloss die Musikschule -9 Studienjahre mit Auszeichnung ab)  
        🏊🏻 Schwimmen (Ich schwimme seit 6 Jahr in einer Proffigruppe)  
        🧁 Kochen    
        🎶 Musik hören  
        """)

st.header("Schulbildung", anchor=False, divider="blue")
st.markdown("""
        2023-2024 – Wienerberg Mittelschule 

        Fachmittelschule Schaumburgergasse, Wien    
        ► Schwerpunkt: Intensive IT-Spezialisierung, Fokus auf modernen Webtechnologien und Wirtschaft  
        ► Zeitraum: September 2024 - Juli 2025  
            
        2014-2026 – Gymnasium (ukrainische)  
        """) 

st.header("Eigenschaften", anchor=False, divider="blue")
st.markdown("""
        🗣️ Kontaktfreudig  
        👩🏻‍🤝‍👩🏼 Freundlich  
        ⌛ Organisiert  
        🤝🏻 Teamfähig  
        🫶🏻 Hilfsbereit  
            """)

st.write("")
st.write("")
st.write("")
st.write("")

left, right = st.columns(2)

with left:
        st.link_button("Zeugnis FMS4", "https://de.wikipedia.org/wiki/Wikipedia:Hauptseite")

     
with left:
        # Pfad zur PDF-Datei
        file_path = 'Mittelschule.pdf'

st.write("")

# Lese den Inhalt der PDF-Datei als Bytes
file_bytes = get_file_content_as_bytes(file_path)
with left:
      with right:
        st.download_button(
                label="Mittelschule Zeugnis",
                data=file_bytes,
                file_name=file_path,
                mime='application/pdf')
        
 

left, right = st.columns(2)

# Pfad zur PDF-Datei
file_path = 'Ukrainische.pdf'

st.write("")

# Lese den Inhalt der PDF-Datei als Bytes
file_bytes = get_file_content_as_bytes(file_path)
with left:
      with right:
        st.download_button(
                label="Ukrainische Zeugnis 9. Schuljahr",
                data=file_bytes,
                file_name=file_path,
                mime='application/pdf')
        
        

with left:
        left, right = st.columns(2)

# Pfad zur PDF-Datei
file_path = 'Bewerbung.pdf'

st.write("")

# Lese den Inhalt der PDF-Datei als Bytes
file_bytes = get_file_content_as_bytes(file_path)
with left:
      with left:
        st.download_button(
                label="Bewerbung",
                data=file_bytes,
                file_name=file_path,
                mime='application/pdf')
        

left, right = st.columns(2)

# Pfad zur PDF-Datei
file_path = '10.Schuljahr.pdf'

st.write("")

# Lese den Inhalt der PDF-Datei als Bytes
file_bytes = get_file_content_as_bytes(file_path)
with left:
      with right:
        st.download_button(
                label="Ukrainische Zeugnis 10. Schuljahr",
                data=file_bytes,
                file_name=file_path,
                mime='application/pdf')

