<?php

// Settings from Corrie Config arrive as environment variables. Read them here, in a config
// file, and use config('example.*') in the app: after `php artisan config:cache`, env()
// returns null everywhere outside the config folder.
return [
    'api_url' => env('API_URL'),
    'new_checkout' => (bool) env('FEATURE_NEW_CHECKOUT', false),
    'db_pool' => (int) env('DB_POOL', 5),
];
