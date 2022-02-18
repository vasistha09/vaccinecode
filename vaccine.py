class vaccine:
    def __init__(self,id,name,min_age,max_age):
        self.id = id
        self.name = name
        self.min_age= min_age
        self.max_age=max_age
        
        
class child:
    def __init__(self, name,dob,age,vacc_det):
        self.name = name
        self.dob = dob
        self.age = age
        self.vacc_det = vacc_det
        
def vacc_check_1(vac_list,child):
    remain_vacc = [x for x in vac_list if( x.id not in child.vacc_det)]
    eligible_vacc = [x for x in remain_vacc if (x.min_age < child.age and x.max_age>child.age)]
    if(eligible_vacc):
        for i in range(len(eligible_vacc)):
            child.vacc_det.update({eligible_vacc.id == today_date } )
        return True
    else:
        return False

def vacc_check_all(vac_list , childs):
    count = 0
    for i in range(len(childs)):
        b = vacc_check_1(vac_list,childs[i])
        if b == True:
            count = count + 1
    return (count)

if __name__=="__main__":
    vac_list = []
    no_of_vacc = int(input())
    for i in range(no_of_vacc):
        vac_id = int(input())
        vac_name = input()
        min_age = int(input())
        max_age =int(input())
        vac_list.append(vaccine(vac_id,vac_name,min_age,max_age))
    childs = []
    no_of_child = int(input())
    for i in range(no_of_child):
        name =  input()
        dob =  input()
        age =  int(input())
        vacc_det = {}
        for i in range(2):
            vacc_det[int(input())] = 220121
    today_date = int(input())    
    
    a = vacc_check_all(vac_list,childs)
    print(a)    
    
