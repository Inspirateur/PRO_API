-- user vars
CREATE TABLE IF NOT EXISTS Var (
    name text PRIMARY KEY ON CONFLICT REPLACE,
    value numeric,
    date text,
    days integer
);