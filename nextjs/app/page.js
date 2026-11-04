// Reads its settings from environment variables on the server, on every request.
// Start the app with the Corrie Config launcher so the variables come from config.corrie.io:
//   CORRIE_CONFIG_KEY=cfg_... sh launch.sh -- next start

// Render on each request, so the page shows the settings the server is running with
// instead of the values that happened to be set during next build.
export const dynamic = "force-dynamic";

export default function Home() {
  const settings = {
    apiUrl: process.env.API_URL || "",
    newCheckout: process.env.FEATURE_NEW_CHECKOUT === "true",
    dbHost: process.env.DB_HOST || "",
    dbPool: Number(process.env.DB_POOL || 5),
  };
  return (
    <main>
      <h1>Settings</h1>
      <pre id="settings">{JSON.stringify(settings, null, 2)}</pre>
    </main>
  );
}
