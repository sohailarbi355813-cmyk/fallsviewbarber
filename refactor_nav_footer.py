import os
import glob
import re

html_files = glob.glob('*.html')

tailwind_nav = """<nav id="navbar" class="fixed top-0 left-0 right-0 z-50 bg-zinc-900/95 backdrop-blur-md border-b border-white/5 py-5 transition-all">
  <div class="max-w-7xl mx-auto px-6 md:px-12 flex items-center justify-between">
    <a href="index.html" class="font-serif text-2xl font-medium tracking-wide text-stone-100 flex flex-col">
      INdustry <span class="text-amber-700 italic inline">CUTS</span>
      <span class="font-sans text-[0.55rem] tracking-[0.3em] text-stone-500 uppercase mt-1 font-semibold">Men's Grooming</span>
    </a>
    <ul class="hidden md:flex items-center gap-8">
      <li><a href="index.html" class="nav-link">Home</a></li>
      <li><a href="about-us.html" class="nav-link">About</a></li>
      <li><a href="hair-cutting.html" class="nav-link">Services</a></li>
      <li><a href="portfolio.html" class="nav-link">Portfolio</a></li>
      <li><a href="contact.html" class="nav-link">Contact</a></li>
    </ul>
    <a href="contact.html" class="hidden md:inline-flex btn-primary">Book Now</a>
    
    <!-- Mobile Menu Button -->
    <button class="md:hidden text-stone-200 p-2">
      <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16M4 18h16"></path></svg>
    </button>
  </div>
</nav>"""

tailwind_footer = """<footer class="bg-[#12100f] border-t border-white/5 py-20 mt-20">
  <div class="max-w-7xl mx-auto px-6 md:px-12 grid grid-cols-1 md:grid-cols-4 gap-12">
    <div class="col-span-1 md:col-span-1">
      <div class="font-serif text-2xl font-medium tracking-wide text-stone-100 mb-4 flex flex-col">
        INdustry <span class="text-amber-700 italic inline">CUTS</span>
      </div>
      <p class="text-stone-400 text-sm leading-relaxed mb-6">Niagara's premier barbershop. Precision cuts, expert grooming, and an authentic experience.</p>
    </div>
    
    <div>
      <h4 class="font-sans text-[0.6rem] font-semibold tracking-[0.2em] uppercase text-amber-700 mb-6">Navigate</h4>
      <ul class="space-y-3 text-sm text-stone-400">
        <li><a href="about-us.html" class="hover:text-stone-200 transition-colors">About Us</a></li>
        <li><a href="hair-cutting.html" class="hover:text-stone-200 transition-colors">Services</a></li>
        <li><a href="portfolio.html" class="hover:text-stone-200 transition-colors">Portfolio</a></li>
        <li><a href="contact.html" class="hover:text-stone-200 transition-colors">Contact</a></li>
      </ul>
    </div>
    
    <div>
      <h4 class="font-sans text-[0.6rem] font-semibold tracking-[0.2em] uppercase text-amber-700 mb-6">Visit Us</h4>
      <ul class="space-y-3 text-sm text-stone-400">
        <li><a href="mailto:info@industryhair.ca" class="hover:text-stone-200 transition-colors">info@industryhair.ca</a></li>
        <li><a href="tel:9053975888" class="hover:text-stone-200 transition-colors">(905) 397-5888</a></li>
        <li>215 Pelham Rd, St. Catharines</li>
      </ul>
    </div>
  </div>
  <div class="max-w-7xl mx-auto px-6 md:px-12 mt-16 pt-8 border-t border-white/5 text-xs text-stone-600 flex justify-between">
    <p>© 2026 INdustry CUTS. All rights reserved.</p>
    <p>Crafted with precision.</p>
  </div>
</footer>"""

for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Replace old Nav (from <nav id="navbar"> to </nav>)
    content = re.sub(r'<nav id="navbar">.*?</nav>', tailwind_nav, content, flags=re.DOTALL)
    
    # Remove old mobile menu
    content = re.sub(r'<div class="mobile-menu">.*?</div>', '', content, flags=re.DOTALL)
    
    # Replace old Footer (from <footer> to </footer>)
    content = re.sub(r'<footer>.*?</footer>', tailwind_footer, content, flags=re.DOTALL)
    
    # Remove old custom cursor
    content = re.sub(r'<div class="cursor"></div><div class="cursor-ring"></div>', '', content)
    content = re.sub(r'<div id="scroll-progress"></div><div class="page-transition"></div>', '', content)
    content = re.sub(r'<button id="back-to-top">.*?</button>', '', content)

    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)

print("Updated Navigation and Footer in all HTML files.")
