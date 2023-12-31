import random
import sys
import names
import string


instr_list = ['ap', 'ar', 'qv', 'qci','qbs','qts', 'ag', 'atg', 'dfg',
               'qgvs', 'qgav','mr','qba','qcs','am', 'sm', 'qsv', 'qrm',
                'arem','anm','cn','aem','sei','qp','dce','qm','qlm']
# instr_list = ['ap', 'ar', 'ag', 'atg', 'dfg','am', 'sm',
              #  'mr','aem','arem','anm','cn','dce','sei','qlm']
# instr_list = ['ap', 'ar','mr','qlm']
instr_limit = {'ap' : 9000, 'qci' : 9000, 'ag' : 9000}
# int_min=-2147483648
int_min=1
# int_max=9
int_max=9000
instr_num=50000
# instr_num=100

person_id_set = set()
group_id_set = set()
msg_id_set = set()
emoji_id_set = set()

money_msg_id_set = set()
emoji_msg_id_set = set()
notice_msg_id_set = set()

link_map = {}
group_map = {}
msg_info = {}
emoji_heat_map = {}

max_heat = 0

####################################################################################
#disjointSet
class DisJointSet():

    def __init__(self) :
        self.pre = {}
        self.rank = {}
    
    def add (self, id) :
        if (id not in self.pre.keys()) :
            self.pre[id] = id
            self.rank[id] = 0

    def find(self, id) :
        rep = id
        while (rep != self.pre[rep]) :
            rep = self.pre[rep]
        
        now = id
        while (now != rep) :
            fa = self.pre[now]
            self.pre[now] = rep
            now = fa
        return rep
    
    def union(self, id1, id2) :
        fa1 = self.find(id1)
        fa2 = self.find(id2)
        rank1 = self.rank[id1]
        rank2 = self.rank[id2]

        if (rank1 < rank2) :
            self.pre[fa1] = fa2
        elif (rank1 > rank2) :
            self.pre[fa2] = fa1
        else :
            self.pre[fa1] = fa2
            self.rank[fa2] += 1
    
    def is_circle(self, id1, id2) :
        return self.find(id1) == self.find(id2)


disjoint_set = DisJointSet()


#####################################################################################

# def get_unexist_id(id_set, min = -2147483648, max = 2147483647) :
def get_unexist_id(id_set, min = int_min, max = int_max) :
    id = random.randint(min, max)
    while (id in id_set) :
        id = random.randint(min, max)
    return str(id)

def get_exist_id(id_set) :
    id = random.choice(list(id_set))
    return str(id)
        
def get_name() :
    name = names.get_first_name()
    while (len(name) > 10) :
        name = names.get_first_name()
    return name

def get_age() :
    age = random.randint(0, 200)
    return str(age)

def get_value() :
    value = random.randint(1, 1000)
    return str(value)

def get_type() :
    type =random.randint(0, 1)
    return str(type)

def get_social_value() :
    social_value = random.randint(-1000, 1000)
    return str(social_value)

def get_money() :
    money = random.randint(0, 200)
    return str(money)

def get_string() :
    num = random.randint(1, 100)
    notice = ""
    for _ in range(num) :
        notice += str(random.choice(string.ascii_letters))
    return notice



########################################################################################

# def get_id(id_set, min = -2147483648, max = 2147483647) :
def get_id(id_set, min = int_min, max = int_max) :
    prob = random.uniform(0, 1)
    id = get_unexist_id(id_set, min, max)
    if (prob < 0.8) :
        if (id_set) :
            id = get_exist_id(id_set)
    else :
        id = get_unexist_id(id_set, min, max)
    return id 

