# bert-toxicity-classification
This repo show how to train bert model on [Jigsaw Unintended Bias in Toxicity Classification](https://www.kaggle.com/c/jigsaw-unintended-bias-in-toxicity-classification )  
**star me and i will keep update the code**

### LB Score 
1. 2019-04-06: 0.91216

### prepare
1. download the pretrain model
2. split the train and dev data(for convenience, i just tyde this command)
> cat train.csv | tail -n 1000 > dev_1000.csv

### train model
1. run run_classifier.py
```
python run_classifier.py \
  --data_dir=input/ --vocab_file=uncased_L-12_H-768_A-12/vocab.txt \
  --bert_config_file=uncased_L-12_H-768_A-12/bert_config.json \
  --init_checkpoint=uncased_L-12_H-768_A-12/bert_model.ckpt \
  --task_name=toxic \
  --do_train=True \
  --do_eval=True \
  --do_predict=True \
  --output_dir=model_output/
```

### To Do
1. text clean and OOV
2. CV
3. average different checkpoint prediction