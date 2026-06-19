import re

pages = [
    {
        'file': 'hair-products.html',
        'title': 'Premium <em class="italic text-amber-700">Products.</em>',
        'desc': 'We stock only the highest quality grooming products to ensure your hair looks as good at home as it does leaving the chair.',
        'img': 'images/sections/products.png',
        'sub': 'Essentials',
        'h2': 'Curated for Excellence.',
        'p': 'Our shelves are stocked with industry-leading pomades, clays, and beard oils. Ask your stylist for a personalized recommendation during your visit.',
        'cards': [
            {'title': 'Matte Clay', 'desc': 'High hold, low shine. Perfect for textured crops and messy styles.', 'price': '$28'},
            {'title': 'Classic Pomade', 'desc': 'Medium hold, high shine. Ideal for classic tapers and slick backs.', 'price': '$24'},
            {'title': 'Beard Oil', 'desc': 'Nourishing oil to soften the beard and soothe the skin underneath.', 'price': '$22'}
        ]
    },
    {
        'file': 'industry-cosmetics.html',
        'title': 'INdustry <em class="italic text-amber-700">Styling.</em>',
        'desc': 'Our signature line of professional styling tools and accessories.',
        'img': 'images/hero-bg.jpg',
        'sub': 'Signature Line',
        'h2': 'Tools of the Trade.',
        'p': 'Achieve barbershop quality results at home with our custom-branded grooming tools, designed for durability and precision.',
        'cards': [
            {'title': 'Texture Comb', 'desc': 'Wide-tooth comb designed specifically for creating separation and volume.', 'price': '$15'},
            {'title': 'Boar Bristle Brush', 'desc': 'Essential for training beard hair and distributing natural oils.', 'price': '$35'},
            {'title': 'Travel Kit', 'desc': 'TSA-approved grooming essentials bundled in a premium leather washbag.', 'price': '$65'}
        ]
    }
]

for page in pages:
    try:
        with open(page['file'], 'r', encoding='utf-8') as f:
            content = f.read()

        cards_html = ""
        for i, card in enumerate(page['cards']):
            border_top = '<div class="absolute top-0 left-0 right-0 h-1 bg-amber-700"></div>' if i == 0 else ''
            cards_html += f"""
            <div class="bg-zinc-800/30 border border-white/5 rounded-lg p-8 relative overflow-hidden">
              {border_top}
              <h3 class="font-serif text-2xl text-stone-200 mb-2">{card['title']}</h3>
              <p class="text-stone-400 text-sm font-light mb-8">{card['desc']}</p>
              <div class="flex items-baseline gap-2 mb-8">
                <span class="text-amber-700 font-serif text-3xl">{card['price']}</span>
              </div>
            </div>
            """

        body_replacement = f"""
        <!-- Header -->
        <section class="pt-40 pb-20 px-6 md:px-12 max-w-7xl mx-auto text-center">
          <span class="block font-sans text-xs font-semibold tracking-[0.3em] uppercase text-amber-700 mb-6">Products</span>
          <h1 class="font-serif text-5xl md:text-6xl text-stone-100 mb-8">{page['title']}</h1>
          <p class="text-stone-400 max-w-2xl mx-auto font-light leading-relaxed">
            {page['desc']}
          </p>
        </section>

        <!-- Image + Intro -->
        <section class="py-20 bg-zinc-800/20 border-y border-white/5">
          <div class="px-6 md:px-12 max-w-7xl mx-auto grid grid-cols-1 md:grid-cols-2 gap-16 items-center">
            <img src="{page['img']}" alt="{page['sub']}" class="w-full h-96 object-cover rounded-lg border border-white/10" />
            <div>
              <span class="block font-sans text-[0.6rem] uppercase tracking-widest text-amber-700 mb-4">{page['sub']}</span>
              <h2 class="font-serif text-4xl text-stone-100 mb-6">{page['h2']}</h2>
              <p class="text-stone-400 font-light leading-relaxed mb-8">
                {page['p']}
              </p>
              <a href="contact.html" class="btn-primary">Reserve Products</a>
            </div>
          </div>
        </section>

        <!-- Product List -->
        <section class="py-32 px-6 md:px-12 max-w-7xl mx-auto">
          <div class="text-center mb-16">
            <h2 class="font-serif text-4xl text-stone-100">Featured Items</h2>
            <p class="text-stone-500 text-sm mt-4">Available in-store only.</p>
          </div>
          
          <div class="grid grid-cols-1 md:grid-cols-3 gap-6">
            {cards_html}
          </div>
        </section>
        """

        content = re.sub(r'</nav>.*?<footer', '</nav>\n' + body_replacement + '\n<footer', content, flags=re.DOTALL)

        with open(page['file'], 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f"Updated {page['file']}")
    except Exception as e:
        print(f"Error updating {page['file']}: {e}")
