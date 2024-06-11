/** @type {import('tailwindcss').Config}*/
const config = {
  content: [
    "./src/**/*.{html,js,svelte,ts}",
    "./node_modules/flowbite-svelte/**/*.{html,js,svelte,ts}",
  ],

  theme: {
    extend: {colors: {
      grayCustom: '#7D7D7D',
      grayCustomLight: '#F4F4F4',
      grayCustomSide: '#F9F9F9',
      grayCustomDark: '#8A8A8A',
      grayCustomCard: "#ECECEC",
    },
  },
  },

  plugins: [
    require('flowbite/plugin')
  ],
  darkMode: 'class',
};

module.exports = config;
