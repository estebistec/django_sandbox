DEBUG = True
DEPLOYMENT_MODE = 'local'

import os.path
here = lambda *x: os.path.join(os.path.abspath(os.path.dirname(__file__)), *x)

DATABASE_ENGINE = 'sqlite3'
DATABASE_NAME = here('data/django_sandbox.sqlitedb')

DEBUG_TOOLBAR_PANELS = (
    'debug_toolbar.panels.version.VersionDebugPanel',
    'debug_toolbar.panels.timer.TimerDebugPanel',
    'debug_toolbar.panels.settings_vars.SettingsVarsDebugPanel',
    'debug_toolbar.panels.headers.HeaderDebugPanel',
    'debug_toolbar.panels.request_vars.RequestVarsDebugPanel',
    'debug_toolbar.panels.template.TemplateDebugPanel',
    'debug_toolbar.panels.sql.SQLDebugPanel',
    'debug_toolbar.panels.signals.SignalDebugPanel',
    'debug_toolbar.panels.logger.LoggingPanel',
)
    
INSTALLED_APPS += ('debug_toolbar',)
MIDDLEWARE_CLASSES += ('debug_toolbar.middleware.DebugToolbarMiddleware',)

# Finally, apply any final custom, developer-specific settings
try:
    execfile("my_settings.py", globals(), locals())
except IOError:
    pass
