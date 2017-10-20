class CommonMath(object):
    @classmethod
    def get_gender(cls, idCardNumber):
        if len(idCardNumber) == 18:
            gender_number = int(idCardNumber[-2:-1])
            if gender_number % 2 == 0:
                return {'女': '2'}
            else:
                return {'男': '1'}

    @classmethod
    def get_birthday(cls, idCardNumber):
        if len(idCardNumber) == 18:
            birthday = idCardNumber[6:14]
            return '{0}-{1}-{2}'.format(birthday[:4], birthday[4:6], birthday[-2:])

    @classmethod
    def get_education(cls, edu):
        edu_dict = {
            '研究生及以上': '10',
            '博士研究生': '11',
            '硕士研究生': '14',
            '本科': '20',
            '专科': '30',
            '中专职校': '40',
            '中等专科': '41',
            '职业高中': '44',
            '技工学校': '47',
            '高中': '60',
            '初中及以下': '70',
            '初级中学': '71',
            '小学': '80',
            '其他': '90'
        }
        if edu in edu_dict.keys():
            return edu_dict[edu]
        return None

    @classmethod
    def get_marital_status(cls, marital_status):
        marital_status_dict = {
            '未婚': '1',
            '已婚': '2',
            '丧偶': '3',
            '离婚': '4',
            '其它': '9'
        }
        if marital_status in marital_status_dict.keys():
            return marital_status_dict[marital_status]
        return None

    @classmethod
    def get_work_status(cls, work_status):
        work_status_dict = {
            '务农': '1',
            '外出务工': '2',
            '自主创业': '3'
        }
        if work_status in work_status_dict.keys():
            return work_status_dict[work_status]
        return None

    @classmethod
    def get_work_status_way(cls, work_status_way):
        work_status_way_dict = {
            '政府组织转移': '0',
            '自发转移': '1',
            '企业组织转移': '2',
            '其他': '3'
        }
        if work_status_way in work_status_way_dict.keys():
            return work_status_way_dict[work_status_way]
        return None

    @classmethod
    def get_job_type(cls, job_type):
        job_type_dict = {
            '农林牧渔业': '01',
            '采掘业': '02',
            '制造业': '03',
            '建筑业': '05',
            '批发零售业': '08',
            '住宿和餐饮业': '09',
            '金融业': '10',
            '房地产业': '11',
            '租赁和商务服务业': '12',
            '居民服务和其它服务业': '15',
            '教育': '16',
            '公共管理和社会组织': '19',
            '国际组织': '20',
            '其他': '90'
        }
        if job_type in job_type_dict.keys():
            return job_type_dict[job_type]
        return None

    @classmethod
    def get_income(cls, income):
        if income >= 0 and income < 1000:
            return '1'
        elif income >= 1000 and income < 2000:
            return '2'
        elif income >= 2000 and income < 5000:
            return '3'
        elif income >= 5000:
            return '4'
        else:
            return '0'

    @classmethod
    def get_agree_coming_home(cls, coming_home):
        coming_home_dict = {
            '返乡务农': '1',
            '返乡务工': '2',
            '返乡创业': '3',
            '无返乡意愿': '4'
        }
        if coming_home in coming_home_dict.keys():
            return coming_home_dict[coming_home]
        return None

    @classmethod
    def get_skill_training(cls, training):
        training_dict = {
            '是': '0',
            '否': '1'
        }
        if training in training_dict.keys():
            return training_dict[training]
        return None

    @classmethod
    def get_yes_or_no(cls, v):
        if v == '是':
            return '1'
        elif v == '否':
            return '0'
        else:
            return None

    @classmethod
    def get_job_site(cls, job_site):
        job_site_dict = {
            '县内': '0',
            '市内县外': '1',
            '省外': '2',
            '省内市外': '3'
        }
        if job_site in job_site_dict.keys():
            return job_site_dict[job_site]
        return None

    @classmethod
    def get_village(cls, village):
        village_list = [
            '鹿角垭村',
            '中江村',
            '白梁村',
            '井坝村',
            '石龙村',
            '长坝村',
            '白马村',
            '梁坪村',
            '齐坪村',
            '西坝村',
            '川心村',
            '柳池村',
            '金骡村'
        ]
        if village in village_list:
            return '巴中市南江县{0}民委员会'.format(village)
        return None

    @classmethod
    def get_village_code(cls, village):
        village_dict = {
            '鹿角垭村': '5119223703',
            '中江村': '5119223704',
            '白梁村': '5119223705',
            '井坝村': '5119223706',
            '石龙村': '5119223707',
            '长坝村': '5119223708',
            '白马村': '5119223709',
            '梁坪村': '5119223710',
            '齐坪村': '5119223711',
            '西坝村': '5119223712',
            '川心村': '5119223712',
            '柳池村': '5119223714',
            '金骡村': '5119223715'
        }
        if village in village_dict.keys():
            return village_dict[village]
        return None

    @classmethod
    def get_marital(cls, idCardNum):
        if len(idCardNum) ==18:
            if 2017-int(idCardNum[6:10]) >= 25:
                return '已婚'
            return '未婚'
        return '其它'

if __name__ == '__main__':
    print(CommonMath.get_village('中江村'))
