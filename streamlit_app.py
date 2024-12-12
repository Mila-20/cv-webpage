import streamlit as st

left, right = st.columns(2)
left.image("Bild.jpg", width=200)
right.header("Milana Bondar")

st.header("IT-Kompetenz", anchor=False, divider="blue") 

st.markdown("""
        - 🗺️ Webentwicklung: Fundierte Grundkenntnisse in HTML, CSS und Streamlit (Fullstack-Framework)
        - 💻 Programmierung: Praktische Erfahrung in Python, Entwicklung kleiner Anwendungen und Skripte
        - 👩🏻‍💼 Office-Suite: Versierter Umgang mit Microsoft Word, Excel und PowerPoint
        - 📊 Eigene Projekte: Konzeption und Umsetzung verschiedener Projekte inklusive Hosting
        - 🎒 Schulprojekte: Erstellung datenbasierter Präsentationen und interaktiver Tabellenkalkulationen""",)

st.header("Arbeitserfahrung", anchor=False, divider="blue") 
st.subheader("Fachmittelschule Schaumburgergasse, Wien", anchor=False)
st.markdown("""
       - ► Schwerpunkt: Intensive IT-Spezialisierung, Fokus auf modernen Webtechnologien und Wirtschaft
       - ► Zeitraum: September 2024 - Juli 2025
       - ► Derzeitiger Notenschnitt: 1,5""")

st.subheader("Mittelschule Kayniongasse, Wien", anchor=False)
st.markdown("""
      -  ► Zeitraum: September 2020 – Juli 2024
      -  ► Abschluss-Notendurchschnitt: 1,7""")
            

st.header("Schulbildung", anchor=False, divider="blue") 

st.markdown("""
        - 🛠️ Berufspraktische Tage 1: Bei XYZ von 18. bis 22. Nov. 2024
        - 🛠️ Berufspraktische Tage 2: Bei XYZ von 24. bis 28. Feb. 2025""")

st.header("Zusätzliche Qualifikationen", anchor=False, divider="blue") 
st.markdown("""
        - 💨 Schnelle Auffassungsgabe für neue Softwareanwendungen und Technologien
        - 💨 Großes Interesse an der kontinuierlichen Weiterentwicklung im IT-Bereich
        - 💨 Teamfähigkeit und Kommunikationsstärke bei gemeinsamen Coding-Projekten""")

st.header("Interessen und Hobbys", anchor=False, divider="blue") 
st.markdown("""
        - 💻 Programmieren (HTML, Streamlit, Python)
        - 🎹 Klavier spielen (Schloss die Musikschule (9 Studienjahre) mit Auszeichnung ab)
        - 🏊🏻 Schwimmen (Ich schwimme seit 6 Jahr in einer Proffigruppe)""")



