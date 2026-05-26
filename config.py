"""
Configuration file for the Association Rule Mining System
"""
import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    """Base configuration"""
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'arm-system-secret-key-2024'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'instance', 'arm_system.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    UPLOAD_FOLDER = os.path.join(basedir, 'uploads')
    REPORTS_FOLDER = os.path.join(basedir, 'reports')
    CHARTS_FOLDER = os.path.join(basedir, 'app', 'static', 'charts')
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024  # 16MB max upload
    ALLOWED_EXTENSIONS = {'csv'}

    # Default mining parameters
    DEFAULT_MIN_SUPPORT = 0.20
    DEFAULT_MIN_CONFIDENCE = 0.50
    DEFAULT_MIN_LIFT = 1.0
