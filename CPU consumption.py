from tkinter import*
import matplotlib .pyplot as graph
import psutil as p
root=Tk()
root.geometry('600x800')
root.configure(bg='white')

app_name_dict={}
count=0

for process in p.process_iter():
    count=count+1
    if count <= 6:
        name=process.name()
        percentage=p.cpu_percent()
        print("Name: ",name," Percent Usage: ",percentage)
        app_name_dict.update({name:percentage})
        print(app_name_dict)
        
    keymax=max(app_name_dict, key=app_name_dict.get)
    print(keymax)
    keymin=min(app_name_dict, key=app_name_dict.get)
    print(keymin)
    name_list=[keymax,keymin]
    print(name_list)
    
    app=app_name_dict.values()
    print(app)
    
    
    app_max=max(app)
    print(app_max)
    app_min=min(app)
    print(app_min)
    app_list=[app_max,app_min]
    print(app_list)
    
    graph.figure(figsize=(15,7))
    graph.xlabel("Min-Max CPU Consumption")
    graph.ylabel("Usage")
    graph.bar(name_list,app_list,width=0.6,color=("blue","orange"))
    graph.show()
    root.mainloop()