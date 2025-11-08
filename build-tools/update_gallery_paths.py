#!/usr/bin/env python3
"""Update image paths in HTML to use Skin Gallery folder"""

# Read the HTML file
with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Update all media/ paths to media/Skin Gallery/
content = content.replace('src="media/', 'src="media/Skin Gallery/')
# Fix the one we already updated
content = content.replace('src="media/Skin Gallery/Skin Gallery/', 'src="media/Skin Gallery/')

# Write back
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Updated all image paths to use Skin Gallery folder")
