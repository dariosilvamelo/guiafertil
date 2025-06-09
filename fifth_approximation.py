import constants as c
from data_base_availability_attributes import DataBaseAvailabilityAttributes
from data_base_availability_p import DataBaseAvailability_P
from data_base_availability_p_wheat import DataBaseAvailability_P_wheat
from data_base_availability_s import DataBaseAvailability_S
from data_base_micro_fertilizer import DataBaseMicroFertilizer
from data_base_npk import DataBaseNpk
from data_base_npk_wheat import DataBaseNpkWheat
from data_base_saturation import DataBaseSaturation


class FifthApproximation():
    def __init__(self) -> None:
        pass    

    def base_saturation(self, sum_bases, ctc_ph_7, ve):
        va = 100 * sum_bases / ctc_ph_7
        nc = ctc_ph_7 * (ve - va) / 100
        return nc

    def neutralization_Al_elevation_Ca_Mg(self, clay, p_rem, al, mt, t, x, ca, mg):
        nc_clay = 0
        nc_p_rem = 0

        if clay > 0:

            ca_clay = self.acidity_correction(self.y_clay(clay), al, mt, t)
            nc_clay = ca_clay + self.correction_Ca_Mg_deficiency(x, ca, mg)

        if p_rem > 0:

            ca_p_rem = self.acidity_correction(self.y_p_rem(p_rem), al, mt, t)
            nc_p_rem = ca_p_rem + self.correction_Ca_Mg_deficiency(x, ca, mg)

        return [nc_clay, nc_p_rem]

    def y_clay(self, clay):
        y = 0.0302+(0.06532*clay)+(-0.000257*(clay**2))
        return y

    def y_p_rem(self, p_rem):
        y = 4.002+(- 0.125901*p_rem)+(0.001205*(p_rem**2))+(-0.00000362*(p_rem** 3))
        return y

    def acidity_correction(self, y, al, mt, t):
        ca = y * (al - (mt * t / 100))
        if ca < 0:
            ca = 0
        return ca

    def correction_Ca_Mg_deficiency(self, x, ca, mg):
        cd = x - (ca + mg)
        if cd < 0:
            cd = 0
        return cd

    def need_plaster_clay(self, clay):
        ng = 0.00034+(-0.002445*(clay**0.5))+(0.0338886*clay)+(-0.00176366*(clay**1.5))
        return ng

    def need_plaster_p_rem(self, p_rem, tca):
        ng = 0
        if (p_rem > 0) and (tca > 0):
            ca = 315.8 + (-25.5066 * (p_rem ** 0.5))+(-5.70675*p_rem)+(0.485335 * (p_rem ** 1.5))
            ng = ca / (10 * tca)
        return ng

    def need_plaster_nc(self, nc_neutralization_Al_elevation_Ca_Mg):
        ng = 0
        ng = 0.25 * nc_neutralization_Al_elevation_Ca_Mg
        return ng

    def amount_plaster(self, ng, surface, initial_depth, final_depth):
        qg = ng * (surface/100) * ((final_depth - initial_depth)/20)
        return qg

    def amount_limestone(self, nc, surface, initial_depth, final_depth, prnt):
        qc = nc * (surface/100) * ((final_depth - initial_depth)/20) * (100/prnt)
        return qc

    def p_availability(self, clay, p_rem, p):
        p_level_range_clay = []
        p_level_range_p_rem = []
        query = DataBaseAvailability_P(c.DATABASE_ADDRESS)

        if clay > 0:
            p_level_range_clay = query.query_p_availability_clay(clay, p)

        if p_rem > 0:
            p_level_range_p_rem = query.query_p_availability_p_rem(p_rem, p)

        return [p_level_range_clay, p_level_range_p_rem]

    def s_availability(self, p_rem, s):

        query = DataBaseAvailability_S(c.DATABASE_ADDRESS)

        s_level_range_p_rem = query.query_s_availability_p_rem(p_rem, s)

        return s_level_range_p_rem

    def availability_soil_attributes(self, attribute, attribute_value):
        query = DataBaseAvailabilityAttributes(c.DATABASE_ADDRESS)
        attribute_level_range = query.query_availability_attributes(attribute, attribute_value)
        return attribute_level_range

    def p_availability_wheat(self, clay, p):
        query = DataBaseAvailability_P_wheat(c.DATABASE_ADDRESS)
        p_level_range_wheat = query.query_p_availability_wheat(clay, p)
        return p_level_range_wheat

    def npk(self, culture, p_availability, k_availability, technology='not applicable', previous_culture_soy='not applicable'):
        query = DataBaseNpk(c.DATABASE_ADDRESS)

        result = list(query.query_npk_culture(culture, p_availability, k_availability, technology))

        if (culture in (c.CORN, c.SORGHUM)):
            if (technology == c.DIRECT_PLANTING):
                planting_n = (result[0][0] + 30, result[0][1])
                result.pop(0)
                result.insert(0, planting_n)

            if previous_culture_soy == c.CONFIRMED:
                planting_n = (result[0][0], result[0][1] - 20)
                result.pop(0)
                result.insert(0, planting_n)
        return result

    def npk_wheat(self, type_fertilizer, p_availability, clay, rainfed_irrigated, k, size_cultivar, previous_culture_corn, altitude):
        query = DataBaseNpkWheat(c.DATABASE_ADDRESS)
        n = query.query_n_wheat(rainfed_irrigated, size_cultivar, previous_culture_corn)
        p2o5 = query.query_p_wheat(type_fertilizer, p_availability, clay, rainfed_irrigated)
        k2o = query.query_k_wheat(k, clay, rainfed_irrigated)
        b = query.query_b_wheat(altitude)
        return [n, p2o5, k2o, b]

    def micronutrient_fertilizer(self, culture, soil_attributes, technology='not applicable'):
        query = DataBaseMicroFertilizer(c.DATABASE_ADDRESS)
        fertilizer = {}
        keys = ['Mg2+', 'S', 'Zn', 'Mn', 'Cu', 'B', 'Mo', 'Co']
        for field in keys:
            fertilizer[field] = None

        for line in soil_attributes:

            if line[0][0] in ('Mg2+', 'S', 'Zn', 'Mn', 'Cu', 'B', 'Mo', 'Co'):
                if line[1] in (c.VERY_LOW_AVAILABILITY, c.LOW_AVAILABILITY, c.AVERAGE_AVAILABILITY):
                    micros = query.query_micro_fertilizer(culture, technology)
                    fertilizer[line[0][0]] = micros[line[0][0]]
                elif line[0][0] in ('Mo', 'Co'):
                    micros = query.query_micro_fertilizer(culture, technology)
                    fertilizer[line[0][0]] = micros[line[0][0]]
                else:
                    fertilizer[line[0][0]] = 0

        return fertilizer

    def search_saturation(self, culture):
        query = DataBaseSaturation(c.DATABASE_ADDRESS)
        resul = query.query_saturation(culture)
        return resul