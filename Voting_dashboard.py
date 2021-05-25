import streamlit as st
import glob
import cv2 as cv
import pandas as pd
import os
import datetime
import csv
import SessionState  

st.set_page_config(layout="wide") #use wide layout

st.title("Dashboard for CNN Interpretation")
st.markdown("Welcome to this interactive dashboard.")

img_path = 'sample_images/ori_images/'
heat_map_path = 'sample_images/heat_maps/'
images_list = os.listdir(img_path)
images_list.insert(0,'')

session = SessionState.get(run_id=0)
clear_selection_button = st.sidebar.button("Click to reset selection")
if clear_selection_button:
	session.run_id += 1

selected = st.sidebar.selectbox('Select one option:',images_list, format_func=lambda x: 'Select an option' if x == '' else x, key=session.run_id)


col1, col2, col3, col4, col5 = st.beta_columns((1,1,1,1,1))
agree1, agree2, agree3, agree4, agree5 = st.beta_columns((1,1,1,1,1))

mapping_table = pd.read_csv('mapping_table.csv')


if selected:
	st.sidebar.success('Yay! 🎉')
	st.sidebar.success('You selected '+str(selected))
	image_1 = cv.imread(img_path +selected)
	image_1 = cv.cvtColor(image_1,cv.COLOR_BGR2RGB)
	tmp = mapping_table.loc[mapping_table['ori']==selected,'mapped']
	print(tmp)
	image_2 = cv.imread(heat_map_path+tmp.iloc[0])
	image_3 = cv.imread(heat_map_path+tmp.iloc[1])
	image_4 = cv.imread(heat_map_path+tmp.iloc[2])
	image_5 = cv.imread(heat_map_path+tmp.iloc[3])
	image_2 = cv.cvtColor(image_2,cv.COLOR_BGR2RGB)
	image_3 = cv.cvtColor(image_3,cv.COLOR_BGR2RGB)
	image_4 = cv.cvtColor(image_4,cv.COLOR_BGR2RGB)
	image_5 = cv.cvtColor(image_5,cv.COLOR_BGR2RGB)

	col1.header("Original image")
	col1.image(image_1, use_column_width=True)

	col2.header("Method A")
	col2.image(image_2, use_column_width=True)
	
	col3.header("Method B")
	col3.image(image_3, use_column_width=True)
	
	col4.header("Method C")
	col4.image(image_4, use_column_width=True)

	col5.header("Method D")
	col5.image(image_5, use_column_width=True)
	

	with agree2:	
		tmp2 = st.checkbox('Method A',value=False, key=session.run_id)

	with agree3:
		tmp3 = st.checkbox('Method B',value=False,key=session.run_id )

	with agree4:
		tmp4 = st.checkbox('Method C',value=False,key=session.run_id )

	with agree5:
		tmp5 = st.checkbox('Method D',value=False,key=session.run_id )

    	
	tmp6 = st.checkbox('None',value=False,key=session.run_id)
	submit = st.button('Submit your choice')
	if submit:
		if tmp2 or tmp3 or tmp4 or tmp5 or tmp6:
			st.write("Selected image is: "+str(selected))
			#st.write("The selected options are: " +str(calculation))
			selected_list = [tmp2,tmp3,tmp4,tmp5,tmp6]
			st.write("Selected  heatmaps: "+str(selected_list))
			
			csvRow = [selected,tmp2,tmp3,tmp4,tmp5,tmp6,datetime.datetime.now()]
			#Save selected options in CSV file
			csv_file = "./output/selected_options.csv"
			
			if os.path.exists(csv_file):
				with open(csv_file,'a',newline='') as f:
					st.write("CSV file exists. Appending data")
					csv_writer = csv.writer(f)
					csv_writer.writerow(csvRow)
			else:
				with open(csv_file,'w',newline='') as f:
					st.write("CSV file not found. Creating new file and writing data")
					csv_writer = csv.writer(f)
					header_list = ['selected_image','Method A','Method B','Method C','Method D','None','timestamp']
					csv_writer.writerow(header_list)
					csv_writer.writerow(csvRow)
			session.run_id += 1 #Reset the app (reset checkbox selections)
		else:
			st.warning('Please select atleast one heatmap')
	

else:
	st.warning('No option is selected')


