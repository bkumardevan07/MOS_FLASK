#!/bin/bash

i=1
while read p;
do
	if [ $i -lt 21 ]
	then
		echo skipping $p
		#cp ../../Desktop/TTS-Hindi/fastspeech_prediction_june_2_115k/"$p"_prediction_fastspeech.wav ./tmp_audio_dir/
		#cp ../../Desktop/TTS-Hindi/wavernn_synthesized_test_audios/"$p"_wavernn_synthesized_target.wav ./tmp_audio_dir/
	elif [ $i -lt 31 ]
	then
		cp ../../Desktop/TTS-Hindi/fastspeech_prediction_june_2_115k/"$p"_prediction_fastspeech.wav ./tmp_audio_dir/
		cp ../../Desktop/TTS-Hindi/wavernn_synthesized_test_audios/"$p"_wavernn_synthesized_target.wav ./tmp_audio_dir/
		cp ../../Desktop/TTS-Hindi/test_audios/"$p".wav ./tmp_audio_dir/
	else
		exit
	fi	
	i=$(( i+1  ))
done <test_filenames_hindi.txt
