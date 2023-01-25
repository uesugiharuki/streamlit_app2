import streamlit as st 
from PIL import Image
import pandas as pd
import numpy as np
import folium
from streamlit_folium import folium_static
st.title('はるきのページ')
st.caption('これは、テストアプリです。')



#イメージテスト

image=Image.open(r'haruki_app\data\img_2.gif')
st.image(image,width=200)


#動画テスト
if st.checkbox('音声を再生....'):
    video_file =open(r'haruki_app\data\01.m4a','rb')
    video_bytes=video_file.read()
    st.video(video_bytes)


with st.form(key='profile_form'):

    #textbox
    name=st.text_input('名前')
    address=st.text_input('住所')
    
    #selectbox
    age_category=st.selectbox(
        '年齢層',
        ('子供(18未満)','大人(18以上60未満)','シニア(60以上)')    )
    
    
    
    sumit_btn=st.form_submit_button('送信')
    cancel_btn=st.form_submit_button('キャンセル')
    if sumit_btn:
        st.text(f'{address}にお住みの{name}さん、こんにちは')
        st.text(f'年齢層　:  {age_category}')
        
    exp=st.expander('よく、買物、食事に行く場所です。')
    exp.write('マクドナルドR165店')
    exp.write('ビック　名張店')
    exp.write('サンディ　名張店')
    
  
        
   
 # ページ設定

# 地図の中心の緯度/経度、タイル、初期のズームサイズを指定します。




df1=pd.DataFrame([[34.620535, 136.105488,'ビック　名張店'],
                     [34.62287760357736, 136.10483940110373,'マクドナルドR165店'],
                     [34.624148949984914, 136.1024683283538,'サンディ　名張店']],columns=['lat','lon','shopname'])


st.title("店舗地図") # タイトル
rad = st.slider('拠点を中心とした円の半径（m）',
                value=40,min_value=5, max_value=50) # スライダーをつける
st.subheader("各拠点からの距離{:,}m".format(rad)) # 半径の距離を表示
m = folium.Map(location=[34.620535, 136.105488], zoom_start=15
              ) # 地図の初期設定



for i ,row in df1.iterrows():
    folium.Marker(
        # 緯度と経度を指定
        #location=['lat','lon'],
        location=[row.lat, row.lon],
        
        popup=folium.Popup(row.shopname, max_width=50),
        # アイコンの指定(アイコン、色)
        icon=folium.Icon(icon="home",icon_color="green", color="red")
    ).add_to(m) 
    


folium_static(m) # 地図情報を表示

   