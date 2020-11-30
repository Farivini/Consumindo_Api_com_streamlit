import requests
import streamlit as st


st.title("Consultar CEP")
busca = st.text_input("Digite o CEP que quer buscar: ")
requisicao= requests.get('https://viacep.com.br/ws/{}/json/'.format(busca))
data = requisicao.json()

if st.button("Buscar"):
    if len(busca) < 8:
        st.write("{} : Cep invalido".format(busca))

    if 'erro' not in data:
        st.write("----------- Cep localizado  -----------")
        st.write('CEP: {}'.format(data['cep']))
        st.write('Cidade: {}'.format(data['localidade']))
        st.write('Estado: {}'.format(data['uf']))
        st.write('{} => Bairro {}'.format(data['logradouro'], data['bairro']))
    else:
        st.write("{}: Cep invalido".format(busca))



""" Autor : Vinicius Farineli Freire"""