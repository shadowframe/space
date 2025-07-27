import requests
import streamlit as st

# URL of the API providing information about people in space
url = "https://corquaid.github.io/international-space-station-APIs/JSON/people-in-space.json"

# Fetch data from the API
r = requests.get(url)
data = r.json()

# Extract the number of people in space and the expedition image from the API response
people = data["number"]
expeditionImage = data["expedition_image"]

# Display the number of people currently in space
st.title(f"Es befinden sich {people} Menschen im Weltraum")

# Display information about the ISS crew members
st.markdown("### ISS Crew Members")  # Section title
st.image(expeditionImage, caption="The crew of the ISS")  # Expedition image with caption

# Function to convert a country flag code (ISO 3166-1 alpha-2) to an emoji
def get_flag_emoji(flag_code):
    try:
        # Ensure the flag_code is in uppercase
        flag_code = flag_code.upper()
        # Convert each character to a regional indicator symbol
        return ''.join(chr(127462 + ord(char) - ord('A')) for char in flag_code)
    except Exception as e:
        # Return a default white flag emoji if conversion fails
        return "🏳️"

# Function to display astronaut details based on their presence on the ISS or Tiangong
def get_astronaut_by_attribute(iss_status):
    # Filter astronauts based on their presence on the ISS or Tiangong
    astronauts = [person for person in data["people"] if person["iss"] == iss_status]
    for astronaut in astronauts:
        # Extract astronaut details
        name = astronaut["name"]
        country = astronaut["country"]
        flag_code = astronaut["flag_code"]
        image = astronaut["image"]
        # Convert the flag code to an emoji
        flag_emoji = get_flag_emoji(flag_code)
        # Display astronaut details in the Streamlit app
        st.subheader(f"{name} {flag_emoji}")  # Astronaut name with flag emoji
        st.markdown(f"Land: {country}")  # Country of the astronaut
        st.image(image, caption="Sunrise by the mountains")  # Astronaut image with caption

# Create two tabs for displaying the ISS and Tiangong crew
tab1, tab2 = st.tabs(["ISS", "Tiangong"])

# Display the ISS crew in the first tab
with tab1:
    st.title("Crew of the ISS")  # Title for the ISS crew section
    st.divider(width="stretch")  # Add a visual divider
    get_astronaut_by_attribute(iss_status=True)  # Display astronauts on the ISS

# Display the Tiangong crew in the second tab
with tab2:
    st.title("Crew of the Tiangong")  # Title for the Tiangong crew section
    st.divider(width="stretch")  # Add a visual divider
    get_astronaut_by_attribute(iss_status=False)  # Display astronauts on the Tiangong



