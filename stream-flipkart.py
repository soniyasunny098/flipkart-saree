 
from pycaret.classification import load_model, predict_model
import streamlit as st
import pandas as pd
import numpy as np
model = load_model('flipkart')






def predict(model, input_df):
    predictions_df = predict_model(estimator=model, data=input_df)
    predictions = predictions_df['Label'][0]
    return predictions

def run():
    from PIL import Image
    image = Image.open('saree-flip.jpeg')
    image_office = Image.open('sareeset.jpg')
    st.image(image,use_column_width=True)
    add_selectbox = st.sidebar.selectbox(
    "How would you like to predict?",
    ("Online", "Batch"))
    st.sidebar.info('This app is created to predict OFFER of sarees ')
    st.sidebar.success('https://www.pycaret.org')
    st.sidebar.image(image_office)
    st.title("Predicting OFFER of sarees")
    if add_selectbox == 'Online':
        product_name = st.selectbox('product_name', ['other', 'Printed Daily Wear','Woven','Solid Fashion','Self Design'])
        brand_name = st.selectbox('brand_name', ['other', 'SAARA','Ad SAREES','KARA','VeBNoR'])
        item_name = st.selectbox('item_name', ['Printed Daily Wear', 'Embroidered Kanjivaram','Solid Fashion Cotton','Banarasi Art Silk','other'])
        Type = st.selectbox('Type', ['Regular Sari', 'other','Unstitched','Bollywood'])
        discount_price=st.number_input('discount_price' , min_value=0.1, max_value=10000.0, value=0.1)
        orginal_price =st.number_input('orginal_price',min_value=0.1, max_value=10000.0, value=0.1)
        secondary_colour= st.selectbox('secondary_colour', ['other colour', 'Casual','Pink','Gold','Multicolor'])
        fashion= st.selectbox('fashion', ['Printed', 'other','Woven','Embroidered','Solid'])
        rating = st.number_input('rating', min_value=3.0, max_value=5.0, value=3.0)
        Trend_place= st.selectbox('Trend_place', ['Wedding', 'Casual','other','Dry Clean Only	','Machine Wash'])
        
        output=""
        input_dict={'product_name':product_name,'brand_name':brand_name,'item_name':item_name,'Type':Type,'discount_price': discount_price,'orginal_price':orginal_price,'secondary_colour' : secondary_colour,'fashion':fashion,'rating':rating,'Trend_place':Trend_place}
        input_df = pd.DataFrame([input_dict])
        if st.button(" PREDICT OFFER"):
            output = predict(model=model, input_df=input_df)
            output = str(output)
            if output == '0' :
              output="YOU WILL GET ABOVE 75% OFFER"
            else:
              output="YOU WILL GET 75 AND LESSER PERCENT OFFER"
        st.success('The Prediction   --  {}'.format(output))
       
    if add_selectbox == 'Batch':
        file_upload = st.file_uploader("Upload csv file for predictions", type=["csv"])
        if file_upload is not None:
            data = pd.read_csv(file_upload)            
            predictions = predict_model(estimator=model,data=data)
            st.write(predictions)
def main():
    run()

if __name__ == "__main__":
  main()
