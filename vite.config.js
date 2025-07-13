import { defineConfig } from "vite";
import vue from "@vitejs/plugin-vue";
import svgLoader from "vite-svg-loader";

// https://vite.dev/config/
export default defineConfig({
  plugins: [
    vue(),
    svgLoader()
  ],
  assetsInclude: ["**/*.ttf", "**/*.otf"],
  build: {
    assetsInlineLimit: 0, // Отключаем встраивание шрифтов в base64
  },
});
