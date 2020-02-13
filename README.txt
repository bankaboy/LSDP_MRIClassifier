Project : Classification of brain cancer images on BigDL

Members : Dhrubanka Dutta - 17BCE1019
		  Arnav Tripathy - 17BCE1026
		  Aman Shah - 17BCE1221
		  Shikhar Bharadwaj - 17BCE1250 
		  
Requirements : Hadoop 
			   PySpark - pip install pyspark
			   BigDL - pip install bigdl
			   Tensorflow - pip install tensorflow
			   OpenCV - pip install python-opencv
			   
Procedure :

1. Train classifier on different brain tumor images.
	a. Go to Image-Classification-Transfer-Learning.
	b. Open terminal and run "python retrain.py --image_dir classify_bain_tumor_dataset.
	c. After training is finished, go to /tmp folder of system.
	d. Transfer weights to desired folder.
	e. Change path of model in label_image_test.py to set location.
	f. Change image file path to test image location.
2. Convert dataset into binary files. (run dataset_binary.py) 
3. Load binary file datset into hdfs.
4. Open hdfs_classify_dataset.ipynb (jupyter notebook hdfs_classify_dataset.ipynb)
	a. Load tensorflow, pyspark, opencv, bigdl.
	b. Start the Spark engine.
	c. Load the classifier model into script using bigdl.
	d. Load the graph from the model.
	e. For each binary file in hdfs :
		i. Extract it using SparkContext.
		ii. Convert it back to image using OpenCV.
		iii. Pass the image to the graph.
		iv. Get the output of classifier.
		v. Write input image path and the prediction of classifier into csv file.
	
	
Note : Python3 is default on manjaro. Use python3 on other Operating Systems.
