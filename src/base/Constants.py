from redis import Redis

class Constants:
    ZOOM = 19
    NUMBER_OF_THREADS = 50
    REDIS = Redis('152.96.56.62', 40001, password='crosswalks')
    QUEUE_FAILED = 'failed'
    QUEUE_JOBS = 'jobs'
    QUEUE_RESULTS = 'results'
    SMALL_BBOX_SIDE_LENGHT = 3000.0
    PATH_TO_CROSSWALKS = './crosswalks.json'
    SQUAREDIMAGE_PIXELPERSIDE = 50
    METER_PER_PIXEL = 0.404428571/19