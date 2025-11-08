#!/usr/bin/env python3
"""Move Contact section before Portfolio section"""

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Find Contact section
contact_start = content.find('    <!-- Contact Section -->')
contact_end = content.find('    <!-- Footer -->')

if contact_start == -1 or contact_end == -1:
    print("Error: Could not find Contact section")
    exit(1)

# Extract Contact section
contact_section = content[contact_start:contact_end]

# Remove Contact section from original position
content_without_contact = content[:contact_start] + content[contact_end:]

# Find where to insert (before Portfolio section)
portfolio_start = content_without_contact.find('    <!-- Gallery Section -->')

if portfolio_start == -1:
    print("Error: Could not find Portfolio section")
    exit(1)

# Insert Contact section before Portfolio
new_content = content_without_contact[:portfolio_start] + contact_section + '\n' + content_without_contact[portfolio_start:]

# Write back
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(new_content)

print("Contact section moved before Portfolio")
