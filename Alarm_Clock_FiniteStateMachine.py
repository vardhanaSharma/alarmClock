#!/usr/bin/env python
# coding: utf-8

# In[1]:


# importing all necessary libraries and modules

from playsound import playsound
import tkinter as tk
from tkinter import ttk as ttk
import datetime     
import time
root=tk.Tk()
from statemachine import State,StateMachine


# defining class
class Alarmclk(StateMachine):
    
# states
    ideal = State('No ring',initial=True)
    ringing = State('ringing')
    snoozing = State('Snoozing')
    
# transitions
    ring= ideal.to(ringing)
    snooze= ringing.to(snoozing)
    stop= ringing.to(ideal)
    stop_2= snoozing.to(ideal)
    
ac=Alarmclk()

class AlarmClock(tk.Frame):
    
# defining functions
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.all_alarms = []
        
        self.ini_body()
        self.ini_clock()
        self.ini_mid()
        self.ini_table()

# defining frames of GUI
    def ini_body(self):
        self.up_frame = tk.Frame(self)
        self.mid_frame= tk.Frame(self)
        self.dow_frame= tk.Frame(self)

        self.up_frame.pack(side='top')
        self.mid_frame.pack(side='top',fill='x')
        self.dow_frame.pack(side='top')

# Label
    def ini_clock(self):
        self.clock = tk.Label(self.up_frame, text='00:00:00')
        self.clock.pack(side='top', fill='x')
        self.tick()

# defining current time        
    def tick(self):
        self.showed_time = ''
        self.current_time = datetime.datetime.now().strftime("%H:%M:%S")
        if self.showed_time != self.current_time:
            self.showed_time = self.current_time         
            self.clock.configure(text=self.current_time)
        if self.showed_time in self.all_alarms:
            self.invoke_alarm(self.showed_time)
        self.after(1000, self.tick)

# defining headings
    def ini_table(self):
        self.table = ttk.Treeview(self.dow_frame,height=1,columns=('#1'))
        self.table.heading('#0', text='Alarm ID')
        self.table.heading('#1', text='Alarm time')
        self.table.pack()
        
# defining position of buttons
    def ini_mid(self):
        self.alarm_id = tk.Entry(self.mid_frame,justify='center')
        self.alarm_id.insert('end','Alarm ID')

        self.alarm_time = tk.Entry(self.mid_frame,justify='center')
        self.alarm_time.insert('end','HH:MM')

        
        self.set_button = tk.Button(self.mid_frame, text='set alarm',
                                    command=self.set_alarm)
        self.cancel_button=tk.Button(self.mid_frame, text='cancel alarm',
                                     command=self.cancel_alarm)
        self.snooze_button=tk.Button(self.mid_frame, text='snooze alarm',
                                     command=self.snooze_alarm)

        self.alarm_time.grid(column=1,row=0,sticky='ew')
        self.alarm_id.grid(column=0,row=0, sticky='ew')
        self.set_button.grid(column=0, row=1, sticky='ew')
        self.cancel_button.grid(column=1, row=2, sticky='ew')
        self.snooze_button.grid(column=2, row=3, sticky='ew')
        self.mid_frame.columnconfigure(0, weight=1)
        self.mid_frame.columnconfigure(1, weight=1)
        
# defining set alarm 
    def set_alarm(self):
        if ac.is_ideal:
            ac.ring()
            Id = self.alarm_id.get()
            time = self.alarm_time.get()
            self.table.insert('','end', iid=Id, text=Id,
                              values=time, tags=time)
            self.register_alarm()
            
# defining cancel alarm         
    def cancel_alarm(self):
        if ac.is_ringing:                           
            ac.stop()
            Id = self.alarm_id.get()
            time = self.alarm_time.get()
            if self.table.exists(Id):
                tag = self.table.item(Id, "tags")[0]
                alarm_time=tag+":00"
                self.all_alarms.remove(alarm_time)
                self.table.delete(Id)
            elif self.table.tag_has(time):
                Id = self.table.tag_has(time)[0]
                tag = self.table.item(Id, "tags")[0]
                alarm_time=tag+":00"
                self.all_alarms.remove(alarm_time)
                self.table.delete(Id)
  
           
# defining snooze alarm
    def snooze_alarm(self):
         if ac.is_ringing:
            ac.snooze()
            time.sleep(5)
            display(self)
            playsound("C:/Users/user/Alarm clock project/.spyproject/config/sound.mp3")        # adding sound
            Snooze_Window = tk.Toplevel(root)
            Snooze_Window.geometry("400x200")
            Snooze_Window.title("Snoozing Window") 
            Snooze_Window.configure(bg='red')
            labelExample = tk.Label(Snooze_Window, text = "Alarm After Snoozing",font=("Cambria",20,"bold")).place(x=100,y=50)
            labelExample.pack()
            self.snooze_button.pack()
        
# register alarm
    def register_alarm(self):
        self.all_alarms.append(f'{self.alarm_time.get()}:00')
        
# invoke alarm
    def invoke_alarm(self, time):
        playsound("C:/Users/user/Alarm clock project/.spyproject/config/sound.mp3")             # adding sound
        self.alarm_window = tk.Toplevel()
        self.alarm_window.geometry("500x200")
        self.alarm_window.title('Alarm!')
        self.alarm_window.configure(bg='green')
        self.message = tk.Label(self.alarm_window,
                                text=f"ALARM!! It's {time[:5]} o'clock!",font=("Cambria",17,"bold")).place(x=120,y=50)
        self.message.pack(fill='both')
        
        
