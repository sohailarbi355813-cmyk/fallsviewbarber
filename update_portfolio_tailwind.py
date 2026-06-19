import re

with open('portfolio.html', 'r', encoding='utf-8') as f:
    content = f.read()

portfolio_body = """
<!-- Header -->
<section class="pt-40 pb-12 px-6 md:px-12 max-w-7xl mx-auto text-center">
  <span class="block font-sans text-xs font-semibold tracking-[0.3em] uppercase text-amber-700 mb-6">Our Work</span>
  <h1 class="font-serif text-5xl md:text-6xl text-stone-100 mb-8">The <em class="italic text-amber-700">Gallery.</em></h1>
  <p class="text-stone-400 max-w-2xl mx-auto font-light leading-relaxed">
    A curated selection of our recent cuts, fades, and styles. Real clients, real results.
  </p>
</section>

<!-- Portfolio Grid -->
<section class="py-12 px-6 md:px-12 max-w-7xl mx-auto min-h-screen">
  <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
    
    <!-- Item 1 (Featured) -->
    <div class="group relative rounded-lg overflow-hidden border border-white/10 aspect-[3/4] md:col-span-2 md:aspect-auto md:h-[600px]">
      <img src="images/portfolio/client-2.png" alt="Textured Fringe Fade" class="w-full h-full object-cover transition-transform duration-700 group-hover:scale-105" />
      <div class="absolute inset-0 bg-gradient-to-t from-zinc-900 via-zinc-900/20 to-transparent opacity-80 transition-opacity duration-300"></div>
      <div class="absolute bottom-0 left-0 right-0 p-8 transform translate-y-4 group-hover:translate-y-0 transition-transform duration-300">
        <h4 class="font-serif text-2xl text-stone-100 mb-1">Textured Fringe Fade</h4>
        <span class="font-sans text-[0.6rem] uppercase tracking-widest text-amber-700">Fade & Crop</span>
      </div>
    </div>

    <!-- Item 2 -->
    <div class="group relative rounded-lg overflow-hidden border border-white/10 aspect-[3/4]">
      <img src="images/portfolio/client-1.png" alt="Textured Taper" class="w-full h-full object-cover transition-transform duration-700 group-hover:scale-105" />
      <div class="absolute inset-0 bg-gradient-to-t from-zinc-900 via-zinc-900/20 to-transparent opacity-80 transition-opacity duration-300"></div>
      <div class="absolute bottom-0 left-0 right-0 p-6 transform translate-y-4 group-hover:translate-y-0 transition-transform duration-300">
        <h4 class="font-serif text-xl text-stone-100 mb-1">Textured Taper</h4>
        <span class="font-sans text-[0.6rem] uppercase tracking-widest text-amber-700">Precision Fade</span>
      </div>
    </div>

    <!-- Item 3 -->
    <div class="group relative rounded-lg overflow-hidden border border-white/10 aspect-[3/4]">
      <img src="images/portfolio/client-3.png" alt="Classic Taper Flow" class="w-full h-full object-cover transition-transform duration-700 group-hover:scale-105" />
      <div class="absolute inset-0 bg-gradient-to-t from-zinc-900 via-zinc-900/20 to-transparent opacity-80 transition-opacity duration-300"></div>
      <div class="absolute bottom-0 left-0 right-0 p-6 transform translate-y-4 group-hover:translate-y-0 transition-transform duration-300">
        <h4 class="font-serif text-xl text-stone-100 mb-1">Classic Taper Flow</h4>
        <span class="font-sans text-[0.6rem] uppercase tracking-widest text-amber-700">Classic Cut</span>
      </div>
    </div>

    <!-- Item 4 -->
    <div class="group relative rounded-lg overflow-hidden border border-white/10 aspect-[3/4]">
      <img src="images/portfolio/client-4.png" alt="Modern Textured Mullet" class="w-full h-full object-cover transition-transform duration-700 group-hover:scale-105" />
      <div class="absolute inset-0 bg-gradient-to-t from-zinc-900 via-zinc-900/20 to-transparent opacity-80 transition-opacity duration-300"></div>
      <div class="absolute bottom-0 left-0 right-0 p-6 transform translate-y-4 group-hover:translate-y-0 transition-transform duration-300">
        <h4 class="font-serif text-xl text-stone-100 mb-1">Modern Textured Mullet</h4>
        <span class="font-sans text-[0.6rem] uppercase tracking-widest text-amber-700">Textured Cut</span>
      </div>
    </div>

    <!-- Item 5 -->
    <div class="group relative rounded-lg overflow-hidden border border-white/10 aspect-[3/4]">
      <img src="images/portfolio/p1.png" alt="Precision Skin Fade" class="w-full h-full object-cover transition-transform duration-700 group-hover:scale-105" />
      <div class="absolute inset-0 bg-gradient-to-t from-zinc-900 via-zinc-900/20 to-transparent opacity-80 transition-opacity duration-300"></div>
      <div class="absolute bottom-0 left-0 right-0 p-6 transform translate-y-4 group-hover:translate-y-0 transition-transform duration-300">
        <h4 class="font-serif text-xl text-stone-100 mb-1">Precision Skin Fade</h4>
        <span class="font-sans text-[0.6rem] uppercase tracking-widest text-amber-700">Skin Fade</span>
      </div>
    </div>

    <!-- Item 6 -->
    <div class="group relative rounded-lg overflow-hidden border border-white/10 aspect-[3/4]">
      <img src="images/portfolio/p2.png" alt="Sharp Shears Work" class="w-full h-full object-cover transition-transform duration-700 group-hover:scale-105" />
      <div class="absolute inset-0 bg-gradient-to-t from-zinc-900 via-zinc-900/20 to-transparent opacity-80 transition-opacity duration-300"></div>
      <div class="absolute bottom-0 left-0 right-0 p-6 transform translate-y-4 group-hover:translate-y-0 transition-transform duration-300">
        <h4 class="font-serif text-xl text-stone-100 mb-1">Sharp Shears Work</h4>
        <span class="font-sans text-[0.6rem] uppercase tracking-widest text-amber-700">Classic Scissors</span>
      </div>
    </div>

  </div>
  
  <div class="mt-20 text-center">
    <a href="contact.html" class="btn-primary">Book Your Look</a>
  </div>
</section>
"""

content = re.sub(r'</nav>.*?<footer', '</nav>\n' + portfolio_body + '\n<footer', content, flags=re.DOTALL)

with open('portfolio.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Updated portfolio.html")
