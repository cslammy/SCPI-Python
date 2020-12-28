import pyvisa
#import visa
rm = pyvisa.ResourceManager()
print(rm.list_resources())

avg = rm.open_resource('USB0::0xF4ED::0xEE3A::SDG10GAD1R1738::INSTR')
print(avg.query('*IDN?'))

#new waveform, 0 sym,
avg.write('C1:BaSic_WaVe WVTP,RAMP')
avg.write('C1:BaSic_WaVe SYM,0')
avg.write('C1:BaSic_WaVe FRQ,2000')
