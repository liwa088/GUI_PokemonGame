import pandas as pd
from tkinter import *
from PIL import Image, ImageTk
import random
from tkinter import messagebox
import matplotlib.pyplot as plt


def csvfile(): # this function will create the cleaned version of the csv file that you the professor provided for us 
    df = pd.read_csv("pokemon.csv")
    polist = ['Bulbasaur', 'Ivysaur', 'Venusaur', 'Charmander', 'Charmeleon', 'Charizard', 'Squirtle', 'Wartortle',
              'Blastoise', 'Caterpie', 'Metapod', 'Butterfree', 'Weedle', 'Kakuna', 'Beedrill', 'Pidgey', 'Pidgeotto',
              'Pidgeot']
    cleanlist = []
    for i in polist:
        pokname = df[(df['Name'] == i)]
        cleanlist.append(pokname)
    clean_df = pd.concat(cleanlist)
    columns_to_drop = ['Total', 'Type 2', 'Defense', 'Sp. Atk', 'Sp. Def', 'Speed', 'Generation', 'Legendary']
    cleanver = clean_df.drop(columns_to_drop, axis=1)
    cleanver = cleanver.rename(columns={"Type 1": "Element"})
    cleanver.to_csv("cleanPokemons.csv", index=False)


csvfile()
def evolvingfile(): # this function i make it to create a csv file that has each pokemon evolve and help me to make th evolving process 
    evolve1=['Bulbasaur','Charmander','Squirtle','Caterpie','Weedle','Pidgey']
    evolve2=['Ivysaur','Charmeleon','Wartortle','Metapod','Kakuna','Pidgeotto']
    evolve3=['Venusaur','Charizard','Blastoise','utterfree','Beedrill','Pidgeot']
    df=pd.DataFrame(list(zip(evolve1,evolve2,evolve3)),columns=['1','2','3'])
    df.to_csv('evolvelist.csv',index=False)


evolvingfile() 
   
class Player1(Frame): # selection pokemon class that will help to chose the pokemon for the second player 
    def __init__(self, parent, second_player_window):
        Frame.__init__(self, parent)
        self.second_player_window = second_player_window
        self.initUI()

    def initUI(self):
        self.pack(fill=BOTH, expand=True)
        self.imageframe = LabelFrame(self)
        self.values = ["Bulbasaur", 'Squirtle', 'Charmander', 'Caterpie', 'Weedle', 'Pidgey']
        self.title = Label(self, text="Player 1 chooses Pokemons")
        self.title.grid(row=0, column=2, rowspan=2)
        self.poklist = Listbox(self, selectmode=SINGLE, height=10, width=20)
        for i in self.values:
            self.poklist.insert(END, i)
        self.poklist.bind('<<ListboxSelect>>', self.pokselection)
        self.poklist.grid(row=2, column=1, pady=60, padx=20)
        self.choosebutton = Button(self, text='Choose!', command=self.chooseplayer1)
        self.choosebutton.grid(row=3, column=2, pady=10)
        self.image_path = "images\\none.png"
        self.image = ImageTk.PhotoImage(Image.open(self.image_path).resize((150, 150)))
        self.labelimage = Label(self.imageframe, image=self.image)
        self.labelimage.pack()
        self.imageframe.grid(row=2, column=2, padx=10)

    def pokselection(self, event):
        if self.poklist.curselection():
            index = self.poklist.curselection()[0]
            selected_pokemon = self.values[index]
            self.image_path = "images\\" + selected_pokemon.lower() + ".png"
            self.image = ImageTk.PhotoImage(Image.open(self.image_path).resize((150, 150)))
            self.labelimage.configure(image=self.image)

    def chooseplayer1(self):
        global selected_pokemon1
        index = self.poklist.curselection()[0]
        selected_pokemon1 = self.values[index]
        print(selected_pokemon1)
        self.choosebutton.configure(state=DISABLED)  # Disable the choose button
        self.poklist.configure(state=DISABLED)  # Disable the listbox
        self.second_player_window.deiconify()  # Show the second player window
        self.master.withdraw()  # Hide the first player window


