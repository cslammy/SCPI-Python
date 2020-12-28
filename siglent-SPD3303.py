import pyvisa
import time
############CHANGE THIS####################
ch1 = 10  #voltage ch1
ch2 = 10  #voltage ch2
amp1 = .20 #max curr ch 1
amp2 = .20 #max chrr ch 2

#turn channels on or off
x = "Off"

########################################

value1 = x.upper()
value2 = x.upper()
value3 = x.upper()


rm = pyvisa.ResourceManager()
print(rm.list_resources())
print(rm)

p=rm.open_resource('USB0::0x0483::0x7540::SPD3XHBX2R0646::INSTR')
p.read_termination = '\n'
p.write_termination = '\n'

qq = p.query('*IDN?',.1)

print(qq)


ch1volts = 'CH1:VOLTage ' + str(ch1)
ch2volts = 'CH2:VOLTage ' + str(ch2)

ch1curr = 'CH1:CURRent ' + str(amp1)
ch2curr = 'CH2:CURRent ' + str(amp2)

ch1onoff = 'OUTPut CH1,' + value1
ch2onoff = 'OUTPut CH2,' + value2
ch3onoff = 'OUTPut CH3,' + value3

p.write(ch1volts)
time.sleep(.1)
p.write(ch2volts)
time.sleep(.1)
p.write(ch1curr)
time.sleep(.1)
p.write(ch2curr)
time.sleep(.1)

p.write(ch1onoff)
time.sleep(.1)
p.write(ch2onoff)
time.sleep(.1)
p.write(ch3onoff)
p.close()
#avg = rm.open_resource('USB0::0xF4ED::0xEE3A::SDG10GAD1R1738::INSTR')
#print(avg.query('*IDN?'))

#new waveform, 0 sym,
#avg.write('C1:BaSic_WaVe WVTP,RAMP')
#avg.write('C1:BaSic_WaVe SYM,0')
#avg.write('C1:BaSic_WaVe FRQ,2000')
