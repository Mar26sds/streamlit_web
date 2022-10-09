#IMPORTACIONES
import streamlit as st
import pandas as pd
import webbrowser #para abrir un link  
from PIL import Image 
import gmaps
import streamlit.components.v1 as components #web embebida
import numpy as np



#CARGAR LOS DATOS QUE NECESITAMOS
data=pd.read_csv('/Users/mar/Proyecto final linkedin selenium/base_datos_limpia/data_limpia.csv')
coor=pd.read_csv('/Users/mar/Proyecto final linkedin selenium/coor/coor_folium.csv')

#CONFIGURACIONES DE LA PÁGINA
st.set_page_config(layout='centered', page_icon="img/logo3.png", page_title='Tu empresa ideal',menu_items={
        'Report a bug': 'https://www.linkedin.com/in/mar-sanchez-de-salas/',
        'About': "https://github.com/Mar26sds"})
        #poner en el about el link al repositorio


#CÓDIGO DE LA PÁGINA
st.title('BUSCAMOS LA EMPRESA IDEAL SEGÚN TUS GUSTOS')
#st.dataframe(data)


#PRIMER FILTRO POR COMUNIDAD AUTÓNOMA
st.caption('# Selecciona una Comunidad Autónoma o ciudad donde quieras buscar tu empresa ideal')
com=sorted(data['Comunidad Autónoma o ciudad'].unique())
com_autonoma = st.selectbox('',list(com))

data_ca_filtered=data[data['Comunidad Autónoma o ciudad']==com_autonoma]
data_ca_filtered.reset_index(drop=True, inplace=True)
if st.button('Ver todas las empresas de tu selección'):
    st.dataframe(data_ca_filtered)


#SEGUNDO FILTRO POR PALABRAS CLAVE
def filtrar (filtro):
    
    busqueda=[]
    #data_ca_filtered=data[data['Comunidad Autónoma o ciudad']==com_autonoma]
    for i in range(len(data_ca_filtered['Resumen de la empresa'])):
        if filtro in str(data_ca_filtered['Resumen de la empresa'][i]):
            busqueda.append(data_ca_filtered.loc[i])

    busqueda_df=pd.DataFrame(busqueda)
    
    return busqueda_df


st.caption('''# Escribe aquí tus palabras clave
## Sugerencias: consultoría, marketing, cloud, farmacéutica, videojuegos, deporte...''')
filtro= st.text_input('')
        
if filtro:
   busqueda_df=filtrar(filtro)
   st.dataframe(busqueda_df)


