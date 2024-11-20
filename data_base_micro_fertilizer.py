import sqlite3

import constants as c


class DataBaseMicroFertilizer:

    def __init__(self, name_data_base):
        self.data_base = name_data_base

    def open_data_base(self):
        self.connection_data_base = sqlite3.connect(self.data_base)

    def close_data_base(self):
        self.connection_data_base.close()

    def query_micro_fertilizer(self, culture, technology):
        result_fields = {}
        self.open_data_base()
        try:
            cursor = self.connection_data_base.cursor()
            if culture == c.WHEAT:
                sql = """SELECT
                            F.S_sulfur,
                            F.Zn_zinc,
                            F.B_boron,
                            F.Cu_copper,
                            F.Mn_manganese,
                            F.Mo_molybdenum,
                            F.Co_cobalt,
                            F.Mg_magnesium
                            FROM micro_fertilizer_wheat F"""
                cursor.execute(sql)
            elif culture == c.BEAN:
                sql = """SELECT
                            F.S_sulfur,
                            F.Zn_zinc,
                            F.B_boron,
                            F.Cu_copper,
                            F.Mn_manganese,
                            F.Mo_molybdenum,
                            F.Co_cobalt,
                            F.Mg_magnesium
                            FROM mineral_fertilizer F
                            WHERE
                                F.Culture = ?
                            AND	F.technology = ?"""
                cursor.execute(sql, (culture, technology))
            else:
                sql = """SELECT
                            F.S_sulfur,
                            F.Zn_zinc,
                            F.B_boron,
                            F.Cu_copper,
                            F.Mn_manganese,
                            F.Mo_molybdenum,
                            F.Co_cobalt,
                            F.Mg_magnesium
                            FROM mineral_fertilizer F
                            WHERE
                                F.Culture = ?"""
                cursor.execute(sql, (culture,))

            micro_fertilizer = cursor.fetchall()

            result_fields['S'] = self.validates_float(micro_fertilizer[0][0])
            result_fields['Zn'] = self.validates_float(micro_fertilizer[0][1])
            result_fields['B'] = self.validates_float(micro_fertilizer[0][2])
            result_fields['Cu'] = self.validates_float(micro_fertilizer[0][3])
            result_fields['Mn'] = self.validates_float(micro_fertilizer[0][4])
            result_fields['Mo'] = self.validates_float(micro_fertilizer[0][5])
            result_fields['Co'] = self.validates_float(micro_fertilizer[0][6])
            result_fields['Mg2+'] = self.validates_float(micro_fertilizer[0][7])

            return result_fields
        finally:
            self.close_data_base()

    def validates_float(self, number):
        if isinstance(number, str):
            number = number.replace(',', '.')
        try:
            return float(number)
        except (ValueError, TypeError):
            return 0
