import requests
import streamlit as st

url = "https://corquaid.github.io/international-space-station-APIs/JSON/people-in-space.json"
r = requests.get(url)
data = r.json()

people = data["number"]
expeditionImage = data["expedition_image"]
st.title(f"Es befinden sich {people} Menschen im Weltraum")  # Display the number of people in space

# Informationen rund um Crewmitglieder der ISS
st.markdown("### ISS Crew Members")  # Title for the ISS crew members section
st.image(expeditionImage, caption="The crew of the ISS")  # Display the expedition image of ISS

# Function to convert flag_code to emoji
def get_flag_emoji(flag_code):
    try:
        # Ensure the flag_code is in uppercase (ISO 3166-1 alpha-2 standard)
        flag_code = flag_code.upper()
        # Convert each character to a regional indicator symbol
        return ''.join(chr(127462 + ord(char) - ord('A')) for char in flag_code)
    except Exception as e:
        return "🏳️"  # Default to a white flag if conversion fails

def get_astronaut_by_attribute(iss_status):
    astronauts = [person for person in data["people"] if person["iss"] == iss_status]
    for astronaut in astronauts:
        name = astronaut["name"]
        country = astronaut["country"]
        flag_code = astronaut["flag_code"]
        image = astronaut["image"]
        flag_emoji = get_flag_emoji(flag_code)
        st.subheader(f"{name} {flag_emoji}")
        st.markdown(f"Land: {country}")
        st.image(image, caption="Sunrise by the mountains")

# Ausgabe der ISS-Besatzung
tab1, tab2 = st.tabs(["ISS", "Tiangong"])

with tab1:
    st.title("Crew of the ISS")
    st.divider(width="stretch")
    get_astronaut_by_attribute(iss_status=True)
with tab2:
    st.title("Crew of the Tiangong")
    st.divider(width="stretch")
    get_astronaut_by_attribute(iss_status=False)

  

