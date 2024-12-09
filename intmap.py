# Import necessary libraries
import streamlit as st
import pandas as pd
import plotly.express as px


def load_data(data):
    return pd.read_csv(data)

def main():
    st.title('Interactive Map')
    menu = ['Home','Advanced','Attendees','About']
    world = load_data('worldcities.csv')

    choice = st.sidebar.selectbox('Menu',menu)
    color = st.sidebar.color_picker('Color',value='#9E1FA2')

    if choice == 'Home':
        
        with st.expander('Data View'):
            st.dataframe(world)

            fig = px.scatter_mapbox(world, lat='lat', lon='lng',hover_name='city',hover_data=['country','population'],
                              color_discrete_sequence=[color], zoom=1,height=700)
            
            fig.update_layout(mapbox_style='open-street-map')
            st.plotly_chart(fig)

    elif choice == 'Advanced':

        countries_list = world['country'].unique().tolist()
        selected_country = st.sidebar.selectbox('Countries',countries_list)

        with st.expander('Selected country view'):
            df = world[world['country']==selected_country]
            st.dataframe(df)

            fig = px.scatter_mapbox(df, lat='lat', lon='lng',hover_name='city',hover_data=['country','population'],
                              color_discrete_sequence=[color], zoom=1,height=700)
            
            fig.update_layout(mapbox_style='open-street-map')
            st.plotly_chart(fig)
    elif choice == 'Attendees':
        cities_list = world['city'].unique().tolist()
        selected_city = st.multiselect('Cities',cities_list)

        with st.expander('Data View'):
            df = world[world['city'].isin(selected_city)]
            st.dataframe(df)

            fig = px.scatter_mapbox(df, lat='lat', lon='lng',hover_name='city',hover_data=['country','population'],
                              color_discrete_sequence=[color], zoom=1,height=700)
            
            fig.update_layout(mapbox_style='open-street-map')
            st.plotly_chart(fig)
    else:
        st.subheader('About')


if __name__ == '__main__':
    main()

