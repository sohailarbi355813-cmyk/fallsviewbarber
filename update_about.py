import re

with open('about-us.html', 'r', encoding='utf-8') as f:
    content = f.read()

about_body = """
<!-- About Header -->
<section class="pt-40 pb-20 px-6 md:px-12 max-w-7xl mx-auto text-center">
  <span class="block font-sans text-xs font-semibold tracking-[0.3em] uppercase text-amber-700 mb-6">Who We Are</span>
  <h1 class="font-serif text-5xl md:text-6xl text-stone-100 mb-8">The INdustry <em class="italic text-amber-700">Standard.</em></h1>
  <p class="text-stone-400 max-w-2xl mx-auto font-light leading-relaxed">
    Opened in 2016 by award-winning stylists David and Marilyn, INdustry CUTS was built on a simple vision: to elevate men's grooming and mentor the next generation of top-tier barbers.
  </p>
</section>

<!-- Founders -->
<section class="py-20 bg-zinc-800/20 border-y border-white/5">
  <div class="px-6 md:px-12 max-w-7xl mx-auto">
    <div class="grid grid-cols-1 md:grid-cols-2 gap-16 md:gap-24">
      
      <!-- David -->
      <div class="flex flex-col md:flex-row gap-8 items-start">
        <img src="images/about-interior.jpg" alt="David" class="w-full md:w-48 h-64 object-cover rounded-md border border-white/10" />
        <div>
          <span class="block font-sans text-[0.6rem] uppercase tracking-widest text-amber-700 mb-2">Master Colourist</span>
          <h3 class="font-serif text-3xl text-stone-100 mb-4">David</h3>
          <p class="text-stone-400 text-sm leading-relaxed font-light mb-6">
            Recognized globally as one of Canada's master colourists. Most recently awarded Gold for Master Colourist of the Year at the 2025 Contessa Awards.
          </p>
          <ul class="text-xs text-stone-500 space-y-2">
            <li>🥇 2025 Contessa Gold</li>
            <li>🥇 2024 IBI Awards</li>
          </ul>
        </div>
      </div>

      <!-- Marilyn -->
      <div class="flex flex-col md:flex-row gap-8 items-start">
        <img src="images/hero-bg.jpg" alt="Marilyn" class="w-full md:w-48 h-64 object-cover rounded-md border border-white/10" />
        <div>
          <span class="block font-sans text-[0.6rem] uppercase tracking-widest text-amber-700 mb-2">Men's Specialist</span>
          <h3 class="font-serif text-3xl text-stone-100 mb-4">Marilyn</h3>
          <p class="text-stone-400 text-sm leading-relaxed font-light mb-6">
            An international award-winning stylist specializing in precision men's cutting and styling. A dedicated educator and mentor to the region's finest emerging talent.
          </p>
          <ul class="text-xs text-stone-500 space-y-2">
            <li>🥇 2024 Contessa Gold</li>
            <li>🥇 2023 KAO Colour Zoom Gold</li>
          </ul>
        </div>
      </div>

    </div>
  </div>
</section>

<!-- The Crew -->
<section class="py-20 px-6 md:px-12 max-w-7xl mx-auto text-center">
  <h2 class="font-serif text-4xl text-stone-100 mb-16">The Crew</h2>
  <div class="grid grid-cols-2 md:grid-cols-4 gap-8">
    <div class="text-center">
      <img src="images/hero-bg.jpg" alt="Ashlynn" class="w-full h-72 object-cover rounded-md border border-white/10 mb-4" />
      <h4 class="font-serif text-xl text-stone-200">Ashlynn</h4>
      <span class="font-sans text-[0.6rem] uppercase tracking-widest text-stone-500">Senior Stylist</span>
    </div>
    <div class="text-center">
      <img src="images/about-interior.jpg" alt="Veronica" class="w-full h-72 object-cover rounded-md border border-white/10 mb-4" />
      <h4 class="font-serif text-xl text-stone-200">Veronica</h4>
      <span class="font-sans text-[0.6rem] uppercase tracking-widest text-stone-500">Colour Specialist</span>
    </div>
    <div class="text-center">
      <img src="images/hero-bg.jpg" alt="Marissa" class="w-full h-72 object-cover rounded-md border border-white/10 mb-4" />
      <h4 class="font-serif text-xl text-stone-200">Marissa</h4>
      <span class="font-sans text-[0.6rem] uppercase tracking-widest text-stone-500">Men's Specialist</span>
    </div>
    <div class="text-center">
      <img src="images/about-interior.jpg" alt="Taylor" class="w-full h-72 object-cover rounded-md border border-white/10 mb-4" />
      <h4 class="font-serif text-xl text-stone-200">Taylor</h4>
      <span class="font-sans text-[0.6rem] uppercase tracking-widest text-stone-500">Stylist</span>
    </div>
  </div>
  
  <div class="mt-20">
    <a href="contact.html" class="btn-primary">Book an Appointment</a>
  </div>
</section>
"""

content = re.sub(r'</nav>.*?<footer', '</nav>\n' + about_body + '\n<footer', content, flags=re.DOTALL)

with open('about-us.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Updated about-us.html")
