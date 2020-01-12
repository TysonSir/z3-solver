
from z3 import *

s = Solver()

Activate = Bool('Activate')
S_ChannelA = Bool('S_ChannelA')
S_ChannelB = Bool('S_ChannelB')
Timer = Int('Timer')
DiscrepancyTime = Int('DiscrepancyTime')

s.add(Or(Not(S_ChannelA),Not(S_ChannelB)), And(Not(S_ChannelA),Not(S_ChannelB)))

print(s.check(), end='')

m = s.model()
with open('log_data.txt', 'a+', encoding='utf-8') as f:
    log_data = ''
    for d in m.decls():
        log_data += "%s = %s, " % (d.name(), m[d])
    log_data += '\n'
    f.write(log_data)
