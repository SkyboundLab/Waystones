import os

# List of dyes in Minecraft
dyes = [
    "black", "blue", "brown", "cyan", "gray", "green", "light_blue", "light_gray", "lime", "magenta", "orange", "pink", "purple", "red", "white", "yellow"
]

# Function to generate the properties file content for a dye
def generate_dye_properties_content(dye):
    properties_content = (
        f"type=item\n"
        f"matchItems=minecraft:ender_pearl\n"
        f"texture=minecraft:item/{dye}_dye\n"
        f"components.minecraft\\:custom_name=ipattern:*{dye}*"
    )
    return properties_content

# Function to create .properties files for each dye
def create_dye_properties_files(folder_path):
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    for dye in dyes:
        properties_filename = os.path.join(folder_path, f"{dye}_dye.properties")
        properties_content = generate_dye_properties_content(dye)

        with open(properties_filename, 'w') as properties_file:
            properties_file.write(properties_content)

        print(f"Created: {properties_filename}")

# Specify the folder to save the .properties files
folder_path = "../assets/minecraft/optifine/cit/color"  # Replace with your desired folder path

# Create the .properties files
create_dye_properties_files(folder_path)
