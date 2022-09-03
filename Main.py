from kivy.uix.floatlayout import FloatLayout
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from kivy.uix.textinput import TextInput
from kivy.uix.popup import Popup
from kivy.uix.image import Image
from kivy.graphics import Rectangle, Color
from os import getcwd as getPath
import Genotype


dataPrivacy = 0
manager = ScreenManager()
n = 0
#if data privacy is 0 names arent hidden elif 1 names are hidden as 8 bit words seperated by comma inside system
# inside data1
#Language[target sentence][n] n is for language n:1 = English and n:0 = Turkish
Languages = [
    ["Hastalar", "Patients"],
    ["Rahatsızlıklar", "Diseases"],#1
    ["Excel", "Excel"],#2
    ["HATA!", "ERROR!"],#3
    ["Tekrar Dene", "Retry"],#4
    ["Kişi Göster", "Show Person"],#5
    ["Kişinin Rahatsızlıkları", "Diseases of Person"],#6
    ["Çocuk Rahatsızlık Olasılıkları", "Disease Posibilities for Child"],#7
    ["İd", "Id"],#8
    ["Ara", "Search"],#9
    ["Rapor oluşturuldu", "Report created"],#10
    ["Rapor oluşturuldu\nRapora Raporlar klasöründen ulaşabilirsiniz",
     "Report created\nReport is located at Reports file "],#11
    ["Kapat", "Close"],#12
    ["Herkesi Göster", "Show Everyone"],#13
    ["Herkesi Hesapla", "Calculate Everyone"],#14
    ["Annenin İdsi", "Mother İd"],#15
    ["Babanın İdsi", "Father İd"],#16
    ["Ayarlar", "Settings"],#17
    ["Sistem", "System"],#18
    ["Veri Gizliliği", "Data Privacy"],#19
    ["Gizli", "Hidden"],#20
    ["Gizli Değil", "Public"],#21
    ["Sistem", "System"],#22
    ["Menü", "Home"],#23
    ["Kişi Değiştir", "Change Person"],#24
    ["Genin Harflerini Değiştir", "Change Letters of Gene"],#25
    ["Excel'i Yenile", "Reload Excel"],#26
    ["Uygula", "Apply"],#27
    ["Fenotip", "Phenotype"],#28
    ["Genotip", "Genotype"],#29
    ["isim", "Name"],#30
    ["Cinsiyet", "Sex"],#31
    ["Lütfen excel dosyasını kapatıp tekrar deneyin", "Please close the excel file and retry"],#32
    ["Excel yenilendi", "Excel reloaded"],#33
    ["Excel başarı ile yenilendi", "Excel reloaded succesfully"],#34
    ["Seç", "Select"],#35
    ["Eski harfler: {}", "Old letters: {}"],#36
    ["Değiştir", "Change"],#37
    ["Yeni Harfler:", "New Letters:"]

]

def sysCheck():
    '''
    Checks the values n and dataprivacy
    dataprivacy is written inside system inside options

    but for language the code tries to find the file from Language[22][x] if error raises then the language isnt
    x so x += 1 until language is found
    '''
    x = 0
    global dataPrivacy
    global n
    while True:
        try:
            data = open(getPath() +"\{}\options.txt".format(Languages[22][x]), "r")
            data.seek(9)
            privacy = data.read(1)
            dataPrivacy = int(privacy)
            n = int(x)
            print(dataPrivacy, n)
            return None
        except:
            x += 1

sysCheck()
Genotype.n = n
Genotype.dataPrivacy = dataPrivacy

def goToScene(sceneName):
    #CHANGES THE SCENE sceneName = "Wanted scene"
    manager.current = sceneName


