class Calculation:

    #any and all necessary calculations and unit conversions are here. units are exclusively metric (N, Pa, kg, kg/m^3, m, etc.)
    def __init__(self, time, press, thrust, press_smoothed, thrust_smoothed, mass, density, throat_area, grain_len, grain_init_core, grain_OD, burn_time, impulse, press_integral, c_star, isp):
        self._time = time
        self._press = press
        self._thrust = thrust
        self._press_smoothed = press_smoothed
        self._thrust_smoothed = thrust_smoothed
        self._mass = mass
        self._density = density
        self._throat_area = throat_area
        self._grain_len = grain_len
        self._grain_init_core = grain_init_core
        self._grain_OD = grain_OD
        self._burn_time = burn_time
        self._impulse = impulse
        self._press_integral = press_integral
        self._c_star = c_star
        self._isp = isp

    #getters and setters

    def get_time(self):
        return self._time

    def set_time(self, value):
        self._time = value

    def get_press(self):
        return self._press

    def set_press(self, value):
        self._press = value

    def get_thrust(self):
        return self._thrust

    def set_thrust(self, value):
        self._thrust = value
    
    def get_press_smoothed(self):
        return self._press_smoothed

    def set_press_smoothed(self, value):
        self._press_smoothed = value
    
    def get_thrust_smoothed(self):
        return self._thrust_smoothed

    def set_thrust_smoothed(self, value):
        self._thrust_smoothed = value

    def get_mass(self):
        return self._mass

    def set_mass(self, value):
        self._mass = value

    def get_density(self):
        return self._density

    def set_density(self, value):
        self._density = value

    def get_throat_area(self):
        return self._throat_area

    def set_throat_area(self, value):
        self._throat_area = value

    def get_grain_len(self):
        return self._grain_len

    def set_grain_len(self, value):
        self._grain_len = value

    def get_grain_init_core(self):
        return self._grain_init_core

    def set_grain_init_core(self, value):
        self._grain_init_core = value

    def get_grain_OD(self):
        return self._grain_OD

    def set_grain_OD(self, value):
        self._grain_OD = value

    def get_burn_time(self):
        return self._burn_time

    def set_burn_time(self, value):
        self._burn_time = value

    def get_impulse(self):
        return self._impulse

    def set_impulse(self, value):
        self._impulse = value

    def get_press_integral(self):
        return self._press_integral

    def set_press_integral(self, value):
        self._press_integral = value

    def get_c_star(self):
        return self._c_star

    def set_c_star(self, value):
        self._c_star = value

    def get_isp(self):
        return self._isp

    def set_isp(self, value):
        self._isp = value
    
    
    #getters and setters for variables not in the constructor
    
    def set_sArr(self, sArr):
        self.sArr = sArr

    def get_sArr(self):
        return self.sArr

    def set_dsArr(self, dsArr):
        self.dsArr = dsArr

    def get_dsArr(self):
        return self.dsArr

    def set_A_bArr(self, A_bArr):
        self.A_bArr = A_bArr

    def get_A_bArr(self):
        return self.A_bArr

    def set_ds_dtArr(self, ds_dtArr):
        self.ds_dtArr = ds_dtArr

    def get_ds_dtArr(self):
        return self.ds_dtArr