def get_double_person() :
    prob = random.uniform(0, 1)
    id1 = get_unexist_id(person_id_set)
    id2 = get_unexist_id(person_id_set)
    if (prob < 0.2) :
        id1 = get_unexist_id(person_id_set)
        id2 = str(random.randint(int_min, int_max))
    elif (prob < 0.4) :
        if (person_id_set) :
            id1 = get_exist_id(person_id_set)
        id2 = get_unexist_id(person_id_set)
    elif (prob < 0.7) :
        if (person_id_set) :
            id1 = get_exist_id(person_id_set)
            id2 = get_exist_id(person_id_set)
            if (len(link_map[id1]) + 1 < len(person_id_set)) :
                while (id2 in link_map[id1]) :
                    id2 = get_exist_id(person_id_set)
    else :
        if (person_id_set) :
            id1 = get_exist_id(person_id_set)
            if (link_map[id1]) :
                if (random.uniform(0, 1) < 0.2) : id2 = id1
                else : id2 = random.choice(link_map[id1])
            else :
                id2 = id1 
    return id1, id2

def get_person_group() :
    prob = random.uniform(0, 1)
    group_id = get_unexist_id(group_id_set)
    person_id = get_unexist_id(person_id_set)
    if (prob < 0.2) :
        group_id = get_unexist_id(group_id_set)
        person_id = str(random.randint(int_min, int_max))
    elif (prob < 0.4) :
        if (group_id_set):
            group_id = get_exist_id(group_id_set)
        person_id = get_unexist_id(person_id_set)
    elif (prob < 0.7) :
        for it in group_id_set:
            if (group_map[it]) :
                group_id = it
                person_id = random.choice(group_map[group_id])
                break    
    else :
        if (person_id_set and group_id_set) :
            group_id = get_exist_id(group_id_set)
            person_id = get_exist_id(person_id_set)
            if (len(group_map[group_id]) < len(person_id_set)) : 
                while (person_id in group_map[group_id]) :
                    person_id = get_exist_id(person_id_set)
    return person_id, group_id



#########################################################################################

# fuctions relative to person

def add_person(switch = False, _id = 0) :
    if (switch) :
        return  "ap " + str(_id) + " " + get_name() + " " + get_age()
    id = get_id(person_id_set)
    if (id not in person_id_set) :
        person_id_set.add(id)
        link_map[id] = []
        disjoint_set.add(id)
    return "ap " + id + " " + get_name() + " " + get_age()


def add_relation(switch = False, _id1 = 0, _id2 = 0) :
    if (switch) :
        return "ar " + str(_id1) + " " + str(_id2) + " " + get_value()
    id1, id2 = get_double_person()
    if (id1 in person_id_set and id2 in person_id_set and id2 not in link_map[id1]) :
        link_map[id1].append(id2)
        link_map[id2].append(id1)
        disjoint_set.union(id1, id2)
    return "ar " + id1 + " " + id2 + " " + get_value()


def query_value(switch = False, _id1 = 0, _id2 = 0) :
    if (switch) :
        return "qv " + str(_id1) + " " + str(_id2) 
    id1, id2 = get_double_person() 
    return "qv " + id1 + " " + id2 


def query_people_sum() :
    return "qps"


def query_circle(switch = False, _id1 = 0, _id2 = 0) :
    if (switch) :
        return "qci " + str(_id1) + " " + str(_id2)
    id1, id2 = get_double_person()
    return "qci " + id1 + " " + id2 


def query_block_sum() :
    return "qbs"

def query_triple_sum():
    return "qts"
# functions relative to group

def add_group(switch = False, _id = 0) :
    if (switch) :
        return "ag " + str(_id) 
    id = get_id(group_id_set)
    if (id not in group_id_set) :
        group_id_set.add(id)
        group_map[id] = []
    return "ag " + id     


def add_to_group(switch = False, _id1 = 0, _id2 = 0) :
    if (switch) :
        return "atg " + str(_id1) + " " + str(_id2)
    person_id, group_id = get_person_group() 
    if (group_id in group_id_set and person_id not in group_map[group_id]) :
        group_map[group_id].append(person_id)
    
    return "atg " + person_id + " " + group_id


def del_from_group(switch = False, _id1 = 0, _id2 = 0) :
    if (switch) :
        return "dfg " + str(_id1) + " " + str(_id2)
    person_id, group_id = get_person_group() 
    if (group_id in group_id_set and person_id in group_map[group_id]) :
        group_map[group_id].remove(person_id)
    return "dfg " + person_id + " " + group_id


