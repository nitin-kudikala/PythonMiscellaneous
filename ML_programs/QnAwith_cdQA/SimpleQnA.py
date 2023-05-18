import os
import pandas as pd

from ast import literal_eval

from cdQA.cdqa.utils.filters import filter_paragraphs
from cdQA.cdqa.pipeline import QAPipeline



from cdQA.cdqa.utils.download import download_model, download_bnpp_data

#download_bnpp_data(dir='./data/bnpp_newsroom_v1.1/')
#download_model(model='bert-squad_1.1', dir='./models')

