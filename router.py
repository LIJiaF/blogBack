from api import *

url = [
    (r"/login", LoginHandle),
    (r"/regist", RegisterHandle),
    (r"/upload", UploadHandle),
    (r"/article_class", ArticleClassHandle),
    (r"/article", ArticleHandle)
]
