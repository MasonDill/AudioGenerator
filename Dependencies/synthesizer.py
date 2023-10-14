import numpy as np
from Dependencies.score_composer import Note, Chord, Score
import soundfile as sf


def make_fundamental(score: Score, note: Note):
    """_summary_

    Args:
        score (Score): _description_
        note (Note): _description_
    """
    num_beats = note.note_length*int(score.time_sig[1])
    note_time = num_beats*60/score.tempo
    time = np.arange(0, note_time, 1/score.sample_rate)
    note.data_samples = np.array(
        (2**score.bit_depth)*np.sin(2*np.pi*note.fundamental_freq*time), dtype=np.int16)


def make_chord(chord: Chord):
    """_summary_

    Args:
        score (Score): _description_
        chord (Chord): _description_
    """
    data = 0
    for note in chord.chord_notes:
        data += note.data_samples
    chord.data_samples = data


def make_layer(score: Score, layer: list, samples_per_measure):
    """_summary_

    Args:
        score (Score): _description_
        staff (_type_): _description_
        samples_per_measure (_type_): _description_
        layer_num (_type_): _description_
    """
    # print(score.num_measures)
    data = np.zeros(samples_per_measure*score.num_measures, dtype=np.int16)
    curr_measure = 0
    start = 0

    for event in layer:
        num_samples = len(event.data_samples)
        if curr_measure != event.measure:
            curr_measure = event.measure
            start = (curr_measure-1)*samples_per_measure
            print("New measure " + str(curr_measure) + " " + str(event) +
                  " " + str(start))
            data[start:start+num_samples] = event.data_samples
        else:
            print("\tsame measure " + str(curr_measure) + " " + str(event) +
                  " " + str(start))
            data[start:start+num_samples] = event.data_samples

        start += num_samples-1
        # print("\t" + str(event) + str(len(event.data_samples)))

    return data


def write_audio_file(score: Score, data, temp=""):
    """_summary_

    Args:
        score (Score): _description_
        data (_type_): _description_
    """
    sf.write("./Output_Audio/"+score.title+".wav", data,
             score.sample_rate)
    return


def play_each_note(score: Score):
    """_summary_

    Args:
        score (Score): _description_
    """

    for staff in score.staves:
        for layer in staff.layers:
            for num, event in enumerate(layer):
                write_audio_file(score, event.data_samples, str(num))


def make_audio_file(score: Score):
    """_summary_

    Args:
        score (Score): _description_
    """

    samples_per_measure = int(
        (score.tempo/60.0)*score.sample_rate*int(score.time_sig[0]))
    print(samples_per_measure, score.num_measures)
    data = np.zeros(samples_per_measure*score.num_measures, dtype=np.int16)

    for staff in score.staves:
        for layer in staff.layers:
            start = (layer[0].measure-1)*samples_per_measure
            layer_data = make_layer(score, layer, samples_per_measure)
            data[start:start+len(layer_data)] = layer_data

    write_audio_file(score, data)
