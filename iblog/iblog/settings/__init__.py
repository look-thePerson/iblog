import os

settings_model = 'iblog.settings.' + os.environ.setdefault('IBLOG_PROFILE', 'dev')
