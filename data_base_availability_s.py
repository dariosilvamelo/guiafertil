import sqlite3

import constants as c


class DataBaseAvailability_S:

    def __init__(self, name_data_base):
        self.data_base = name_data_base

    def open_data_base(self):
        self.connection_data_base = sqlite3.connect(self.data_base)

    def close_data_base(self):
        self.connection_data_base.close()

    def query_s_availability_p_rem(self, p_rem, s):
        self.open_data_base()
        try:
            cursor = self.connection_data_base.cursor()
            sql = """SELECT S.low_s,
                    S.average_s,
                    S.high_s,
                    S.very_high_s
                    FROM
                    s_availability S
                    where
                         S.initial_p_rem_s <  ?
                    and  S.final_p_rem_s   >= ?"""
            cursor.execute(sql, (p_rem, p_rem))
            s_availability_p_rem = cursor.fetchall()

            result = ''
            for index, value in enumerate(list(s_availability_p_rem[0])):

                if isinstance(value, str):
                    value = value.replace(',', '.')

                if s < float(value):
                    if index == 0:
                        result =  c.VERY_LOW_AVAILABILITY
                        break
                    elif index == 1:
                        result = c.LOW_AVAILABILITY
                        break
                    elif index == 2:
                        result = c.AVERAGE_AVAILABILITY
                        break
                    elif index == 3:
                        result = c.GOOD
            if result == '':
                result = c.VERY_GOOD

            soil_attribute = ('S', 'Enxofre disponível', 'mg/dm3',) + s_availability_p_rem[0]
            s_availability_p_rem.clear()
            s_availability_p_rem.append(soil_attribute)
            s_availability_p_rem.append(result)
            s_availability_p_rem.append(s)
            s_availability_p_rem.append("P-REM")
            s_availability_p_rem.append(p_rem)

            return s_availability_p_rem
        finally:
            self.close_data_base()
