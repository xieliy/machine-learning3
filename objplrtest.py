'''
test file of objplr.py
'''
from objplr import run
from objplrer import error_run
from numpy import array

#you need to change input_txt_file_url to your absolute directory below
training_url = r'C:\Users\xieliy\Desktop\master thesis\code\machine learning\machine-learning3\training data.txt'
run(training_url)

#test error rate using testing data set and computed classifier
testing_url = r'C:\Users\xieliy\Desktop\master thesis\code\machine learning\machine-learning3\testing data.txt'
classifier_url = r'C:\Users\xieliy\Desktop\master thesis\code\machine learning\machine-learning3\output classifier.txt'
error_run(testing_url, classifier_url)
