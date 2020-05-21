-- Table to keep all the experiment scripts
CREATE TABLE IF NOT EXISTS scripts (
  id INTEGER PRIMARY KEY,
  namespace TEXT NOT NULL,  -- Namespace for organizing experiments
  name TEXT NOT NULL,       -- Experiment identifier
  enabled BOOLEAN NOT NULL, -- Whether experiment is active
  planout TEXT NOT NULL,    -- Original planout script
  compiled TEXT NOT NULL,   -- Compiled to JSON planout script
  UNIQUE(namespace, name)
);
