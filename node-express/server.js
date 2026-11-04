// Minimal Express app that reads its settings from environment variables.
// Start it with the Corrie Config launcher so the variables come from config.corrie.io:
//   CORRIE_CONFIG_KEY=cfg_... sh launch.sh -- node server.js
const express = require("express");

const settings = {
  apiUrl: process.env.API_URL || "",
  newCheckout: process.env.FEATURE_NEW_CHECKOUT === "true",
  dbHost: process.env.DB_HOST || "",
  dbPool: Number(process.env.DB_POOL || 5),
};

const app = express();

app.get("/", (req, res) => {
  res.json({ ok: true, settings });
});

const port = Number(process.env.PORT || 3000);
app.listen(port, () => {
  console.log(`listening on ${port}, API_URL=${settings.apiUrl}, DB_HOST=${settings.dbHost}`);
});