def query_group_people_sum(switch = False, _id = 0) :
    if (switch) :
        return "qgps " + str(_id)
    id = get_id(group_id_set)
    return "qgps " + id


def query_group_value_sum(switch = False, _id = 0) :
    if (switch) :
        return "qgvs " + str(_id)
    id = get_id(group_id_set)
    return "qgvs " + id


def query_group_age_var(switch = False, _id = 0) :
    if (switch) :
        return "qgav " + str(_id)
    id = get_id(group_id_set)
    return "qgav " + id


# functions relative to message


def add_message(switch = False, _id = 0, _type = 0, _id1 = 0, _id2 = 0) :    
    if (switch) :
        return "am " + str(_id) + " " + get_social_value() + " " + str(_type) + " " + str(_id1) + " " + str(_id2)
    id = get_id(msg_id_set)
    type = get_type()
    if (type == '0') :
        id1, id2 = get_double_person()
        if (id not in msg_id_set and id1 in person_id_set and id2 in person_id_set and id1 != id2) :
            msg_id_set.add(id)
            msg_info[id] = (type, id1, id2)
            
        return "am " + id + " " + get_social_value() + " " + type + " " + id1 + " " + id2
    else :
        person_id, group_id = get_person_group()
        if (id not in msg_id_set and person_id in person_id_set and group_id in group_id_set) :
            msg_id_set.add(id)
            msg_info[id] = (type, person_id, group_id)
        return "am " + id + " " + get_social_value() + " " + type + " " + person_id + " " + group_id


def add_red_envelope_messages(switch = False, _id = 0, _type = 0, _id1 = 0, _id2 = 0) :
    if (switch) :
        return "arem " + str(_id) + " " + get_money() + " " + str(_type) + " " + str(_id1) + " " + str(_id2)
    id = get_id(msg_id_set)
    type = get_type()
    money = get_money()
    if (type == '0') :
        id1, id2 = get_double_person()
        if (id not in msg_id_set and id1 in person_id_set and id2 in person_id_set and id1 != id2) :
            msg_id_set.add(id)
            money_msg_id_set.add(id)
            msg_info[id] = (type, id1, id2, money)
        return "arem " + id + " " + money + " " + type + " " + id1 + " " + id2
    else :
        person_id, group_id = get_person_group()
        if (id not in msg_id_set and person_id in person_id_set and group_id in group_id_set) :
            msg_id_set.add(id)
            money_msg_id_set.add(id)
            msg_info[id] = (type, person_id, group_id, money)
        return "arem " + id + " " + money + " " + type + " " + person_id + " " + group_id


def add_notice_messages(switch = False, _id = 0, _type = 0, _id1 = 0, _id2 = 0) :
    if (switch) :
        return "anm " + str(_id) + " " + get_string() + " " + str(_type) + " " + str(_id1) + " " + str(_id2)
    id = get_id(msg_id_set)
    type = get_type()
    notice = get_string()
    if (type == '0') :
        id1, id2 = get_double_person()
        if (id not in msg_id_set and id1 in person_id_set and id2 in person_id_set and id1 != id2) :
            msg_id_set.add(id)
            notice_msg_id_set.add(id)
            msg_info[id] = (type, id1, id2, notice)
        return "anm " + id + " " + notice + " " + type + " " + id1 + " " + id2
    else :
        person_id, group_id = get_person_group()
        if (id not in msg_id_set and person_id in person_id_set and group_id in group_id_set) :
            msg_id_set.add(id)
            notice_msg_id_set.add(id)
            msg_info[id] = (type, person_id, group_id, notice)
        return "anm " + id + " " + notice + " " + type + " " + person_id + " " + group_id


