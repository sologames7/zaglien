from PIL import Image
import os

def generate_combinations(characters_path, backgrounds_path, accessories_path, generation_path):
    # List file names in each folder
    characters = os.listdir(characters_path)
    backgrounds = os.listdir(backgrounds_path)
    accessories = os.listdir(accessories_path)
    
    # Initialize counter for unique file names
    counter = 1
    
    # Loop through each combination of character, background, and accessory
    for character in characters:
        for background in backgrounds:
            for accessory in accessories + [None]:  # Include None for cases without accessory
                # Create unique file name for the combination
                character_name = os.path.splitext(character)[0]
                background_name = os.path.splitext(background)[0]
                accessory_name = os.path.splitext(accessory)[0] if accessory is not None else "None"
                filename = f"{character_name}_{background_name}_{accessory_name}#{str(counter)}.png"
                
                # Paths to asset files
                character_path = os.path.join(characters_path, character)
                background_path = os.path.join(backgrounds_path, background)
                accessory_path = os.path.join(accessories_path, accessory) if accessory is not None else None
                
                # Load images
                character_img = Image.open(character_path).convert("RGBA")
                background_img = Image.open(background_path).convert("RGBA")
                
                # Resize character image to match background dimensions
                background_img = background_img.resize(character_img.size)
                
                # Set DPI of character image to 72 DPI
                character_img.info['dpi'] = (72, 72)
                
                # Superpose images
                img = Image.alpha_composite(background_img, character_img)
                if accessory is not None:
                    accessory_img = Image.open(accessory_path).convert("RGBA")
                    accessory_img = accessory_img.resize(character_img.size)
                    img = Image.alpha_composite(img, accessory_img)
                
                # Save image with the composed name
                img.save(os.path.join(generation_path, filename), dpi=(72, 72))
                
                # Print the combination (for testing)
                print(f"Generated {filename}: {character}, {background}, {accessory}")
                
                # Increment counter for next file name
                counter += 1

# Paths to asset folders
characters_path = 'generation-images/characters'
backgrounds_path = 'generation-images/backgrounds'
accessories_path = 'generation-images/accessories'
generation_path = 'generation-images/generation'

# Generate image combinations
generate_combinations(characters_path, backgrounds_path, accessories_path, generation_path)
