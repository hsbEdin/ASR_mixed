#!/usr/bin/env bash

# Copyright 2019 Xingyu Na
# Apache 2.0

. ./path.sh || exit 1;

if [ $# != 2 ]; then
  echo "Usage: $0 <corpus-path> <data-path>"
  echo " $0 /export/a05/xna/data/magicdata data/magicdata"
  exit 1;
fi
#200小时词库
corpus=$1
#200小时语音 data=data/200hour
data=$2

if [ ! -d $corpus/train ] || [ ! -d $corpus/dev ] ; then
  echo "Error: $0 requires complete corpus"
  exit 1;
fi

echo "**** Creating 200hourdata data folder ****"
if [ ! -d "$data/train" ] || [ ! -d "$data/dev" ] || [ ! -d "$data/tmp" ]; then
  echo "$0: no such directory 'train' or 'dev' or 'tmp' in $data, make it."
  mkdir -p $data/{train,dev,tmp}
  #mkdir -p 创建多级目录
fi

# find wav audio file for train, dev and test resp.
tmp_dir=$data/tmp
find $corpus -iname "*.wav" > $tmp_dir/wav.flist
n=`cat $tmp_dir/wav.flist | wc -l`
#[ $n -ne 609552 ] && \
echo Notice: Found $n data files

for x in train dev; do
  grep -i "/$x/" $tmp_dir/wav.flist > $data/$x/wav.flist || exit 1;
  echo "Filtering data using found wav list and provided transcript for $x"
  local/filter_data.py $data/$x/wav.flist $corpus/$x/TRANS.txt $data/$x
  cat $data/$x/transcripts.txt |\
    local/jieba_segment.py |\
    tr '[a-z]' '[A-Z]' |\
    #sed 's/FIL/[FIL]/g' | sed 's/SPK/[SPK]/' |\
    awk '{if (NF > 1) print $0;}' > $data/$x/text
  for file in wav.scp utt2spk text; do
    sort $data/$x/$file -o $data/$x/$file
  done
  utils/utt2spk_to_spk2utt.pl $data/$x/utt2spk > $data/$x/spk2utt
done

rm -r $tmp_dir

utils/data/validate_data_dir.sh --no-feats $data/train || exit 1;
utils/data/validate_data_dir.sh --no-feats $data/dev || exit 1;

echo "$0: 200hour data preparation succeeded"
exit 0;
