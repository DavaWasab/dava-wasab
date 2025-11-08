#!/usr/bin/env python3
"""
Advanced Obfuscator - Maximum Protection
Creates heavily obfuscated production version
"""
import re
import base64
import random
import string
import os
from pathlib import Path

class AdvancedObfuscator:
    def __init__(self):
        self.var_map = {}
        self.counter = 0
    
    def generate_random_name(self):
        """Generate random variable name"""
        chars = string.ascii_letters
        return '_' + ''.join(random.choices(chars, k=8))
    
    def obfuscate_variable_names(self, js_content):
        """Obfuscate variable names"""
        # Find function declarations
        functions = re.findall(r'function\s+(\w+)\s*\(', js_content)
        for func in functions:
            if func not in ['DOMContentLoaded', 'addEventListener']:
                new_name = self.generate_random_name()
                self.var_map[func] = new_name
                js_content = re.sub(rf'\b{func}\b', new_name, js_content)
        
        # Find const/let/var declarations
        variables = re.findall(r'(?:const|let|var)\s+(\w+)\s*=', js_content)
        for var in variables:
            if var not in self.var_map and len(var) > 2:
                new_name = self.generate_random_name()
                self.var_map[var] = new_name
                js_content = re.sub(rf'\b{var}\b', new_name, js_content)
        
        return js_content
    
    def encode_strings(self, js_content):
        """Encode all string literals"""
        def encode_match(match):
            string = match.group(1)
            # Use hex encoding
            hex_encoded = ''.join([f'\\x{ord(c):02x}' for c in string])
            return f'"{hex_encoded}"'
        
        # Encode strings in quotes
        js_content = re.sub(r'"([^"]+)"', encode_match, js_content)
        return js_content
    
    def add_dead_code(self, js_content):
        """Add fake code to confuse"""
        dead_code = [
            "const _deadVar1=Math.random()*999;",
            "const _deadVar2=Date.now()%1000;",
            "const _deadFunc=()=>{return _deadVar1+_deadVar2;};",
            "if(false){console.log('never');}",
        ]
        return '\n'.join(dead_code) + '\n' + js_content
    
    def split_strings(self, js_content):
        """Split strings to make them harder to find"""
        # Split long strings
        def split_match(match):
            string = match.group(1)
            if len(string) > 10:
                mid = len(string) // 2
                return f'"{string[:mid]}"+"{ string[mid:]}"'
            return match.group(0)
        
        js_content = re.sub(r'"([^"]{10,})"', split_match, js_content)
        return js_content

