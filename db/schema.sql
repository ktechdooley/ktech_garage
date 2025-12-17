PRAGMA foreign_keys = ON;

CREATE TABLE IF NOT EXISTS schema_version (
  id INTEGER PRIMARY KEY CHECK (id=1),
  version INTEGER NOT NULL,
  applied_at TEXT DEFAULT (datetime('now'))
);

CREATE TABLE IF NOT EXISTS users (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  username TEXT NOT NULL UNIQUE,
  password_hash TEXT NOT NULL,
  role TEXT NOT NULL DEFAULT 'admin',
  created_at TEXT DEFAULT (datetime('now'))
);

CREATE TABLE IF NOT EXISTS settings (
  id INTEGER PRIMARY KEY CHECK (id=1),
  business_name TEXT NOT NULL DEFAULT 'kTech Automotive',
  tagline TEXT NOT NULL DEFAULT 'Vehicle Maintenance • Alloy Wheel Refurbishment • Remapping • Detailing',
  location TEXT NOT NULL DEFAULT 'Rathvilly, Co. Carlow, Ireland',
  phone TEXT NOT NULL DEFAULT '083 158 7937',
  email TEXT NOT NULL DEFAULT 'ktechautomotive.irl@gmail.com',
  default_labour_rate REAL NOT NULL DEFAULT 0,
  default_vat_rate REAL NOT NULL DEFAULT 0
);

CREATE TABLE IF NOT EXISTS customers (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  first_name TEXT,
  last_name TEXT,
  phone TEXT,
  email TEXT,
  notes TEXT,
  status TEXT NOT NULL DEFAULT 'active',
  created_at TEXT DEFAULT (datetime('now'))
);

CREATE TABLE IF NOT EXISTS vehicles (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  customer_id INTEGER,
  registration TEXT NOT NULL,
  make TEXT,
  model TEXT,
  year INTEGER,
  engine_code TEXT,
  displacement TEXT,
  fuel TEXT,
  ecu_type TEXT,
  vin TEXT,
  status TEXT NOT NULL DEFAULT 'active',
  created_at TEXT DEFAULT (datetime('now')),
  FOREIGN KEY (customer_id) REFERENCES customers(id) ON DELETE SET NULL
);

CREATE UNIQUE INDEX IF NOT EXISTS idx_vehicles_registration ON vehicles(registration);

CREATE TABLE IF NOT EXISTS mileage_logs (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  vehicle_id INTEGER NOT NULL,
  mileage INTEGER NOT NULL,
  date_logged TEXT NOT NULL DEFAULT (date('now')),
  notes TEXT,
  FOREIGN KEY (vehicle_id) REFERENCES vehicles(id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS ecu_jobs (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  vehicle_id INTEGER,
  ecu_brand TEXT,
  ecu_family TEXT,
  package TEXT NOT NULL,
  solutions TEXT,
  read_tool TEXT,
  read_type TEXT,
  master_slave TEXT,
  transmission TEXT,
  original_file TEXT,
  modified_file TEXT,
  ecu_id_file TEXT,
  stock_bhp REAL,
  stock_nm REAL,
  modified_bhp REAL,
  modified_nm REAL,
  price REAL NOT NULL DEFAULT 0,
  notes TEXT,
  date_done TEXT NOT NULL DEFAULT (date('now')),
  status TEXT NOT NULL DEFAULT 'active',
  created_at TEXT DEFAULT (datetime('now')),
  FOREIGN KEY (vehicle_id) REFERENCES vehicles(id) ON DELETE SET NULL
);

CREATE TABLE IF NOT EXISTS sales_invoices (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  invoice_number TEXT NOT NULL UNIQUE,
  invoice_date TEXT NOT NULL DEFAULT (date('now')),
  customer_id INTEGER,
  vehicle_id INTEGER,
  mileage INTEGER,
  paid INTEGER NOT NULL DEFAULT 0,
  subtotal REAL NOT NULL DEFAULT 0,
  vat_total REAL NOT NULL DEFAULT 0,
  total REAL NOT NULL DEFAULT 0,
  status TEXT NOT NULL DEFAULT 'active',
  created_at TEXT DEFAULT (datetime('now')),
  FOREIGN KEY (customer_id) REFERENCES customers(id) ON DELETE SET NULL,
  FOREIGN KEY (vehicle_id) REFERENCES vehicles(id) ON DELETE SET NULL
);

CREATE TABLE IF NOT EXISTS sales_invoice_items (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  sales_invoice_id INTEGER NOT NULL,
  description TEXT NOT NULL,
  qty REAL NOT NULL DEFAULT 1,
  unit_price REAL NOT NULL DEFAULT 0,
  vat_rate REAL NOT NULL DEFAULT 0,
  line_subtotal REAL NOT NULL DEFAULT 0,
  line_vat REAL NOT NULL DEFAULT 0,
  line_total REAL NOT NULL DEFAULT 0,
  FOREIGN KEY (sales_invoice_id) REFERENCES sales_invoices(id) ON DELETE CASCADE
);
