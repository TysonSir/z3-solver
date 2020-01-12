import sys
import os
import xml.etree.cElementTree as ET
import TwoExpCtrl as tec

def check_state_priority(state):
    all_trans_num = len(state)
    set_prior = set()
    for transition in state:
        trans_attr = transition.attrib
        set_prior.add(trans_attr['priority'])

    if all_trans_num == len(set_prior):
        return True
    else:
        return False

def get_trans_pairs(state):
    set_state_pairs = set()
    for trans_1 in state:
        trans_attr_1 = trans_1.attrib
        for trans_2 in state:
            trans_attr_2 = trans_2.attrib
            state_pair = set()
            state_pair.add((trans_attr_1['priority'], trans_attr_1['condition']))
            state_pair.add((trans_attr_2['priority'], trans_attr_2['condition']))
            if len(state_pair) == 1:
                continue
            set_state_pairs.add(tuple(state_pair))
    return set_state_pairs

def check_state(state):
    # 优先级不重复，无冲突
    if check_state_priority(state):
        return True

    for trans_pair in get_trans_pairs(state):
        # 调用z3
        list_trans = list(trans_pair)
        is_sat = tec.get_two_exp_z3_ret(list_trans[0][1], list_trans[1][1])
        if list_trans[0][0] == list_trans[1][0] and is_sat:
            print(str(list_trans))
            return False
    return True

def check_state_chart(xml_path):
    tree = ET.parse(xml_path)
    root = tree.getroot()

    for state in root:
        if not check_state(state):
            print("状态冲突-->",state.tag,":", state.attrib)
            return False
    return True

if __name__ == '__main__':
    if len(sys.argv) == 2:
        xml_path = sys.argv[1]
    else:
        xml_path = 'state1.xml'

    if(check_state_chart(xml_path)):
        print("OK:所有状态不冲突")
    else:
        print("ERROR:有状态冲突")
