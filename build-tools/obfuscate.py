#!/usr/bin/env python3
"""
Obfuscator for Portfolio - Creates production version with protected code
Does NOT modify original files!
"""
import re
import base64
import os
from pathlib import Path

def minify_css(css_content):
    """Minify CSS"""
    # Remove comments
    css_content = re.sub(r'/\*.*?\*/', '', css_content, flags=re.DOTALL)
    # Remove extra whitespace
    css_content = re.sub(r'\s+', ' ', css_content)
    # Remove spaces around special characters
    css_content = re.sub(r'\s*([{}:;,>+~])\s*', r'\1', css_content)
    return css_content.strip()

def minify_js(js_content):
    """Minify JavaScript (basic)"""
    # Remove single-line comments
    js_content = re.sub(r'//.*?$', '', js_content, flags=re.MULTILINE)
    # Remove multi-line comments
    js_content = re.sub(r'/\*.*?\*/', '', js_content, flags=re.DOTALL)
    # Remove extra whitespace
    js_content = re.sub(r'\s+', ' ', js_content)
    # Remove spaces around operators
    js_content = re.sub(r'\s*([{}();,=+\-*/<>!&|])\s*', r'\1', js_content)
    return js_content.strip()

def obfuscate_strings(js_content):
    """Obfuscate string literals"""
    def encode_string(match):
        string = match.group(1)
        # Base64 encode
        encoded = base64.b64encode(string.encode()).decode()
        return f"atob('{encoded}')"
    
    # Only obfuscate specific strings (not all to avoid breaking)
    # Obfuscate console messages
    js_content = re.sub(r"console\.log\('([^']+)'\)", 
                       lambda m: f"console.log(atob('{base64.b64encode(m.group(1).encode()).decode()}'))", 
                       js_content)
    return js_content

def create_production_version():
    """Create obfuscated production version"""
    
    print("🔒 Creating Production Version with Code Protection...")
    print("=" * 60)
    
    # Create production directory
    prod_dir = Path("production")
    prod_dir.mkdir(exist_ok=True)
    
    # Copy media folder
    print("\n📁 Copying media folder...")
    os.system(f'xcopy /E /I /Y media "{prod_dir}/media" >nul 2>&1')
    
    # Read original files
    print("\n📖 Reading original files...")
    with open('index.html', 'r', encoding='utf-8') as f:
        html_content = f.read()
    
    with open('styles.css', 'r', encoding='utf-8') as f:
        css_content = f.read()
    
    with open('script.js', 'r', encoding='utf-8') as f:
        js_content = f.read()
    
    # Minify CSS
    print("🎨 Minifying CSS...")
    minified_css = minify_css(css_content)
    
    # Minify and obfuscate JS
    print("⚡ Minifying and obfuscating JavaScript...")
    minified_js = minify_js(js_content)
    minified_js = obfuscate_strings(minified_js)
    
    # Inline CSS and JS into HTML
    print("📦 Creating inline production HTML...")
    
    # Replace CSS link with inline style
    html_content = re.sub(
        r'<link rel="stylesheet" href="styles\.css">',
        f'<style>{minified_css}</style>',
        html_content
    )
    
    # Replace JS script with inline script
    html_content = re.sub(
        r'<script src="script\.js"></script>',
        f'<script>{minified_js}</script>',
        html_content
    )
    
    # Add anti-inspect code
    anti_inspect = """
    <script>
    // Anti-DevTools Protection
    (function(){
        const d=()=>{const e=new Date();console.log(e);console.clear();};
        setInterval(d,1000);
        document.addEventListener('contextmenu',e=>e.preventDefault());
        document.addEventListener('keydown',e=>{
            if(e.key==='F12'||(e.ctrlKey&&e.shiftKey&&e.key==='I')||(e.ctrlKey&&e.shiftKey&&e.key==='J')||(e.ctrlKey&&e.key==='U')){
                e.preventDefault();
                return false;
            }
        });
        const c=()=>{const s=window.outerWidth-window.innerWidth>160||window.outerHeight-window.innerHeight>160;if(s){document.body.innerHTML='<div style=\"display:flex;align-items:center;justify-content:center;height:100vh;background:#01000D;color:#E0FF00;font-family:monospace;font-size:24px;\">⚠️ DevTools Detected</div>';}};
        setInterval(c,500);
    })();
    </script>
    """
    
    # Add before closing body tag
    html_content = html_content.replace('</body>', f'{anti_inspect}</body>')
    
    # Minify HTML
    print("📄 Minifying HTML...")
    html_content = re.sub(r'<!--.*?-->', '', html_content, flags=re.DOTALL)
    html_content = re.sub(r'\s+', ' ', html_content)
    html_content = re.sub(r'>\s+<', '><', html_content)
    
    # Write production file
    prod_file = prod_dir / "index.html"
    with open(prod_file, 'w', encoding='utf-8') as f:
        f.write(html_content)
    
    # Create README for production
    readme_content = """# Production Version - Obfuscated

This is the production version with code protection:

## Features:
- ✅ Minified CSS (inline)
- ✅ Minified JavaScript (inline)
- ✅ Obfuscated strings
- ✅ Anti-DevTools protection
- ✅ Right-click disabled
- ✅ F12/Inspect shortcuts blocked
- ✅ DevTools detection

## Usage:
Upload the contents of this folder to your web server.

## Note:
Original files remain untouched in the parent directory.
This is a separate production build for deployment.

## File Size Reduction:
Original: ~100KB+ (separate files)
Production: Single optimized HTML file

## Security:
- Code is harder to read and copy
- DevTools access is restricted
- Strings are encoded
- All assets are protected
"""
    
    with open(prod_dir / "README.md", 'w', encoding='utf-8') as f:
        f.write(readme_content)
    
    # Calculate sizes
    original_size = os.path.getsize('index.html') + os.path.getsize('styles.css') + os.path.getsize('script.js')
    prod_size = os.path.getsize(prod_file)
    reduction = ((original_size - prod_size) / original_size) * 100
    
    print("\n" + "=" * 60)
    print("✅ Production Version Created Successfully!")
    print("=" * 60)
    print(f"\n📊 Statistics:")
    print(f"   Original Size: {original_size:,} bytes")
    print(f"   Production Size: {prod_size:,} bytes")
    print(f"   Reduction: {reduction:.1f}%")
    print(f"\n📁 Location: {prod_dir.absolute()}")
    print(f"\n🔒 Protection Features:")
    print("   ✓ Minified code")
    print("   ✓ Obfuscated strings")
    print("   ✓ Inline assets")
    print("   ✓ Anti-DevTools")
    print("   ✓ Right-click disabled")
    print("   ✓ Inspect shortcuts blocked")
    print("\n⚠️  Original files are UNCHANGED!")
    print("=" * 60)

if __name__ == "__main__":
    try:
        create_production_version()
    except Exception as e:
        print(f"\n❌ Error: {e}")
        import traceback
        traceback.print_exc()
