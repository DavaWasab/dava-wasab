#!/usr/bin/env python3
"""Rename all images in media folders by their creation date"""
import os
from pathlib import Path
from datetime import datetime

# Gallery folders
galleries = ['Model Gallery', 'PixelArt Gallery', 'Render Gallery', 'Skin Gallery']

renamed_count = 0

for gallery in galleries:
    folder_path = Path('..') / 'media' / gallery
    
    if not folder_path.exists():
        continue
    
    # Get all image files
    images = []
    for ext in ['*.png', '*.jpg', '*.jpeg', '*.gif']:
        images.extend(folder_path.glob(ext))
    
    # Sort by creation time
    images.sort(key=lambda x: os.path.getctime(x))
    
    # Rename each image
    for idx, img in enumerate(images, 1):
        # Get creation date
        creation_time = os.path.getctime(img)
        date_str = datetime.fromtimestamp(creation_time).strftime('%Y-%m-%d_%H-%M-%S')
        
        # Get extension
        ext = img.suffix
        
        # New name with index to avoid duplicates
        new_name = f"{date_str}_{idx:03d}{ext}"
        new_path = img.parent / new_name
        
        # Skip if already has this name
        if img.name != new_name:
            # Avoid overwriting
            counter = 1
            while new_path.exists():
                new_name = f"{date_str}_{idx:03d}_{counter}{ext}"
                new_path = img.parent / new_name
                counter += 1
            
            img.rename(new_path)
            print(f"Renamed: {img.name} -> {new_name}")
            renamed_count += 1

print(f"\nTotal renamed: {renamed_count} images")
