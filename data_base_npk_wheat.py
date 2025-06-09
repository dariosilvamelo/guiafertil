import sqlite3

import constants as c


class DataBaseNpkWheat:

    def __init__(self, name_data_base):
        self.data_base = name_data_base

    def open_data_base(self):
        self.connection_data_base = sqlite3.connect(self.data_base)

    def close_data_base(self):
        self.connection_data_base.close()

    def query_n_wheat(self, rainfed_irrigated, size_cultivar, previous_culture_corn):
        self.open_data_base()
        try:
            cursor = self.connection_data_base.cursor()
            sql = """SELECT N.n_planting, N.n_top_dressing
                     FROM
                            n_wheat N
                     WHERE
                            N.rainfed_irrigated = ?
                        and N.size_cultivar = ?
                        and	N.previous_culture_corn = ?"""
            cursor.execute(sql, (rainfed_irrigated, size_cultivar, previous_culture_corn))
            result = cursor.fetchall()
            return result[0]
        finally:
            self.close_data_base()

    def query_p_wheat(self, type_fertilizer, p_availability, clay, rainfed_irrigated):
        self.open_data_base()
        try:
            cursor = self.connection_data_base.cursor()
            if type_fertilizer == c.TOTAL_FERTILIZATION:
                sql = """SELECT
                            P.very_low_p
                            ,P.low_p
                            ,P.high_p
                            FROM
                            p2o5_total_wheat P
                            WHERE
                                P.initial_clay <= ?
                            and P.final_clay >= ?"""
            else:
                sql = """SELECT
                            P.very_low_p
                            ,P.low_p
                            ,P.high_p
                            FROM
                            p2o5_gradual_wheat P
                            WHERE
                                P.initial_clay <= ?
                            and P.final_clay >= ?"""

            cursor.execute(sql, (clay, clay))
            result = cursor.fetchall()

            if p_availability == c.VERY_LOW_AVAILABILITY:
                p = result[0][0]
                if rainfed_irrigated == c.IRRIGATED:
                    p = p * 1.20

            elif p_availability == c.LOW_AVAILABILITY:
                p = result[0][1]
                if rainfed_irrigated == c.IRRIGATED:
                    p = p * 1.20
            else:
                p = self.maintenance_fertilizer_p(rainfed_irrigated)

            return p
        finally:
            self.close_data_base()

    def query_k_wheat(self, k, clay, rainfed_irrigated):
        self.open_data_base()
        try:
            cursor = self.connection_data_base.cursor()
            sql = """SELECT
                            K.k2o_total_corrective,
                            K.k2o_gradual_corrective
                    FROM
                            k2o_wheat K
                    WHERE
                                K.initial_K <= ?
                            and K.final_K   >= ?"""
            cursor.execute(sql, (k, k,))
            result = cursor.fetchall()

            if k < 50:
                if clay > 20:
                    k2o = result[0][0]
                else:
                    k2o = result[0][1]

                if rainfed_irrigated == c.IRRIGATED:
                    k2o += 10
            else:
                k2o = self.maintenance_fertilizer_k(rainfed_irrigated)

            return k2o

        finally:
            self.close_data_base()

    def query_b_wheat(self, altitude):
        self.open_data_base()
        try:
            cursor = self.connection_data_base.cursor()
            sql = """SELECT altitude_below_wheat, B FROM altitude_wheat"""
            cursor.execute(sql)
            result = cursor.fetchall()
            b = 0
            if int(altitude) >= result[0][0]:
                b = result[0][1]
            else:
                b = 0    

            if isinstance(b, str):
                b = b.replace(',', '.')

            return float(b)
        finally:
            self.close_data_base()

    def maintenance_fertilizer_p(self, rainfed_irrigated):
        self.open_data_base()
        try:
            cursor = self.connection_data_base.cursor()
            sql = """ SELECT p2o5_rainfed_planting, p2o5_irrigated_planting
                      FROM pk_maintenance_wheat"""
            cursor.execute(sql)
            result = cursor.fetchall()

            if c.RAINFED == rainfed_irrigated:
                return result[0][0]

            elif c.IRRIGATED == rainfed_irrigated:
                return result[0][1]
            else:
                return result[0][0]
        finally:
            self.close_data_base()

    def maintenance_fertilizer_k(self, rainfed_irrigated):
        self.open_data_base()
        try:
            cursor = self.connection_data_base.cursor()
            sql = """ SELECT k2o_rainfed_top_dressing, k2o_irrigated_top_dressing
                      FROM pk_maintenance_wheat"""
            cursor.execute(sql)
            result = cursor.fetchall()

            if c.RAINFED == rainfed_irrigated:
                return result[0][0]

            elif c.IRRIGATED == rainfed_irrigated:
                return result[0][1]
            else:
                result[0][0]
        finally:
            self.close_data_base()
