import customtkinter
from PIL import Image
from time import sleep as s

# front end
class DataInputFrame(customtkinter.CTkFrame):
    def __init__(self, master,**kwargs):
        super().__init__(master, **kwargs)
        self.rowconfigure(0,weight=1)
        self.rowconfigure(1,weight=1)
        self.rowconfigure(2,weight=1)
        self.rowconfigure(3,weight=1)
        self.rowconfigure(4,weight=1)
        self.rowconfigure(5,weight=1)
        self.columnconfigure(0,weight=1)
        self.columnconfigure(1,weight=1)
        self.columnconfigure(2,weight=1)

        # title label
        self.title_label=customtkinter.CTkLabel(self,text="Finance Food",font=customtkinter.CTkFont(size=40,weight="bold"))
        self.title_label.grid(row=0,column=1)

        #List thingy mabob
        #savings
        self.svngs_checkbox= customtkinter.CTkCheckBox(self,text='')
        self.svngs_label=customtkinter.CTkLabel(self,text="Amount In Savings")
        self.svngs_textbox=customtkinter.CTkTextbox(self,width=100,height=35)
        self.svngs_checkbox.grid(row=1,column=0)
        self.svngs_label.grid(row=1,column=1)
        self.svngs_textbox.grid(row=1,column=2)

        #emergency fund
        self.emfund_checkbox= customtkinter.CTkCheckBox(self,text='')
        self.emfund_label=customtkinter.CTkLabel(self,text="Amount In Emergency Fund")
        self.emfund_textbox=customtkinter.CTkTextbox(self,width=100,height=35)
        self.emfund_checkbox.grid(row=2,column=0)
        self.emfund_label.grid(row=2,column=1)
        self.emfund_textbox.grid(row=2,column=2)   

        #Debt
        self.debt_checkbox= customtkinter.CTkCheckBox(self,text='')
        self.debt_label=customtkinter.CTkLabel(self,text="Amount of Debt")
        self.debt_textbox=customtkinter.CTkTextbox(self,width=100,height=35)
        self.debt_checkbox.grid(row=4,column=0)
        self.debt_label.grid(row=4,column=1)
        self.debt_textbox.grid(row=4,column=2)    

        #Credit Cards
        self.ccards_checkbox= customtkinter.CTkCheckBox(self,text='')
        self.ccards_label=customtkinter.CTkLabel(self,text="Number of Credit Cards")
        self.ccards_textbox=customtkinter.CTkTextbox(self,width=100,height=35)
        self.ccards_checkbox.grid(row=5,column=0)
        self.ccards_label.grid(row=5,column=1)
        self.ccards_textbox.grid(row=5,column=2)

        #prefill
        self.svngs_textbox.insert("0.0","0")
        self.emfund_textbox.insert("0.0","0")
        self.debt_textbox.insert("0.0", "0")
        self.ccards_textbox.insert("0.0","0")


    def update_data(self):
        if self.svngs_textbox.get("0.0","end").split('\n')[0] =='':self.svngs_textbox.insert("0.0","0") 
        if self.ccards_textbox.get("0.0","end").split('\n')[0] =='':self.emfund_textbox.insert("0.0","0")
        if self.debt_textbox.get("0.0","end").split('\n')[0] =='':self.debt_textbox.insert("0.0", "0")
        if self.emfund_textbox.get("0.0","end").split('\n')[0] =='':self.ccards_textbox.insert("0.0","0")
    
    def export_data(self):
        #SVNGS EMFUND DEBT CCARDS
        return[float(self.svngs_textbox.get("0.0","end").split('\n')[0]),float(self.emfund_textbox.get("0.0","end").split('\n')[0]),float(self.debt_textbox.get("0.0", "end").split('\n')[0]),float(self.ccards_textbox.get("0.0", "end").split('\n')[0])]
    