def ChangeN(val):
    '''
    Changes all variables text that use Language system
    reason for this is text variable for all labels and buttons arent updated they are just called once
    inside __init__ method.
    '''
    global n
    n = val
    set = Settings.this
    fr = First.this
    er = Error.this
    pat = Patients.this
    ex = Excel.this
    Genotype.LangChange(val)

    set.home.text = Languages[23][n]
    set.logo.source = getPath()+"\{}".format(Languages[18][n]+"\logo.jpg")
    set.data.text = Languages[19][n]
    set.pop2.title = Languages[24][n]
    set.lab1.text = Languages[32][n]
    set.bttn2.text = Languages[12][n]
    if dataPrivacy == 0:
        set.priv.text = Languages[21][n]
    elif dataPrivacy == 1:
        set.priv.text = Languages[20][n]
    if n == 0:
        set.lang.text = "dil: Türkçe"
    elif n == 1:
        set.lang.text = "Language: English"

    pat.home.text = Languages[23][n]
    pat.search_by_id.text = Languages[5][n]
    pat.disease_of_person.text =Languages[6][n]
    pat.diseases_of_child.text=Languages[7][n]
    pat.txt.text=Languages[8][n]
    pat.submit.text=Languages[9][n]
    pat.txt1.text=Languages[11][n]
    pat.bttn.text=Languages[12][n]
    pat.bttn1.text=Languages[13][n]
    pat.pop.text=Languages[10][n]
    pat.txt1.text=Languages[8][n]
    pat.submit1.text=Languages[9][n]
    pat.bttn2.text=Languages[14][n]
    pat.fathertxt.text=Languages[16][n]
    pat.mothertxt.text=Languages[15][n]
    pat.submit2.text=Languages[9][n]

    fr.patients.text=Languages[0][n]
    fr.Excel.text = Languages[2][n]
    fr.settings.text = Languages[17][n]

    er.header.text = Languages[3][n]
    er.button.text = Languages[4][n]

    ex.ChangePerson.text =Languages[24][n]
    ex.ReloadExcel.text =Languages[26][n]
    ex.ChangeDisLetter.text =Languages[25][n]
    ex.txt.text =Languages[8][n]
    ex.submit.text =Languages[9][n]
    ex.text1.text =Languages[30][n]
    ex.text2.text =Languages[29][n]
    ex.text3.text =Languages[28][n]
    ex.text4.text =Languages[8][n]
    ex.text5.text =Languages[31][n]
    ex.bttn1.text = Languages[27][n]
    ex.bttn2.text =Languages[12][n]
    ex.pop.title =Languages[24][n]
    ex.pop2.title =Languages[24][n]
    ex.pop3.title = Languages[33][n]
    ex.lab2.text = Languages[34][n]
    ex.bttn3.text = Languages[12][n]
    ex.sbmt.text = Languages[35][n]
    ex.txxt.text =Languages[36][n]
    ex.txxt2.text =Languages[38][n]
    ex.sent.text =Languages[37][n]


class HomeButton(Button):
    #A HOME BUTTON ON THE TOP RİGHT OF THE SCREEN ON CLİCK TAKES BACK TO THE SCENE NAMED "First"
    this = None
    def __init__(self, **kwargs):
        super(HomeButton, self).__init__(**kwargs)
        this = self
        self.text = Languages[23][n]
        self.size_hint = (0.12, 0.1)
        self.pos_hint = {"x": 0.87, "top": 0.93}
        self.manager = manager
        self.on_press = lambda: goToScene("First")


class First(Screen):
    this = None
    #First screen of the program
    def __init__(self, **kwargs):
        super(First, self).__init__(**kwargs)

        self.patients = Button(text=Languages[0][n], size_hint=(0.4, 0.2), pos_hint={"x": 0.3, "top": 0.9}, font_size=30,
                               on_press=lambda a: goToScene("Patients"))
        self.Excel = Button(text=Languages[2][n], size_hint=(0.4, 0.2), pos_hint={"x": 0.3, "top": 0.6}, font_size=30,
                            on_press= lambda a: goToScene("Excel"))
        self.settings = Button(text=Languages[17][n], size_hint=(0.4, 0.2), pos_hint={"x": 0.3, "top": 0.3},
                               font_size=30, on_press=lambda a: goToScene("Settings"))

        self.add_widget(self.settings)
        self.add_widget(self.patients)
        self.add_widget(self.Excel)
        First.this = self

    def Start(self):
        '''
        Once opened this calls the new_excel() and main_Func() from Genotype.py
        if len of Genotype.Errror is greater then 0 that means
        Genotype.py raised an error and all errors caught will have a text inside the list Genotype.Error
        and the program wil automaticly go to "Error" scene
        '''
        Genotype.new_excel()

        if len(Genotype.errors) > 0:
            self.manager.current = "Error"
            Error.this.setText()

        Genotype.main_func()

        if len(Genotype.errors) > 0:
            self.manager.current = "Error"
            Error.this.setText()


