import streamlit as st
import json

criteria = {"title": "Acrocanthosaurus"}

with open("pageData.json", "r", encoding="utf-8") as file:
    dinoFacts = json.load(file)
    print("Hab alle Fakten über Dinos fertig geladen")

for entry in dinoFacts:  # check that the set-like criteria items are subset of entry items:
    if criteria.items() <= entry.items():
        print(entry)
        print("Name:" + entry["title"])
        # print("Beschreibung:")
        # print(entry["extract"])
        st.title(entry["title"] + " 🦖")

        st.write(entry["extract"])
        st.markdown("Lizenz: " + entry['rightsInfo']['text'])
        st.markdown("Quelle: " + entry['fullurl'])

st.markdown("*Quelle: Wikipedia* - **really** ***cool***.")

