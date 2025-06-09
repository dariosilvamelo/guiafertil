import sqlite3

import constants as c


class DataBaseAvailability_P:

    def __init__(self, name_data_base):
        self.data_base = name_data_base

    def open_data_base(self):
        self.connection_data_base = sqlite3.connect(self.data_base)

    def close_data_base(self):
        self.connection_data_base.close()

    def query_p_availability_clay(self, clay, p):
        self.open_data_base()
        try:
            cursor = self.connection_data_base.cursor()
            sql = """SELECT P.low_p,
                    P.average_p,
                    P.high_p,
                    P.very_high
                    FROM
                    p_availability P
                    where
                        P.soil_characteristics = "ARGILA (%)"
                    and  P.initial_soil_characteristics < ?
                    and  P.final_soil_characteristics  >= ?"""
            cursor.execute(sql, (clay, clay))
            p_availability_clay = cursor.fetchall()
            result = ''

            for index, value in enumerate(list(p_availability_clay[0])):
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
                    elif index == 3:
                        result = c.GOOD
            if result == '':
                result = c.VERY_GOOD
            
            soil_attribute = ('P', 'Fósforo disponível', 'mg/dm3',) + p_availability_clay[0]
            p_availability_clay.clear()
            p_availability_clay.append(soil_attribute)
            p_availability_clay.append(result)
            p_availability_clay.append(p)
            p_availability_clay.append("ARGILA")
            p_availability_clay.append(clay)

            return p_availability_clay
        finally:
            self.close_data_base()

    def query_p_availability_p_rem(self, p_rem, p):
        self.open_data_base()
        try:
            cursor = self.connection_data_base.cursor()
            sql = """SELECT P.low_p,
                    P.average_p,
                    P.high_p,
                    P.very_high
                    FROM
                    p_availability P
                    where
                        P.soil_characteristics = "P-REM (mg/dm3)"
                    and  P.initial_soil_characteristics < ?
                    and  P.final_soil_characteristics  >= ?"""
            cursor.execute(sql, (p_rem, p_rem))
            p_availability_p_rem = cursor.fetchall()

            result = ''
            for index, value in enumerate(list(p_availability_p_rem[0])):

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
                    elif index == 3:
                        result = c.GOOD
            if result == '':
                result = c.VERY_GOOD

            soil_attribute = ('P', 'Fósforo disponível', 'mg/dm3',) + p_availability_p_rem[0]
            p_availability_p_rem.clear()
            p_availability_p_rem.append(soil_attribute)
            p_availability_p_rem.append(result)
            p_availability_p_rem.append(p)
            p_availability_p_rem.append("P-REM")
            p_availability_p_rem.append(p_rem)

            return p_availability_p_rem
        finally:
            self.close_data_base()
