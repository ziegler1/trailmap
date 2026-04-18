import os

class Config:
    """Base configuration."""
    DEBUG = False
    TESTING = False
    
    # Paths
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    DATA_DIR = os.path.join(BASE_DIR, 'data')
    TRAILS_DATA_FILE = os.path.join(DATA_DIR, 'ohio_trails.geojson')
    SAMPLE_DATA_FILE = os.path.join(BASE_DIR, 'static', 'ohio-trails-sample.json')
    
    # USGS API
    USGS_TRAILS_BASE = 'https://services.nationalmap.gov/arcgis/rest/services/USGSTrails/MapServer/0/query'
    USGS_TIMEOUT = 10
    OHIO_BBOX = '-84.82,38.40,-80.52,41.98'
    
    # Flask
    JSONIFY_PRETTYPRINT_REGULAR = True
    

class DevelopmentConfig(Config):
    """Development configuration."""
    DEBUG = True
    

class ProductionConfig(Config):
    """Production configuration."""
    DEBUG = False
    

class TestingConfig(Config):
    """Testing configuration."""
    TESTING = True


def get_config():
    """Get configuration based on environment."""
    env = os.getenv('FLASK_ENV', 'development')
    if env == 'production':
        return ProductionConfig
    elif env == 'testing':
        return TestingConfig
    return DevelopmentConfig
