class SettingsController < ApplicationController
  def show
    example = Rails.configuration.x.example
    render json: {
      api_url: example.api_url,
      new_checkout: example.new_checkout,
      db_host: example.db_host,
      db_pool: example.db_pool
    }
  end
end
