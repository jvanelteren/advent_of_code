## Kamermoties
Project to predict someone's age from their face. Published at [blog](https://jvanelteren.github.io/blog/2020/11/24/face2age.html)

### Usage
First extract the [the dataset](https://www.kaggle.com/frabbisw/facial-age) to a `data` directory. After that, play around with training a neural net with 2020-11-24-age_pure_pytorch.ipynb
I did make the model into an app:
* db --> database to store predictions from model and humans
* html --> html page + js code to communicate with backend
* models --> traing pytorch model and pickled predictions

### Thanks
Thanks to Fazle Rabbi for making [the dataset available](https://www.kaggle.com/frabbisw/facial-age) at Kaggle.

### License
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
You can use this under the MIT license