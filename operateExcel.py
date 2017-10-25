import xlrd, xlwt
from config import *


class OperateExcel(object):
    def __init__(self, filename=FILENAME):
        # 参数formatting_info=True，得以保存之前数据的格式
        self._sheet = xlrd.open_workbook(filename, formatting_info=True).sheet_by_index(2)

    def get_cols_num(self):
        return self._sheet.ncols

    def read_excel(self):
        for row_num in range(0, self._sheet.nrows):
            row = self._sheet.row_values(row_num)
            # print(row)
            item = {
                'village': row[1],
                'name': row[2],
                'idCardNum': row[4],
                'telephone': row[7],
                'education': row[8],
                'work_status': row[13],
                'hangYe': row[15],
                'addr': row[16],
                'coming_home': row[18],
                'training': row[19],
                'rowNum': row_num
            }
            yield item

    def write_excel(self, row_num, col_num, data):
        try:
            self._sheet.put_cell(row_num, col_num, 1, data)
            return 1
        except:
            return None


if __name__ == '__main__':
    items = OperateExcel().read_excel()
    for item in items:
        print(item)
