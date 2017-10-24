import xlrd, xlwt
from config import *


class OperateExcel(object):
    def __init__(self, filename=FILENAME):
        self._filename = filename


    def get_cols_num(self):
        workbook = xlrd.open_workbook(self._filename)
        sheet = workbook.sheet_by_index(2)
        return sheet.ncols()

    def read_excel(self):
        workbook = xlrd.open_workbook(self._filename)
        sheet = workbook.sheet_by_index(2)
        for row_num in range(0, sheet.nrows):
            row = sheet.row_values(row_num)
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
        workbook = xlrd.open_workbook(self._filename)
        sheet = workbook.sheet_by_index(2)
        try:
            sheet.put_cell(row_num, col_num, 1, data)
            return 1
        except:
            return None


if __name__ == '__main__':
    items = OperateExcel().read_excel()
    for item in items:
        print(item)
