import { defineConfig } from "vite";
import react from "@vitejs/plugin-react";

// base must match the GitHub Pages project path:
// https://topsun-bot.github.io/wm-vla-vln-vlm-survey/
export default defineConfig({
  base: "/wm-vla-vln-vlm-survey/",
  plugins: [react()],
  build: {
    chunkSizeWarningLimit: 1200,
  },
});
