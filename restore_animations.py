import glob
import re

html_files = glob.glob('*.html')

reveal_css = """
    .reveal { opacity: 0; transform: translateY(30px); transition: all 0.8s cubic-bezier(0.5, 0, 0, 1); }
    .reveal.revealed { opacity: 1; transform: translateY(0); }
    .reveal-left { opacity: 0; transform: translateX(-30px); transition: all 0.8s cubic-bezier(0.5, 0, 0, 1); }
    .reveal-left.revealed { opacity: 1; transform: translateX(0); }
  </style>
"""

for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Add CSS rules to the style block
    content = re.sub(r'</style>', reveal_css, content)

    # 2. Add main.js to index.html if missing
    if file == 'index.html' and 'js/main.js' not in content:
        content = re.sub(r'</body>', '<script src="js/main.js"></script>\n</body>', content)

    # 3. Add reveal class to common elements
    # Be careful not to add reveal to navbar or hero elements which should load instantly
    
    # We can inject reveal class to <h2>, <h3>, <p> that are NOT in the nav or hero
    # Actually, a simpler way is to just replace specific opening tags with reveal classes
    # Only replace if they don't already have 'reveal'
    
    # It's safer to add `reveal` to all <section> elements that are not the Hero or Navbar
    content = re.sub(r'<section class="(py-[0-9]+|pt-[0-9]+|bg-zinc-800/20|section-padding)(.*?)"', r'<section class="\1\2 reveal"', content)
    
    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)

print("Restored animations across all files.")
