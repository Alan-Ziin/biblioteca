from classes import Library, Book
import streamlit as st

if "bookcase" not in st.session_state:
    st.session_state["bookcase"] = Library()

if "error" not in st.session_state:
    st.session_state["error"] = ""

bookcase = st.session_state["bookcase"]

name_book = st.text_input("Name of book: ", key="titleText")
actor_of_book = st.text_input("Actor and writer of book: ", key="actorText")
year_publication = st.text_input("Year of publication of book: ", key="yearNumber")
idOfBook = st.text_input("Id of Book: ", key="idNumber")
textsInputs = [name_book, actor_of_book, year_publication, idOfBook]

def buttonSubmit():
    st.session_state['error'] = ""
    for i in textsInputs:
        if i == "":
            st.session_state['error'] = "Error, please filled the forms"
            return
    try:
       int(year_publication)
    except:
        st.session_state['error'] = "Error, please write just number in Year"
        return
        
    bookCreated = Book(name_book,actor_of_book,year_publication,idOfBook)
    bookcase.add_books(bookCreated)
    st.session_state["titleText"] = ""
    st.session_state["actorText"] = ""
    st.session_state["yearNumber"] = ""
    st.session_state["idNumber"] = ""

buttonForms = st.button("Confirm the Forms", on_click=buttonSubmit)

if st.session_state['error']:
    st.write(st.session_state['error'])
else:
    for i in bookcase.books:
        st.text(str(i))