from model.DBmysql import DataBase 

class DBProceso():
    def __init__(self):
        self.connection = DataBase().connection
        self.cursor = self.connection.cursor()
    
    def select_all_name_proceso(self):
        try:
            sql = "SELECT nombre FROM esterilizadora.parametros order by id"
            self.cursor.execute(sql)
            result = self.cursor.fetchall()
            list = []
            for name in result:
                list.append(name[0]) 
            return list
        except Exception as e:
            print("Error: {}".format(e))
            print(e)
            raise

    def select_proceso(self, value):
        sql= """SELECT 
    v_evacuation_pressure,
    v_anticavitation_pressure,
    v_gas_interlock_pressure,
    v_pressure_increment,
    v_time_increment,
    v_fast_increment_tolerance,
    v_slow_increment_termination_pressure,
    v_print_interval,
    l_leak_test_time,
    l_leak_test_tolerance,
    l_print_interval,
    i_of_dilution_cycles,
    i_inert_gas_pressure,
    i_inert_pressure_increment,
    i_inert_time_increment,
    i_inert_fast_increment_tolerance,
    i_evacuation_pressure,
    i_vacuum_pressure_increment,
    i_vacuum_time_increment,
    i_vaccum_fast_inc_tolerance,
    i_vacuum_slow_increment_termination_pressure,
    i_anticavitation_pressure,
    i_hi_pressure,
    i_print_interval,
    h_type,
    h_pressure_rise,
    h_pressure_increment,
    h_time_increment,
    h_fast_increment_tolerance,
    h_maximum_time,
    h_print_interval,
    hd_type,
    hd_control_pressure,
    hd_control_diferential,
    hd_hi_humidity,
    hd_lo_humidity,
    hd_maximum_humidity,
    hd_dwell_time,
    hd_print_interval,
    g_gas_pressure,
    g_pressure_increment,
    g_time_increment,
    g_fast_increment_tolerance,
    g_print_interval,
    g_gas_by_weight,
    gd_control_pressure,
    gd_control_differential,
    gd_dwell_time,
    gd_maximum_makeups,
    gd_long_exposure,
    gd_short_exposure,
    gd_hi_pressure,
    gd_lo_pressure,
    gd_hi_pressure_abort,
    gd_emission_control_lead_time,
    gd_print_interval,
    a_evacuation_pressure,
    a_anticavitation_pressure,
    a_air_interlock_pressure,
    a_pressure_increment,
    a_time_increment,
    a_fast_increment_tolerance,
    a_slow_increment_termination_pressure,
    a_vacuum_hold_time,
    a_print_interval,
    gwa_of_wash_cycles,
    gwa_release_type,
    gwa_release_pressure,
    gwa_evacuation_pressure,
    gwa_anticavitation_pressure,
    gwa_hi_pressure,
    gwa_release_pressure_increment,
    gwa_release_time_increment,
    gwa_fast_inc_tolerance,
    gwa_release_slow_increment_termination_pressure,
    gwa_release_hold_time,
    gwa_vacuum_pressure_increment,
    gwa_vacuum_time_increment,
    gwa_vacuum_fast_inc_tolerance,
    gwa_vacuum_slow_increment_termination_pressure,
    gwa_vacuum_hold_time,
    gwa_print_interval,
    gwb_of_wash_cycles,
    gwb_release_type,
    gwb_release_pressure,
    gwb_evacuation_pressure,
    gwb_anticavitation_pressure,
    gwb_hi_pressure,
    gwb_release_pressure_increment,
    gwb_release_time_increment,
    gwb_release_fast_inc_tolerance,
    gwb_release_slow_increment_termination_pressure,
    gwb_release_hold_time,
    gwb_vacuum_pressure_increment,
    gwb_vacuum_time_increment,
    gwb_vacuum_fast_inc_tolerance,
    gwb_slow_increment_termination_pressure,
    gwb_vacuum_hold_time,
    gwb_print_interval,
    r_release_pressure,
    r_pressure_increment,
    r_time_increment,
    r_fast_increment_tolerance,
    r_slow_increment_termination_pressure,
    r_print_interval
    FROM esterilizadora.parametros where nombre = '{}' """.format(value)
        object_proceso = []
        try:
            self.cursor.execute(sql)
            proceso = self.cursor.fetchone()
            object_proceso = [proceso[0],proceso[1],proceso[2],proceso[3],proceso[4],
            proceso[5],proceso[6],proceso[7],proceso[8],proceso[9],proceso[10],proceso[11],
            proceso[12],proceso[13],proceso[14],proceso[15],proceso[16],proceso[17],proceso[18],
            proceso[19],proceso[20],proceso[21],proceso[22],proceso[23],proceso[24],proceso[25],
            proceso[26],proceso[27],proceso[28],proceso[29],proceso[30],proceso[31],proceso[32],
            proceso[33],proceso[34],proceso[35],proceso[36],proceso[37],proceso[38],proceso[39],
            proceso[40],proceso[41],proceso[42],proceso[43],proceso[44],proceso[45],proceso[46],
            proceso[47],proceso[48],proceso[49],proceso[50],proceso[51],proceso[52],proceso[53],
            proceso[54],proceso[55],proceso[56],proceso[57],proceso[58],proceso[59],proceso[60],
            proceso[61],proceso[62],proceso[63],proceso[64],proceso[65],proceso[66],proceso[67],
            proceso[68],proceso[69],proceso[70],proceso[71],proceso[72],proceso[73],proceso[74],
            proceso[75],proceso[76],proceso[77],proceso[78], proceso[79],proceso[80],proceso[81],
            proceso[82],proceso[83],proceso[84],proceso[85],proceso[86],proceso[87],proceso[88],
            proceso[89],proceso[90],proceso[91],proceso[92],proceso[93],proceso[94],proceso[95],
            proceso[96],proceso[97],proceso[98],proceso[99],proceso[100],proceso[101],proceso[102],proceso[103], proceso[104]]
            
            print("Proceso: ",proceso[10])

            return object_proceso
        except Exception as e:
            print(e)
            return object_proceso


#con = DBProceso()
#ren =con.select_proceso()
#print(ren)

