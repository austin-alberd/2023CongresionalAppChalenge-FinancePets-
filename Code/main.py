#library imports
import customtkinter, sys
from PIL import Image

#fonts

#A function that calculates the happiness value of the pet
def calc_happiness_value(data_list):
    #SVNGS EMFUND DEBT CCARDS MONTHLY_INCOME
    happinesVal=0
    if data_list[4] !=0:
        percent_mi_svngs=(data_list[0]/data_list[4])*100
        dsr=(data_list[2]/data_list[4])*100
        emfund_calc=data_list[1]/data_list[4]
        if percent_mi_svngs>100:percent_mi_svngs=100
        if dsr>100:dsr=100
        if emfund_calc>100:emfund_calc=100
    elif data_list[4] ==0:
        percent_mi_svngs=0
        dsr=0
        emfund_calc=0
    #savings
    if percent_mi_svngs >= 10:happinesVal=happinesVal+3.33
    elif percent_mi_svngs >= 20:happinesVal=happinesVal+6.66
    elif percent_mi_svngs >= 30:happinesVal=happinesVal+10
    elif percent_mi_svngs >= 40:happinesVal=happinesVal+13.33
    elif percent_mi_svngs >= 50:happinesVal=happinesVal+16.66
    elif percent_mi_svngs >= 60:happinesVal=happinesVal+20
    elif percent_mi_svngs >= 70:happinesVal=happinesVal+23.33
    elif percent_mi_svngs >= 80:happinesVal=happinesVal+26.66
    elif percent_mi_svngs >= 90:happinesVal=happinesVal+30
    elif percent_mi_svngs >= 100:happinesVal=happinesVal+33.33
    #Emergency Fund
    if emfund_calc >0 and emfund_calc<=1:happinesVal=happinesVal+5.55
    if emfund_calc>=2:happinesVal=happinesVal+11.11
    if emfund_calc>=3:happinesVal=happinesVal+15.27
    if emfund_calc>=4:happinesVal=happinesVal+19.44
    if emfund_calc>=5:happinesVal+23.61
    if emfund_calc>=6:happinesVal=happinesVal+27.77
    #debt
    if dsr<30:happinesVal=happinesVal+25
    if dsr==30:happinesVal=happinesVal+12.5
    if dsr>30:happinesVal=happinesVal+0

    #Credit Cards
    if data_list[3] >3:happinesVal=happinesVal+0
    if data_list[3] <= 3: happinesVal=happinesVal+25

    if happinesVal>100:
        happinesVal=100
    return round(happinesVal)

#Tab View

# front end
class DataInputFrame(customtkinter.CTkFrame):
    def __init__(self, master,**kwargs):
        super().__init__(master, **kwargs)
        font_weight=15
        #configure rows and columns
        self.rowconfigure((0,6),weight=1)
        self.columnconfigure((0,2),weight=1)

        # title label
        self.title_label=customtkinter.CTkLabel(self,text="Finance Food",font=customtkinter.CTkFont(size=40,weight="bold"))
        self.title_label.grid(row=0,column=1)

        #Data Input Fields
        #savings
        self.svngs_label=customtkinter.CTkLabel(self,text="Amount In Savings",font=customtkinter.CTkFont(size=font_weight))
        self.svngs_textbox=customtkinter.CTkEntry(self,width=100,height=35)
        self.svngs_label.grid(row=1,column=1)
        self.svngs_textbox.grid(row=1,column=2)

        #emergency fund
        self.emfund_label=customtkinter.CTkLabel(self,text="Amount In Emergency Fund",font=customtkinter.CTkFont(size=font_weight))
        self.emfund_textbox=customtkinter.CTkEntry(self,width=100,height=35)
        self.emfund_label.grid(row=2,column=1)
        self.emfund_textbox.grid(row=2,column=2)   

        #Debt
        self.debt_label=customtkinter.CTkLabel(self,text="Amount of Debt",font=customtkinter.CTkFont(size=font_weight))
        self.debt_textbox=customtkinter.CTkEntry(self,width=100,height=35)
        self.debt_label.grid(row=4,column=1)
        self.debt_textbox.grid(row=4,column=2)    

        #Credit Cards
        self.ccards_label=customtkinter.CTkLabel(self,text="Number of Credit Cards",font=customtkinter.CTkFont(size=font_weight))
        self.ccards_textbox=customtkinter.CTkEntry(self,width=100,height=35)
        self.ccards_label.grid(row=5,column=1)
        self.ccards_textbox.grid(row=5,column=2)

        #Monthly Income
        self.mi_label=customtkinter.CTkLabel(self,text="Monthly Income",font=customtkinter.CTkFont(size=font_weight))
        self.mi_textbox=customtkinter.CTkEntry(self,width=100,height=35)
        self.mi_label.grid(row=6,column=1)
        self.mi_textbox.grid(row=6,column=2)

        #prefill data based on saved data from the data.txt file
        with open("data.txt",'r+') as file:
            list=file.readline().split("[")[1].split("]")[0].split(",")
            for x in range(len(list)):
                list[x]=float(list[x])
            self.svngs_textbox.insert("0",str(list[0]))
            self.emfund_textbox.insert("0",str(list[1]))
            self.debt_textbox.insert("0",str(list[2]))
            self.ccards_textbox.insert("0",str(list[3]))
            self.mi_textbox.insert("0",str(list[4]))

    def export_data(self):
        #SVNGS EMFUND DEBT CCARDS MONTHLY_INCOME
        try:
            return [float(self.svngs_textbox.get()),float(self.emfund_textbox.get()),float(self.debt_textbox.get()),float(self.ccards_textbox.get()),float(self.mi_textbox.get())]
        except:
            return [0,0,0,0,0]
    
