# /PAGES/TEAM.PY
# IMPORTING THE REQUIRED MODULES IN THE WORK SPACE 
import streamlit as stream

# PAGE CONFIGURATION
stream.set_page_config(page_title="TEAM", page_icon=":eye", layout="wide")


def main():
      stream.header("TEAM MAN & WOMAN")
      stream.subheader("SUVAJITKARMKAR -  PRIYA DHARSHINI G")

      stream.success("I, Suvajit Karmakar, along with my talented and supportive teammate Priya Dharshini G, developed this innovative project based on the concept of a handless attendance system. The project leverages cutting-edge face-detection technology to streamline and modernize the attendance process, ensuring accuracy and efficiency while minimizing human intervention.")
      stream.info("THANK YOU SO MUCH")


# MAIN
if __name__ == '__main__':
      main()