# acled_dash
Download ACLED data via API and provide summary statistics through dash app.

# Set-up
1) Clone repository: 'git clone https://github.com/adrianochs/acled_dash.git'
2) cd into repository
3) 'conda env create -f environment.yml'


# Download ACLED data
1) Activate environment: 'conda activate acled'
2) cd into repository
3) 'python3 data_loader.py'
4) Data can be found in folder 'data'

# Run Dash App
1) Activate environment: 'conda activate acled'
2) cd into repository
3) 'python3 app.py'
4) Copy past the link into browser of choice