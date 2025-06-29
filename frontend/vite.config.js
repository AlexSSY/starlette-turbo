import { defineConfig } from 'vite';

export default defineConfig({
  build: {
    manifest: true,
    outDir: '../src/app/static/js',
    rollupOptions: {
      input: 'src/main.js',
      output: {
        entryFileNames: '[name].[hash].js',
      },
    },
    emptyOutDir: false,
  },
});
