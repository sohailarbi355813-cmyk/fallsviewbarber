import re

with open('hair-cutting.html', 'r', encoding='utf-8') as f:
    content = f.read()

body_replacement = """
<!-- Header -->
<section class="pt-40 pb-20 px-6 md:px-12 max-w-7xl mx-auto text-center">
  <span class="block font-sans text-xs font-semibold tracking-[0.3em] uppercase text-amber-700 mb-6">Services</span>
  <h1 class="font-serif text-5xl md:text-6xl text-stone-100 mb-8">Men's <em class="italic text-amber-700">Cuts.</em></h1>
  <p class="text-stone-400 max-w-2xl mx-auto font-light leading-relaxed">
    Award-winning stylists. Precision barbering. We deliver cuts that suit your head shape, hair texture, and lifestyle.
  </p>
</section>

<!-- Image + Intro -->
<section class="py-20 bg-zinc-800/20 border-y border-white/5">
  <div class="px-6 md:px-12 max-w-7xl mx-auto grid grid-cols-1 md:grid-cols-2 gap-16 items-center">
    <img src="images/sections/mens-cut.png" alt="Men's Haircut" class="w-full h-96 object-cover rounded-lg border border-white/10" />
    <div>
      <span class="block font-sans text-[0.6rem] uppercase tracking-widest text-amber-700 mb-4">Precision</span>
      <h2 class="font-serif text-4xl text-stone-100 mb-6">Every cut, a masterpiece.</h2>
      <p class="text-stone-400 font-light leading-relaxed mb-8">
        Whether you're coming in for a sharp fade, a textured crop, or a clean classic cut, every client receives the same level of care and attention to detail that has earned us international recognition.
      </p>
      <a href="contact.html" class="btn-primary">Book Your Cut</a>
    </div>
  </div>
</section>

<!-- Pricing -->
<section class="py-32 px-6 md:px-12 max-w-7xl mx-auto">
  <div class="text-center mb-16">
    <h2 class="font-serif text-4xl text-stone-100">Service Menu</h2>
    <p class="text-stone-500 text-sm mt-4">Starting prices.</p>
  </div>
  
  <div class="grid grid-cols-1 md:grid-cols-3 gap-6">
    <!-- Card 1 -->
    <div class="bg-zinc-800/30 border border-white/5 rounded-lg p-8 relative overflow-hidden">
      <div class="absolute top-0 left-0 right-0 h-1 bg-amber-700"></div>
      <h3 class="font-serif text-2xl text-stone-200 mb-2">Men's Haircut</h3>
      <p class="text-stone-400 text-sm font-light mb-8">Classic fades, tapers, textured crops, and modern styles tailored to you.</p>
      <div class="flex items-baseline gap-2 mb-8">
        <span class="text-amber-700 font-serif text-4xl">$45</span>
      </div>
      <a href="contact.html" class="block w-full text-center border border-white/10 hover:border-amber-700 text-stone-300 hover:text-amber-700 uppercase tracking-widest text-[0.65rem] py-3 rounded transition-colors">Book Now</a>
    </div>
    
    <!-- Card 2 -->
    <div class="bg-zinc-800/30 border border-white/5 rounded-lg p-8">
      <h3 class="font-serif text-2xl text-stone-200 mb-2">Boys' Haircut</h3>
      <p class="text-stone-400 text-sm font-light mb-8">Kid-friendly approach that delivers practical, stylish cuts (12 & under).</p>
      <div class="flex items-baseline gap-2 mb-8">
        <span class="text-amber-700 font-serif text-4xl">25%</span>
        <span class="text-stone-500 text-sm">Discount</span>
      </div>
      <a href="contact.html" class="block w-full text-center border border-white/10 hover:border-amber-700 text-stone-300 hover:text-amber-700 uppercase tracking-widest text-[0.65rem] py-3 rounded transition-colors">Book Now</a>
    </div>

    <!-- Card 3 -->
    <div class="bg-zinc-800/30 border border-white/5 rounded-lg p-8">
      <h3 class="font-serif text-2xl text-stone-200 mb-2">Cut & Style</h3>
      <p class="text-stone-400 text-sm font-light mb-8">A full haircut combined with professional blow-dry styling and finishing.</p>
      <div class="flex items-baseline gap-2 mb-8">
        <span class="text-amber-700 font-serif text-4xl">$65</span>
      </div>
      <a href="contact.html" class="block w-full text-center border border-white/10 hover:border-amber-700 text-stone-300 hover:text-amber-700 uppercase tracking-widest text-[0.65rem] py-3 rounded transition-colors">Book Now</a>
    </div>
  </div>
</section>
"""

content = re.sub(r'</nav>.*?<footer', '</nav>\n' + body_replacement + '\n<footer', content, flags=re.DOTALL)

with open('hair-cutting.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Updated hair-cutting.html")
