import pyvisa

##print("goober")
rm = pyvisa.ResourceManager()
#print(rm.list_resources())
print(rm)
a = rm.list_resources()
print(a)
p = rm.open_resource('USB0::0x0483::0x7540::SPD3XHBX2R0646::INSTR')
p.read_termination = '\n'
p.write_termination = '\n'
p.query('*IDN?')

#qq = p.query('*IDN?')
#print(qq)
p.read_termination = '\n'
p.write_termination = '\n'

p.write('CH1:VOLTage 15')
p.write('OUTPut CH1,OFF')


#avg = rm.open_resource('USB0::0xF4ED::0xEE3A::SDG10GAD1R1738::INSTR')
#print(avg.query('*IDN?'))

#new waveform, 0 sym,
#avg.write('C1:BaSic_WaVe WVTP,RAMP')
#avg.write('C1:BaSic_WaVe SYM,0')
#avg.write('C1:BaSic_WaVe FRQ,2000')
