import streamlit as st

st.title('SGPA, CGPA and Percentage Converter')

st.subheader('SGPA to CGPA and Percentage')

option = st.selectbox('Select the option', options=['','Percentage', 'SGPA', 'CGPA'])

if option=='Percentage':
    marks_obtain = st.number_input('Enter the marks')
    total_marks = st.number_input('Enter total marks')
    if st.button('Submit'):
        percentage = (marks_obtain/total_marks)*100
        st.text(f'Percentage: {percentage}')

if option=='SGPA':
    percentage = st.number_input('Enter the percentage')
    if st.button('Submit'):
        sgpa = (percentage/10)+0.75
        st.text(f'SGPA: {sgpa}')

if option=='CGPA':
    try:
        sgpas = []
        sems = st.number_input('Number of semester')
        check = True
        j = 0
        for i in range(int(sems)):
            check = False
            a = st.number_input(f'SGPA of Semester {i+1}')
            sgpas.append(a)
        if st.button('Submit'):
            check = True
        if check:
            st.text(f'CGPA of all {sems} semester: {sum(sgpas)/sems}')
    except:
        pass
    
        

