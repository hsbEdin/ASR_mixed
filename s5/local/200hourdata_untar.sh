#!/usr/bin/env bash

# Copyright   2014  Johns Hopkins University (author: Daniel Povey)
#             2019  Xingyu Na
# Apache 2.0

remove_archive=false

if [ "$1" == --remove-archive ]; then
  remove_archive=true
  shift
fi

if [ $# -ne 2 ]; then
  echo "Usage: $0 [--remove-archive] <data-base> <url-base> <corpus-part>"
  #echo "e.g.: $0 /export/a05/xna/data www.openslr.org/resources/68 train_set"
  echo "With --remove-archive it will remove the archive after successfully un-tarring it."
  echo "<corpus-part> can be one of: train_set, dev_set, test_set."
fi

data=$1

#$2=dev
part=$2

#删掉了$3

part1=`echo $part | sed s/_set//`

if [ ! -d "$data" ]; then
  echo "$0: no such directory $data, make it."
  mkdir -p $data
fi

if [ ! -d "$data/$part1" ]; then
  echo "$0: no such directory $data/$part1, make it."
  mkdir -p $data/$part1
  #mkdir -p 创建多级目录
fi

if [ ! -f "$data/$part1/TRANS.txt" ]; then
  echo "$0: Missing the corpus and audio files of $part1 set!"
  exit 1;
  #mkdir -p 创建多级目录
fi

part_ok=false
list="train_set dev_set"
for x in $list; do
  if [ "$part" == $x ]; then part_ok=true; fi
done
if ! $part_ok; then
  echo "$0: expected <corpus-part> to be one of $list, but got '$part'"
  exit 1;
fi


if [ -f $data/$part1/.complete ]; then
  echo "$0: data part $part was already successfully extracted, nothing to do."
  exit 0;
fi

cd $data

# if ! tar -xvzf $part.tar.gz; then
#   echo "$0: error un-tarring archive $data/$part.tar.gz"
#   exit 1;
# fi

touch $data/$part1/.complete

train_dir=$data/$part/corpus/train
dev_dir=$data/$part/corpus/dev
#test_dir=$data/$part/corpus/test
if [ $part == "aidatatang_200zh" ]; then
  for set in $dev_dir $train_dir;do
    cd $set
    for wav in ./*.tar.gz; do
      echo "Extracting wav from $wav"
      tar -zxf $wav && rm $wav
    done
  done
fi

echo "$0: Successfully un-tarred $data/$part.tar.gz"

if $remove_archive; then
  echo "$0: removing $data/$part.tar.gz file since --remove-archive option was supplied."
  rm $data/$part.tar.gz
fi

exit 0;
