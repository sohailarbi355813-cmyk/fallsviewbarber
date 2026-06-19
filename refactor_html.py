import os
import glob
import re

html_files = glob.glob('*.html')

tailwind_head = """  <!-- Tailwind & Fonts -->
  <script src="https://cdn.tailwindcss.com"></script>
  <script>
    tailwind.config = {
      theme: {
        extend: {
          fontFamily: {
            serif: ['"Cormorant Garamond"', 'Georgia', 'serif'],
            sans: ['"Outfit"', '"Inter"', 'system-ui', 'sans-serif'],
          },
          colors: {
            stone: {
              900: '#1c1917',
              800: '#292524',
              200: '#e7e5e4',
              100: '#f5f5f4',
            },
            amber: {
              700: '#b08d57',
              800: '#927344',
            }
          }
        }
      }
    }
  </script>
  <style type="text/tailwindcss">
    @layer components {
      .btn-primary {
        @apply inline-flex items-center justify-center gap-2 px-6 py-3 rounded-lg border border-amber-700 text-amber-700 hover:bg-amber-700 hover:text-zinc-900 transition-colors duration-300 uppercase tracking-widest text-xs font-semibold;
      }
      .nav-link {
        @apply uppercase tracking-widest text-xs font-medium text-stone-400 hover:text-amber-700 transition-colors duration-200;
      }
      .section-padding {
        @apply py-20 md:py-32 px-6 md:px-12 max-w-7xl mx-auto;
      }
    }
  </style>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,300;0,400;0,500;0,600;0,700;1,400&family=Outfit:wght@300;400;500;600&display=swap" rel="stylesheet">
"""

for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Replace <link rel="stylesheet" href="css/main.css" /> with tailwind_head
    content = re.sub(r'<link rel="stylesheet" href="css/main.css" />', tailwind_head, content)
    
    # Remove the old google fonts link if it exists
    content = re.sub(r'<style>[\s\S]*?</style>', '', content) # remove internal styles
    content = re.sub(r'@import url.*?;\n', '', content)

    # Update body tag
    content = re.sub(r'<body>', '<body class="bg-zinc-900 text-stone-200 font-sans antialiased overflow-x-hidden">', content)

    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)

print(f"Injected Tailwind into {len(html_files)} files.")