class Error(Screen):
    this = None
    #THIS SCENE IS OPENED IF len of Genotype.Error IS GREATER THEN 0
    def __init__(self, **kwargs):
        super(Error, self).__init__(**kwargs)
        self.layout = FloatLayout()

        self.header = Label(text=Languages[3][n], font_size=60, pos_hint={"x": 0.45,"top": 0.9}, size_hint=(0.1, 0.1))
        self.label = Label(text="", font_size=40, pos_hint={"top": 1})
        self.button = Button(text=Languages[4][n], size_hint=(0.3, 0.2), pos_hint={"x": 0.35, "top": 0.25}, on_press=lambda a: self.clicked())

        self.layout.add_widget(self.button)
        self.layout.add_widget(self.label)
        self.layout.add_widget(self.header)

        self.add_widget(self.layout)
        Error.this = self

    def setText(self):
        #SETS THE TEXT OF SELF.LABEL
        self.label.text = Genotype.errors[0]

    def clicked(self):
        #FUCNTİON THATS CALLED WHEN THE BUTTON NAMED self.button IS CALLED
        Genotype.errors = []
        Genotype.new_excel()
        Genotype.main_func()
        if len(Genotype.errors) > 0:
            self.label.text = Genotype.errors[0]
        else:
            self.manager.current = "First"


