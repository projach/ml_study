import streamlit as st
import requests
import json



def fetch_somth():
	base_url = "http://127.0.0.1:8000/results"
	resp = requests.post(base_url)
	return json.dumps(resp.json())

def formating_string():
    return  fetch_somth().replace('[','').split(',')
    
    


def main():
	st.title("Main App")

	if st.button("Retrieve"):
		results = formating_string()
		st.write(f"{results[0]}")



if __name__ == '__main__':
	main()
