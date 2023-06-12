import random
import sys
import names

instr_list = ['ap', 'ar', 'qv', 'qci', 'qbs','qts']
person_id_set = set()
group_id_set = set()
link_map = {}
group_map = {}
# MAX_INT=2147483648
MAX_INSTR=10000
MAX_INT=9

def get_unexist_id(id_set) :
    id = random.randint(-MAX_INT, MAX_INT-1)
    while (id in id_set) :
        id = random.randint(-MAX_INT, MAX_INT-1)
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
    age = random.randint(0, 201)
    return str(age)

def get_value() :
    value = random.randint(1, 101)
    return str(value)

def get_instr() :
    instr = random.choice(instr_list)
    if (instr == 'ap') :
        return add_person(instr)
    elif (instr == 'ar') :
        return add_relation(instr)
    elif (instr == 'qv') :
        return query_value(instr)
    elif (instr == 'qci') :
        return query_circle(instr)
    elif (instr == 'qbs') :
        return instr 
    elif (instr == 'qts') :
        return instr


def add_person(instr) :
    prob = random.uniform(0, 1)
    id = get_unexist_id(person_id_set)
    if (prob < 0.4) :
        if (person_id_set) :
            id = get_exist_id(person_id_set)
    else :
        id = get_unexist_id(person_id_set)
        person_id_set.add(id)
        link_map[id] = []
    return instr + " " + id + " " + get_name() + " " + get_age()

def add_relation(instr) :
    prob = random.uniform(0, 1)
    id1 = get_unexist_id(person_id_set)
    id2 = get_unexist_id(person_id_set)
    if (prob < 0.2) :
        id1 = get_unexist_id(person_id_set)
        id2 = str(random.randint(-2147483648, 2147483647))
    elif (prob < 0.4) :
        if (person_id_set) :
            id1 = get_exist_id(person_id_set)
        id2 = get_unexist_id(person_id_set)
    elif (prob < 0.6) :
        if (person_id_set) :
            id1 = get_exist_id(person_id_set)
            if (link_map[id1]) :
                id2 = random.choice(link_map[id1])
            else :
                id2 = id1
        
    else :
        if (person_id_set) :
            id1 = get_exist_id(person_id_set)
            id2 = get_exist_id(person_id_set)
            if (len(link_map[id1]) + 1 < len(person_id_set)) :
                while (id2 in link_map[id1]) :
                    id2 = get_exist_id(person_id_set)
                link_map[id1].append(id2)
                link_map[id2].append(id1)
    return instr + " " + id1 + " " + id2 + " " + get_value()

def query_value(instr) :
    prob = random.uniform(0, 1)
    id1 = get_unexist_id(person_id_set)
    id2 = get_unexist_id(person_id_set)
    if (prob < 0.2) :
        id1 = get_unexist_id(person_id_set)
        id2 = str(random.randint(-2147483648, 2147483647))
    elif (prob < 0.4) :
        if (person_id_set) :
            id1 = get_exist_id(person_id_set)
        id2 = get_unexist_id(person_id_set)
    elif (prob < 0.6) :
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
                id2 = random.choice(link_map[id1])
            else :
                id2 = id1 
    return instr + " " + id1 + " " + id2 

def query_circle(instr) :
    prob = random.uniform(0, 1)
    id1 = get_unexist_id(person_id_set)
    id2 = get_unexist_id(person_id_set)
    if (prob < 0.2) :
        id1 = get_unexist_id(person_id_set)
        id2 = str(random.randint(-2147483648, 2147483647))
    elif (prob < 0.4) :
        if (person_id_set) :
            id1 = get_exist_id(person_id_set)
        id2 = get_unexist_id(person_id_set)
    else :
        if (person_id_set) :
            id1 = get_exist_id(person_id_set)
            id2 = get_exist_id(person_id_set)
    return instr + " " + id1 + " " + id2 

if __name__ == '__main__':
    n = random.randint(10,MAX_INSTR)
    # n=30
    for i in range(n) :
        instr = get_instr()
        print(instr)