#MOSTRAR LAS PRIMERAS EMPRESAS CON SU WEB EMBEBIDA Y SU LINK A LINKEDIN
#components.iframe("https://docs.streamlit.io/en/latest")
if filtro:

    if len(busqueda_df)>0:
        if len(busqueda_df)>=3:
            top3_3=busqueda_df[:3]
            #Sacar los nombres de las tres primeras empresas
            top3_nombres_3=busqueda_df[:3]['Nombre de la Empresa']
            nombre1_3=top3_nombres_3.iloc[0]
            nombre2_3=top3_nombres_3.iloc[1]
            nombre3_3=top3_nombres_3.iloc[2]
            st.balloons()

            #Sacar las url de la página web de las tres primeras
            top3_url_3=busqueda_df[:3]['Página web de la empresa']
            #st.dataframe(top3)
            url1_3=top3_url_3.iloc[0]
            url2_3=top3_url_3.iloc[1]
            url3_3=top3_url_3.iloc[2]

            #Sacar los links de linkedin de las tres primeras
            top3_linkedin_3=busqueda_df[:3]['Perfil en linkedin']
            linkedin1_3=top3_linkedin_3.iloc[0]
            linkedin2_3=top3_linkedin_3.iloc[1]
            linkedin3_3=top3_linkedin_3.iloc[2]
            
        
            #Mostrar los resultados, el nombre, la página web embebida y el link de linkedin
            st.write('Página web primera empresa', nombre1_3)
            st.components.v1.iframe(str(url1_3), width=500, height=500, scrolling=True)
            st.write(nombre1_3, "[página web](%s)" % url1_3)
            st.write(nombre1_3, "[Perfil linkedin](%s)" % linkedin1_3)


            st.write('Página web segunda empresa', nombre2_3)
            st.components.v1.iframe(str(url2_3), width=500, height=500, scrolling=True)
            st.write(nombre2_3, "[página web](%s)" % url2_3)
            st.write(nombre2_3, "[Perfil linkedin](%s)" % linkedin2_3)


            st.write('Página web tercera empresa,', nombre3_3)
            st.components.v1.iframe(str(url3_3), width=500, height=500, scrolling=True)
            st.write(nombre3_3, "[página web](%s)" % url3_3)
            st.write(nombre3_3, "[Perfil linkedin](%s)" % linkedin3_3)
             #Se repite lo anterior para los resultados que tengan menos de 3 empresas

        if len(busqueda_df)<3:  
            if len(busqueda_df)==1:
                top3_nombres=busqueda_df[:1]['Nombre de la Empresa']
                nombre1=top3_nombres.iloc[0]
                st.balloons()


                top3_url=busqueda_df[:1]['Página web de la empresa'] 
                url1=top3_url.iloc[0]

                top3_linkedin=busqueda_df[:1]['Perfil en linkedin']
                linkedin1=top3_linkedin.iloc[0]

                st.write('Página web primera empresa', nombre1)
                st.components.v1.iframe(url1, width=500, height=500, scrolling=True)
                st.write(nombre1, "[página web](%s)" % url1)
                st.write(nombre1, "[Perfil linkedin](%s)" % linkedin1)

            elif len(busqueda_df)==2:
                top3_nombres=busqueda_df[:2]['Nombre de la Empresa']
                nombre1=top3_nombres.iloc[0]
                nombre2=top3_nombres.iloc[1]
                st.balloons()


                top3_url=busqueda_df[:2]['Página web de la empresa'] 
                url1=top3_url.iloc[0]
                url2=top3_url.iloc[1]

                top3_linkedin=busqueda_df[:2]['Perfil en linkedin']
                linkedin1=top3_linkedin.iloc[0]
                linkedin2=top3_linkedin.iloc[1]

                st.write('Página web primera empresa', nombre1)
                st.components.v1.iframe(url1, width=500, height=500, scrolling=True)
                st.write(nombre1, "[página web](%s)" % url1)
                st.write(nombre1, "[Perfil linkedin](%s)" % linkedin1)

                st.write('Página web segunda empresa', nombre2)
                st.components.v1.iframe(url2, width=500, height=500, scrolling=True)
                st.write(nombre2, "[página web](%s)" % url2)
                st.write(nombre2, "[Perfil linkedin](%s)" % linkedin2)
    else:
        st.write('Por ahora no encontramos tu empresa ideal 😢, intenta hacer la búsqueda en inglés')




#BARRA LATERAL
st.sidebar.image(Image.open("img/logo2.png"))
st.sidebar.caption('## Herramienta creada en octubre de 2022 por Mar Sánchez de Salas')

if st.sidebar.button("¿Qué es 'Tu empresa ideal'?"):
    st.sidebar.info('''
    Busca tu empresa ideal.

    Este proyecto nació por la necesidad de resolver un problema personal. Tras mi formación como Data Analyst empecé la búsqueda de empleo. 
       
    Quería encontrar una empresa en la que poder desarrollar alguno de mis gustos o habilidades, pero después de varios días no encontré ninguna. Además los filtros de LinkedIn hacían muy costoso el obtener una lista de empresas que cumplieran esos criterios.
        
    Por eso decidí desarrollar esta herramienta que solucionaría el problema. Establecí en LinkedIn un primer filtro que fue "empresas que trabajaran con data", y de ahí obtuve todas las empresas de España que ofrecían trabajo. Con el trabajo de limpieza de la base de datos y la implementación de filtros podía encontrar de forma sencilla un conjunto de empresas que cumplieran estos criterios.

    Teniendo la lista de empresas solo haría falta ponerse en contacto con cada una y tener un poco de suerte. Yo sigo buscando trabajo pero al menos me he puesto la búsqueda de mi empresa ideal un poco más sencilla.
    ''')


#BOTONES FINALES

st.caption('# Otras curiosidades')

if st.button('Ver gráfica del número de empresas por comunidad autonoma o ciudad de España'):
    st.image(Image.open("img/plot.png"))


