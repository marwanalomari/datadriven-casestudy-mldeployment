# rd-technical-test
This repo builds on concepts of any data driven machine learning project, which include training, serving and exposing a model learning model in Docker. The repo consists of two parts.

The first part: the program will first import the data (not included because it is private), doing some clean up and data preparation. Then, the text data will be represented numerically and split into training and testing sets. The results of logistic regression model will be assessed on F1 score and precision and recall. At the end, the model is saved (pickled) for later use in micro service.

- For performing the first part of the program:
  Perform:
  - make train (a command on your terminal)

The second part: Deploying the model using flask api in Docker
- For performing the second part of the program:
  Perform:
  - make api (a command on your terminal)

Warning: the program uses private dataset, so it is avaliable upon request, please contact: research@posos.fr
