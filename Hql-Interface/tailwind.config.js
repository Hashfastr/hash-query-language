/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{js,ts,jsx,tsx}",
  ],
  darkMode: 'class',
  theme: {
    extend: {
      colors: {
        gruvbox: {
          // Dark mode colors
          dark: {
            bg: '#282828',
            bg0: '#282828',
            bg1: '#3c3836',
            bg2: '#504945',
            bg3: '#665c54',
            fg: '#ebdbb2',
            fg0: '#fbf1c7',
            fg1: '#ebdbb2',
            fg2: '#d5c4a1',
            fg3: '#bdae93',
            red: '#fb4934',
            green: '#b8bb26',
            yellow: '#fabd2f',
            blue: '#83a598',
            purple: '#d3869b',
            aqua: '#8ec07c',
            orange: '#fe8019',
            gray: '#928374',
          },
          // Light mode colors
          light: {
            bg: '#fbf1c7',
            bg0: '#fbf1c7',
            bg1: '#ebdbb2',
            bg2: '#d5c4a1',
            bg3: '#bdae93',
            fg: '#3c3836',
            fg0: '#282828',
            fg1: '#3c3836',
            fg2: '#504945',
            fg3: '#665c54',
            red: '#cc241d',
            green: '#98971a',
            yellow: '#d79921',
            blue: '#458588',
            purple: '#b16286',
            aqua: '#689d6a',
            orange: '#d65d0e',
            gray: '#7c6f64',
          }
        }
      }
    },
  },
  plugins: [],
}
