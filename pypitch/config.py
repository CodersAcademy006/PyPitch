"""
Global configuration and debug mode for PyPitch.
"""

import os
from typing import Optional
from pathlib import Path

# Debug mode
debug = False

# Data sources
CRICSHEET_URL = os.getenv("CRICSHEET_URL", "https://cricsheet.org/downloads/ipl_json.zip")

# Database settings
DEFAULT_DATA_DIR = Path(os.getenv("PYPITCH_DATA_DIR", Path.home() / ".pypitch_data"))
DATABASE_THREADS = int(os.getenv("PYPITCH_DB_THREADS", "4"))
DATABASE_MEMORY_LIMIT = os.getenv("PYPITCH_DB_MEMORY", "2GB")

# API settings
# Default to 0.0.0.0 for container compatibility; use network controls for security
# In production, restrict access via environment overrides (PYPITCH_API_HOST) and network controls
API_HOST = os.getenv("PYPITCH_API_HOST", "0.0.0.0")  # nosec B104
API_PORT = int(os.getenv("PYPITCH_API_PORT", "8000"))

# Parse CORS origins from comma-separated string
_cors_origins = os.getenv("PYPITCH_CORS_ORIGINS", "*")
if _cors_origins:
    API_CORS_ORIGINS = [origin.strip() for origin in _cors_origins.split(",") if origin.strip()]
else:
    API_CORS_ORIGINS = []

# Cache settings
CACHE_TTL = int(os.getenv("PYPITCH_CACHE_TTL", "3600"))  # 1 hour default

# Security settings
SECRET_KEY = os.getenv("PYPITCH_SECRET_KEY", "dev-secret-key-change-in-production")
API_KEY_REQUIRED = os.getenv("PYPITCH_API_KEY_REQUIRED", "false").lower() == "true"

def validate_config():
    """Validate configuration for production readiness."""
    if SECRET_KEY == "dev-secret-key-change-in-production":
        raise ValueError(
            "PYPITCH_SECRET_KEY must be set to a secure value in production. "
            "The default development key is not secure and allows authentication bypass via forged tokens."
        )

def set_debug(value: bool = True):
    """
    Set debug mode. If True, forces eager execution and verbose errors.
    """
    global debug
    debug = value
    if debug:
        print("[PyPitch] Debug mode ON: Forcing eager execution and verbose errors.")
    else:
        print("[PyPitch] Debug mode OFF.")

def is_debug():
    return debug

def get_config():
    """Get all configuration as a dict."""
    return {
        "debug": debug,
        "cricsheet_url": CRICSHEET_URL,
        "data_dir": str(DEFAULT_DATA_DIR),
        "db_threads": DATABASE_THREADS,
        "db_memory_limit": DATABASE_MEMORY_LIMIT,
        "api_host": API_HOST,
        "api_port": API_PORT,
        "cors_origins": API_CORS_ORIGINS,
        "cache_ttl": CACHE_TTL,
        "api_key_required": API_KEY_REQUIRED,
    }
