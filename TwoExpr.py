
from z3 import *

s = Solver()

Activate = Bool('Activate')
S_ChannelA = Bool('S_ChannelA')
S_ChannelB = Bool('S_ChannelB')
Timer = Int('Timer')
DiscrepancyTime = Int('DiscrepancyTime')

s.add(And(Not(S_ChannelA),Not(S_ChannelB)), Or(Not(S_ChannelA),Not(S_ChannelB)))

print(s.check(), end='')

