import streamlit as st
import requests

def fetch_somth():
	base_url = "http://127.0.0.1:8000/results"
	resp = requests.post(base_url)
	return resp.json()

def main():
	st.title("Main App")

	if st.button("Retrieve"):
		results = fetch_somth()
		st.json(results)



if __name__ == '__main__':
	main()
