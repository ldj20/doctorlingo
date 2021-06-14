
import os
import tempfile
import shutil
import glob

import numpy as np
import pandas as pd



junkdir = './junk'
os.makedirs(junkdir, exist_ok=True)
testdir = "/home/karl/UMLS/UMLS_Metathesaurus_2021/2021AA/META"
print(testdir)


filelist = sorted(glob.glob(f'{testdir}/*'))
sizelist = [os.stat(filename).st_size for filename in filelist]
total_size = sum(sizelist)
print(f'generated {len(filelist)} files in {testdir}; total size = {total_size/1024**2:.1f}MB')


import boto3
import botocore
import boto3.s3.transfer as s3transfer


botocore_config = botocore.config.Config(max_pool_connections=20)
s3client = boto3.client('s3', config=botocore_config)

transfer_config = s3transfer.TransferConfig(
    use_threads=True,
    max_concurrency=20,
)



bucket_name = 'sagemaker-studio-757570088617-lvhv3fp3v5'
s3junkdir = 'junk'


import tqdm


%%time
progress = tqdm.tqdm(
    desc='upload',
    total=total_size, unit='B', unit_scale=1,
    position=0,
    bar_format='{desc:<10}{percentage:3.0f}%|{bar:10}{r_bar}')

s3t = s3transfer.create_transfer_manager(s3client, transfer_config)
for src in filelist:
    dst = os.path.join(s3junkdir, os.path.basename(src))
    s3t.upload(
        src, bucket_name, dst, subscribers=[s3transfer.ProgressCallbackInvoker(progress.update)])

s3t.shutdown()
progress.close();