class PetStatsFrame(customtkinter.CTkFrame):
    def __init__(self,master,**kwargs):
        super().__init__(master,**kwargs)
        #row and column configure
        self.rowconfigure((0,3),weight=1)
        self.columnconfigure((0,2),weight=1)

        #lable configure
        self.title_lable=customtkinter.CTkLabel(self, text="Pet Stats",font=customtkinter.CTkFont(size=40,weight="bold"))
        self.title_lable.grid(row=0,column=1)

        self.happiness_label=customtkinter.CTkLabel(self,text="Happiness",font=customtkinter.CTkFont(size=20))
        self.happiness_data_label=customtkinter.CTkLabel(self,font=customtkinter.CTkFont(size=20))
        self.happiness_data_label.grid(row=3,column=2)
        self.happiness_label.grid(row=3,column=1,padx=10)
        
    def update_data(self,data_list):
        #This function calculates the happines value
        #SVNGS EMFUND DEBT CCARDS
        happinesVal=calc_happiness_value(data_list=data_list)
        #Update the happines value label
        self.happiness_data_label.configure(text=f"{happinesVal}%")

class PetIMGFrame(customtkinter.CTkFrame):
    def __init__(self, master,**kwargs):
        super().__init__(master, **kwargs)
        #this is the label that holds the images
        self.label=customtkinter.CTkLabel(self,text='')
        self.label.pack()

    def update_data(self,metric):
        #based on the metric (happiness value) put the correct image in the label
        if metric <0:
            self.label.configure(image=customtkinter.CTkImage(light_image=Image.open("dead.png"),dark_image=Image.open("dead.png"),size=(350,350)))
        if 0<= metric <=10:
            self.label.configure(image=customtkinter.CTkImage(light_image=Image.open("dead.png"),dark_image=Image.open("dead.png"),size=(350,350)))
        if 11 <= metric <=25 :
            self.label.configure(image=customtkinter.CTkImage(light_image=Image.open("meh.png"),dark_image=Image.open("meh.png"),size=(350,350)))
        if 26<= metric <=50:
            self.label.configure(image=customtkinter.CTkImage(light_image=Image.open("beter.png"),dark_image=Image.open("beter.png"),size=(350,350)))
        if 51<= metric <=75:
            self.label.configure(image=customtkinter.CTkImage(light_image=Image.open("happy.png"),dark_image=Image.open("happy.png"),size=(350,350)))
        if 76 <= metric <= 100:
            self.label.configure(image=customtkinter.CTkImage(light_image=Image.open("amazing.png"),dark_image=Image.open("amazing.png"),size=(350,350)))

#the main window
class App(customtkinter.CTk):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        #main window fancy setup stuff :)
        self.geometry("1000x500")
        self.title("Finance Pets")
        self.rowconfigure((0,4),weight=1)
        self.columnconfigure((0,2),weight=1)

        #Load in the frames previously made above
        self.dif=DataInputFrame(master=self)
        self.dif.grid(row=0,column=0,pady=25)

        self.psf=PetStatsFrame(self)
        self.psf.grid(row=1,column=1)
        
        self.pif=PetIMGFrame(self)
        self.pif.grid(row=0,column=1)

#this function updates the data with real time stuff
def update_master_function():
    data=app.dif.export_data()
    app.psf.update_data(data)
    app.pif.update_data(calc_happiness_value(data))
    app.after(5000,update_master_function)

# this saves the data into the data.txt file when the program is closed
def save_on_close():
    with open("data.txt",'r+') as file:
        file.truncate()
        file.write(str(app.dif.export_data()))
    sys.exit()

#initialize the app class
app = App()
update_master_function()

# run the program and handle the when closed event
app.protocol("WM_DELETE_WINDOW",save_on_close)
app.mainloop()