import sqlite3
from tkinter import *
from tkinter import ttk
from tkinter.ttk import *

def testing():
    i=e1.get()
    l=list_status.get()
    dd=list_user.get()
    df=list_env_1.get()
    dg=list_env_2.get()
    
    
    conn = sqlite3.connect("RELEASE_DB_1.db")
    #conn1 = sqlite3.connect("RELEASE_DB.db")
    c1=conn.cursor()
    c2=conn.cursor()
    c3=conn.cursor()
    
    c1.execute(" select user_no from user where user_name =? ",(dd,))
    user_no=c1.fetchall()
    
    c2.execute(" select env_no from environment where env_name =?",(df,))
    env_no=c2.fetchall()
    
    c3.execute(" select env_no from environment where env_name =?",(dg,))
    env_no_1=c3.fetchall()
    
    
    
    print(user_no)
    
    try:
        c1.execute('''insert into monthly_release (release_name,user_id, dev_env, test_env, release_status ) values(?,?,?,?,?)''', (i,user_no[0][0],env_no[0][0],env_no_1[0][0],l))
    except sqlite3.IntegrityError as e:
        print('sqlite error: ', e.args[0]) # column name is not unique
        

    conn.commit()
    conn.close() 
    
    
    
def Hotfix() :
    

    i=list_rel.get()
    j=list_user_1.get()
    k=f1.get()
    
    conn = sqlite3.connect("RELEASE_DB_1.db")
    
    c1=conn.cursor()
    c2=conn.cursor()
    c3=conn.cursor()
    
    
    c1.execute(" select user_no from user where user_name =? ",(j,))
    user_no_1=c1.fetchall()
    
    c2.execute(" select release_no from monthly_release where release_name =? ",(i,))
    rel_no=c2.fetchall()
    
    try:
        c3.execute('''insert into hotfix (hf_name, release_id, user_id ) values(?,?,?)''', (k,rel_no[0][0],user_no_1[0][0]))
    except sqlite3.IntegrityError as e:
        print('sqlite error: ', e.args[0]) # column name is not unique
        
        
        
    conn.commit()
    conn.close()  
    
    


def User_1() :
    
    i=g1.get()
    
    conn = sqlite3.connect("RELEASE_DB_1.db")
    c1=conn.cursor()
    
    print(type(i))
    try:
        c1.execute('''insert into user (user_name) values(?)''', [i])
    except sqlite3.IntegrityError as e:
        print('sqlite error: ', e.args[0]) # column name is not unique
        
    print(i)    
        
    conn.commit()
    conn.close()  


    
def enrich():
        
    i=list_user_2.get()
    j=list_rel_1.get()
    k=h1.get()
    l=h2.get()
    
    conn = sqlite3.connect("RELEASE_DB_1.db")
    
    
    c2=conn.cursor()
    c3=conn.cursor()
   
    
    c2.execute(" select release_no from monthly_release where release_name =? ",(j,))
    rel_no_1=c2.fetchall()
    try:
        c3.execute('''insert into enrichment (date, user, release_id, review_status ) values(?,?,?,?)''', (k,i,rel_no_1[0][0],l))
    except sqlite3.IntegrityError as e:
        print('sqlite error: ', e.args[0]) # column name is not unique

        
    conn.commit()
    conn.close()  
    
    
def plan():
    
    i=i1.get()  
    j=i2.get()
    k=i3.get()
    l=i4.get()
    m=list_activity.get()
    n=list_release.get()
    
    conn= sqlite3.connect("RELEASE_DB_1.db")
    
    c1=conn.cursor()
    c2=conn.cursor()
    c3=conn.cursor()
    
    c1.execute(" select activity_no from activity where activity_name=? "(m,))
    act=c1.fetchall()
    
    c2.execute(" select release_no from monthly_release where release_name=? "(n,))
    rel=c2.fetchall()
    
    try:
        c3.execute('''insert into plan (activity_id,planned_date, actual_date, status , comment, release_id) values(?,?,?,?,?,?)''', (act[0][0],i,j,k,l,rel[0][0]))
    except sqlite3.IntegrityError as e:
        print('sqlite error: ', e.args[0]) # column name is not unique

        
    conn.commit()
    conn.close()    
    
    
    
    
    
    
    
    

#code for GUI
main = Tk()
main.title('AM object tracker')
tab_control=ttk.Notebook()

########################################

conn = sqlite3.connect("RELEASE_DB_1.db")
c2=conn.cursor()
c3=conn.cursor()
c4=conn.cursor()
c5=conn.cursor()

c2.execute("select USER_NAME from USER")         #user table
user = c2.fetchall()

c3.execute("select env_name from environment")   #environment
env =c3.fetchall()

c4.execute("select release_name from monthly_release")      #release_name
rel= c4.fetchall()

c5.execute("select activity_name from activity")      #activity
act= c5.fetchall()



########################################

