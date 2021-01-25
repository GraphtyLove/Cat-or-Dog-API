docker build -t cat_or_dog .;
docker run  -v /ai_tainings_output/models:/model -v /ai_tainings_output/outputs:/output -it cat_or_dog;