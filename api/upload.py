import tornado.web
import os

from config import BASE_DIR, IMAGE_FORMAT
from common.log_print import logger


class UploadHandle(tornado.web.RequestHandler):
    def post(self):
        files = self.request.files.get('img', None)

        res = {
            'code': 0
        }

        if not files:
            res['code'] = 1
            res['msg'] = '上传图片不能为空'
            logger.warning('[ERROR] %s' % '上传图片不能为空')
            return self.finish(res)

        if files[0]['content_type'] not in IMAGE_FORMAT:
            res['code'] = 1
            res['msg'] = '上传图片格式有误'
            logger.warning('[ERROR] %s' % '上传图片格式有误')
            return self.finish(res)

        upload_path = os.path.join(BASE_DIR, 'static/upload')
        if not os.path.exists(upload_path):
            os.mkdir(upload_path)

        for file in files:
            with open(upload_path + '/' + file['filename'], 'wb') as up:
                up.write(file['body'])
            res['msg'] = '图片上传成功'
            logger.info('[SUCCESS] %s' % '图片上传成功')

        return self.finish(res)
