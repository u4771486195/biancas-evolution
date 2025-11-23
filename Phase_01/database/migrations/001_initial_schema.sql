-- Phase 1 Schema

CREATE TYPE user_role AS ENUM ('owner', 'customer', 'worker');
CREATE TYPE job_status AS ENUM ('pending', 'scheduled', 'completed', 'cancelled');

CREATE TABLE users (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    email VARCHAR(255) UNIQUE NOT NULL,
    phone_number VARCHAR(50),
    role user_role NOT NULL DEFAULT 'customer',
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

CREATE TABLE jobs (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    customer_id UUID NOT NULL REFERENCES users(id),
    worker_id UUID REFERENCES users(id), -- Nullable for now (CEO picks it up)
    
    -- Location Data (Will evolve into PostGIS later)
    address_line_1 TEXT NOT NULL,
    city VARCHAR(100) NOT NULL DEFAULT 'Stockholm',
    
    -- Scheduling
    scheduled_time TIMESTAMP WITH TIME ZONE NOT NULL,
    estimated_duration_minutes INT DEFAULT 120,
    
    status job_status DEFAULT 'pending',
    price_amount DECIMAL(10, 2), -- Storing price directly for MVP
    price_currency VARCHAR(3) DEFAULT 'SEK',
    
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

-- Simple index for the CEO's dashboard
CREATE INDEX idx_jobs_scheduled_time ON jobs(scheduled_time);
