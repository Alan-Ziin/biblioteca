from classes import Library, Book
import streamlit as st

if "bookcase" not in st.session_state:
    st.session_state["bookcase"] = Library()

bookcase = st.session_state["bookcase"]

name_book = st.text_input("Name of book: ", key="titleText")
actor_of_book = st.text_input("Actor and writer of book: ", key="actorText")
year_publication = st.text_input("Year of publication of book: ", key="yearNumber")
idOfBook = st.text_input("Id of Book: ", key="idNumber")

def buttonSubmit():
    bookCreated = Book(name_book,actor_of_book,year_publication,idOfBook)
    bookcase.add_books(bookCreated)
    st.session_state["titleText"] = ""
    st.session_state["actorText"] = ""
    st.session_state["yearNumber"] = ""
    st.session_state["idNumber"] = ""

buttonForms = st.button("Confirm the Forms", on_click=buttonSubmit)

for i in bookcase.books:
    st.text(str(i))