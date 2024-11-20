import sqlite3

import constants as c


class DataBaseAvailabilityAttributes:

    def __init__(self, name_data_base):
        self.data_base = name_data_base

    def open_data_base(self):
        self.connection_data_base = sqlite3.connect(self.data_base)

    def close_data_base(self):
        self.connection_data_base.close()

    def query_availability_attributes(self, attribute, attribute_value):
        self.open_data_base()
        try:
            cursor = self.connection_data_base.cursor()
            sql = """SELECT
                        A.name_soil_attribute
                        ,A.description_soil_attribute
                        ,A.unit_soil_attribute
                        ,A.low_soil_attribute
                        ,A.middle_soil_attribute
                        ,A.high_soil_attribute
                        ,A.very_high_soil_attribute
                        FROM
                        soil_attribute A
                        WHERE
                        A.name_soil_attribute = ?"""
            cursor.execute(sql, (attribute,))
            availability_classes = cursor.fetchall()
            availability_classes_aux = list(availability_classes[0][3:])
            result = ''
            for index, value in enumerate(availability_classes_aux):

                if isinstance(value, str):
                    value = value.replace(',', '.')

                if attribute_value < float(value):
                    if index == 0:
                        result = c.VERY_LOW_AVAILABILITY
                        break
                    elif index == 1:
                        result = c.LOW_AVAILABILITY
                        break
                    elif index == 2:
                        if attribute in (c.PH_CACL2, c.PH_H2O):
                            result = c.GOOD
                        else:
                            result = c.AVERAGE_AVAILABILITY
                        break
                    elif index == 3:
                        if attribute in (c.AL, c.SB, c.H_AL, c.CTC_EFFECTIVE, c.CTC_PH7, c.M, c.V):
                            result = c.HIGH_AVAILABILITY
                        else:
                            result = c.GOOD
            if result == '':
                if attribute in (c.AL, c.SB, c.H_AL, c.CTC_EFFECTIVE, c.CTC_PH7, c.M, c.V):
                    result = c.VERY_HIGH_AVAILABILITY
                else:
                    result = c.VERY_GOOD

            availability_classes.append(result)
            availability_classes.append(attribute_value)

            return availability_classes

        finally:
            self.close_data_base()