tab_1 = ttk.Frame(tab_control)
tab_2 = ttk.Frame(tab_control)
tab_3 = ttk.Frame(tab_control)
tab_4 = ttk.Frame(tab_control)
tab_5 = ttk.Frame(tab_control)
tab_6 = ttk.Frame(tab_control)

tab_control.add(tab_1,text='Release')
tab_control.add(tab_2,text='Hotfix')
tab_control.add(tab_3,text='User')
tab_control.add(tab_4,text='enrichment')
tab_control.add(tab_5,text='Plan')
tab_control.add(tab_6,text='object')



tab_control.pack(expand=1, fill='both')

## tab_Release ##

Label(tab_1, text ="release name").grid(row=0)
Label(tab_1, text ="user_id").grid(row=1)
Label(tab_1, text ="dev_env").grid(row=2)
Label(tab_1, text ="test_env").grid(row=3)
Label(tab_1, text ="release_status").grid(row=4)


###########
list_user=ttk.Combobox(tab_1, width=17 , height = 20)  # user dropdown
list_user['values']=user
list_user.grid(row=1,column=1)

list_env_1=ttk.Combobox(tab_1, width=17 , height = 20)     # dev dropdown
list_env_1['values']=env
list_env_1.grid(row=2,column=1)


list_env_2=ttk.Combobox(tab_1, width=17 , height = 20)     # test dropdown
list_env_2['values']=env
list_env_2.grid(row=3,column=1)

list_status=ttk.Combobox(tab_1, width=17 , height = 20)     # Release status
list_status['values']=('Y','N')
list_status.grid(row=4,column=1)
############

e1=Entry(tab_1)
e1.grid(row=0, column=1)

Button(tab_1, text='Finish', command=testing).grid(row=5, column=0, sticky=W, pady=4)


# # tab_Hotfix # #

Label(tab_2,text="Hotfix Name").grid(row =0)
Label(tab_2,text="release_id").grid(row =1)
Label(tab_2,text="user_id").grid(row =2)

f1=Entry(tab_2)
f1.grid(row=0, column=1)

rel_1=[]
for k in rel:
    rel_1.append(k[0]) 

##
list_rel=ttk.Combobox(tab_2, width=17 , height = 20)  #release
list_rel['values']=rel_1
list_rel.grid(row=1,column=1)

list_user_1=ttk.Combobox(tab_2, width=17 , height = 20)  #user dropdown
list_user_1['values']=user
list_user_1.grid(row=2,column=1)

Button(tab_2, text='Finish', command=Hotfix).grid(row=3, column=0, sticky=W, pady=4)


# # user tab # #


Label(tab_3, text ="User name").grid(row=0)

g1=Entry(tab_3)
g1.grid(row=0, column=1)


Button(tab_3, text='Finish', command=User_1).grid(row=1, column=0, sticky=W, pady=4)




# # enrichment # #


Label(tab_4, text = "Date").grid(row=0)
Label(tab_4, text = "user_id").grid(row=1)
Label(tab_4, text = "release_id").grid(row=2)
Label(tab_4, text = "review_status").grid(row=3)

h1=Entry(tab_4)
h1.grid(row=0, column=1)

h2=Entry(tab_4)
h2.grid(row=3, column=1)

#####

list_user_2=ttk.Combobox(tab_4, width=17 , height = 20)  #user dropdown
list_user_2['values']=user
list_user_2.grid(row=1,column=1)




list_rel_1=ttk.Combobox(tab_4, width=17 , height = 20)  #release
list_rel_1['values']=rel_1
list_rel_1.grid(row=2,column=1)
#####

Button(tab_4, text="Finish" , command=enrich).grid(row=4, column =0, sticky =W, pady=4)


# # Plan # #

Label(tab_5, text = "activity_id").grid(row=0)
Label(tab_5, text = "planned_date").grid(row=1)
Label(tab_5, text = "actual_date").grid(row=2)
Label(tab_5, text = "status").grid(row=3)
Label(tab_5, text = "comment").grid(row=4)
Label(tab_5, text = "release_id").grid(row=5)


list_activity=ttk.Combobox(tab_5, width=17 , height = 20)  #activity_id dropdown


activity=[]
for i in act:
    activity.append(i[0])                   #to remove the curly braces from dropdown
    
    
list_activity['values']=activity
list_activity.grid(row=0,column=1)

i1=Entry(tab_5)
i1.grid(row=1,column=1)

i2=Entry(tab_5)
i2.grid(row=2,column=1)

i3=Entry(tab_5)
i3.grid(row=3,column=1)

i4=Entry(tab_5)
i4.grid(row=4,column=1)

 

list_release=ttk.Combobox(tab_5, width=17 , height = 20)  #release dropdown
list_release['values']=rel_1
list_release.grid(row=5,column=1)

Button(tab_5 , text="Finish", command=plan).grid(row=6, column=0, sticky=W, pady=4)


# # object # #






mainloop()
