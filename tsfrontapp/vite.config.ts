import { fileURLToPath, URL } from "node:url";
import { defineConfig } from "vite";
import vue from "@vitejs/plugin-vue";

// https://vitejs.dev/config/
export default defineConfig({
    plugins: [vue()],
    server: {
        host: "192.168.1.6",
        port: 3000,
        proxy: {
            "/api": {
                target: "http://192.168.1.6:8000",
                changeOrigin: true,
            }
        }
    },
    resolve: {
        alias: {
            "@": fileURLToPath(new URL("./src", import.meta.url)),
        },
    },
});
