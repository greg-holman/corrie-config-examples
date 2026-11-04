// Minimal Spring Boot app that reads its settings from environment variables.
//
// Build the jar, then start it with the Corrie Config launcher so the variables
// come from config.corrie.io:
//
//   mvn package
//   CORRIE_CONFIG_KEY=cfg_... sh launch.sh -- java -jar target/config-example.jar

package com.example.config;

import jakarta.validation.constraints.Min;
import java.util.Map;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.boot.context.properties.ConfigurationProperties;
import org.springframework.boot.context.properties.ConfigurationPropertiesScan;
import org.springframework.validation.annotation.Validated;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

@SpringBootApplication
@ConfigurationPropertiesScan
public class ConfigExampleApplication {
    public static void main(String[] args) {
        SpringApplication.run(ConfigExampleApplication.class, args);
    }
}

// Relaxed binding maps DB_HOST and DB_POOL onto db.host and db.pool.
// A DB_POOL that isn't a whole number of at least 1 stops the app at start.
@Validated
@ConfigurationProperties(prefix = "db")
record DbSettings(String host, @Min(1) int pool) {
}

@RestController
class SettingsController {
    private final DbSettings db;
    private final String apiUrl;
    private final boolean newCheckout;

    SettingsController(DbSettings db,
                       @Value("${API_URL:}") String apiUrl,
                       @Value("${FEATURE_NEW_CHECKOUT:false}") boolean newCheckout) {
        this.db = db;
        this.apiUrl = apiUrl;
        this.newCheckout = newCheckout;
    }

    @GetMapping("/")
    Map<String, Object> index() {
        return Map.of("ok", true, "settings", Map.of(
                "api_url", apiUrl,
                "new_checkout", newCheckout,
                "db_host", db.host() == null ? "" : db.host(),
                "db_pool", db.pool()));
    }
}
