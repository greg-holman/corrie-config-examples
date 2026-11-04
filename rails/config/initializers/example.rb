# Settings from Corrie Config arrive as environment variables when the app starts.
# ENV.fetch without a default stops the boot with KeyError if a setting is missing.
Rails.application.configure do
  config.x.example.api_url = ENV.fetch("API_URL")
  config.x.example.new_checkout = ENV.fetch("FEATURE_NEW_CHECKOUT", "false") == "true"
  config.x.example.db_host = ENV.fetch("DB_HOST")
  config.x.example.db_pool = Integer(ENV.fetch("DB_POOL", "5"))
end
