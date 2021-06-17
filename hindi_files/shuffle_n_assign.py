import os
import pickle
import random


if __name__=='__main__':
    all_filenames = os.listdir('tmp_audio_dir')
    random.shuffle(all_filenames)

    final_assigned_names_with_filenames= {}
    for i, x in enumerate(all_filenames, start=1):
        final_assigned_names_with_filenames[i] = x

    with open('final_assigned_names_with_filenames_c.pickle', 'wb') as handle:
        pickle.dump(final_assigned_names_with_filenames, handle, protocol=pickle.HIGHEST_PROTOCOL)

    print(final_assigned_names_with_filenames)
    print(len(all_filenames))
    all_filenames = [x + '\n' for x in all_filenames]
    with open('temp_filenames.txt', 'w+') as f:
        f.writelines(all_filenames)



