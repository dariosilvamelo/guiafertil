import sqlite3

import constants as c


class DataBaseSaturation:

    def __init__(self, name_data_base):
        self.data_base = name_data_base

    def open_data_base(self):
        self.connection_data_base = sqlite3.connect(self.data_base)

    def close_data_base(self):
        self.connection_data_base.close()

    def query_saturation(self, culture):
        self.open_data_base()

        try:
            cursor = self.connection_data_base.cursor()
            sql = """SELECT
                        S.mt,
                        S.X,
                        S.V,
                        S.maximum_amount_limestone
                        FROM saturation_mt_X_V S
                        WHERE
                        S.culture = ?"""
            cursor.execute(sql, (culture,))
            result_cursor = cursor.fetchall()
            saturation = []

            for index, value in enumerate(list(result_cursor[0])):
                if isinstance(value, str):
                    value = value.replace(',', '.')
                    saturation.append(float(value))
                else:
                    if value == None:
                        saturation.append(0)
                    else:
                        saturation.append(value)

            result = {}
            result['m'] = saturation[0]
            result['X'] = saturation[1]
            result['V'] = saturation[2]
            result['OBS'] = saturation[3]

            return result

        finally:
            self.close_data_base()
