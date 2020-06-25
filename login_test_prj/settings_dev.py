from .settings_common import *

DEBUG = True
ALLOWED_HOSTS = ['127.0.0.1']


def show_toolbar(request):
    return True
    # return False

LOGGING = {
    'version': 1,  # 1固定
    'disable_existing_loggers': False,

    # ロガーの設定
    'loggers': {
        # Djangoが利用するロガー
        'django': {
            'handlers': ['console'],
            'level': 'INFO',
        },
        # login_test_appが利用するロガー
        'login_test_app': {
            'handlers': ['console'],
            'level': 'DEBUG',
        },
    },
    # ハンドラの設定
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'dev'
        },
    },
    # フォーマッタの設定
    'formatters': {
        'dev': {
            'format': '\t'.join([
                '%(asctime)s',
                '[%(levelname)s]',
                '%(pathname)s(Line:%(lineno)d)',
                '%(message)s'
            ])
        },
    }
}

# 開発環境にメールの配信先をコンソールする設定
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# mail（本番環境）
'''
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp14.gmoserver.jp'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'ning_wen@aliber.co.jp'
EMAIL_HOST_PASSWORD = 'czT$X7BD'
EMAIL_USE_TLS = False
'''

MEDIA_ROOT = os.path.join(BASE_DIR,'media')

DEBUG_TOOLBAR_CONFIG = {
        'SHOW_TOOLBAR_CALLBACK': show_toolbar,
    }