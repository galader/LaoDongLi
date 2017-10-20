import random
import re
import urllib
import requests

import excel
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
    items = excel.ReadExcel().read_excel()
    for item in items:
        token_str = 'org.apache.struts.taglib.html.TOKEN={0}&reqCode=save'.format(token[0])
        post_data = '&dto(columncomment)=@~@~@~@~@~@~所属村（社区）@~@~@~@~公民身份号码@~@~姓名@~@~性别@~出生日期@~民族@~@~@~文化程度@~婚姻状况@~联系电话@~@~@~转移就业状况@~@~@~@~@~@~@~@~@~@~@~@~@~是否接受过职业培训@~@~@~@~@~@~@~@~是否有转移就业意愿@~@~@~@~@~@~@~@~@~@~@~@~@~&dto(oldcolumn)=@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~&dto(newcolumn)=@~@~@~@~@~@~{village}@~@~@~@~{idCardNum}@~@~{name}@~@~{gender}@~{birthday}@~汉族@~@~@~{education}@~{marital_status}@~{telephone}@~@~@~{workStatus}@~@~@~@~@~@~@~@~@~@~@~@~@~{skillTraining}@~@~@~@~@~@~@~@~{isAgree}@~@~@~@~@~@~@~@~@~@~@~@~@~&descdto(aac117)={village}&dto(aac117)={villageCode}&dto(aac002)={idCardNum}&dto(aac003)={name}&dto(aac001)=5119220123054&dto(aac004)={gender}&dto(aac006)={birthday}&dto(aac005)=汉族&label_dto(aac009)={jobType}&dto(aac009)={jobType}&dto(aac011)={education}&dto(aac017)={marital_status}&dto(aae005)={telephone}&dto(ycc451)=&dto(ycc46a)={workStatus}&descdto(ycc45j)=&dto(ycc45k)=&dto(yac01l)=&dto(ycc45c)={skillTraining}&descdto(aca111)=&dto(aca111)=&dto(aca112)=&dto(aac015)=&dto(ahc059)=&dto(yac01p)={agreeComing}&dto(ycc458)=&dto(aae013)=&dto(aae011)=胡多&label_dto(aae017)=巴中市南江县赶场镇劳动保障所&dto(aae017)=5119223799&dto(aae036)=2017-10-18&save=保存[S]&fr.improve.struts.taglib.layout.util.FormUtils.FORM_MODE_KEY=0&jsessionid=rtdbZnJQ07nvb61nLQ392jxKwpvdWKdGQ9fdDbTpLVtgs3k06y7S!1446600895!1508365328266'.format(
                village=CommonMath.get_village(item['village']), idCardNum=item['idCardNum'], name=item['name'],
                gender=CommonMath.get_gender(item['idCardNum']), birthday=CommonMath.get_birthday(item['idCardNum']),
                education=CommonMath.get_education(item['education']),
                marital_status=CommonMath.get_marital_status(CommonMath.get_marital(item['idCardNum'])),
                telephone=item['telephone'], workStatus=CommonMath.get_work_status(item['work_status']),
                skillTraining=CommonMath.get_skill_training(item['training']), isAgree=CommonMath.get_yes_or_no('否'),
                villageCode=CommonMath.get_village_code(item['village']), jobType=CommonMath.get_job_type(item['hangYe']),
                agreeComing=CommonMath.get_agree_coming_home(item['coming_home']))

        post_data_result = '{0}{1}'.format(token_str, urllib.parse.quote(post_data))
        result = session.post(POST_DATA_URL,post_data_result)
        if result.status_code == 200:
            print('插入数据成功！')
    session.close()
