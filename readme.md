# Traffic Sign Classification CNN for 12 Ukrainian road sign classes

Includes:
1. Crosswalk (Right): 1967 entries;
2. No stopping: 812 entries;
3. Priority Road: 770 entries;
4. Give Way: 546 entries;
5. Children: 280 entries;
6. Crosswalk (left): 280 entries;
7. Do Not Enter: 224 entries;
8. Bus Stop: 203 entries;
9. No Trucks: 189 entries;
10. No Parking: 189 entries;
11. Stop: 175 entries;
12. Speed Limit (40 km/h): 175 entries.
* Total: 5810 entries *

To train machine run:
python train.py -d path_to_dataset -m model_output_name -p plot_output_name

To test machine run:
python predict.py -m model_name -i test_floder_path -e output_path