def add_emoji_messages(switch = False, _id = 0, _type = 0, _id1 = 0, _id2 = 0) :
    if (switch) :
        return "aem " + str(_id) + " " + get_id(emoji_id_set, 0, 10000) + " " + str(_type) + " " + str(_id1) + " " + str(_id2)
    id = get_id(msg_id_set)
    type = get_type()
    emoji_id = get_id(emoji_id_set, 0, 10000) 
    if (type == '0') :
        id1, id2 = get_double_person()
        if (id not in msg_id_set and id1 in person_id_set and id2 in person_id_set and id1 != id2 and emoji_id in emoji_id_set) :
            msg_id_set.add(id)
            emoji_msg_id_set.add(id)
            msg_info[id] = (type, id1, id2, emoji_id)
            
        return "aem " + id + " " + emoji_id + " " + type + " " + id1 + " " + id2
    else :
        person_id, group_id = get_person_group()
        if (id not in msg_id_set and person_id in person_id_set and group_id in group_id_set and emoji_id in emoji_id_set) :
            msg_id_set.add(id)
            emoji_msg_id_set.add(id)
            msg_info[id] = (type, person_id, group_id, emoji_id)
        return "aem " + id + " " + emoji_id + " " + type + " " + person_id + " " + group_id


def clean_notices(switch = False, _id = 0) :
    if (switch) :
        return "cn " + str(_id) 
    id = get_id(person_id_set)
    return "cn " + id


def delete_cold_emoji(switch = False, _limit = 0) :
    if (switch) :
        return "dce " + str(_limit)
    limit = random.randint(0, max_heat)
    rec = set()
    for emoji_id in emoji_id_set :
        if (emoji_heat_map[emoji_id] < limit) :
            rec.add(emoji_id)
    for emoji_id in rec :
        emoji_id_set.remove(emoji_id)
        emoji_heat_map.pop(emoji_id)

    rec = set()
    for msg_id in emoji_msg_id_set :
        emoji_id = msg_info[msg_id][3]
        if (emoji_id not in emoji_id_set) :
            rec.add(msg_id)

    for msg_id in rec :
        emoji_msg_id_set.remove(msg_id)
        msg_id_set.remove(msg_id)
    return "dce " + str(limit)  


def send_message(switch = False, _id = 0) :
    if (switch) :  
        return "sm " + str(_id)
    global max_heat
    id = get_id(msg_id_set) 
    if (id in msg_id_set) :
        if (emoji_msg_id_set and random.uniform(0, 1) < 0.4) :
            id = get_exist_id(emoji_msg_id_set)
        type, id1, id2 = msg_info[id][:3]
        if (id in emoji_msg_id_set and msg_info[id][3] in emoji_id_set) :
            emoji_id = msg_info[id][3]
            emoji_heat_map[emoji_id] += 1
            if (emoji_heat_map[emoji_id] > max_heat) : max_heat = emoji_heat_map[emoji_id]
        if ((type == '0' and (id1 in link_map[id2] or id1 == id2)) or 
            (type == '1' and id1 in group_map[id2])) :
            msg_id_set.remove(id)
            if (id in notice_msg_id_set) : notice_msg_id_set.remove(id)
            if (id in money_msg_id_set) : money_msg_id_set.remove(id)
            if (id in emoji_msg_id_set) : emoji_msg_id_set.remove(id)
            msg_info.pop(id)
    return "sm " + id


def send_indirect_message(switch = False, _id = 0) :
    if (switch) :  
        return "sim " + str(_id)
    global max_heat
    id = get_id(msg_id_set) 
    if (id in msg_id_set) :
        if (emoji_msg_id_set and random.uniform(0, 1) < 0.4) :
            id = get_exist_id(emoji_msg_id_set)
        type, id1, id2 = msg_info[id][:3]
        if (id in emoji_msg_id_set and msg_info[id][3] in emoji_id_set) :
            emoji_id = msg_info[id][3]
            emoji_heat_map[emoji_id] += 1
            if (emoji_heat_map[emoji_id] > max_heat) : max_heat = emoji_heat_map[emoji_id]
        if (type == '0' and disjoint_set.is_circle(id1, id2)) :
            msg_id_set.remove(id)
            if (id in notice_msg_id_set) : notice_msg_id_set.remove(id)
            if (id in money_msg_id_set) : money_msg_id_set.remove(id)
            if (id in emoji_msg_id_set) : emoji_msg_id_set.remove(id)
            msg_info.pop(id)
    return "sim " + id


