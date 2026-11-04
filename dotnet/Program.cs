// Minimal ASP.NET Core app that reads its settings from environment variables.
//
// Publish it, then start it with the Corrie Config launcher so the variables
// come from config.corrie.io:
//
//   dotnet publish -c Release -o out
//   CORRIE_CONFIG_KEY=cfg_... sh launch.sh -- dotnet out/ConfigExample.dll

var builder = WebApplication.CreateBuilder(args);

// WebApplication already reads environment variables into builder.Configuration,
// and they win over appsettings.json. A double underscore in a name is .NET's
// section separator, so a setting saved as Cache__Ttl is read as Cache:Ttl.
var config = builder.Configuration;

if (!int.TryParse(config["DB_POOL"] ?? "5", out var dbPool))
{
    Console.Error.WriteLine("DB_POOL must be a whole number");
    return 1;
}

var settings = new
{
    api_url = config["API_URL"] ?? "",
    new_checkout = config["FEATURE_NEW_CHECKOUT"] == "true",
    db_host = config["DB_HOST"] ?? "",
    db_pool = dbPool,
    cache_ttl = config.GetSection("Cache")["Ttl"] ?? "",
};

builder.WebHost.UseUrls("http://127.0.0.1:" + (config["PORT"] ?? "8080"));

var app = builder.Build();

app.MapGet("/", () => Results.Json(new { ok = true, settings }));

// The launcher sends TERM when settings change or when it is stopped.
// ASP.NET Core finishes requests in flight, then exits so the new settings can load.
app.Run();
return 0;
