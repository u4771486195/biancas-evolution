package main

import (
    "fmt"
    "log"
    "net/http"
    "os"
)

func main() {
    port := os.Getenv("PORT")
    if port == "" {
        port = "8080"
    }

    fmt.Printf("🚀 Project Bianca (Phase 1) starting on port %s...\n", port)
    
    // Simple Health Check
    http.HandleFunc("/health", func(w http.ResponseWriter, r *http.Request) {
        w.WriteHeader(http.StatusOK)
        w.Write([]byte("OK - The Village is Alive"))
    })

    log.Fatal(http.ListenAndServe(":"+port, nil))
}
