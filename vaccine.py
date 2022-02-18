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
        
def vacc_check_1(vac_list,child,today_date):
    print("in function vac_check_1")
    print("AGE OF CHILD = {}".format(child.age))
    print("list of vaccines before updating "+str(list(child.vacc_det)))
    remain_vacc = [x for x in vac_list if( x.id not in list((child.vacc_det).keys()))] #MADE THE VACC_DET OF CHILD INTO A LIST FROM A DICTIONARY BEFORE COMPARING

    eligible_vacc = [x for x in remain_vacc if ((x.min_age < child.age) and x.max_age>child.age)]

    if(len(eligible_vacc)>0):
        print("eligible vacc found")
        for i in range(len(eligible_vacc)):
            child.vacc_det.update({eligible_vacc[i].id:today_date})
        print("list of vaccine after updating "+ str(list(child.vacc_det.keys())))


        return True
    else:
        return False

def vacc_check_all(vac_list , childs,today_date):
    count = 0
    print("in function vac_check_all")
    for i in range(len(childs)):
        b = vacc_check_1(vac_list,childs[i],today_date)
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
        childs.append(child(name,dob,age,vacc_det)) #WE DID NOT UPDATE CHILDS WHILE TAKING INPUT

    today_date = input()


    a = vacc_check_all(vac_list,childs,today_date)
    print("number of children vaccined is "+str(a))
    #gopal has small banana