class Patients(Screen):
    this = None
    #THIS IS THE PATIENT SCENE OPENED FROM First SCENE
    def __init__(self, **kwargs):
        super(Patients, self).__init__(**kwargs)
        Patients.this = self
        self.search_active = False
        self.search_dis = False
        self.search_child = False
        self.layer = FloatLayout()
        self.add_widget(self.layer)

        self.search_by_id = Button(text=Languages[5][n], size_hint=(0.3, .2), pos_hint={"x": 0.1, "top": 0.9},
                                   font_size=20, on_press=lambda a: self.SearchById())
        self.disease_of_person = Button(text=Languages[6][n], size_hint=(0.3, .2), pos_hint={"x": 0.1, "top": 0.6},
                                        font_size=20, on_press=lambda a: self.SearchDisease())
        self.diseases_of_child = Button(text=Languages[7][n], size_hint=(0.3, .2), pos_hint={"x": 0.1, "top": 0.3},
                                        font_size=18, on_press=lambda a: self.SearchChild())
        self.home = HomeButton()
        self.layer.add_widget(self.home)

        if True:
            #Search by id
            self.id = TextInput(size_hint=(0.15, 0.1), pos_hint={"x": 0.68, "top": 0.88}, multiline=False, font_size=25)
            self.txt = Label(size_hint=(0.15, 0.1), pos_hint={"x": 0.68, "top": 0.95}, text=Languages[8][n], font_size=25)
            self.submit = Button(size_hint=(0.15, 0.1), pos_hint={"x": 0.68, "top": 0.77}, text=Languages[9][n],
                                 on_press=lambda a: self.Search())

            self.lay = FloatLayout()
            self.txt1 = Label(text=Languages[11][n], pos_hint={"x": 0.4, "top": 0.7}, size_hint=(0.2, 0.2), font_size=15)
            self.lay.add_widget(self.txt1)
            self.bttn = Button(text=Languages[12][n], pos_hint={"x": 0.4, "top": 0.3}, size_hint=(0.2, 0.1),
                               on_press=lambda a: self.pop.dismiss())
            self.bttn1 = Button(size_hint=(0.15, 0.1), pos_hint={"x": 0.49, "top": 0.88}, text=Languages[13][n],
                                 on_press=lambda a: self.Search(mode=1))

            self.lay.add_widget(self.bttn)

            self.pop = Popup(title=Languages[10][n], content=self.lay, size_hint=(0.5, 0.5))

        if True:
            #Disease of person
            self.id1 = TextInput(size_hint=(0.15, 0.1), pos_hint={"x": 0.68, "top": 0.58}, multiline=False, font_size=25)
            self.txt1 = Label(size_hint=(0.15, 0.1), pos_hint={"x": 0.68, "top": 0.65}, text=Languages[8][n],
                             font_size=25)
            self.submit1 = Button(size_hint=(0.15, 0.1), pos_hint={"x": 0.68, "top": 0.47}, text=Languages[9][n],
                                 on_press=lambda a: self.SearchDis(mode=0))
            self.bttn2 = Button(size_hint=(0.15, 0.1), pos_hint={"x": 0.49, "top": 0.58}, text=Languages[14][n],
                                on_press=lambda a: self.SearchDis(mode=1))

        if True:
            #Child disease
            self.father = TextInput(size_hint=(0.15, 0.1), pos_hint={"x": 0.48, "top": 0.28}, multiline=False,
                                 font_size=25)
            self.fathertxt = Label(size_hint=(0.15, 0.1), pos_hint={"x": 0.48, "top": 0.35}, text=Languages[16][n],
                              font_size=25)
            self.mother = TextInput(size_hint=(0.15, 0.1), pos_hint={"x": 0.68, "top": 0.28}, multiline=False,
                                    font_size=25)
            self.mothertxt = Label(size_hint=(0.15, 0.1), pos_hint={"x": 0.68, "top": 0.35}, text=Languages[15][n],
                                   font_size=25)
            self.submit2 = Button(size_hint=(0.15, 0.1), pos_hint={"x": 0.58, "top": 0.17}, text=Languages[9][n],
                                  on_press=lambda a: self.ChildDisease())

        self.layer.add_widget(self.search_by_id)
        self.layer.add_widget(self.disease_of_person)
        self.layer.add_widget(self.diseases_of_child)

    def SearchById(self):
        #WHEN search_by_id IS CLICKED OPENS RELATED LABEL AND BUTTONS AND CLOSES UNRELATED ONES IF THEY ARE OPEN
        if self.search_active == False:
            if self.search_dis is True:
                self.SearchDisease()
            if self.search_child == True:
                self.SearchChild()
            self.layer.add_widget(self.id)
            self.layer.add_widget(self.txt)
            self.layer.add_widget(self.submit)
            self.layer.add_widget(self.bttn1)
            self.search_active = True

        else:
            self.pop.dismiss()
            self.id.text = ""
            self.layer.remove_widget(self.id)
            self.layer.remove_widget(self.txt)
            self.layer.remove_widget(self.submit)
            self.layer.remove_widget(self.bttn1)
            self.search_active = False

    def SearchDisease(self):
        #WHEN disease_of_person IS CLICKED OPENS RELATED LABEL AND BUTTONS AND CLOSES UNRELATED ONES IF THEY ARE OPEN
        if self.search_dis is False:
            if self.search_active is True:
                self.SearchById()
            if self.search_child == True:
                self.SearchChild()
            self.layer.add_widget(self.id1)
            self.layer.add_widget(self.txt1)
            self.layer.add_widget(self.submit1)
            self.layer.add_widget(self.bttn2)
            self.search_dis = True
        else:
            self.id1.text = ""
            self.layer.remove_widget(self.id1)
            self.layer.remove_widget(self.txt1)
            self.layer.remove_widget(self.submit1)
            self.layer.remove_widget(self.bttn2)
            self.search_dis = False

    def Search(self, mode=0):
        #SEARCHS BY ID AND REPORTS THE PERSON WITH ID'S INFORMATION
        #IF ID IS INVALID THEN RETURNS NONE
        if mode == 0:
            id = self.id.text
            try:
                if id == None:
                    return None
                int(id)
                if Genotype.show_person(int(id)) == None:
                    self.pop.open()
            except:
                return None
        elif mode == 1:
            if Genotype.show_person(None, mode=1) == None:
                self.pop.open()

    def SearchDis(self, mode=0):
        #SEARCHS DISASE OF PERSON BY ID AND WRITES A REPORT INSIDE REPORTS FILE
        #IF ID IS INVALID RETURNS NONE
        if mode == 0:
            id = self.id1.text
            try:
                int(id)
                if Genotype.show_disease(int(id), 0) == None:
                    self.pop.open()
            except:

                return None
        elif mode == 1:
            Genotype.show_disease(mode=1)
            self.pop.open()

    def SearchChild(self):
        #WHEN diseases_of_child IS CLICKED OPENS RELATED LABEL AND BUTTONS AND CLOSES UNRELATED ONES IF THEY ARE OPEN
        if self.search_child == False:
            if self.search_dis == True:
                self.SearchDisease()
            if self.search_active == True:
                self.SearchById()
            self.layer.add_widget(self.father)
            self.layer.add_widget(self.fathertxt)
            self.layer.add_widget(self.mother)
            self.layer.add_widget(self.mothertxt)
            self.layer.add_widget(self.submit2)
            self.search_child = True
        else:
            self.father.text = ""
            self.mother.text = ""
            self.layer.remove_widget(self.father)
            self.layer.remove_widget(self.fathertxt)
            self.layer.remove_widget(self.mother)
            self.layer.remove_widget(self.mothertxt)
            self.layer.remove_widget(self.submit2)
            self.search_child = False

    def ChildDisease(self):
        #WRİTES A REPORT ABOUT THE FATHER WITH ID AND MOTHER WİTH İD'S CHİLDS DİSEASE POSİBİLİTİES
        #IF INVALID IDS RETURN NONE
        try:
            mother_id = self.mother.text
            father_id = self.father.text
            if Genotype.child_disease(int(father_id), int(mother_id)) == None:
                self.pop.open()
                self.father.text = ""
                self.mother.text = ""
        except:
            return None


