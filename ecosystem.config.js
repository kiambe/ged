module.exports = {
  apps: [{
    name: 'ged-django',
    script: '/root/ged/ged_env/bin/gunicorn',
    args: 'ged_backend.wsgi:application --workers 3 --bind 127.0.0.1:8000 --timeout 120',
    interpreter: 'python3',
    cwd: '/root/ged/ged_backend',
    autorestart: true,
    watch: false,
    max_memory_restart: '1G',
    env: {
      DJANGO_SETTINGS_MODULE: 'ged_backend.settings',
      PYTHONUNBUFFERED: '1',
    },
    env_production: {
      DJANGO_SETTINGS_MODULE: 'ged_backend.settings',
      PYTHONUNBUFFERED: '1',
      DEBUG: 'False',
    }
  }]
};