class Player2(Frame): # selection pokemon class that will help to chose the pokemon for the second player 
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.initUI()

    def initUI(self):
        self.pack(fill=BOTH, expand=True)
        self.imageframe = LabelFrame(self)
        self.values = ["Bulbasaur", 'Squirtle', 'Charmander', 'Caterpie', 'Weedle', 'Pidgey']
        self.title = Label(self, text="Player 2 chooses Pokemons")
        self.title.grid(row=0, column=2, rowspan=2)
        self.poklist = Listbox(self, selectmode=SINGLE, height=10, width=20)
        for i in self.values:
            self.poklist.insert(END, i)
        self.poklist.bind('<<ListboxSelect>>', self.pokselection)
        self.poklist.grid(row=2, column=2, pady=60, padx=20)
        self.choosebutton = Button(self, text='Choose!', command=self.chooseplayer2)
        self.choosebutton.grid(row=3, column=1, sticky=N, pady=10)
        self.image_path = "images\\none.png"
        self.image = ImageTk.PhotoImage(Image.open(self.image_path).resize((150, 150)))
        self.labelimage = Label(self.imageframe, image=self.image)
        self.labelimage.pack()
        self.imageframe.grid(row=2, column=1, padx=30)

    def pokselection(self, event):
        if self.poklist.curselection():
            index = self.poklist.curselection()[0]
            selected_pokemon = self.values[index]
            self.image_path = "images\\" + selected_pokemon.lower() + ".png"
            self.image = ImageTk.PhotoImage(Image.open(self.image_path).resize((150, 150)))
            self.labelimage.configure(image=self.image)

    def chooseplayer2(self):
        global selected_pokemon2
        index = self.poklist.curselection()[0]
        selected_pokemon2 = self.values[index]
        print(selected_pokemon2)
        self.master.destroy()
        FightWindow(selected_pokemon1, selected_pokemon2)


