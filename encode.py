
# coding: utf-8

import sys
import pandas as pd

preds = pd.read_csv('model_output/test_results.tsv', header=None, delimiter="\t")
sub = pd.read_csv('input/sample_submission.csv')

sub['prediction'] = preds[1]

print(sub.head())

sub.to_csv('output/sub.csv', index=False)

sys.exit(0)