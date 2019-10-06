$ brew install redis
$ brew services start redis
$ celery -A celery_example.celery worker --loglevel=info