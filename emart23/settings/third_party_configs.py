""" # Project Third Party Configurations # """


"""
----------------------- * Django Memcache Configurations * -----------------------
"""

SESSIONS_ENGINE = 'django.contrib.sessions.backends.cache'

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': '127.0.0.1:11211',
    }
}


"""
----------------------- * Django SafeDelete Configurations * -----------------------
"""

SAFE_DELETE_INTERPRET_UNDELETED_OBJECTS_AS_CREATED = True


"""
----------------------- * Django WhiteNoise Configurations * -----------------------
"""

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'


"""
----------------------- * Rest Framework Configuration * -----------------------
"""
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        # 'rest_framework_simplejwt.authentication.JWTAuthentication',
        'rest_framework.authentication.TokenAuthentication',
    ],
    'DEFAULT_FILTER_BACKENDS': [
        'django_filters.rest_framework.DjangoFilterBackend'
    ],
    'DATETIME_FORMAT': '%Y-%m-%d %H:%M',
    'DEFAULT_SCHEMA_CLASS': 'rest_framework.schemas.coreapi.AutoSchema',
    # 'EXCEPTION_HANDLER': 'utils.helpers.custom_exception_handler',
    # 'EXCEPTION_HANDLER': 'utils.custom_exception_handler.handle_exception',
}
