# Phase 01: The Village (0 - 100 Workers)

**Goal:** Prove the business model. The CEO performs the cleaning.
**Constraint:** 0 kr/mo costs.

## Tech Stack
- **Frontend:** Next.js (Deployed on Vercel Hobby)
- **Backend:** Go Monolith (Deployed on Fly.io Free / DigitalOcean App)
- **Database:** PostgreSQL (Supabase Free Tier)

## Architecture
At this stage, we use a **Modular Monolith**.
- We do NOT use Microservices yet.
- We do NOT use Kafka yet.
- We focus on **Data Integrity** (SQL Schemas) to prepare for the future.
