cd /people/druc594/ML/
python3 -m debugpy --wait-for-client --listen 0.0.0.0:5678 -m DeepKS.models.individual_classifiers --train ../data/raw_data_31834_formatted_65_26610.csv --val ../data/raw_data_6500_formatted_95_5698.csv --test ../data/raw_data_6406_formatted_95_5616.csv --device cuda:4 -s