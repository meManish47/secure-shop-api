import yaml

# Vulnerability: Hardcoded password
DB_PASSWORD = "super_secret_admin_password_123"

def load_config():
    config_yaml = """
    db_host: localhost
    db_port: 5432
    """
    # Vulnerability: unsafe yaml.load
    return yaml.load(config_yaml, Loader=yaml.Loader)\n