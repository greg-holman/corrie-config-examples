import { defineConfig, loadEnv } from "vite";

// Settings the page can't work without. Each one must start with VITE_,
// because Vite only puts VITE_ settings into the files it builds.
const REQUIRED = ["VITE_API_URL"];

export default defineConfig(({ mode }) => {
  const env = loadEnv(mode, process.cwd(), "VITE_");
  const missing = REQUIRED.filter((name) => !env[name]);
  if (missing.length) {
    throw new Error("Missing settings: " + missing.join(", ") + ". Build with: sh launch.sh -- npx vite build");
  }
  return {};
});
