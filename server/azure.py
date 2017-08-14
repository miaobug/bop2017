#coding=utf8
import sys
reload(sys)
sys.setdefaultencoding('utf8')
import cognitive_face as CF

KEY = 'ed496164086047439ddbe7c54e5920a0'  # Replace with a valid Subscription Key here.
CF.Key.set(KEY)
BASE_URL = 'https://westus.api.cognitive.microsoft.com/face/v1.0/'  # Replace with your regional Base URL
CF.BaseUrl.set(BASE_URL)

#result = CF.face.detect(img_url,landmarks=True,attributes='age,gender,headPose,smile,facialHair,glasses,emotion,hair,makeup,occlusion,accessories,blur,exposure,noise');
#result = CF.person.create('1','miaorui')
#result = CF.person.add_face('http://y-doctor-oss.oss-cn-shenzhen.aliyuncs.com/match/miaorui3.jpeg','1',id_miaorui)
#result = CF.person.delete_face('1',id_panhong,'b50fd6db-d0ba-40be-820e-e71186e46084')

id = {
    '4aca3d42-d712-4cc1-9505-95843d7a328b':'王丰',
    '9cf2d44d-5980-4feb-adc1-7c6c972d4fa4':'潘虹',
    '2a0e8751-a531-499c-a37f-1c58d6fcf17b':'苗睿'
}

def get_user_info(file_name):
    try:
        data = open(file_name)
        img_result = CF.face.detect(data)[0]
        user_id = img_result.get('faceId')
        user_result = CF.face.identify([user_id],'1')[0]
        user = user_result['candidates'][0]['personId']
        return id[user]
    except Exception, e:
        return -1

if __name__ == '__main__' :
    print get_user_info('/Users/wangpei/Desktop/WechatIMG8470.jpeg')