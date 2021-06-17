#!/bin/bash
i=1
while read p;
do
	cp tmp_audio_dir/$p ../static/audio_files_c/$i.wav
	i=$(( i+1 ))
	echo $i
done <temp_filenames.txt
