import requests
import json
from tkinter import*
corona=Tk()
corona.title("COVID19 STATS")

def COVID19():
    global row1
    row1=1
    api_request=requests.get("https://corona.lmao.ninja/countries")
    api=json.loads(api_request.content)
    print(api[42])
    country=["India","Italy","Pakistan","Germany","China","USA","UK","France","Japan"]
    for j in country:
        for i in range(0,183):
            if (j==api[i]["country"]):
                if(j=="India"):
                    print(i)
                name=Label(corona,text=api[i]["country"],bg="grey",fg="black",font="Lato 12 bold",borderwidth=2,padx=2,pady=2,relief="groove")
                name.grid(row=row1,column=0,sticky=N+S+E+W)
                confirm=Label(corona,text=api[i]["cases"],bg="white",fg="black",font="Lato 12",borderwidth=2,padx=2,pady=2,relief="groove")
                confirm.grid(row=row1,column=1,sticky=N+S+E+W)
                death=Label(corona,text=api[i]["deaths"],bg="white",fg="red",font="Lato 12",borderwidth=2,padx=2,pady=2,relief="groove")
                death.grid(row=row1,column=2,sticky=N+S+E+W)
                recov=Label(corona,text=api[i]["recovered"],bg="white",fg="green",font="Lato 12",borderwidth=2,padx=2,pady=2,relief="groove")
                recov.grid(row=row1,column=3,sticky=N+S+E+W)
                mr=api[i]["deaths"]/api[i]["cases"]*100
                mrate=Label(corona,text="{:.2f}".format(mr),bg="grey",fg="black",font="Lato 12 bold",borderwidth=2,padx=2,pady=2,relief="groove")
                mrate.grid(row=row1,column=4,sticky=N+S+E+W)
                row1=row1+1


api=""
update=Button(corona,text="UPDATE",bg="blue",fg="black",font="Lato 12 bold",borderwidth=2,command=COVID19())
update.grid(row=row1,column=4,sticky=N+S+E+W)
name=Label(corona,text="COUNTRY",bg="yellow",fg="black",font="Lato 12 bold",padx="5",pady="5",borderwidth=2)
name.grid(row=0,column=0,sticky=N+S+E+W)
confirm=Label(corona,text="CONFIRMED CASES",bg="orange",fg="black",font="Lato 12 bold",padx="5",pady="5",borderwidth=2)
confirm.grid(row=0,column=1,sticky=N+S+E+W)
death=Label(corona,text="DEATHS",bg="yellow",fg="black",font="Lato 12 bold",padx="5",pady="5",borderwidth=2)
death.grid(row=0,column=2,sticky=N+S+E+W)
recov=Label(corona,text="RECOVERED",bg="orange",fg="black",font="Lato 12 bold",padx="5",pady="5",borderwidth=2)
recov.grid(row=0,column=3,sticky=N+S+E+W)
mrate=Label(corona,text="MORTALITY RATE %",bg="yellow",fg="black",font="Lato 12 bold",padx="5",pady="5",borderwidth=2)
mrate.grid(row=0,column=4,sticky=N+S+E+W)
corona.mainloop()
