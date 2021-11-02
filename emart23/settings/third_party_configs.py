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
