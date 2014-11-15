
# -*- coding: utf-8 -*-
from Tkinter import *
import tkMessageBox
from tpb import TPB
from tpb import CATEGORIES, ORDERS
import webbrowser
import urllib
import json
import datetime



top = Tk()
top.geometry("700x700+30+30")
top.title('Series Downloader')
top['bg']="#D3D8E8"
seasonno=0
class season:
    
    def __init__(self):
        self.seasonflag=0

        self.ses=StringVar()
        self.ep=StringVar()
        self.title=""
        self.B = Button(top, text ="Proceed", command = self.listing ,bg='#3b5998',fg='white')
        self.mvid=-1
        label = Label( top, text="Enter name of the Series",fg='#0e385f',bg='#D3D8E8',font=("Helvetica", 12))
        label.place(x=20,y=60,width=200,height=30)
        moviename = StringVar()
        self.name = Entry(top, textvariable=moviename)
        self.name.config(font=('Helvetica',(10)),bg='white',fg='black')
        self.name.place(x=240,y=60,width=300,height=30)
        """
        label = Label( top, text="Enter Season Number",fg='#0e385f',bg='#D3D8E8',font=("Helvetica", 12))
        label.place(x=20,y=100,width=200,height=30)
        moviename = StringVar()
        season = Entry(top, textvariable=moviename)
        season.config(font=('Helvetica',(10)),bg='white',fg='black')
        season.place(x=240,y=100,width=300,height=30)

        label = Label( top, text="Enter Episode Number",fg='#0e385f',bg='#D3D8E8',font=("Helvetica", 12))
        label.place(x=20,y=140,width=200,height=30)
        moviename = StringVar()
        ep = Entry(top, textvariable=moviename)
        ep.config(font=('Helvetica',(10)),bg='white',fg='black')
        ep.place(x=240,y=140,width=300,height=30)"""
        """quality=StringVar()
        quality.set('Quality')
        qualitychoices = ['480p,720p']
        option = OptionMenu(top, quality, *qualitychoices)
        option.config(font=('Helvetica',(10)),bg='#3b5998',fg='white')
        option.place( x=210,y=120,width=80,height=30)
        """

        label = Label( top, text="©Melvin Philips Y.N.W.A",fg='#0e385f',bg='#D3D8E8',font=("Helvetica", 10))
        label.place(x=400,y=610,width=200,height=30)



        self.B.place(x=280,y=180,width=100,height=30)
        

    def listing(self):
        if(self.seasonflag==1):
            selectedseason=self.ses.get()
            #print selectedseason
        flag=0
        print "1st time"+self.title
        if(self.title==""):
            flag=0
        elif(self.title!=self.name.get()):
            flag=1
            self.seasonflag=0
            try:
                print 'in'
                label = Label( top, text='',fg='#0e385f',bg='#D3D8E8')
                label.place(x=280,y=(330),width=100,height=30)
                label = Label( top, text='',fg='#0e385f',bg='#D3D8E8')
                label.place(x=300,y=120,width=80,height=30)
                self.dbutton.place_forget()
                self.epoption.place_forget()
                self.dbutton.destroy()
                self.epoption.destroy()
            except(AttributeError):
                print "error"
                
                
            
            
            
        
        if(self.seasonflag==0):    
             # create a TPB object with default domain

            # search for 'public domain' in 'movies' category
            
            # sort this search by count of seeders, and return a multipage result
            #search.order(ORDERS.SEEDERS.ASC).multipage()

            # print all torrent descriptions
            nameofseries=self.name.get()
            self.title=nameofseries
            #url="http://series-ortiz.rhcloud.com/series?name=dexter"
            url = "http://www.omdbapi.com/?t="+nameofseries
            #url="https://api.themoviedb.org/3/find/tt0773262?api_key=7d6201e37c46d499e85aa5ed657a3386&external_source=imdb"
            try:
                response = urllib.urlopen(url).read()
                #print response
                jsonvalues = json.loads(response)
            except IOError:
                tkMessageBox.showerror(title='Not Availabel',message='Internet Connection needs to be checked')

            try:
                imdbid= jsonvalues['imdbID']
            except(KeyError):
                tkMessageBox.showerror(title='Not Available',message='Check name of the series! Not listed on Imdb.com')
                exit
                
            url="https://api.themoviedb.org/3/find/"+imdbid+"?api_key=7d6201e37c46d499e85aa5ed657a3386&external_source=imdb_id"
            response = urllib.urlopen(url).read()
            jsonvalues = json.loads(response)
            #print jsonvalues
            try:
                self.mvid=jsonvalues['tv_results'][0]['id']
            except(IndexError):
                tkMessageBox.showerror(title='Not Available',message='Seems like the Series is not popular .Sorry ! Not listed on TheMovieDB.com')
            url="https://api.themoviedb.org/3/tv/"+str(self.mvid)+"?api_key=7d6201e37c46d499e85aa5ed657a3386"
            response = urllib.urlopen(url).read()
            #print response
            jsonvalues = json.loads(response)
            seasonsno=jsonvalues['number_of_seasons']
            #print seasonsno
            
            self.ses.set('Season')
            sno=[1]
            for i in range(2,int(seasonsno)+1):
                t=str(i)
                sno=sno+[t]
            option = OptionMenu(top,self.ses, *sno)
            option.config(font=('Helvetica',(10)),bg='#3b5998',fg='white')
            option.place( x=210,y=120,width=80,height=30)
            

            self.seasonflag=1
            """no_of_season=season.get()
            if(int(no_of_season)<10):
                no_of_season='0'+no_of_season
            epno=ep.get()
            if(int(epno)<10):
                epno='0'+epno
            
            searchquery=nameofseries+' s'+no_of_season+'e'+epno
            print searchquery
            for torrent in t.search(searchquery):
                 link=torrent.magnet_link;
                 webbrowser.open_new_tab(link)
                 break;
                 """
        else:
            selectedseason=self.ses.get()
            eplist=[1]
            self.ep.set('Episode')
            url="https://api.themoviedb.org/3/tv/"+str(self.mvid)+"/season/"+selectedseason+"?api_key=7d6201e37c46d499e85aa5ed657a3386"
            response = urllib.urlopen(url).read()
            #print response
            jsonvalues = json.loads(response)
            maxep=jsonvalues['episodes'][-1]['episode_number']
            todaysdate=datetime.datetime.now().date()
            todaysdate=str(todaysdate)
            date1= datetime.datetime.strptime(todaysdate, '%Y-%m-%d')
            maxepno=maxep
            for i in range (0,maxep):
                airdate=jsonvalues['episodes'][i]['air_date']
                date2=datetime.datetime.strptime(airdate, '%Y-%m-%d')
                if date2>date1:
                    maxepno=i
                    break;
            
		
            jsonep=jsonvalues
            #print maxep

            for j in range(2,maxepno+1):
                t=str(j)
                eplist=eplist+[t]
                
            self.epoption = OptionMenu(top, self.ep, *eplist)
            self.epoption.config(font=('Helvetica',(10)),bg='#3b5998',fg='white')
            self.epoption.place( x=300,y=120,width=80,height=30)
            self.dbutton = Button(top, text ="Download", command = lambda:self.download(jsonep),bg='#3b5998',fg='white')
            self.dbutton.place(x=280,y=330,width=100,height=30)
        print "1st time"+self.title

    def download(self,jsonep):
        t = TPB('https://thepiratebay.org')
        #search = t.search('Game Of Thrones s04e01', category=CATEGORIES.VIDEO)
        no_of_season=self.ses.get()
        if(int(no_of_season)<10):
            no_of_season='0'+no_of_season
        epno=self.ep.get()
        if(int(epno)<10):
            epno='0'+epno
            
        searchquery=self.title+' s'+no_of_season+'e'+epno
        print searchquery
        
      
        i=0
	try:
		for torrent in t.search(searchquery,category=CATEGORIES.VIDEO.TV_SHOWS):
		    nameoftorr=torrent.title
		    nameoftorr=nameoftorr.lower()
		    size=torrent.size
		    i=i+1
		    if(nameoftorr.find(searchquery.lower())):
		        link=torrent.magnet_link;
			
			webbrowser.open_new_tab(link)
			
		        try:
		            shortdescp=jsonep['episodes'][int(self.ep.get())-1]['overview']
		            #print jsonep['episodes'][int(self.ep.get())]['overview']
		            sdesc=StringVar()
		            sdesc.set('Short Description :')
		            label = Label( top, textvariable=sdesc,fg='#0e385f',bg='#D3D8E8')
		            label.place(x=50,y=375,width=300,height=30)

		            lengthofshort=len(shortdescp)
		            no=lengthofshort/75
		            temp2=0
		            temp3=0
		            for j in range(0,no+1) :
		                shortdesc=StringVar()
		                
		                temp=shortdescp.find(' ',(75*j)+75,(75*j)+90)
		                temp2=temp
		                temp=temp%75
		                stri=shortdescp[(75*j)+temp3:(75*j)+75+temp]
		                temp3=temp2%75
		                shortdesc.set(stri)
		                label = Label( top, textvariable=shortdesc,fg='#0e385f',bg='#D3D8E8')
		                if j!=no:
		                    label.place(x=50,y=(400+(30*j)),width=600,height=30)
		                else:
		                    t=j%8
		                    label.place(x=50,y=(400+(30*j)),width=600,height=30)
		                    label = Label( top, text='',fg='#0e385f',bg='#D3D8E8')
		                    label.place(x=50,y=(400+(30*(j+1))),width=600,height=30*t)
		        except(Exception):
		            print "Error";
		        break;
		    if(i>10):
		        tkMessageBox.showerror(title='Not Available',message='Torrent File not available on PirateBay')
		        break;
		    
		if(i==0):
		    tkMessageBox.showerror(title='Not Available',message='Torrent File not available on PirateBay')
	except Exception:
		print "Net connection not established or Pirate Bay Blocked"	
		
        

if __name__ == "__main__":
    s=season()
    top.mainloop()