alarm = AlarmClock(root)
alarm.pack()
root.title("ALARM CLOCK")
root.mainloop()


# In[2]:


# importing all necessary libraries and modules

from playsound import playsound
import tkinter as tk
from tkinter import ttk as ttk
import datetime     
import time
root=tk.Tk()
from statemachine import State,StateMachine


# defining class
class Alarmclk(StateMachine):
    
# states
    ideal = State('No ring',initial=True)
    ringing = State('ringing')
    snoozing = State('Snoozing')
    
    ring= ideal.to(ringing)
    snooze= ringing.to(snoozing)
    stop= ringing.to(ideal)
    
ac=Alarmclk()

class AlarmClock(tk.Frame):
    
# defining functions
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.all_alarms = []
        
        self.ini_body()
        self.ini_clock()
        self.ini_mid()
        self.ini_table()

# defining frames of GUI
    def ini_body(self):
        self.up_frame = tk.Frame(self)
        self.mid_frame= tk.Frame(self)
        self.dow_frame= tk.Frame(self)

        self.up_frame.pack(side='top')
        self.mid_frame.pack(side='top',fill='x')
        self.dow_frame.pack(side='top')

# Label
    def ini_clock(self):
        self.clock = tk.Label(self.up_frame, text='00:00:00')
        self.clock.pack(side='top', fill='x')
        self.tick()

# defining current time        
    def tick(self):
        self.showed_time = ''
        self.current_time = datetime.datetime.now().strftime("%H:%M:%S")
        if self.showed_time != self.current_time:
            self.showed_time = self.current_time         
            self.clock.configure(text=self.current_time)
        if self.showed_time in self.all_alarms:
            self.invoke_alarm(self.showed_time)
        self.after(1000, self.tick)

# defining headings
    def ini_table(self):
        self.table = ttk.Treeview(self.dow_frame,height=1,columns=('#1'))
        self.table.heading('#0', text='Alarm ID')
        self.table.heading('#1', text='Alarm time')
        self.table.pack()
        
# defining position of buttons
    def ini_mid(self):
        self.alarm_id = tk.Entry(self.mid_frame,justify='center')
        self.alarm_id.insert('end','Alarm ID')

        self.alarm_time = tk.Entry(self.mid_frame,justify='center')
        self.alarm_time.insert('end','HH:MM')

        
        self.set_button = tk.Button(self.mid_frame, text='set alarm',
                                    command=self.set_alarm)
        self.cancel_button=tk.Button(self.mid_frame, text='cancel alarm',
                                     command=self.cancel_alarm)
        self.snooze_button=tk.Button(self.mid_frame, text='snooze alarm',
                                     command=self.snooze_alarm)

        self.alarm_time.grid(column=1,row=0,sticky='ew')
        self.alarm_id.grid(column=0,row=0, sticky='ew')
        self.set_button.grid(column=0, row=1, sticky='ew')
        self.cancel_button.grid(column=1, row=2, sticky='ew')
        self.snooze_button.grid(column=2, row=3, sticky='ew')
        self.mid_frame.columnconfigure(0, weight=1)
        self.mid_frame.columnconfigure(1, weight=1)
        
# defining set alarm 
    def set_alarm(self):
        if ac.is_ideal:
            ac.ring()
            Id = self.alarm_id.get()
            time = self.alarm_time.get()
            self.table.insert('','end', iid=Id, text=Id,
                              values=time, tags=time)
            self.register_alarm()
            
# defining cancel alarm         
    def cancel_alarm(self):
        if ac.is_ringing:                           
            ac.stop()
            Id = self.alarm_id.get()
            time = self.alarm_time.get()
            if self.table.exists(Id):
                tag = self.table.item(Id, "tags")[0]
                alarm_time=tag+":00"
                self.all_alarms.remove(alarm_time)
                self.table.delete(Id)
            elif self.table.tag_has(time):
                Id = self.table.tag_has(time)[0]
                tag = self.table.item(Id, "tags")[0]
                alarm_time=tag+":00"
                self.all_alarms.remove(alarm_time)
                self.table.delete(Id)

# defining snooze alarm
    def snooze_alarm(self):
         if ac.is_ringing:
            ac.snooze()
            time.sleep(5)
            display(self)
            playsound("C:/Users/user/Alarm clock project/.spyproject/config/sound.mp3")        # adding sound
            Snooze_Window = tk.Toplevel(root)
            Snooze_Window.geometry("400x200")
            Snooze_Window.title("Snoozing Window") 
            Snooze_Window.configure(bg='red')
            labelExample = tk.Label(Snooze_Window, text = "Alarm After Snoozing",font=("Cambria",20,"bold")).place(x=100,y=50)
            labelExample.pack()
            self.snooze_button.pack()
        
# register alarm
    def register_alarm(self):
        self.all_alarms.append(f'{self.alarm_time.get()}:00')
        
# invoke alarm
    def invoke_alarm(self, time):
        playsound("C:/Users/user/Alarm clock project/.spyproject/config/sound.mp3")             # adding sound
        self.alarm_window = tk.Toplevel()
        self.alarm_window.geometry("500x200")
        self.alarm_window.title('Alarm!')
        self.alarm_window.configure(bg='green')
        self.message = tk.Label(self.alarm_window,
                                text=f"ALARM!! It's {time[:5]} o'clock!",font=("Cambria",17,"bold")).place(x=120,y=50)
        self.message.pack(fill='both')
        
        
alarm = AlarmClock(root)
alarm.pack()
root.title("ALARM CLOCK")
root.mainloop()


# In[ ]:




