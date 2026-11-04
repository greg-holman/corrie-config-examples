<?php

use Illuminate\Support\Facades\Route;

Route::get('/', function () {
    return [
        'api_url' => config('example.api_url'),
        'new_checkout' => config('example.new_checkout'),
        'db_host' => config('database.connections.mysql.host'),
        'db_pool' => config('example.db_pool'),
    ];
});
