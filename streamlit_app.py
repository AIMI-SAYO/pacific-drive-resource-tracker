import pandas as pd
import streamlit as st

# ✅ Full Crafting Data with Up to 4 Resources Fixed
data = {
    "Item Name": [
        "First Aid Kit", "Scraper", "Plasma Scraper", "Prybar", "Magnetic Hammer",
        "Hand-Vac", "Thermal Vacuum", "Flare Gun", "Relightable Flare", "Crude Flashlight",
        "Bioflare", "Bioflare Gun", "Biolantern", "Liberator", "Liberator Mk.2", "Anchor Radar",
        "Repair Putty", "Blowtorch", "Olympium Torch", "Battery Jumper", "Plasma Charger",
        "Mechanic Kit", "Sealing Kit", "Light Replacement Kit", "Electrician Kit", "Large Fuel Can",
        "Crude Door", "Steel Door", "Insulated Door", "Lead Plated Door", "Armored Door",
        "Anti Corrosive Door", "Olympium Door", "Crude Panel", "Steel Panel", "Insulated Panel",
        "Lead Plated Panel", "Armored Panel", "Anti Corrosive Panel", "Olympium Panel",
        "Crude Bumper", "Steel Bumper", "Insulated Bumper", "Lead Plated Bumper", "Armored Bumper",
        "Anti Corrosive Bumper", "Olympium Bumper", "Powered Bumper", "Spare Tire", "Summer Tire",
        "Offroad Tire", "Puncture-Proof Tire", "All-Terrain Tire", "Power Grip Tires", "Puddle Tire",
        "Crude Headlight", "Headlight", "Insulated Headlight", "Bio Headlight", "Reinforced Headlight",
        "Side Floodlights", "Roof Floodlights", "Auto Tracking Spotlight", "Side Fuel Tank",
        "Backseat Tank", "Expanded Backseat Tank", "Leak-Resistant Fuel Tank", "Gas Reservoir",
        "Gas Synthesizer", "Side Battery", "Lead-Acid Battery", "High-Capacity Battery",
        "Leak-Resistant Battery", "XL Roof Battery", "Lightning Rod", "Mini Turbine",
        "Hydro Generators", "Solar Panel", "Anchor Energy Converter", "Carbureted Engine",
        "Turbolight Engine", "AMP Engine", "LIM-Chipped Engine", "Side Storage", "XL Roof Storage",
        "LIMPulse Emitter", "The Auto Parker", "Jump Jacks", "Resource Radar", "ION Shield",
        "Juke Jet", "Nitro Boost", "LIM Shield", "The Lazarus Device", "Magnetic Bumper",
        "Anti-Grav Emitter", "Chrono Dilator", "Gear", "Bulb", "Steel Sheet", "Circuit Board",
        "Carbonfiberglass", "LIM Chip"
    ],
    "Qty 1": [4, 2, 8, 2, 6, 4, 6, 3, 2, 4, 2, 3, 4, 3, 10, 2, 2, 6, 12, 4, 8, 3, 2, 1, 1, 6, 3, 2, 6, 6, 6, 6, 8,
              4, 2, 4, 8, 4, 5, 4, 3, 4, 6, 6, 6, 8, 10, 2, 2, 2, 4, 8, 12, 18, 6, 2, 2, 3, 6, 3, 2, 5, 15, 6, 7, 8,
              2, 3, 2, 10, 8, 8, 4, 6, 1, 8, 6, 3],
    "Resource 1": [
        "Duct Tape", "Scrap Metal", "Scrap Metal", "Scrap Metal", "Scrap Metal", "Plastic", "Plastic",
        "Scrap Metal", "Scrap Metal", "Scrap Metal", "Plastic", "Scrap Metal", "Scrap Metal", "Scrap Metal",
        "Scrap Metal", "Plastic", "Scrap Metal", "Scrap Metal", "Scrap Metal", "9V Battery", "Scrap Metal",
        "Scrap Metal", "Duct Tape", "Copper Wire", "9V Battery", "Plastic", "Scrap Metal", "Scrap Metal",
        "Glass Shards", "Glass Shards", "Glass Shards", "Glass Shards", "Glass Shards", "Scrap Metal"
    ],
    "Qty 2": [4, 2, 4, 2, 2, 4, 8, 1, 1, 2, 1, 1, 6, 4, 5, 2, 2, 5, 4, 2, 10, 1, 3, 1, 2, 2, 4],
    "Resource 2": [
        "Fabric", "Plastic", "Rubber", "Plastic", "Gas Cylinder", "Rubber", "Rubber", "Pressurized Cartridges",
        "9V Battery", "9V Battery", "Copper Wire", "Pressurized Cartridges"
    ],
    "Qty 3": [1, 4, 3, 2, 2, 2, 1, 1, 1, 2, 2, 2],
    "Resource 3": [
        "Glass Shards", "Plasma", "Gear", "Pressurized Cartridges", "Electronics", "Road Flare",
        "Copper Wire", "Electronics", "Road Flare", "Bioflare", "Copper Wire",
        "Thermosap Crystal"
    ],
    "Qty 4": [0, 2, 1, 0, 2, 0, 2, 0, 1, 2, 1, 4],
    "Resource 4": [
        "", "Explosives", "LIM Magnet", "", "Electronics", "", "Tree Candy", "", "Duct Tape", "Bioflare", "Rubber", ""
    ]
}

# ✅ Ensure All Columns Have the Same Length
max_length = max(len(v) for v in data.values())
for key, values in data.items():
    while len(values) < max_length:
        values.append("" if "Resource" in key else 0)

# ✅ Create DataFrame
df = pd.DataFrame(data)
df['Original Order'] = range(len(df))  # Preserve Original Order

# ✅ Flatten and Clean Resources for Dropdown
resources = pd.concat([df['Resource 1'], df['Resource 2'], df['Resource 3'], df['Resource 4']]).dropna().unique()
resources = [res for res in resources if res.strip() != ""]

# ✅ Streamlit UI
st.set_page_config(page_title="Pacific Drive Crafting Tracker", layout="wide")
st.title("A.R.D.A Resource Tracker")

# Sidebar
st.sidebar.header("Filter Options")
show_all_items = st.sidebar.button("Show All Items")
selected_resource = st.sidebar.selectbox("Select a Resource:", resources)

if show_all_items:
    st.write("### All Crafting Items (Original Order Preserved)")
    st.table(df.sort_values(by="Original Order"))
else:
    df['Selected Resource Qty'] = df.apply(
        lambda row: sum([
            row[f'Qty {i}'] if row[f'Resource {i}'] == selected_resource else 0 for i in range(1, 5)
        ]), axis=1
    )
    filtered_df = df[df['Selected Resource Qty'] > 0].sort_values(by='Selected Resource Qty', ascending=False)
    st.write(f"### Items using **{selected_resource}** sorted by Quantity:")
    st.table(filtered_df)