class FightWindow(Toplevel): # the fight window class this class will make the fighting window between two pokemons 
    def __init__(self, selected_pokemon1, selected_pokemon2, **kwargs):
        super().__init__(**kwargs)
        self.successlist=['S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'M', 'M', 'M', 'M', 'M', 'M', 'M', 'M', 'M', 'M', 'M', 'M', 'M', 'M', 'M', 'M', 'M', 'M', 'M', 'M']
        self.pokemon1db=[]
        self.pokemon2db=[]
        self.health1db=[]
        self.health2db=[]
        self.damage1db=[]
        self.damage2db=[]
        self.element1db=[]
        self.element2db=[]
        self.critical1db=[]
        self.critical2db=[]
        self.winnum1 = 0
        self.winnum2 = 0
        self.selected_pokemon1 = selected_pokemon1
        self.selected_pokemon2 = selected_pokemon2
        self.title("Fight Window")
        self.geometry("800x400+200+200")
        self.label1 = Label(self, text="Player 1")
        self.label2 = Label(self, text="Player 2")
        self.label1.grid(row=0, column=0, sticky=NSEW, padx=150, pady=5)
        self.label2.grid(row=0, column=1, sticky=NSEW, padx=150, pady=5)
        self.score1 = Label(self, text=f"Score: {self.winnum1}")
        self.score2 = Label(self, text=f"Score: {self.winnum2}")
        self.score1.grid(row=1, column=0, sticky=NSEW, padx=150, pady=5)
        self.score2.grid(row=1, column=1, sticky=NSEW, padx=150, pady=5)

        # Initialize health bars with Pokemon names
        self.health_bar1 = healthbar(self, self.selected_pokemon1)
        self.health_bar2 = healthbar(self, self.selected_pokemon2)
        self.health_bar1.grid(row=3, column=0, padx=75, pady=5)
        self.health_bar2.grid(row=3, column=1, padx=75, pady=5)
        df = pd.read_csv("cleanPokemons.csv")
        self.max_health1 = df.loc[df['Name'] == self.selected_pokemon1, 'HP'].iloc[0] * 5
        self.max_health2 = df.loc[df['Name'] == self.selected_pokemon2, 'HP'].iloc[0] * 5
        self.current_health1=df.loc[df['Name'] == self.selected_pokemon1, 'HP'].iloc[0] * 5                                                                                                                                                                                                            
        self.current_health2=df.loc[df['Name'] == self.selected_pokemon2, 'HP'].iloc[0] * 5 
        self.healthcode1=Label(self,text=f'{self.current_health1}/{self.max_health1}')
        self.healthcode2=Label(self,text=f'{self.current_health2}/{self.max_health2}')
        self.healthcode1.grid(row=3,column=0,sticky=E)
        self.healthcode2.grid(row=3,column=1,sticky=E)
        
        self.image1_frame = LabelFrame(self, text="Player 1 Pokemon")
        self.image2_frame = LabelFrame(self, text="Player 2 Pokemon")
        self.image1_frame.grid(row=4, column=0, padx=75, pady=5)
        self.image2_frame.grid(row=4, column=1, padx=75, pady=5)
        self.image1_label = Label(self.image1_frame)
        self.image1_label.pack()  # Ensure the image label is packed inside the frame
        self.image2_label = Label(self.image2_frame)
        self.image2_label.pack()  # Ensure the image label is packed inside the frame

        # Display the chosen Pokemon images
        image1_path = "images\\" + self.selected_pokemon1.lower() + ".png"
        image2_path = "images\\" + self.selected_pokemon2.lower() + ".png"
        self.image1 = ImageTk.PhotoImage(Image.open(image1_path).resize((150, 150)))
        self.image2 = ImageTk.PhotoImage(Image.open(image2_path).resize((150, 150)))
        self.image1_label.configure(image=self.image1)
        self.image2_label.configure(image=self.image2)

        self.button1_frame = LabelFrame(self)
        self.button2_frame = LabelFrame(self)
        self.button1_frame.grid(row=5, column=0, padx=75, pady=5)
        self.button2_frame.grid(row=5, column=1, padx=75, pady=5)
        self.elem1 = Button(self.button1_frame, text="elemental", command=self.elementalattack1)
        self.elem2 = Button(self.button2_frame, text="elemental", state=DISABLED, command=self.elementalattack2)
        self.elem1.pack(side=RIGHT)
        self.elem2.pack(side=RIGHT)
        self.phy1 = Button(self.button1_frame, text="physical", command=self.physicalattack1)
        self.phy2 = Button(self.button2_frame, text="physical", state=DISABLED, command=self.physicalattack2)
        self.phy1.pack(side=RIGHT)
        self.phy2.pack(side=RIGHT)
        
    def physicalattack1(self):# the function of the physical attack button for the first pokemon 
        df = pd.read_csv("cleanPokemons.csv")
        self.physicaldamage1=df.loc[df['Name'] == self.selected_pokemon1, 'Attack'].iloc[0]
        self.per=75
        self.rand=random.randint(0,25)
        self.totper=(self.per+self.rand)/100
        self.totdamage=round(int(self.physicaldamage1)*self.totper)
        print(self.totdamage)
        self.damage1db.append(self.totdamage)
        self.health2db.append(self.current_health2)
        self.pokemon1db.append(self.selected_pokemon1)
        self.element1db.append("0.0")
        
        print(self.damage1db,self.health2db,self.pokemon1db,self.element1db)
        self.current_health2 -= self.totdamage
        self.message=messagebox.showinfo(f"{self.selected_pokemon1} Attack!",f"{self.selected_pokemon1} hit {self.totdamage} damage!")
        if self.current_health2 < 0:
            self.current_health2 = 0
            self.winnum1+=1
            self.lose=messagebox.showinfo("Lose!",f"{self.selected_pokemon2} lost! Player 2 chooses a pokemon and player 1 gets evolved!")
            if self.winnum1==3:
                self.winner=messagebox.showinfo("WINNER!","Player 1 won!")
                self.gameover=messagebox.showinfo("END","GAME IS OVER!!")
                stat(FightWindow(selected_pokemon1, selected_pokemon2))
                exit()           
            else:
                self.score1.config(text=f"Score: {self.winnum1}")
                evolution_df = pd.read_csv('evolvelist.csv')
                self.found = False
                for index, row in evolution_df.iterrows():
                    for column in evolution_df.columns:
                        if row[column] == self.selected_pokemon1:
                            self.found = True
                            print(f"Pokemon name '{self.selected_pokemon1}' found at row {index}, column '{column}'")
                            self.pokcol=int(column)+1
                            self.pokrow=index
                            break
            print(self.pokcol,self.pokrow)
            self.selected_pokemon1=evolution_df[str(self.pokcol)].iloc[self.pokrow]
            image1_path = "images\\" + self.selected_pokemon1.lower() + ".png"
            self.image1 = ImageTk.PhotoImage(Image.open(image1_path).resize((150, 150))) 
            self.image1_label.config(image=self.image1)
            self.max_health1=df.loc[df['Name'] == self.selected_pokemon1, 'HP'].iloc[0] * 5
            self.current_health1=round(self.max_health1*0.7)
            self.healthcode1.config(text=f'{self.current_health1}/{self.max_health1}')
            self.health_bar1.set_health(self.current_health1,self.max_health1) 
            Player2(Toplevel())
        self.healthcode2.config(text=f'{self.current_health2}/{self.max_health2}')
        self.health_bar2.set_health(self.current_health2,self.max_health2)
        print(self.current_health2)
        self.phy1.config(state=DISABLED)
        self.phy2.config(state=NORMAL)
        self.elem1.config(state=DISABLED)
        self.elem2.config(state=NORMAL)
    def elementalattack1(self):# the function of the elemental attack button for the first pokemon 
        df = pd.read_csv("cleanPokemons.csv")
        self.physicaldamage1=df.loc[df['Name'] == self.selected_pokemon1, 'Attack'].iloc[0]
        self.elementtype1=df.loc[df['Name'] == self.selected_pokemon1, 'Element'].iloc[0]
        self.elementtype2=df.loc[df['Name'] == self.selected_pokemon2, 'Element'].iloc[0]
        self.per=50
        self.rand=random.randint(0,50)
        self.totper=(self.per+self.rand)/100
        self.totdamage=round(self.physicaldamage1*self.totper)
        print(self.totdamage)
        self.damage1db.append(self.totdamage)
        self.health2db.append(self.current_health2)
        self.pokemon1db.append(self.selected_pokemon1)
        self.element1db.append(1.0)
        print(self.damage1db,self.health2db,self.pokemon1db,self.element1db)
        if (self.elementtype1=="Fire" and self.elementtype2=="Grass") or (self.elementtype1=="Water" and self.elementtype2=="Fire")or (self.elementtype1=="Grass" and self.elementtype2=="Water")or (self.elementtype1=="Bug" and self.elementtype2=="Normal")or (self.elementtype1=="Normal" and self.elementtype2=="Bug"):
            self.result=random.sample(self.successlist,1)
            if self.result==["S"]:
                self.criticaldam=self.totdamage*2
                self.current_health2 -= self.criticaldam
                self.critic=messagebox.showwarning('critical','critical')
                self.message=messagebox.showinfo(f"{self.selected_pokemon1} Attack!",f"{self.selected_pokemon1} hit {self.criticaldam} damage!")
            else:
                self.current_health2 -= self.totdamage
                self.message=messagebox.showinfo(f"{self.selected_pokemon1} Attack!",f"{self.selected_pokemon1} hit {self.totdamage} damage!")            
        else:
            self.current_health2 -= self.totdamage
            self.message=messagebox.showinfo(f"{self.selected_pokemon1} Attack!",f"{self.selected_pokemon1} hit {self.totdamage} damage!")
        if self.current_health2 < 0:
            self.current_health2 = 0
            self.winnum1+=1
            self.lose=messagebox.showinfo("Lose!",f"{self.selected_pokemon2} lost! Player 2 chooses a pokemon and player 1 gets evolved!")
            if self.winnum1==3:
                self.winner=messagebox.showinfo("WINNER!","Player 1 won!")
                self.gameover=messagebox.showinfo("END","GAME IS OVER!!")
                stat(FightWindow(selected_pokemon1, selected_pokemon2))
                exit()           
            else:
                self.score1.config(text=f"Score: {self.winnum1}")
                evolution_df = pd.read_csv('evolvelist.csv')
                self.found = False
                for index, row in evolution_df.iterrows():
                    for column in evolution_df.columns:
                        if row[column] == self.selected_pokemon1:
                            self.found = True
                            print(f"Pokemon name '{self.selected_pokemon1}' found at row {index}, column '{column}'")
                            self.pokcol=int(column)+1
                            self.pokrow=index
                            break
            print(self.pokcol,self.pokrow)
            self.selected_pokemon1=evolution_df[str(self.pokcol)].iloc[self.pokrow]
            image1_path = "images\\" + self.selected_pokemon1.lower() + ".png"
            self.image1 = ImageTk.PhotoImage(Image.open(image1_path).resize((150, 150))) 
            self.image1_label.config(image=self.image1)
            self.max_health1=df.loc[df['Name'] == self.selected_pokemon1, 'HP'].iloc[0] * 5
            self.current_health1=round(self.max_health1*0.7)
            self.healthcode1.config(text=f'{self.current_health1}/{self.max_health1}')
            self.health_bar1.set_health(self.current_health1,self.max_health1)
            Player2(Toplevel())
            
        self.healthcode2.config(text=f'{self.current_health2}/{self.max_health2}')    
        self.health_bar2.set_health(self.current_health2,self.max_health2)
        print(self.current_health2)
        self.phy1.config(state=DISABLED)
        self.phy2.config(state=NORMAL)
        self.elem1.config(state=DISABLED)
        self.elem2.config(state=NORMAL)
    def physicalattack2(self): # the function of the physical attack button for the second pokemon 
        df = pd.read_csv("cleanPokemons.csv")
        self.physicaldamage2=df.loc[df['Name'] == self.selected_pokemon2, 'Attack'].iloc[0]
        self.per=75
        self.rand=random.randint(0,25)
        self.totper=(self.per+self.rand)/100
        self.totdamage=round(int(self.physicaldamage2)*self.totper)
        print(self.totdamage)
        self.damage2db.append(self.totdamage)
        self.health1db.append(self.current_health1)
        self.pokemon2db.append(self.selected_pokemon2)
        self.element2db.append("0.0")
        print(self.damage2db,self.health1db,self.pokemon2db,self.element2db)
        self.current_health1 -= self.totdamage
        self.message=messagebox.showinfo(f"{self.selected_pokemon2} Attack!",f"{self.selected_pokemon2} hit {self.totdamage} damage!")
        if self.current_health1 < 0:
            self.current_health1 = 0
            self.winnum2 += 1
            self.lose=messagebox.showinfo("Lose!",f"{self.selected_pokemon1} lost! Player 1 chooses a pokemon and player 2 gets evolved!")
            if self.winnum2==3:
                self.winner=messagebox.showinfo("WINNER!","Player 2 won!")
                self.gameover=messagebox.showinfo("END","GAME IS OVER!!")
                stat(FightWindow(selected_pokemon1, selected_pokemon2))
                exit()           
            else:
                
                self.score2.config(text=f"Score: {self.winnum2}")
                evolution_df = pd.read_csv('evolvelist.csv')
                self.found = False
                for index, row in evolution_df.iterrows():
                    for column in evolution_df.columns:
                        if row[column] == self.selected_pokemon2:
                            self.found = True
                            print(f"Pokemon name '{self.selected_pokemon2}' found at row {index}, column '{column}'")
                            self.pokcol=int(column)+1
                            self.pokrow=index
                            break
            print(self.pokcol,self.pokrow)
            self.selected_pokemon1=evolution_df[str(self.pokcol)].iloc[self.pokrow]
            image2_path = "images\\" + self.selected_pokemon2.lower() + ".png"
            self.image2 = ImageTk.PhotoImage(Image.open(image2_path).resize((150, 150))) 
            self.image2_label.config(image=self.image2)
            self.max_health2=df.loc[df['Name'] == self.selected_pokemon2, 'HP'].iloc[0] * 5
            self.current_health2=round(self.max_health2*0.7)
            self.healthcode2.config(text=f'{self.current_health2}/{self.max_health2}')
            self.health_bar2.set_health(self.current_health2,self.max_health2)
            Player1(Toplevel())
        self.health_bar1.set_health(self.current_health1,self.max_health1)
        self.healthcode1.config(text=f'{self.current_health1}/{self.max_health1}')
        print(self.current_health2)
        self.phy2.config(state=DISABLED)
        self.phy1.config(state=NORMAL)
        self.elem2.config(state=DISABLED)
        self.elem1.config(state=NORMAL)

    def elementalattack2(self): # the function of the elemental attack button for the second pokemon 
        df = pd.read_csv("cleanPokemons.csv")
        self.physicaldamage2=df.loc[df['Name'] == self.selected_pokemon2, 'Attack'].iloc[0]
        self.elementtype1=df.loc[df['Name'] == self.selected_pokemon1, 'Element'].iloc[0]
        self.elementtype2=df.loc[df['Name'] == self.selected_pokemon2, 'Element'].iloc[0]
        self.per=50
        self.rand=random.randint(0,50)
        self.totper=(self.per+self.rand)/100
        self.totdamage=round(self.physicaldamage2*self.totper)
        print(self.totdamage)
        self.damage2db.append(self.totdamage)
        self.health1db.append(self.current_health1)
        self.pokemon2db.append(self.selected_pokemon2)
        self.element2db.append(1.0)
        print(self.damage2db,self.health1db,self.pokemon2db,self.element2db)
        if (self.elementtype2=="Fire" and self.elementtype1=="Grass") or (self.elementtype2=="Water" and self.elementtype1=="Fire")or (self.elementtype2=="Grass" and self.elementtype1=="Water")or (self.elementtype2=="Bug" and self.elementtype1=="Normal")or (self.elementtype2=="Normal" and self.elementtype1=="Bug"):
            self.result=random.sample(self.successlist,1)
            if self.result==["S"]:
                self.criticaldam=self.totdamage*2
                self.current_health1 -= self.criticaldam
                self.critic=messagebox.showwarning('critical','critical')
                self.message=messagebox.showinfo(f"{self.selected_pokemon2} Attack!",f"{self.selected_pokemon2} hit {self.criticaldam} damage!")
            else:
                self.current_health1 -= self.totdamage
                self.message=messagebox.showinfo(f"{self.selected_pokemon2} Attack!",f"{self.selected_pokemon2} hit {self.totdamage} damage!")            
        else:
            self.current_health1 -= self.totdamage
            self.message=messagebox.showinfo(f"{self.selected_pokemon2} Attack!",f"{self.selected_pokemon2} hit {self.totdamage} damage!")
        if self.current_health1 < 0:
            self.current_health1 = 0
            self.winnum2 += 1
            self.lose=messagebox.showinfo("Lose!",f"{self.selected_pokemon1} lost! Player 1 chooses a pokemon and player 2 gets evolved!")
            if self.winnum2==3:
                self.winner=messagebox.showinfo("WINNER!","Player 2 won!")
                self.gameover=messagebox.showinfo("END","GAME IS OVER!!")
                stat(FightWindow(selected_pokemon1, selected_pokemon2))
                exit()           
            else:
                self.score2.config(text=f"Score: {self.winnum2}")
                evolution_df = pd.read_csv('evolvelist.csv')
                self.found = False
                for index, row in evolution_df.iterrows():
                    for column in evolution_df.columns:
                        if row[column] == self.selected_pokemon2:
                            self.found = True
                            print(f"Pokemon name '{self.selected_pokemon2}' found at row {index}, column '{column}'")
                            self.pokcol=int(column)+1
                            self.pokrow=index
                            break
            print(self.pokcol,self.pokrow)
            self.selected_pokemon2=evolution_df[str(self.pokcol)].iloc[self.pokrow]
            image2_path = "images\\" + self.selected_pokemon2.lower() + ".png"
            self.image2 = ImageTk.PhotoImage(Image.open(image2_path).resize((150, 150))) 
            self.image2_label.config(image=self.image2)
            self.max_health2=df.loc[df['Name'] == self.selected_pokemon2, 'HP'].iloc[0] * 5
            self.current_health2=round(self.max_health2*0.7)
            self.healthcode2.config(text=f'{self.current_health2}/{self.max_health2}')
            self.health_bar2.set_health(self.current_health2,self.max_health2)
            Player1(Toplevel())
        self.health_bar1.set_health(self.current_health1,self.max_health1)
        self.healthcode1.config(text=f'{self.current_health1}/{self.max_health1}')
        print(self.current_health1)
        self.phy2.config(state=DISABLED)
        self.phy1.config(state=NORMAL)
        self.elem2.config(state=DISABLED)
        self.elem1.config(state=NORMAL)


class healthbar(Canvas):
    def __init__(self, parent, pokemon_name, width=200, height=20, **kwargs):
        super().__init__(parent, width=width, height=height, bg="red", **kwargs)
        self.width = width
        self.height = height
        print(pokemon_name)
        # Read health information from CSV file
        df = pd.read_csv("cleanPokemons.csv")
        max_health = df.loc[df['Name'] == pokemon_name, 'HP'].iloc[0] * 5  # Get max health from CSV
        self.max_health = max_health
        self.current_health = max_health  # Set current health to maximum initially
        self.pokemon_name = pokemon_name  # Store the Pokemon name
        self.draw_bar()
    
    def draw_bar(self):
        self.delete("all")  # Clear canvas
        bar_width = self.width * (self.current_health / self.max_health)  # Calculate bar width based on current health
        self.create_rectangle(0, 0, bar_width, self.height, fill="green")  # Draw filled bar
        self.create_rectangle(0, 0, self.width, self.height, outline="black")  # Draw outline
        
    def set_health(self, current_health,max_health):
        self.current_health = current_health
        self.max_health=max_health
        self.draw_bar()
        
    
class stat(FightWindow): #stat class that will provide us will the final data 
    def __init__(self,parent,selected_pokemon2): # i have created this function for the first graph
        super().__init__(parent,selected_pokemon2)
        self.turns2=len(self.health2db)
        self.health2=self.health2db
        self.turns1=len(self.health1db)
        self.health1=self.health1db
        plt.plot(self.turns1,self.health1,Label='Player 1',c='Green')
        plt.plot(self.turns2,self.health2,Label='Player 2',c='Red')
        plt.xlabel('turns')
        plt.ylabel('health')
        plt.title('Health Analyze')
        plt.legend()
        plt.show()
    def damageanalyse(self):  #i have created this function for the second graph
        self.damage1=self.damage1db 
        self.damage2=self.damage2db
        plt.plot(self.turns1,self.damage1,Label='Player 1',c='Blue')
        plt.plot(self.turns2,self.damage2,Label='Player 2',c='Orange')
        plt.xlabel('turns')
        plt.ylabel('health')
        plt.title('Health Analyze')
        plt.legend()
        plt.show()
    def criticalcount(self): # i have created this function for the third graph
        self.names1=self.pokemon1db
        self.names2=self.pokemon2db
        self.critcount1=len(self.critical1db)
        self.critcount2=len(self.critical2db)
        plt.bar(self.names1,self.critcount1,c='Red')
        plt.bar(self.names2,self.critcount2,c='Blue')
        plt.ylabel('Critical Attack Count')
        plt.title('Pokemons')
        plt.legend()
        plt.show()
    def datavase(self):# i created this function to make the final excel file 
        self.data={"pokemon 1":self.pokemon1db,'pokemon 2':self.pokemon2db,'Health 1':self.health1db,'health 2':self.health2db,'Damage 1':self.damage1db,"Damage 2":self.damage2db,'Critical 1':self.critical1db,'Critical 2':self.critical2db,'Element 1':self.element1db,"Element 2":self.element2db}
        self.df=pd.DataFrame(self.data)
        self.df.to_excel("Final_data.xl")



            
def main():
    root = Tk()
    root.geometry("500x400+200+200")
    root.title("Pokemon")

    player2window = Toplevel(root)
    player2window.geometry("500x400+200+200")
    player2window.title("Player 2")
    player2window.withdraw()  # Hide the second player window initially

    app_player1= Player1(root, player2window)
    app_player2 = Player2(player2window)
    
    root.mainloop()


main()
