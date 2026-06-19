/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./*.html", "./js/**/*.js"],
  theme: {
    extend: {
      fontFamily: {
        serif: ['"Cormorant Garamond"', 'Georgia', 'serif'],
        sans: ['"Outfit"', '"Inter"', 'system-ui', 'sans-serif'],
      },
      colors: {
        stone: {
          900: '#1c1917', // Warm charcoal background
          800: '#292524', // Lighter charcoal for cards
          200: '#e7e5e4', // Off-white for text
          100: '#f5f5f4', // Brighter white for headings
        },
        amber: {
          700: '#b08d57', // Muted bronze/gold accent
          800: '#927344', // Darker bronze for hover states
        }
      }
    },
  },
  plugins: [],
}
