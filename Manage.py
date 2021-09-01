# -*- coding: utf-8 -*-
"""
Created on Sun Jul 18 00:17:45 2021

@author: Abhijna
"""

import streamlit as st
import streamlit.components.v1 as stc
import plotly.express as px
import pandas as pd


def morn(df):
    
                mean1 = df['Idli'].mean()
                mean2 = df['dosa'].mean()
                mean3 = df['Palav'].mean()
                mean4 = df['Set Dosa'].mean()
                mean5 = df['Samosa'].mean()
                mean6 = df['Omelette'].mean()
                mean7 = df['Vada'].mean()
                
                langs = ['Idli','dosa','Palav','Set Dosa','Samosa','Omelette','Vada']
                m = [mean1,mean2,mean3,mean4,mean5,mean6,mean7]
                bar_chart = px.bar(x = langs,y = m)
                st.plotly_chart(bar_chart)
                result,result1 = predi(df)
                st.success('Suggested breakfast for weekday is {}'.format(result))
                st.success('Suggested breakfast for weekend is {}'.format(result1))
                          
def lunc(fd):
      
                mean8 = fd['Veg Biryani'].mean()
                mean9 = fd['Chicken Biryani'].mean()
                mean10 = fd['Mutton Biryani'].mean()
                mean11= fd['Fish Curry'].mean()
                mean12= fd['Ghee Rost'].mean()
                mean13= fd['Gobi Manchurian'].mean()
                mean14= fd['Paneer chili'].mean() 
                
                langs = ['Veg Biryani','Chicken Biryani','Mutton Biryani','Fish Curry','Ghee Rost','Gobi Manchurian','Paneer chili']
                m = [mean8,mean9,mean10,mean11,mean12,mean13,mean14]  
                bar_chart = px.bar(x = langs,y = m)
                st.plotly_chart(bar_chart)  
                
                result,result1 = identify(fd)
                st.success('Suggested Lunch for weekday is {}'.format(result1))
                st.success('Suggested Lunch for weekend is {}'.format(result)) 
                
def predi(df):
    
                df['Time Stamp'] = pd.to_datetime(df['Time Stamp'])
                weekends=df[df['Time Stamp'].dt.weekday > 5] 
                
                wmean1 = weekends['Idli'].mean()
                wmean2 = weekends['dosa'].mean()
                wmean3 = weekends['Palav'].mean()
                wmean4 = weekends['Set Dosa'].mean()
                wmean5 = weekends['Samosa'].mean()
                wmean6 = weekends['Omelette'].mean()
                wmean7 = weekends['Vada'].mean()  
                
                df['Time Stamp'] = pd.to_datetime(df['Time Stamp'])
                weekdays=df[df['Time Stamp'].dt.weekday <= 5] 
                
                wdmean1 = weekdays['Idli'].mean()
                wdmean2 = weekdays['dosa'].mean()
                wdmean3 = weekdays['Palav'].mean()
                wdmean4 = weekdays['Set Dosa'].mean()
                wdmean5 = weekdays['Samosa'].mean()
                wdmean6 = weekdays['Omelette'].mean()
                wdmean7 = weekdays['Vada'].mean()
                
                list1 = [wdmean1,wdmean2,wdmean3,wdmean4,wdmean5,wdmean6,wdmean7]
                wfood = ['Idli','dosa','Palav','Set Dosa','Samosa','Omelette','Vada']
                list2=  [wmean1,wmean2,wmean3,wmean4,wmean5,wmean6,wmean7]
                list3=list1.copy()
                list1.sort()
                list4=list2.copy()
                list2.sort()
                for i in list3:
                    if i == list1[-1]:
                        wdindex=list3.index(i)
                for i in list4:
                    if i == list2[-1]:
                        weindex=list4.index(i)
                return  wfood[wdindex],wfood[weindex] 
            
def identify(fd):
                fd['Time Stamp'] = pd.to_datetime(fd['Time Stamp'])
                lunch_weekends=fd[fd['Time Stamp'].dt.weekday > 5] 
                
                lwmean1 = lunch_weekends['Veg Biryani'].mean()
                lwmean2 = lunch_weekends['Chicken Biryani'].mean()
                lwmean3 = lunch_weekends['Mutton Biryani'].mean()
                lwmean4 = lunch_weekends['Fish Curry'].mean()
                lwmean5 = lunch_weekends['Ghee Rost'].mean()
                lwmean6 = lunch_weekends['Gobi Manchurian'].mean()
                lwmean7 = lunch_weekends['Paneer chili'].mean()  
                
                fd['Time Stamp'] = pd.to_datetime(fd['Time Stamp'])
                lunch_weekdays=fd[fd['Time Stamp'].dt.weekday <= 5]  
                
                lwdmean1 = lunch_weekdays['Veg Biryani'].mean()
                lwdmean2 = lunch_weekdays['Chicken Biryani'].mean()
                lwdmean3 = lunch_weekdays['Mutton Biryani'].mean()
                lwdmean4 = lunch_weekdays['Fish Curry'].mean()
                lwdmean5 = lunch_weekdays['Ghee Rost'].mean()
                lwdmean6 = lunch_weekdays['Gobi Manchurian'].mean()
                lwdmean7 = lunch_weekdays['Paneer chili'].mean()  
                
                llist1 = [lwdmean1,lwdmean2,lwdmean3,lwdmean4,lwdmean5,lwdmean6,lwdmean7]
                lwfood=  ['Veg Biryani','Chicken Biryani','Mutton Biryani','Fish Curry','Ghee Rost','Gobi Manchurian','Paneer chili']
                llist2=  [lwmean1,lwmean2,lwmean3,lwmean4,lwmean5,lwmean6,lwmean7]
                llist3=llist1.copy()
                llist1.sort()
                llist4=llist2.copy()
                llist2.sort()
                for i in llist3:
                    if i == llist1[-1]:
                        lwdindex=llist3.index(i)
                for i in llist4:
                    if i == llist2[-1]:
                        lweindex=llist4.index(i)    
                return  lwfood[lwdindex],lwfood[lweindex]               
                              

def main():
    st.title("Make Choice Easier")

    menu = ["Morning","Afternoon","About"]
    choice = st.sidebar.selectbox("Menu",menu)

    if choice == "Morning":
        st.subheader("Breakfast")
        data_file = st.file_uploader("Upload CSV",type=['csv'])
        if st.button("Process"):
            if data_file is not None:
                file_details = {"Filename":data_file.name,"FileType":data_file.type,"FileSize":data_file.size}
                st.write(file_details)
                df = pd.read_csv(data_file)
                st.dataframe(df)
                morn(df)
                 
                     


    elif choice == "Afternoon":
        st.subheader("Lunch")
        data_file = st.file_uploader("Upload CSV",type=['csv'])
        if st.button("Process"):
            if data_file is not None:
                file_details = {"Filename":data_file.name,"FileType":data_file.type,"FileSize":data_file.size}
                st.write(file_details)
                fd = pd.read_csv(data_file)
                st.dataframe(fd)
                lunc(fd)
            

    else:
        st.subheader("About")
        #st.info("Built with Streamlit")
        st.info("Harshith and @Team")
        st.text("Food Management")



if __name__ == '__main__':
    main()