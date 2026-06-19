import re

with open('contact.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace everything between </nav> and <footer>
contact_body = """
<!-- Contact Section -->
<section class="pt-32 pb-20 md:pt-40 md:pb-32 px-6 md:px-12 max-w-7xl mx-auto min-h-screen">
  <div class="grid grid-cols-1 md:grid-cols-2 gap-16 md:gap-24">
    
    <!-- Left: Info -->
    <div>
      <span class="block font-sans text-xs font-semibold tracking-[0.3em] uppercase text-amber-700 mb-6">Come See Us</span>
      <h1 class="font-serif text-5xl md:text-6xl text-stone-100 mb-8">Book your <br/><em class="italic text-amber-700">chair.</em></h1>
      <p class="text-stone-400 font-light leading-relaxed mb-12 max-w-sm">
        Located in St. Catharines. Walk in or reserve a time. We're ready when you are.
      </p>

      <div class="space-y-6 mb-16">
        <div>
          <span class="block font-sans text-[0.6rem] uppercase tracking-widest text-stone-500 mb-2">Location</span>
          <p class="text-stone-300">215 Pelham Rd, St. Catharines, ON</p>
        </div>
        <div>
          <span class="block font-sans text-[0.6rem] uppercase tracking-widest text-stone-500 mb-2">Contact</span>
          <p class="text-stone-300"><a href="tel:9053975888" class="hover:text-amber-700 transition-colors">(905) 397-5888</a> <br/> info@industryhair.ca</p>
        </div>
      </div>

      <div>
        <span class="block font-sans text-[0.6rem] uppercase tracking-widest text-stone-500 mb-4">Hours</span>
        <ul class="space-y-2 text-stone-400 text-sm">
          <li class="flex justify-between max-w-xs"><span>Tuesday</span> <span>9am – 6pm</span></li>
          <li class="flex justify-between max-w-xs"><span>Wednesday</span> <span>9am – 5pm</span></li>
          <li class="flex justify-between max-w-xs"><span>Thursday</span> <span>9am – 8pm</span></li>
          <li class="flex justify-between max-w-xs"><span>Friday</span> <span>9am – 5pm</span></li>
          <li class="flex justify-between max-w-xs"><span>Saturday</span> <span>8am – 2pm</span></li>
        </ul>
      </div>
    </div>

    <!-- Right: Form -->
    <div class="bg-zinc-800/30 border border-white/5 p-8 md:p-12 rounded-lg relative overflow-hidden">
      <!-- Success message (hidden by default) -->
      <div id="form-success" class="hidden absolute inset-0 bg-zinc-900/95 flex flex-col items-center justify-center p-8 text-center z-10">
        <div class="w-16 h-16 rounded-full border-2 border-amber-700 flex items-center justify-center text-amber-700 text-2xl mb-6">✓</div>
        <h3 class="font-serif text-3xl text-stone-100 mb-4">Request Sent</h3>
        <p class="text-stone-400">We'll be in touch shortly to confirm your booking.</p>
      </div>

      <form id="contact-form" action="https://formspree.io/f/placeholder" method="POST" class="space-y-6">
        <div>
          <label class="block font-sans text-[0.65rem] uppercase tracking-widest text-stone-500 mb-2" for="name">Name</label>
          <input type="text" id="name" name="name" class="w-full bg-zinc-900/50 border border-white/10 rounded px-4 py-3 text-stone-200 focus:outline-none focus:border-amber-700 transition-colors" placeholder="John Doe" required/>
        </div>
        
        <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
          <div>
            <label class="block font-sans text-[0.65rem] uppercase tracking-widest text-stone-500 mb-2" for="email">Email</label>
            <input type="email" id="email" name="email" class="w-full bg-zinc-900/50 border border-white/10 rounded px-4 py-3 text-stone-200 focus:outline-none focus:border-amber-700 transition-colors" placeholder="john@example.com" required/>
          </div>
          <div>
            <label class="block font-sans text-[0.65rem] uppercase tracking-widest text-stone-500 mb-2" for="phone">Phone</label>
            <input type="tel" id="phone" name="phone" class="w-full bg-zinc-900/50 border border-white/10 rounded px-4 py-3 text-stone-200 focus:outline-none focus:border-amber-700 transition-colors" placeholder="(905) 555-5555"/>
          </div>
        </div>

        <div>
          <label class="block font-sans text-[0.65rem] uppercase tracking-widest text-stone-500 mb-2" for="service">Service</label>
          <select id="service" name="service" class="w-full bg-zinc-900/50 border border-white/10 rounded px-4 py-3 text-stone-200 focus:outline-none focus:border-amber-700 transition-colors appearance-none" required>
            <option value="" disabled selected>Select a service...</option>
            <option value="mens-cut">Men's Haircut</option>
            <option value="beard">Beard Trim & Shape</option>
            <option value="colour">Colour & Texture</option>
            <option value="other">Other / Consultation</option>
          </select>
        </div>

        <div>
          <label class="block font-sans text-[0.65rem] uppercase tracking-widest text-stone-500 mb-2" for="message">Additional Notes</label>
          <textarea id="message" name="message" rows="4" class="w-full bg-zinc-900/50 border border-white/10 rounded px-4 py-3 text-stone-200 focus:outline-none focus:border-amber-700 transition-colors resize-none" placeholder="Any special requests?"></textarea>
        </div>

        <button type="submit" class="btn-primary w-full mt-4">Submit Request</button>
      </form>
    </div>
  </div>
</section>
"""

content = re.sub(r'</nav>.*?<footer', '</nav>\n' + contact_body + '\n<footer', content, flags=re.DOTALL)

with open('contact.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Updated contact.html")
