The code is developed for Windows by using Python 3.7

├── requirements.txt   <- The requirements file for reproducing the analysis environment

├── README.md          <- The top-level README for developers using this project.

├── sample_images      <- It includes the sample original image and the corresponding different heat maps

├── output             <- The voting stats will be automatically saved as csv file here once trigger the dashboard file Voting_dashboard.py 

├── mapping_table.csv      <- Mapping original image to corresponding heat maps

├── SessionState.py    <- Dependency for Voting_dashboard.py

├── Voting_dashboard.py    <- Voting dashboard


### Installing development requirements by anaconda

1. A virtual environment named UI <env name> is created in conda prompt

    conda create -n UI python=3.7

2. The new virtual environment is activated

    conda activate UI

3. Install the python packages

    cd <installation_directory> 

    pip install -r requirements.txt

### Running the dashboard    

4. Voting for interpretation methods
    
   streamlit run Voting_dashboard.py