class Settings(Screen):
    this = None
    #THIS IS THE SETTINGS SCENE CALLED FROM First SCENE
    def __init__(self, **kwargs):
        super(Settings, self).__init__(**kwargs)

        Settings.this = self
        self.home = HomeButton()
        self.canvas.add(Color(154/255, 154/255, 154/255, 1))
        self.canvas.add(Rectangle(pos=(390, 160), size=(260, 280)))
        self.canvas.add(Rectangle(pos=(60, 250), size=(200, 200)))

        self.logo = Image(source=getPath()+"\{}".format(Languages[18][n]+"\logo.jpg"), size_hint=(0.255, 0.3), pos_hint={"x": 0.07, "top": 0.4})
        self.add_widget(self.logo)

        self.turk = Button(text="Türkçe", size_hint=(0.2, 0.1), pos_hint={"x": 0.5, "top": 0.65},
                           on_press=lambda a: self.pressed(0))
        self.eng = Button(text="English", size_hint=(0.2, 0.1), pos_hint={"x": 0.5, "top": 0.45},
                          on_press=lambda a: self.pressed(1))

        self.lang = Label(text="", size_hint=(0.2, 0.2), pos_hint={"x": 0.6, "top": 0.60})

        self.data = Label(text=Languages[19][n], size_hint=(0.2, 0.2), pos_hint={"x": 0.1, "top": 0.75})
        self.priv = Button(text="", size_hint=(0.2, 0.1), pos_hint={"x": 0.1, "top": 0.6},
                           on_press=lambda a: self.ChangePrivacy())

        if dataPrivacy == 0:
            self.priv.text = Languages[21][n]
        elif dataPrivacy == 1:
            self.priv.text = Languages[20][n]
        if n == 0:
            self.lang.text = "dil: Türkçe"
        elif n == 1:
            self.lang.text = "Language: English"

        self.add_widget(self.home)
        self.add_widget(self.data)
        self.add_widget(self.priv)
        self.add_widget(self.turk)
        self.add_widget(self.eng)
        self.add_widget(self.lang)

        self.lay1 = FloatLayout()
        self.lab1 = Label(text=Languages[32][n], pos_hint={"x": 0.4, "top": 0.8}, size_hint=(0.2, 0.1))
        self.bttn2 = Button(text=Languages[12][n], pos_hint={"x": 0.4, "top": 0.2}, size_hint=(0.2, 0.1),
                            on_press=lambda a: self.pop2.dismiss())
        self.lay1.add_widget(self.bttn2)
        self.lay1.add_widget(self.lab1)
        self.pop2 = Popup(title=Languages[24][n], content=self.lay1, size_hint=(0.3, 0.3))



    def pressed(self, val):
        #CHANGES THE LANGUAGE VALUE N
        if val != n:
            ChangeN(val)

    def ChangePrivacy(self):
        #CHANGES THE dataPrivacy VALUE
        global dataPrivacy
        if dataPrivacy == 1:
            try:

                Genotype.dataPrivacy = 0
                dataPrivacy = 0
                Genotype.decoder(mode=2)
            except:
                Genotype.dataPrivacy = 1
                dataPrivacy = 1
                self.pop2.open()
        elif dataPrivacy == 0:
            try:


                Genotype.dataPrivacy = 1
                dataPrivacy = 1
                Genotype.decoder(mode=0)
            except:
                Genotype.dataPrivacy = 0
                dataPrivacy = 0
                self.pop2.open()
        if dataPrivacy == 0:
            self.priv.text = Languages[21][n]
        elif dataPrivacy == 1:
            self.priv.text = Languages[20][n]


        if dataPrivacy == 0:
            self.priv.text = Languages[21][n]
        elif dataPrivacy == 1:
            self.priv.text = Languages[20][n]


