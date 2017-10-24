import random
import re
import urllib
import requests

from operateExcel import OperateExcel
from config import *
from common import CommonMath

session = requests.session()
response = session.post(LOGIN_URL, LOGIN_DATA, headers={'User-Agent': random.choice(USER_AGENT)})
cookie = requests.utils.dict_from_cookiejar(session.cookies)
cookie['appMenu_node_1701000000'] = 1
cookies = requests.utils.cookiejar_from_dict(cookie)

if response.status_code == 200:
    response_add = session.get(
            'http://10.160.48.220:8001/lemis/farmlabor/outfarmlabor/outFarmLaborNewEdit.do?reqCode=create&businessId=1702010000',
            data=QUERY_STRING)
    html = response_add.text
    token = re.compile('<input type="hidden" name=".*?TOKEN" value="(.*?)"></div>').findall(html)
    print(token)
    items = OperateExcel().read_excel()
    for item in items:
        post_data_pre = 'org.apache.struts.taglib.html.TOKEN={0}&reqCode=save{1}'.format(token[0],POST_DATA_PRE_2)
        post_data_mid = 'dto(newcolumn)=@~@~@~@~@~@~{village}@~@~@~@~{idCardNum}@~@~{name}@~@~{gender}@~{birthday}@~汉族@~@~@~{education}@~{marital_status}@~{telephone}@~@~@~{workStatus}@~@~@~@~@~@~@~@~@~@~@~@~@~{skillTraining}@~@~@~@~@~@~@~@~{isAgree}@~@~@~@~@~@~@~@~@~@~@~@~@~&descdto(aac117)={village}&dto(aac117)={villageCode}&dto(aac002)={idCardNum}&dto(aac003)={name}&dto(aac001)=5119220123054&dto(aac004)={gender}&dto(aac006)={birthday}&dto(aac005)=汉族&label_dto(aac009)={jobType}&dto(aac009)={jobType}&dto(aac011)={education}&dto(aac017)={marital_status}&dto(aae005)={telephone}&dto(ycc451)=&dto(ycc46a)={workStatus}&descdto(ycc45j)=&dto(ycc45k)=&dto(yac01l)=&dto(ycc45c)={skillTraining}&descdto(aca111)=&dto(aca111)=&dto(aca112)=&dto(aac015)=&dto(ahc059)=&dto(yac01p)={agreeComing}'.format(
                village=CommonMath.get_village(item['village']), idCardNum=item['idCardNum'], name=item['name'],
                gender=CommonMath.get_gender(item['idCardNum']), birthday=CommonMath.get_birthday(item['idCardNum']),
                education=CommonMath.get_education(item['education']),
                marital_status=CommonMath.get_marital_status(CommonMath.get_marital(item['idCardNum'])),
                telephone=item['telephone'], workStatus=CommonMath.get_work_status(item['work_status']),
                skillTraining=CommonMath.get_skill_training(item['training']), isAgree=CommonMath.get_yes_or_no('否'),
                villageCode=CommonMath.get_village_code(item['village']), jobType=CommonMath.get_job_type(item['hangYe']),
                agreeComing=CommonMath.get_agree_coming_home(item['coming_home']))

        post_data = '{0}{1}{2}'.format(post_data_pre, urllib.quote(post_data_mid),POST_DATA_LAST)
        result = session.post(POST_DATA_URL,post_data)
        if result.status_code == 200:
            print('插入数据成功！')
            OperateExcel().write_excel(item['rowNum'],OperateExcel().get_cols_num(),'插入数据成功！')
    session.close()
