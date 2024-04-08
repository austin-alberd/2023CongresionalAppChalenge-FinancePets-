#library imports
import customtkinter, sys
from PIL import Image

#fonts

#A function that calculates the happiness value of the pet
def calc_happiness_value(data_list):
    happinesVal=0
    print(data_list)
    #savings
    if data_list[0] == 0: happinesVal=happinesVal-25
    if 1<= data_list[0] <=70: happinesVal=happinesVal +10
    if 71<= data_list[0] <=500: happinesVal=happinesVal +15
    if 500<= data_list[0]<=1000: happinesVal=happinesVal +20
    if data_list[0]>1000: happinesVal=happinesVal +25
    #Emergency Fund
    if data_list[0] == 0: happinesVal=happinesVal-25
    if 1<= data_list[1] <=70: happinesVal=happinesVal +10
    if 71<= data_list[1] <=500: happinesVal=happinesVal +15
    if 500<= data_list[1]<=1000: happinesVal=happinesVal +20
    if data_list[1]>1000: happinesVal=happinesVal +25
    #debt
    if data_list[2] ==0:happinesVal=happinesVal+25
    if 1<= data_list[2] <=70: happinesVal=happinesVal -10
    if 71<= data_list[2] <=500: happinesVal=happinesVal -15
    if 500<= data_list[2]<=1000: happinesVal=happinesVal -20
    if data_list[2]>1000: happinesVal=happinesVal -25

    #Credit Cards
    if data_list[3] == 0:happinesVal=happinesVal+25
    if 1<= data_list[3] <=3: happinesVal=happinesVal-10
    if 4<= data_list[3] <=5: happinesVal=happinesVal- 20
    if data_list[3] >6: happinesVal=happinesVal-25

    return happinesVal

#Tab View

# front end
class DataInputFrame(customtkinter.CTkFrame):
    def __init__(self, master,**kwargs):
        super().__init__(master, **kwargs)
        font_weight=15
        #configure rows and columns
        self.rowconfigure((0,5),weight=1)
        self.columnconfigure((0,2),weight=1)

        # title label
        self.title_label=customtkinter.CTkLabel(self,text="Finance Food",font=customtkinter.CTkFont(size=40,weight="bold"))
        self.title_label.grid(row=0,column=1)

        #Data Input Fields
        #savings
        self.svngs_label=customtkinter.CTkLabel(self,text="Amount In Savings",font=customtkinter.CTkFont(size=font_weight))
        self.svngs_textbox=customtkinter.CTkTextbox(self,width=100,height=35)
        self.svngs_label.grid(row=1,column=1)
        self.svngs_textbox.grid(row=1,column=2)

        #emergency fund
        self.emfund_label=customtkinter.CTkLabel(self,text="Amount In Emergency Fund",font=customtkinter.CTkFont(size=font_weight))
        self.emfund_textbox=customtkinter.CTkTextbox(self,width=100,height=35)
        self.emfund_label.grid(row=2,column=1)
        self.emfund_textbox.grid(row=2,column=2)   

        #Debt
        self.debt_label=customtkinter.CTkLabel(self,text="Amount of Debt",font=customtkinter.CTkFont(size=font_weight))
        self.debt_textbox=customtkinter.CTkTextbox(self,width=100,height=35)
        self.debt_label.grid(row=4,column=1)
        self.debt_textbox.grid(row=4,column=2)    

        #Credit Cards
        self.ccards_label=customtkinter.CTkLabel(self,text="Number of Credit Cards",font=customtkinter.CTkFont(size=font_weight))
        self.ccards_textbox=customtkinter.CTkTextbox(self,width=100,height=35)
        self.ccards_label.grid(row=5,column=1)
        self.ccards_textbox.grid(row=5,column=2)

        #prefill data based on saved data from the data.txt file
        file=open("data.txt","r+")
        list=file.readline().split("[")[1].split("]")[0].split(",")
        for x in range(len(list)):
            list[x]=float(list[x])
        file.close()
        self.svngs_textbox.insert("0.0",str(list[0]))
        self.emfund_textbox.insert("0.0",str(list[1]))
        self.debt_textbox.insert("0.0",str(list[2]))
        self.ccards_textbox.insert("0.0",str(list[3]))

    def export_data(self):
        #SVNGS EMFUND DEBT CCARDS
        #this is here to make sure that everything goes good with output so the code doesn't break
        try:
            if self.svngs_textbox.get("0.0","end").split('\n')[0] !='' and self.emfund_textbox.get("0.0","end").split('\n')[0] != '' and self.debt_textbox.get("0.0","end").split('\n')[0] !='' and self.ccards_textbox.get("0.0","end").split('\n')[0] != '':
                return[float(self.svngs_textbox.get("0.0","end").split('\n')[0]),float(self.emfund_textbox.get("0.0","end").split('\n')[0]),float(self.debt_textbox.get("0.0", "end").split('\n')[0]),float(self.ccards_textbox.get("0.0", "end").split('\n')[0])]
        except:
            return [0,0,0,0]
    
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
    file_obj=open("data.txt","r+")
    file_obj.truncate()
    file_obj.write(str(app.dif.export_data()))
    file_obj.close()
    sys.exit()

#initialize the app class
app = App()
update_master_function()

# run the program and handle the when closed event
app.protocol("WM_DELETE_WINDOW",save_on_close)
app.mainloop()