def create_advanced_production():
    """Create advanced obfuscated version"""
    
    print("🔐 Creating ADVANCED Production Version...")
    print("=" * 60)
    
    obfuscator = AdvancedObfuscator()
    
    # Create production directory
    prod_dir = Path("production_advanced")
    prod_dir.mkdir(exist_ok=True)
    
    # Copy media
    print("\n📁 Copying media folder...")
    os.system(f'xcopy /E /I /Y media "{prod_dir}/media" >nul 2>&1')
    
    # Read files
    print("\n📖 Reading files...")
    with open('index.html', 'r', encoding='utf-8') as f:
        html = f.read()
    with open('styles.css', 'r', encoding='utf-8') as f:
        css = f.read()
    with open('script.js', 'r', encoding='utf-8') as f:
        js = f.read()
    
    # Obfuscate JavaScript
    print("⚡ Obfuscating JavaScript...")
    print("   → Removing comments...")
    js = re.sub(r'//.*?$', '', js, flags=re.MULTILINE)
    js = re.sub(r'/\*.*?\*/', '', js, flags=re.DOTALL)
    
    print("   → Obfuscating variable names...")
    js = obfuscator.obfuscate_variable_names(js)
    
    print("   → Encoding strings...")
    js = obfuscator.encode_strings(js)
    
    print("   → Adding dead code...")
    js = obfuscator.add_dead_code(js)
    
    print("   → Splitting strings...")
    js = obfuscator.split_strings(js)
    
    print("   → Minifying...")
    js = re.sub(r'\s+', ' ', js)
    
    # Minify CSS
    print("🎨 Minifying CSS...")
    css = re.sub(r'/\*.*?\*/', '', css, flags=re.DOTALL)
    css = re.sub(r'\s+', ' ', css)
    css = re.sub(r'\s*([{}:;,>+~])\s*', r'\1', css)
    
    # Create protection layer
    protection = f"""
    <script>
    (function(){{
        'use strict';
        const _p1='{base64.b64encode(b"protection").decode()}';
        const _p2=()=>{{
            const _d=new Date();
            const _t=_d.getTime();
            if(_t%2===0){{console.clear();}}
        }};
        setInterval(_p2,1000);
        
        // Disable DevTools
        const _d1=()=>{{
            const _w=window.outerWidth-window.innerWidth;
            const _h=window.outerHeight-window.innerHeight;
            if(_w>160||_h>160){{
                document.body.innerHTML='<div style="display:flex;align-items:center;justify-content:center;height:100vh;background:#01000D;color:#E0FF00;font-family:monospace;font-size:20px;">⚠️ Access Denied</div>';
            }}
        }};
        setInterval(_d1,500);
        
        // Disable shortcuts
        document.addEventListener('keydown',e=>{{
            if(e.key==='F12'||
               (e.ctrlKey&&e.shiftKey&&(e.key==='I'||e.key==='J'||e.key==='C'))||
               (e.ctrlKey&&e.key==='U')){{
                e.preventDefault();
                e.stopPropagation();
                return false;
            }}
        }},true);
        
        // Disable right-click
        document.addEventListener('contextmenu',e=>{{
            e.preventDefault();
            return false;
        }},true);
        
        // Disable selection
        document.addEventListener('selectstart',e=>{{
            if(e.target.tagName==='IMG'||e.target.tagName==='CODE'){{
                e.preventDefault();
                return false;
            }}
        }});
        
        // Detect debugger
        const _dbg=()=>{{
            const _start=performance.now();
            debugger;
            const _end=performance.now();
            if(_end-_start>100){{
                window.location.href='about:blank';
            }}
        }};
        setInterval(_dbg,2000);
    }})();
    </script>
    """
    
    # Inline everything
    html = re.sub(r'<link rel="stylesheet" href="styles\.css">', f'<style>{css}</style>', html)
    html = re.sub(r'<script src="script\.js"></script>', f'<script>{js}</script>', html)
    html = html.replace('</head>', f'{protection}</head>')
    
    # Minify HTML
    print("📄 Minifying HTML...")
    html = re.sub(r'<!--.*?-->', '', html, flags=re.DOTALL)
    html = re.sub(r'\s+', ' ', html)
    html = re.sub(r'>\s+<', '><', html)
    
    # Write
    prod_file = prod_dir / "index.html"
    with open(prod_file, 'w', encoding='utf-8') as f:
        f.write(html)
    
    # Create .htaccess for additional protection
    htaccess = """# Disable directory listing
Options -Indexes

# Prevent viewing of source files
<FilesMatch "\.(py|md|txt|log)$">
    Order allow,deny
    Deny from all
</FilesMatch>

# Security headers
<IfModule mod_headers.c>
    Header set X-Content-Type-Options "nosniff"
    Header set X-Frame-Options "SAMEORIGIN"
    Header set X-XSS-Protection "1; mode=block"
    Header set Referrer-Policy "no-referrer-when-downgrade"
</IfModule>
"""
    
    with open(prod_dir / ".htaccess", 'w') as f:
        f.write(htaccess)
    
    # Stats
    original_size = os.path.getsize('index.html') + os.path.getsize('styles.css') + os.path.getsize('script.js')
    prod_size = os.path.getsize(prod_file)
    
    print("\n" + "=" * 60)
    print("✅ ADVANCED Production Created!")
    print("=" * 60)
    print(f"\n📊 Statistics:")
    print(f"   Original: {original_size:,} bytes")
    print(f"   Protected: {prod_size:,} bytes")
    print(f"   Variables obfuscated: {len(obfuscator.var_map)}")
    print(f"\n📁 Location: {prod_dir.absolute()}")
    print(f"\n🔐 Protection Layers:")
    print("   ✓ Variable name obfuscation")
    print("   ✓ String encoding (hex)")
    print("   ✓ Dead code injection")
    print("   ✓ String splitting")
    print("   ✓ DevTools detection")
    print("   ✓ Debugger detection")
    print("   ✓ All shortcuts blocked")
    print("   ✓ Right-click disabled")
    print("   ✓ Selection disabled")
    print("   ✓ .htaccess protection")
    print("\n⚠️  ORIGINAL FILES UNTOUCHED!")
    print("=" * 60)

if __name__ == "__main__":
    try:
        create_advanced_production()
    except Exception as e:
        print(f"\n❌ Error: {e}")
        import traceback
        traceback.print_exc()