if st.button('Ver mapa de las sedes de las empresas en el mundo'):
    st.map(coor)


st.caption('# ¿Contactamos?')
linkedin_mar = 'https://www.linkedin.com/in/mar-sanchez-de-salas/'
if st.button('Mi LinkedIn'):
    webbrowser.open_new_tab(linkedin_mar)

st.caption('''# ¿Quieres ver el código de esta web?
### Lenguaje Python''')
code = (''' 
#IMPORTACIONES
import streamlit as st
import pandas as pd
import webbrowser #para abrir un link  
from PIL import Image 
import gmaps
import streamlit.components.v1 as components #web embebida
import numpy as np



#CARGAR LOS DATOS QUE NECESITAMOS
data=pd.read_csv('/Users/mar/Proyecto final linkedin selenium/base_datos_limpia/data_limpia.csv')
coor=pd.read_csv('/Users/mar/Proyecto final linkedin selenium/coor/coor_folium.csv')

#CONFIGURACIONES DE LA PÁGINA
st.set_page_config(layout='centered', page_icon="img/logo3.png", page_title='Tu empresa ideal',menu_items={
        'Report a bug': 'https://www.linkedin.com/in/mar-sanchez-de-salas/',
        'About': "https://github.com/Mar26sds"})
        #poner en el about el link al repositorio


#CÓDIGO DE LA PÁGINA
st.title('BUSCAMOS LA EMPRESA IDEAL SEGÚN TUS GUSTOS')
#st.dataframe(data)


#PRIMER FILTRO POR COMUNIDAD AUTÓNOMA
st.caption('# Selecciona una Comunidad Autónoma o ciudad donde quieras buscar tu empresa ideal')
com=sorted(data['Comunidad Autónoma o ciudad'].unique())
com_autonoma = st.selectbox('',list(com))

data_ca_filtered=data[data['Comunidad Autónoma o ciudad']==com_autonoma]
data_ca_filtered.reset_index(drop=True, inplace=True)
if st.button('Ver todas las empresas de tu selección'):
    st.dataframe(data_ca_filtered)


#SEGUNDO FILTRO POR PALABRAS CLAVE
def filtrar (filtro):
    
    busqueda=[]
    #data_ca_filtered=data[data['Comunidad Autónoma o ciudad']==com_autonoma]
    for i in range(len(data_ca_filtered['Resumen de la empresa'])):
        if filtro in str(data_ca_filtered['Resumen de la empresa'][i]):
            busqueda.append(data_ca_filtered.loc[i])

    busqueda_df=pd.DataFrame(busqueda)
    
    return busqueda_df


st.caption('# Escribe aquí tus palabras clave
## Sugerencias: consultoría, marketing, cloud, farmacéutica, videojuegos, deporte...')
filtro= st.text_input('')
        
if filtro:
   busqueda_df=filtrar(filtro)
   st.dataframe(busqueda_df)


#MOSTRAR LAS PRIMERAS EMPRESAS CON SU WEB EMBEBIDA Y SU LINK A LINKEDIN
#components.iframe("https://docs.streamlit.io/en/latest")
if filtro:

    if len(busqueda_df)>0:
        if len(busqueda_df)>=3:
            top3_3=busqueda_df[:3]
            #Sacar los nombres de las tres primeras empresas
            top3_nombres_3=busqueda_df[:3]['Nombre de la Empresa']
            nombre1_3=top3_nombres_3.iloc[0]
            nombre2_3=top3_nombres_3.iloc[1]
            nombre3_3=top3_nombres_3.iloc[2]
            st.balloons()

            #Sacar las url de la página web de las tres primeras
            top3_url_3=busqueda_df[:3]['Página web de la empresa']
            #st.dataframe(top3)
            url1_3=top3_url_3.iloc[0]
            url2_3=top3_url_3.iloc[1]
            url3_3=top3_url_3.iloc[2]

            #Sacar los links de linkedin de las tres primeras
            top3_linkedin_3=busqueda_df[:3]['Perfil en linkedin']
            linkedin1_3=top3_linkedin_3.iloc[0]
            linkedin2_3=top3_linkedin_3.iloc[1]
            linkedin3_3=top3_linkedin_3.iloc[2]
            
        
            #Mostrar los resultados, el nombre, la página web embebida y el link de linkedin
            st.write('Página web primera empresa', nombre1_3)
            st.components.v1.iframe(str(url1_3), width=500, height=500, scrolling=True)
            st.write(nombre1_3, "[página web](%s)" % url1_3)
            st.write(nombre1_3, "[Perfil linkedin](%s)" % linkedin1_3)


            st.write('Página web segunda empresa', nombre2_3)
            st.components.v1.iframe(str(url2_3), width=500, height=500, scrolling=True)
            st.write(nombre2_3, "[página web](%s)" % url2_3)
            st.write(nombre2_3, "[Perfil linkedin](%s)" % linkedin2_3)


            st.write('Página web tercera empresa,', nombre3_3)
            st.components.v1.iframe(str(url3_3), width=500, height=500, scrolling=True)
            st.write(nombre3_3, "[página web](%s)" % url3_3)
            st.write(nombre3_3, "[Perfil linkedin](%s)" % linkedin3_3)
             #Se repite lo anterior para los resultados que tengan menos de 3 empresas

        if len(busqueda_df)<3:  
            if len(busqueda_df)==1:
                top3_nombres=busqueda_df[:1]['Nombre de la Empresa']
                nombre1=top3_nombres.iloc[0]
                st.balloons()


                top3_url=busqueda_df[:1]['Página web de la empresa'] 
                url1=top3_url.iloc[0]

                top3_linkedin=busqueda_df[:1]['Perfil en linkedin']
                linkedin1=top3_linkedin.iloc[0]

                st.write('Página web primera empresa', nombre1)
                st.components.v1.iframe(url1, width=500, height=500, scrolling=True)
                st.write(nombre1, "[página web](%s)" % url1)
                st.write(nombre1, "[Perfil linkedin](%s)" % linkedin1)

            elif len(busqueda_df)==2:
                top3_nombres=busqueda_df[:2]['Nombre de la Empresa']
                nombre1=top3_nombres.iloc[0]
                nombre2=top3_nombres.iloc[1]
                st.balloons()


                top3_url=busqueda_df[:2]['Página web de la empresa'] 
                url1=top3_url.iloc[0]
                url2=top3_url.iloc[1]

                top3_linkedin=busqueda_df[:2]['Perfil en linkedin']
                linkedin1=top3_linkedin.iloc[0]
                linkedin2=top3_linkedin.iloc[1]

                st.write('Página web primera empresa', nombre1)
                st.components.v1.iframe(url1, width=500, height=500, scrolling=True)
                st.write(nombre1, "[página web](%s)" % url1)
                st.write(nombre1, "[Perfil linkedin](%s)" % linkedin1)

                st.write('Página web segunda empresa', nombre2)
                st.components.v1.iframe(url2, width=500, height=500, scrolling=True)
                st.write(nombre2, "[página web](%s)" % url2)
                st.write(nombre2, "[Perfil linkedin](%s)" % linkedin2)
    else:
        st.write('Por ahora no encontramos tu empresa ideal 😢, intenta hacer la búsqueda en inglés')




#BARRA LATERAL
st.sidebar.image(Image.open("img/logo2.png"))
st.sidebar.caption('## Herramienta creada en octubre de 2022 por Mar Sánchez de Salas')

if st.sidebar.button("¿Qué es 'Tu empresa ideal'?"):
    st.sidebar.info('Info')


#BOTONES FINALES

st.caption('# Otras curiosidades')

if st.button('Ver gráfica del número de empresas por comunidad autonoma o ciudad de España'):
    st.image(Image.open("img/plot.png"))


if st.button('Ver mapa de las sedes de las empresas en el mundo'):
    st.map(coor)


st.caption('# ¿Contactamos?')
linkedin_mar = 'https://www.linkedin.com/in/mar-sanchez-de-salas/'
if st.button('Mi LinkedIn'):
    webbrowser.open_new_tab(linkedin_mar)

st.caption('# ¿Quieres ver el código de esta web?
### Lenguaje Python')
code = ' copy paste el código

if st.button('Ver código'):
    st.code(code, language='python')
''')
if st.button('Ver código'):
    st.code(code, language='python')

