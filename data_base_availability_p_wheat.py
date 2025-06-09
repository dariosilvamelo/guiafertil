import sqlite3

import constants as c


class DataBaseAvailability_P_wheat:

    def __init__(self, name_data_base):
        self.data_base = name_data_base

    def open_data_base(self):
        self.connection_data_base = sqlite3.connect(self.data_base)

    def close_data_base(self):
        self.connection_data_base.close()

    def query_p_availability_wheat(self, clay, p):
        self.open_data_base()
        try:
            cursor = self.connection_data_base.cursor()

            sql = """SELECT
                            low_p,
                            middle_p,
                            high_p
                     FROM
                        	p_analysis_wheat P
                     WHERE
                        	P.initial_clay <=?
                     and	P.final_clay >=?"""

            cursor.execute(sql, (clay, clay))
            p_availability_wheat = cursor.fetchall()
            result = ''

            for index, value in enumerate(list(p_availability_wheat[0])):

                if isinstance(value, str):
                    value = value.replace(',', '.')

                if p < float(value):
                    if index == 0:
                        result = c.VERY_LOW_AVAILABILITY
                        break
                    elif index == 1:
                        result = c.LOW_AVAILABILITY
                        break
                    elif index == 2:
                        result = c.AVERAGE_AVAILABILITY
                        break
            if result == '':
                result = c.GOOD

            soil_attribute = ('P', 'Fósforo disponível', 'mg/dm3',) + p_availability_wheat[0]

            p_availability_wheat.clear()
            p_availability_wheat.append(soil_attribute)
            p_availability_wheat.append(result)
            p_availability_wheat.append(p)
            p_availability_wheat.append("ARGILA")
            p_availability_wheat.append(clay)

            return p_availability_wheat
        finally:
            self.close_data_base()
