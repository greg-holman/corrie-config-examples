// Minimal Go (net/http) app that reads its settings from environment variables.
//
// Build it, then start it with the Corrie Config launcher so the variables come
// from config.corrie.io:
//
//	go build -o app .
//	CORRIE_CONFIG_KEY=cfg_... sh launch.sh -- ./app
package main

import (
	"context"
	"encoding/json"
	"errors"
	"log"
	"net/http"
	"os"
	"os/signal"
	"strconv"
	"syscall"
	"time"
)

type Settings struct {
	APIURL      string `json:"api_url"`
	NewCheckout bool   `json:"new_checkout"`
	DBHost      string `json:"db_host"`
	DBPool      int    `json:"db_pool"`
}

func getenv(name, fallback string) string {
	if v, ok := os.LookupEnv(name); ok {
		return v
	}
	return fallback
}

func load() (Settings, error) {
	pool, err := strconv.Atoi(getenv("DB_POOL", "5"))
	if err != nil {
		return Settings{}, errors.New("DB_POOL must be a whole number")
	}
	return Settings{
		APIURL:      os.Getenv("API_URL"),
		NewCheckout: os.Getenv("FEATURE_NEW_CHECKOUT") == "true",
		DBHost:      os.Getenv("DB_HOST"),
		DBPool:      pool,
	}, nil
}

func main() {
	settings, err := load()
	if err != nil {
		log.Fatal(err)
	}

	mux := http.NewServeMux()
	mux.HandleFunc("GET /{$}", func(w http.ResponseWriter, r *http.Request) {
		w.Header().Set("Content-Type", "application/json")
		json.NewEncoder(w).Encode(map[string]any{"ok": true, "settings": settings})
	})

	srv := &http.Server{
		Addr:              "127.0.0.1:" + getenv("PORT", "8080"),
		Handler:           mux,
		ReadHeaderTimeout: 10 * time.Second,
	}

	// The launcher sends TERM when settings change or when it is stopped.
	// Finish requests in flight, then exit so the new settings can load.
	ctx, stop := signal.NotifyContext(context.Background(), os.Interrupt, syscall.SIGTERM)
	defer stop()
	go func() {
		<-ctx.Done()
		shutdown, cancel := context.WithTimeout(context.Background(), 5*time.Second)
		defer cancel()
		srv.Shutdown(shutdown)
	}()

	log.Printf("listening on %s", srv.Addr)
	if err := srv.ListenAndServe(); err != nil && !errors.Is(err, http.ErrServerClosed) {
		log.Fatal(err)
	}
}
