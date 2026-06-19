import re

pages = [
    {
        'file': 'hair-colouring.html',
        'title': 'Colour & <em class="italic text-amber-700">Texture.</em>',
        'desc': 'Expert grey blending, vibrant highlights, and full colour transformations to elevate your look.',
        'img': 'images/sections/colour.png',
        'sub': 'Transformation',
        'h2': 'Masterful Colour Work.',
        'p': 'Our Master Colourist, David, brings decades of international award-winning experience to every chair. Whether you need a subtle grey blend or a bold new look, we use premium products to ensure hair health and vibrant results.',
        'cards': [
            {'title': 'Grey Blending', 'desc': 'Subtle, natural-looking coverage that gently fades without harsh root lines.', 'price': '$40'},
            {'title': 'Highlights / Lowlights', 'desc': 'Add dimension and texture to your natural hair colour.', 'price': '$85'},
            {'title': 'Full Colour', 'desc': 'Complete, permanent colour transformations for a bold new style.', 'price': '$95'}
        ]
    },
    {
        'file': 'esthetic-services.html',
        'title': 'Beard & <em class="italic text-amber-700">Grooming.</em>',
        'desc': 'Classic hot towel shaves, precise beard shaping, and skin treatments.',
        'img': 'images/sections/beard.png',
        'sub': 'Refinement',
        'h2': 'The Ultimate Grooming Ritual.',
        'p': 'Experience traditional barbering at its finest. From straight razor shaves with hot towels and essential oils to precise beard sculpting, our grooming services are designed for ultimate relaxation and a pristine finish.',
        'cards': [
            {'title': 'Beard Trim & Shape', 'desc': 'Precision sculpting and line-up with a straight razor finish.', 'price': '$25'},
            {'title': 'Hot Towel Shave', 'desc': 'Traditional straight razor shave with hot lather and essential oils.', 'price': '$45'},
            {'title': 'Express Facial', 'desc': 'Cleansing, exfoliation, and hydration to refresh the skin.', 'price': '$35'}
        ]
    },
    {
        'file': 'celebrations.html',
        'title': 'Event <em class="italic text-amber-700">Styling.</em>',
        'desc': 'Groom packages and group bookings for your most important days.',
        'img': 'images/sections/celebrations.png',
        'sub': 'Special Occasions',
        'h2': 'Look Sharp For the Big Day.',
        'p': 'Whether it\'s your wedding day, graduation, or a major event, INdustry CUTS offers exclusive packages to ensure you and your group look flawless. Enjoy a premium experience tailored for your celebration.',
        'cards': [
            {'title': 'Groom\'s Package', 'desc': 'Haircut, beard trim/shave, styling, and a complimentary beverage.', 'price': '$90'},
            {'title': 'Groomsmen Group', 'desc': 'Private group bookings available. Contact us for group rates.', 'price': 'Call'},
            {'title': 'Event Styling', 'desc': 'Professional wash, blow-dry, and styling for a night out.', 'price': '$30'}
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
                <span class="text-amber-700 font-serif text-4xl">{card['price']}</span>
              </div>
              <a href="contact.html" class="block w-full text-center border border-white/10 hover:border-amber-700 text-stone-300 hover:text-amber-700 uppercase tracking-widest text-[0.65rem] py-3 rounded transition-colors">Book Now</a>
            </div>
            """

        body_replacement = f"""
        <!-- Header -->
        <section class="pt-40 pb-20 px-6 md:px-12 max-w-7xl mx-auto text-center">
          <span class="block font-sans text-xs font-semibold tracking-[0.3em] uppercase text-amber-700 mb-6">Services</span>
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
              <a href="contact.html" class="btn-primary">Book Your Visit</a>
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
