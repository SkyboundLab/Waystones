import os

# Function to generate the properties file content
def generate_properties_content(filename):
    base_name = os.path.splitext(filename)[0]
    properties_content = (
        f"type=item\n"
        f"matchItems=minecraft:ender_pearl\n"
        f"texture=./{filename}\n"
        f"components.minecraft\\:custom_name=ipattern:*{base_name.replace('_', ' ')}*"
    )
    return properties_content

# Function to create .properties files for all .png files in the folder
def create_properties_files(folder_path):
    if not os.path.exists(folder_path):
        print(f"The folder {folder_path} does not exist.")
        return

    for file in os.listdir(folder_path):
        if file.endswith(".png"):
            base_name = os.path.splitext(file)[0]
            properties_filename = os.path.join(folder_path, f"{base_name}.properties")
            properties_content = generate_properties_content(file)

            with open(properties_filename, 'w') as properties_file:
                properties_file.write(properties_content)

            print(f"Created: {properties_filename}")

# Specify the folder containing the .png files
folder_path = "../assets/minecraft/optifine/cit/farms"  # Replace with your folder path

# Create the .properties files
create_properties_files(folder_path)
