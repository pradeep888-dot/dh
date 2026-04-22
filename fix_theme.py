import os
import glob
import re

def process_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Replacements
    content = content.replace("Parvam Project", "DHukandhar the revenge")
    content = content.replace("Parvam", "DHukandhar the revenge")
    content = content.replace("parvam", "dhukandhar")
    content = content.replace("PARVAM", "DHUKANDHAR")
    
    # CSS Update for layout.html
    if 'layout.html' in filepath:
        # replace the root styling
        old_root = """        :root {
            /* White & Gold Theme inspired by Amazon */
            --dhukandhar-nav: #FFFFFF;
            --dhukandhar-sub: #f3f3f3;
            --dhukandhar-accent: #FFD814;
            --dhukandhar-accent-hover: #F7CA00;
            --dhukandhar-bg: #eaeded;
            --dhukandhar-text: #0f1111;
        }"""
        new_root = """        :root {
            /* High Contrast Dark Theme */
            --dhukandhar-nav: #000000;
            --dhukandhar-sub: #111111;
            --dhukandhar-accent: #00FFCC; /* Neon Cyan */
            --dhukandhar-accent-hover: #00D1A3;
            --dhukandhar-bg: #0a0a0a;
            --dhukandhar-text: #FFFFFF;
            --text-muted: #888888;
        }
        
        /* Interactive Animations */
        @keyframes fadeIn { from { opacity: 0; transform: translateY(10px); } to { opacity: 1; transform: translateY(0); } }
        body { background-color: var(--dhukandhar-bg); font-family: 'Inter', sans-serif; padding-top: 110px; color: var(--dhukandhar-text); animation: fadeIn 0.4s ease-out; }
        .card { transition: transform 0.2s, box-shadow 0.2s; background-color: #1A1A1A; color: white; border: 1px solid #333; }
        .card:hover { transform: translateY(-4px); box-shadow: 0 8px 24px rgba(0, 255, 204, 0.15); }
        .card-header { background-color: #222 !important; color: var(--dhukandhar-text); border-bottom: 1px solid #333; }
        .btn-dhukandhar { background: linear-gradient(90deg, #00FFCC, #00BFFF); color: black !important; font-weight: 600; text-transform: uppercase; letter-spacing: 0.5px; border-radius: 20px; transition: all 0.3s ease; border: none; }
        .btn-dhukandhar:hover { transform: scale(1.05); background: linear-gradient(90deg, #00BFFF, #00FFCC); box-shadow: 0 0 15px rgba(0, 255, 204, 0.4); }
        .nav-link-custom { transition: all 0.3s; }
        .nav-link-custom:hover { background-color: #222; border-color: #444; color: var(--dhukandhar-accent) !important; transform: translateY(-2px); }
        .navbar-main { border-bottom: 1px solid #333; }
        .navbar-sub { border-bottom: 1px solid #222; }
        .search-bar-group { border: 2px solid #333; box-shadow: none; transition: all 0.3s; }
        .search-bar-group:focus-within { border-color: var(--dhukandhar-accent); box-shadow: 0 0 10px rgba(0,255,204,0.3); }
        .search-bar-group select, .search-bar-group input { background-color: #222 !important; color: white !important; }
        .search-bar-group select { border-right: 1px solid #444; }
        .search-bar-group button { background: var(--dhukandhar-accent); }
        .text-dhukandhar-dark { color: var(--dhukandhar-text) !important; }
        .alert { background-color: #222; border-color: var(--dhukandhar-accent); color: white; }
        input.form-control, textarea.form-control { background-color: #222 !important; color: white !important; border: 1px solid #444 !important; }
        input.form-control:focus { box-shadow: 0 0 0 0.2rem rgba(0,255,204,0.25); border-color: var(--dhukandhar-accent) !important; color: white !important;}
        .form-select { background-color: #222 !important; color: white !important; border: 1px solid #444 !important; }
        .cart-badge { background-color: var(--dhukandhar-accent); color: black !important; font-weight: bold; }
        /* Fix links and muted text */
        .text-muted { color: var(--text-muted) !important; }
        a { color: var(--dhukandhar-accent); text-decoration: none; transition: 0.2s; }
        a:hover { color: #FFFFFF; text-shadow: 0 0 8px var(--dhukandhar-accent); }
        
        """
        
        # We need to find the old styles and replace them
        # First let's remove the old root block and replace it with the new styling.
        # Since I did the .replace("parvam", "dhukandhar") first, the root block inside content already has `--dhukandhar-nav`
        content = content.replace(old_root, new_root)
        
        # fix brand color
        content = content.replace('style="color: #FF9900;"', 'style="color: var(--dhukandhar-accent);"')
        # fix cart badge color
        content = content.replace('background-color: #FF9900;', 'background-color: var(--dhukandhar-accent);')

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

for filepath in glob.glob('c:/Users/City College/Desktop/shoppingcart/**/*.html', recursive=True):
    process_file(filepath)

process_file('c:/Users/City College/Desktop/shoppingcart/app.py')

print("Update completed.")
