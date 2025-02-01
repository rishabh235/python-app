#oops modules
class Employee(object):
    #constructor used to ini the data at time of initialisation 
    def __init__(self,empno,ename,salary):
        self.eno=empno   #instance variables/properties
        self.name=ename
        self.pay=salary
        #self.bonus=10000  #public property
        self.__bonus=50000 #private property
        

    def showDetails(self):
        print('Empno:',self.eno)
        print('Empname:',self.name)
        print('Salary:',self.pay)
        print('total amt:',self.pay+self.__bonus)

#------------------------------------------   
if __name__=='__main__':     
    e1= Employee(101,"Rishabh",50000)
    e1.showDetails()
    e2= Employee(102,"Sinha",90000)
    e2.showDetails()
    e1.bonus=50000
    print(e1.__bonus)    