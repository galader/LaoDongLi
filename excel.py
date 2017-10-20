import xlrd, xlwt
import config


class ReadExcel(object):
    def __init__(self, filename=config.FILENAME):
        self._filename = filename

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
                'training': row[19]
            }
            yield item


if __name__ == '__main__':
    items = ReadExcel().read_excel()
    for item in items:
        print(item)