class PetStatsFrame(customtkinter.CTkFrame):
    def __init__(self,master,**kwargs):
        super().__init__(master,**kwargs)
        self.rowconfigure(0,weight=1)
        self.rowconfigure(1,weight=1)
        self.rowconfigure(2,weight=1)
        self.rowconfigure(3,weight=1)
        self.columnconfigure(0,weight=1)
        self.columnconfigure(1,weight=1)
        self.columnconfigure(2,weight=1)

        self.title_lable=customtkinter.CTkLabel(self, text="Pet Stats",font=customtkinter.CTkFont(size=40,weight="bold"))
        self.title_lable.grid(row=0,column=2)

        self.happiness_label=customtkinter.CTkLabel(self,text="Happiness")
        self.happiness_data_label=customtkinter.CTkLabel(self,text='100%')#test data will update later
        self.happiness_data_label.grid(row=1,column=1)
        self.happiness_label.grid(row=1,column=0,padx=10)
        
    def update_data(self,data_list):
        #SVNGS EMFUND DEBT CCARDS
        happinesVal=0
        if data_list[0] == 0: happinesVal=happinesVal-25
        if data_list[0] <=10: happinesVal=happinesVal+10
        if data_list[0] <=1000: happinesVal=happinesVal+15
        if data_list[0] <=10000: happinesVal=happinesVal+25

        if data_list[1] == 0: happinesVal=happinesVal-25
        if data_list[1] <=10: happinesVal=happinesVal+10
        if data_list[1] <=1000: happinesVal=happinesVal+15
        if data_list[1] <=10000: happinesVal=happinesVal+25

        if data_list[2] == 0: happinesVal=happinesVal+25
        if data_list[2] <=1000: happinesVal=happinesVal-10
        if data_list[2] >= 10000: happinesVal=happinesVal-25

        if data_list[3] ==0: happinesVal=happinesVal+25
        if data_list[3] >=3: happinesVal=happinesVal-25

        self.happiness_data_label.configure(text=f"{happinesVal}%")


class ButtonFrame(customtkinter.CTkFrame):
    def __init__(self, master,**kwargs):
        super().__init__(master, **kwargs)
        self.rowconfigure(0,weight=1)
        self.rowconfigure(1,weight=1)
        self.columnconfigure(0,weight=1)
        self.columnconfigure(1,weight=1)
        self.columnconfigure(2,weight=1)

        self.title_label=customtkinter.CTkLabel(self,text="Settings",font=customtkinter.CTkFont(size=40,weight="bold"))
        self.title_label.grid(row=0,column=1,columnspan=2)

        #buttons
        self.save_button=customtkinter.CTkButton(self,text="Save Current Data")
        self.save_button.grid(row=1,column=0)

class PetIMGFrame(customtkinter.CTkFrame):
    def __init__(self, master,**kwargs):
        super().__init__(master, **kwargs)
        image_thing=customtkinter.CTkImage(light_image=Image.open("tombstone.png"),dark_image=Image.open("tombstone.png"),size=(350,350))
        self.label=customtkinter.CTkLabel(self,text='',image=image_thing)
        self.label.pack()

    def update_data(self):
        pass

class App(customtkinter.CTk):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.geometry("1000x500")
        self.title("Finance Pet")
        self.rowconfigure(0,weight=1)
        self.rowconfigure(1,weight=1)
        self.rowconfigure(2,weight=1)
        self.rowconfigure(3,weight=1)
        self.rowconfigure(4,weight=1)
        self.columnconfigure(0,weight=1)
        self.columnconfigure(1,weight=1)
        self.columnconfigure(2,weight=1)

        #Other Frames
        self.dif=DataInputFrame(self)
        self.dif.grid(row=0,column=0,pady=25)

        self.setf=ButtonFrame(self)
        self.setf.grid(row=1,column=0)

        self.psf=PetStatsFrame(self)
        self.psf.grid(row=1,column=1)
        
        self.pif=PetIMGFrame(self)
        self.pif.grid(row=0,column=1)

def update_master_function():
    app.dif.update_data()
    s(5)
    data=app.dif.export_data()
    app.psf.update_data(data)
    app.pif.update_data()

    app.after(10000,update_master_function)


app = App()
update_master_function()

if __name__ == "__main__":
    app.mainloop()