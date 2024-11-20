import sqlite3

import constants as c


class DataBaseNpk:

    def __init__(self, name_data_base):
        self.data_base = name_data_base

    def open_data_base(self):
        self.connection_data_base = sqlite3.connect(self.data_base)

    def close_data_base(self):
        self.connection_data_base.close()

    def query_npk_culture(self, culture, p_availability, k_availability, technology='not applicable'):
        self.open_data_base()
        try:
            cursor = self.connection_data_base.cursor()
            if culture != c.BEAN:
                sql = """SELECT
                            A.Culture,
                            A.technology,
                            A.planting_n,
                            A.top_dressing_n,
                            A.low_p,
                            A.average_p,
                            A.high_p,
                            A.low_k,
                            A.average_k,
                            A.high_k
                         FROM
                            mineral_fertilizer A
                         WHERE
                            A.Culture = ?"""
                cursor.execute(sql, (culture,))

            else:
                sql = """SELECT
                            A.Culture,
                            A.technology,
                            A.planting_n,
                            A.top_dressing_n,
                            A.low_p,
                            A.average_p,
                            A.high_p,
                            A.low_k,
                            A.average_k,
                            A.high_k
                         FROM
                            mineral_fertilizer A
                         WHERE
                            A.Culture = ?
                        and A.technology = ?"""
                cursor.execute(sql, (culture, technology))

            npk_culture = cursor.fetchall()

            n = npk_culture[0][2:4]
            p = self.fertilizer_p(npk_culture[0][4:7], p_availability)
            k = self.fertilizer_k(npk_culture[0][7:10], k_availability)
            if culture == c.BEAN:
                technology_level = npk_culture[0][1:2]
                return n, p, k, technology_level
            else:
                return n, p, k
        finally:
            self.close_data_base()

    def fertilizer_p(self, p, p_availability):
        if p_availability in (c.VERY_LOW_AVAILABILITY, c.LOW_AVAILABILITY):
            return p[0]

        elif p_availability == c.AVERAGE_AVAILABILITY:
            return p[1]

        elif p_availability in (c.VERY_GOOD, c.GOOD):
            return p[2]

        else:
            return p[0]

    def fertilizer_k(self, k, k_availability):
        if k_availability in (c.VERY_LOW_AVAILABILITY, c.LOW_AVAILABILITY):
            return k[0]

        elif k_availability == c.AVERAGE_AVAILABILITY:
            return k[1]

        elif k_availability in (c.VERY_GOOD, c.GOOD):
            return k[2]

        else:
            return k[0]