def store_emoji_id(switch = False, _id = 0) :
    if (switch) :
        return "sei " + str(_id) 
    id = get_id(emoji_id_set, 0, 10000)
    if (id not in emoji_id_set) :
        emoji_id_set.add(id)
        emoji_heat_map[id] = 0
    return "sei " + id


def query_popularity(switch = False, _id = 0) :
    if (switch) :
        return "qp " + str(_id) 
    id = get_id(emoji_id_set, 0, 10000)
    return "qp " + id

def query_money(switch = False, _id = 0) :
    if (switch) :
        return "qm " + str(_id)  
    id = get_id(person_id_set)
    return "qm " + id

def query_social_value(switch = False, _id = 0) : 
    if (switch) :   
        return "qsv " + str(_id)
    id = get_id(person_id_set)
    return "qsv " + id


def query_received_messages(switch = False, _id = 0) :   
    if (switch) : 
        return "qrm " + str(_id)
    id = get_id(person_id_set)
    return "qrm " + id


def query_least_connection(switch = False, _id = 0) :   
    if (switch) : 
        return "qlm " + str(_id)
    id = get_id(person_id_set)
    return "qlm " + id

###############################
def modify_relation(switch = False, _id1 = 0, _id2 = 0):
    if (switch) :
        return "mr " + str(_id1) + " " + str(_id2) + " " + get_value()
    id1, id2 = get_double_person()
    if (id1 in person_id_set and id2 in person_id_set and id2 not in link_map[id1]) :
        link_map[id1].append(id2)
        link_map[id2].append(id1)
        disjoint_set.union(id1, id2)
    return "mr " + id1 + " " + id2 + " " + get_value()
    
def query_best_acquaintance(switch = False, _id = 0):
    if (switch) : 
        return "qba " + str(_id)
    id = get_id(person_id_set)
    return "qba " + id

def query_couple_sum():
    return "qcs"

def get_instr(instr) :
    if (instr == 'ap') :
        return add_person()
    elif (instr == 'ar') :
        return add_relation()
    elif (instr == 'qv') :
        return query_value()
    elif (instr == 'qps') :
        return query_people_sum()
    elif (instr == 'qci') :
        return query_circle()
    elif (instr == 'qbs') :
        return query_block_sum()
    elif (instr == 'qts') :
        return query_triple_sum()
    elif (instr == 'ag') :
        return add_group()
    elif (instr == 'atg') :
        return add_to_group()
    elif (instr == 'dfg') :
        return del_from_group()
    elif (instr == 'qgps') :
        return query_group_people_sum()
    elif (instr == 'qgvs') :
        return query_group_value_sum()
    elif (instr == 'qgav') :
        return query_group_age_var() 
    elif (instr == 'am') :
        return add_message()
    elif (instr == 'sm') :
        return send_message() 
    elif (instr == 'qsv') :
        return query_social_value()
    elif (instr == 'qrm') :
        return query_received_messages()
    elif (instr == 'qlm') :
        return query_least_connection()
    elif (instr == 'arem') :
        return add_red_envelope_messages()
    elif (instr == 'anm') :
        return add_notice_messages()
    elif (instr == 'cn') :
        return clean_notices()
    elif (instr == 'aem') :
        return add_emoji_messages()
    elif (instr == 'sei') :
        return store_emoji_id()
    elif (instr == 'qp') :
        return query_popularity()
    elif (instr == 'dce') :
        return delete_cold_emoji()
    elif (instr == 'qm') :
        return query_money()
    elif (instr == 'sim') :
        return send_indirect_message()
    elif (instr=='mr'):
        return modify_relation()
    elif (instr=='qba'):
        return query_best_acquaintance()
    elif (instr=='qcs'):
        return query_couple_sum()

if __name__ == '__main__':
    n = instr_num
    for i in range(n) :
        instr_type = random.choice(instr_list)
        while (instr_type in instr_limit.keys() and instr_limit[instr_type] == 0) :
            instr_type = random.choice(instr_list)
        if (instr_type in instr_limit.keys()) :
            instr_limit[instr_type] -= 1    
        instr = get_instr(instr_type)
        print(instr)
        



    