class Excel(Screen):
    #THIS IS THE EXCEL SCENE WHICH OPENS WHEN FROM First SCENE EXCEL BUTTON IS CLICKED
    this = None
    def __init__(self, **kwargs):
        super(Excel, self).__init__(**kwargs)
        Excel.this = self
        self.open1 = False
        self.open2 = False
        self.i = -1
        self.ChangePerson = Button(text=Languages[24][n], size_hint=(0.3, .2), pos_hint={"x": 0.1, "top": 0.9},
                                   font_size=20, on_press= lambda a: self.Search1())
        self.ReloadExcel = Button(text=Languages[26][n], size_hint=(0.3, .2), pos_hint={"x": 0.1, "top": 0.3},
                                   font_size=20, on_press=lambda a: self.Reloaded())
        self.ChangeDisLetter = Button(text=Languages[25][n], size_hint=(0.3, .2), pos_hint={"x": 0.1, "top": 0.6},
                                        font_size=20, on_press= lambda a: self.Search2())
        self.home = HomeButton()
        self.add_widget(self.home)
        self.add_widget(self.ChangeDisLetter)
        self.add_widget(self.ReloadExcel)
        self.add_widget(self.ChangePerson)

        if True:
            #Change Person
            self.id = TextInput(size_hint=(0.15, 0.1), pos_hint={"x": 0.68, "top": 0.88}, multiline=False, font_size=25)
            self.txt = Label(size_hint=(0.15, 0.1), pos_hint={"x": 0.68, "top": 0.95}, text=Languages[8][n],
                             font_size=25)
            self.submit = Button(size_hint=(0.15, 0.1), pos_hint={"x": 0.68, "top": 0.77}, text=Languages[9][n],
                                 on_press=lambda a: self.openSearch())

            self.lay = FloatLayout()

            self.fullname = TextInput(size_hint=(0.3, 0.1), pos_hint={"x": 0.1, "top": 0.7}, multiline=False, font_size=20)
            self.genotype = TextInput(size_hint=(0.3, 0.1), pos_hint={"x": 0.1, "top":  0.4}, multiline=False,
                                  font_size=25)
            self.phenotype = TextInput(size_hint=(0.2, 0.1), pos_hint={"x": 0.50, "top":  0.4}, multiline=False,
                                  font_size=20)
            self.id1 = Label(size_hint=(0.1, 0.1), pos_hint={"x": 0.5, "top":  0.7},
                                  font_size=20)
            self.sex = TextInput(size_hint=(0.1, 0.1), pos_hint={"x": 0.7, "top":  0.7}, multiline=False,
                                  font_size=20)
            self.text1 = Label(text=Languages[30][n], size_hint=(0.1, 0.1), pos_hint={"x": 0.1, "top":  0.9},
                                  font_size=20)
            self.text2 = Label(text=Languages[29][n], size_hint=(0.1, 0.1), pos_hint={"x": 0.1, "top":  0.5},
                                  font_size=20)
            self.text3 = Label(text=Languages[28][n], size_hint=(0.1, 0.1), pos_hint={"x": 0.50, "top":  0.5},
                                  font_size=20)
            self.text4 = Label(text=Languages[8][n], size_hint=(0.1, 0.1), pos_hint={"x": 0.5, "top":  0.9},
                                  font_size=20)
            self.text5 = Label(text=Languages[31][n], size_hint=(0.1, 0.1), pos_hint={"x": 0.7, "top":  0.9},
                                  font_size=20)
            self.bttn1 = Button(text=Languages[27][n], pos_hint={"x": 0.4, "top": 0.2}, size_hint=(0.2, 0.1),
                               on_press=lambda a: self.Apply())

            self.lay.add_widget(self.fullname)
            self.lay.add_widget(self.genotype)
            self.lay.add_widget(self.phenotype)
            self.lay.add_widget(self.id1)
            self.lay.add_widget(self.sex)
            self.lay.add_widget(self.text1)
            self.lay.add_widget(self.text2)
            self.lay.add_widget(self.text3)
            self.lay.add_widget(self.text4)
            self.lay.add_widget(self.text5)
            self.lay.add_widget(self.bttn1)

            self.lay1 = FloatLayout()
            self.lab1 = Label(text="", pos_hint={"x": 0.4, "top": 0.8}, size_hint=(0.2, 0.1))
            self.bttn2 = Button(text=Languages[12][n], pos_hint={"x": 0.4, "top": 0.2}, size_hint=(0.2, 0.1),
                                on_press=lambda a: self.pop2.dismiss())
            self.lay1.add_widget(self.bttn2)
            self.lay1.add_widget(self.lab1)

            self.pop = Popup(title=Languages[24][n], content=self.lay, size_hint=(0.8, 0.8))
            self.pop2 = Popup(title=Languages[24][n], content=self.lay1, size_hint=(0.3, 0.3))

            self.lay2 = FloatLayout()
            self.lab2 = Label(text=Languages[34][n], pos_hint={"x": 0.4, "top": 0.8}, size_hint=(0.2, 0.1))
            self.bttn3 = Button(text=Languages[12][n], pos_hint={"x": 0.4, "top": 0.2}, size_hint=(0.2, 0.1),
                                on_press=lambda a: self.pop3.dismiss())
            self.lay2.add_widget(self.bttn3)
            self.lay2.add_widget(self.lab2)
            self.pop3 = Popup(title=Languages[33][n], content=self.lay2, size_hint=(0.3, 0.3))

        if True:
            #changeDis letter
            self.geneName = Label(text="", size_hint=(0.15, 0.1), pos_hint={"x": 0.66, "top": 0.6},
                             font_size=15)
            self.next = Button(size_hint=(0.05, 0.1), pos_hint={"x": 0.8, "top": 0.6}, text="-->",
                                 on_press=lambda a: self.selectGene(1))
            self.previous = Button(size_hint=(0.05, 0.1), pos_hint={"x": 0.62, "top": 0.6}, text="<--",
                               on_press=lambda a: self.selectGene(-1))
            self.sbmt = Button(size_hint=(0.15, 0.1), pos_hint={"x": 0.65, "top": 0.45}, text=Languages[35][n],
                                 on_press=lambda a: self.send())
            self.float = FloatLayout()
            self.txxt = Label(text=Languages[36][n], size_hint=(0.1, 0.1), pos_hint={"x": 0.4, "top": 0.6})
            self.txxt2 = Label(text=Languages[38][n], size_hint=(0.1, 0.1), pos_hint={"x": 0.3, "top": 0.4})
            self.inpt = TextInput(size_hint=(0.3, 0.1), pos_hint={"x": 0.53, "top": 0.4}, multiline=False)
            self.sent = Button(text=Languages[37][n], size_hint=(0.1, 0.1), pos_hint={"x": 0.45, "top": 0.2},
                               on_press=lambda a: self.Change())

            self.float.add_widget(self.txxt)
            self.float.add_widget(self.txxt2)
            self.float.add_widget(self.inpt)
            self.float.add_widget(self.sent)


            self.pop4 = Popup(title="",content=self.float, size_hint=(0.6, 0.6))


    def Search1(self):
        #WHEN CHANGE PERSON BUTTON IS CLICKED OPENS RELATED LABEL AND BUTTONS AND CLOSES UNRELATED ONES IF THEY ARE OPEN
        if self.open1 == False:
            if self.open2 == True:
                self.Search2()
            self.add_widget(self.id)
            self.add_widget(self.txt)
            self.add_widget(self.submit)
            self.open1 = True
        elif self.open1 == True:
            self.remove_widget(self.id)
            self.remove_widget(self.txt)
            self.remove_widget(self.submit)
            self.open1 = False

    def openSearch(self):
        #WHEN CHANGE PERSON IS CLICKED THIS WILL OPEN AND FILL POPUPS LABELS AND BUTTONS TEXTS WITH INFORMATION
        #GATHERED FROM Genotype.py
        id = self.id.text
        try:
            int(id)
        except:
            return None
        res = Genotype.givePersonInfo(int(id))
        if type(res) == bool:
            return None
        else:
            self.fullname.text = res[0]
            self.genotype.text = res[1]
            self.phenotype.text = res[2]
            self.id1.text = res[3]
            self.sex.text = res[4]
            self.pop.open()

    def Apply(self):
        #APPLIES CHANGES IF Genotype.Error IS GREATER THEN 0 "Error" SCENE OPENS
        res = Genotype.AppylPerson(self.fullname.text, self.genotype.text, self.phenotype.text, self.id1.text, self.sex.text)
        if type(res) == str:
            self.lab1.text = res
            self.pop2.open()
        elif res == True:
            self.pop.dismiss()
            Genotype.new_excel()
            Genotype.main_func()
            if len(Genotype.errors) > 0:
                Error.this.setText()
                goToScene("Error")

    def Reloaded(self):
        #CALLS NEW_EXCEL() AND MAIN_FUNC() IF Genotype.Error IS GREATER THEN 0 "Error" SCENE OPENS
        Genotype.new_excel()
        Genotype.main_func()
        if len(Genotype.errors) > 0:
            Error.this.setText()
            goToScene("Error")
        else:
            self.pop3.open()

    def Search2(self):
        #WHEN CHANGE DİS LETTER BUTTON IS CLICKED
        #OPENS RELATED LABEL AND BUTTONS AND CLOSES UNRELATED ONES IF THEY ARE OPEN
        self.selectGene(1)
        if self.open2 == False:
            if self.open1 == True:
                self.Search1()
            self.add_widget(self.geneName)
            self.add_widget(self.next)
            self.add_widget(self.previous)
            self.add_widget(self.sbmt)
            self.open2 = True
        elif self.open2 == True:
            self.remove_widget(self.geneName)
            self.remove_widget(self.next)
            self.remove_widget(self.previous)
            self.remove_widget(self.sbmt)
            self.open2 = False

    def selectGene(self, m):
        #DETERMİNES THE TEXT OF self.geneName
        self.i += m
        l = Genotype.allGenes()
        if self.i < 0:
            self.i = len(l) - 1
        if self.i >= len(l):
            self.i = 0
        self.geneName.text = l[self.i]

    def send(self):
        #SENDS THE LETTER NAME FROM self.geneName.text AND OPENS self.pop4
        let = Genotype.OldLetters(self.geneName.text)
        self.txxt.text = Languages[36][n].format(let)
        self.pop4.open()

    def Change(self):
        #CHANGES GENE LETTERS AND ALL LETTERS RELATED TO THAT GENE
        #CALLED FROM pop4
        res = Genotype.ChangeGeneLetter(self.geneName.text, self.inpt.text)
        if type(res) == str:
            self.lab1.text = res
            self.pop2.open()
        elif res == False:
            return None
        elif res == True:
            self.inpt.text = ""
            self.pop4.dismiss()
            self.pop3.open()


class GenÖlçerApp(App):
    def build(self):

        self.icon = getPath() +"\{}\icon.ico".format(Languages[22][n])

        first = First(name="First")
        error = Error(name="Error")
        patients = Patients(name="Patients")
        setting = Settings(name="Settings")
        excel = Excel(name="Excel")
        manager.add_widget(first)
        manager.add_widget(error)
        manager.add_widget(patients)
        manager.add_widget(setting)
        manager.add_widget(excel)
        manager.transition = FadeTransition(duration=0.2)
        first.Start()

        return manager

GenÖlçerApp().run()

