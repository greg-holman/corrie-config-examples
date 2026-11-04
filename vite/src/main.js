// Vite replaces each import.meta.env.VITE_ name with its value when it builds,
// so the values below are fixed in the built files until the next build.
const settings = {
  VITE_API_URL: import.meta.env.VITE_API_URL,
  VITE_FEATURE_NEW_CHECKOUT: import.meta.env.VITE_FEATURE_NEW_CHECKOUT === "true",
  DB_HOST: import.meta.env.DB_HOST,
};

const list = document.getElementById("settings");
for (const [name, value] of Object.entries(settings)) {
  const item = document.createElement("li");
  item.textContent = name + " = " + value;
  list.appendChild(item);
}
