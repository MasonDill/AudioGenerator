class Note:
    """
    Lowest level structure that can be added to a Score (object)
    """

    pitches = {
        "rest": 0,
        "mRest": 0,
        "C0": 16.35,
        "C#0": 17.32,
        "Db0": 17.32,
        "D0": 18.35,
        "D#0": 19.44,
        "Eb0": 19.44,
        "E0": 20.6,
        "E#0": 20.6,
        "Fb0": 21.82,
        "F0": 21.82,
        "F#0": 23.12,
        "Gb0": 23.12,
        "G0": 24.5,
        "G#0": 25.95,
        "Ab0": 25.95,
        "A0": 27.5,
        "A#0": 29.13,
        "Bb0": 29.13,
        "B0": 30.86,
        "B#0": 32.7,
        "Cb0": 30.86,
        "C1": 32.7,
        "C#1": 34.64,
        "Db1": 34.64,
        "D1": 36.7,
        "D#1": 38.88,
        "Eb1": 38.88,
        "E1": 41.2,
        "E#1": 41.2,
        "Fb1": 43.64,
        "F1": 43.64,
        "F#1": 46.24,
        "Gb1": 46.24,
        "G1": 49.0,
        "G#1": 51.9,
        "Ab1": 51.9,
        "A1": 55.0,
        "A#1": 58.26,
        "Bb1": 58.26,
        "B1": 61.72,
        "B#1": 65.4,
        "Cb1": 61.72,
        "C2": 65.4,
        "C#2": 69.28,
        "Db2": 69.28,
        "D2": 73.4,
        "D#2": 77.76,
        "Eb2": 77.76,
        "E2": 82.4,
        "E#2": 82.4,
        "Fb2": 87.28,
        "F2": 87.28,
        "F#2": 92.48,
        "Gb2": 92.48,
        "G2": 98.0,
        "G#2": 103.8,
        "Ab2": 103.8,
        "A2": 110.0,
        "A#2": 116.52,
        "Bb2": 116.52,
        "B2": 123.44,
        "B#2": 130.8,
        "Cb2": 123.44,
        "C3": 130.8,
        "C#3": 138.56,
        "Db3": 138.56,
        "D3": 146.8,
        "D#3": 155.52,
        "Eb3": 155.52,
        "E3": 164.8,
        "E#3": 164.8,
        "Fb3": 174.56,
        "F3": 174.56,
        "F#3": 184.96,
        "Gb3": 184.96,
        "G3": 196.0,
        "G#3": 207.6,
        "Ab3": 207.6,
        "A3": 220.0,
        "A#3": 233.04,
        "Bb3": 233.04,
        "B3": 246.88,
        "B#3": 261.6,
        "Cb3": 246.88,
        "C4": 261.6,
        "C#4": 277.12,
        "Db4": 277.12,
        "D4": 293.6,
        "D#4": 311.04,
        "Eb4": 311.04,
        "E4": 329.6,
        "E#4": 329.6,
        "Fb4": 349.12,
        "F4": 349.12,
        "F#4": 369.92,
        "Gb4": 369.92,
        "G4": 392.0,
        "G#4": 415.2,
        "Ab4": 415.2,
        "A4": 440.0,
        "A#4": 466.08,
        "Bb4": 466.08,
        "B4": 493.76,
        "B#4": 523.2,
        "Cb4": 493.76,
        "C5": 523.2,
        "C#5": 554.24,
        "Db5": 554.24,
        "D5": 587.2,
        "D#5": 622.08,
        "Eb5": 622.08,
        "E5": 659.2,
        "E#5": 659.2,
        "Fb5": 698.24,
        "F5": 698.24,
        "F#5": 739.84,
        "Gb5": 739.84,
        "G5": 784.0,
        "G#5": 830.4,
        "Ab5": 830.4,
        "A5": 880.0,
        "A#5": 932.16,
        "Bb5": 932.16,
        "B5": 987.52,
        "B#5": 1046.4,
        "Cb5": 987.52,
        "C6": 1046.4,
        "C#6": 1108.48,
        "Db6": 1108.48,
        "D6": 1174.4,
        "D#6": 1244.16,
        "Eb6": 1244.16,
        "E6": 1318.4,
        "E#6": 1318.4,
        "Fb6": 1396.48,
        "F6": 1396.48,
        "F#6": 1479.68,
        "Gb6": 1479.68,
        "G6": 1568.0,
        "G#6": 1660.8,
        "Ab6": 1660.8,
        "A6": 1760.0,
        "A#6": 1864.32,
        "Bb6": 1864.32,
        "B6": 1975.04,
        "B#6": 2092.8,
        "Cb6": 1975.04,
        "C7": 2092.8,
        "C#7": 2216.96,
        "Db7": 2216.96,
        "D7": 2348.8,
        "D#7": 2488.32,
        "Eb7": 2488.32,
        "E7": 2636.8,
        "E#7": 2636.8,
        "Fb7": 2792.96,
        "F7": 2792.96,
        "F#7": 2959.36,
        "Gb7": 2959.36,
        "G7": 3136.0,
        "G#7": 3321.6,
        "Ab7": 3321.6,
        "A7": 3520.0,
        "A#7": 3728.64,
        "Bb7": 3728.64,
        "B7": 3950.08,
        "B#7": 4185.6,
        "Cb7": 3950.08,
        "C8": 4185.6,
        "C#8": 4433.92,
        "Db8": 4433.92,
        "D8": 4697.6,
        "D#8": 4976.64,
        "Eb8": 4976.64,
        "E8": 5273.6,
        "E#8": 5273.6,
        "Fb8": 5585.92,
        "F8": 5585.92,
        "F#8": 5918.72,
        "Gb8": 5918.72,
        "G8": 6272.0,
        "G#8": 6643.2,
        "Ab8": 6643.2,
        "A8": 7040.0,
        "A#8": 7457.28,
        "Bb8": 7457.28,
        "B8": 7900.16,
        "B#8": 8371.2,
        "Cb8": 7900.16,
    }

    def __init__(self, pitch_name="A4", num_beats=1/8):
        """
        Creates a Note (object), the lowest level structure of a Score (object)

        Args:
            pitch_name (str, optional): Letter name of note and the number octave. Defaults to "A4".
            num_beats (float, optional): The number of beats the note gets. Defaults to 1/8.
        """
        self.set_note_freq(pitch_name)
        self.set_note_length(num_beats)
        self.set_data_samples([])
        self.measure = 0

    def set_note_freq(self, name: str):
        """
        Takes a note name (str) and gets the  fundamental frequency (float) in Hertz

        Args:
            name (str): letter of the note name and the octave

        Example:
            Note name: A4
            Fundamental frequency: 440.0
        """
        self.fundamental_freq = Note.pitches[name]
        self.note_name = name

    def set_note_length(self, length: float):
        """
        Takes the note division (float) assigned to the note 

        Args:
            length (float): number of beats the note gets
        """
        self.length = 1/length

    def set_data_samples(self, data):
        """
        Fills the data array with the synthesized sample data

        Args:
            data (array-like): data samples
        """
        self.data_samples = data

    def set_measure(self, measure: int):
        """
        Sets what measure the Note (object) is assigned from

        Args:
            measure (int): the measure # of the piece. Starts at 1 
        """
        self.measure = measure

    def __str__(self) -> str:
        return "M:" + str(self.measure) + " " + self.note_name + " {" + str(self.length) + "}[" + str(self.fundamental_freq)+"Hz]"


class Chord:
    """
    A group of Note (objects) that are to be played simultaneously
    """

    def __init__(self) -> None:
        """
        Creates Chord (object)
        """
        self.chord_notes = []
        self.data_samples = []
        self.measure = 0
        self.length = 0

    def __str__(self) -> str:
        all_notes = []
        duration = ""
        for note in self.chord_notes:
            string = note.note_name + "[" + str(note.fundamental_freq) + "]"
            all_notes.append(string)
            duration = note.length

        return "M:" + str(self.measure) + " Chord(" + " ".join(all_notes) + ")" + "<1/" + str(duration) + ">"

    def add_note_to_chord(self, note: Note):
        """
        Takes a Note (object) and adds to the Chord (object) called from

        Args:
            note (Note): the Note (object) to be added to Chord (object)
        """

        self.chord_notes.append(note)

    def set_measure(self, measure):
        """
        Sets what measure the Chord (object) is assigned from

        Args:
            measure (int): the measure # of the piece. Starts at 1 
        """
        for note in self.chord_notes:
            note.set_measure(measure)
        self.measure = measure


class Staff:
    """
    Middle level structure which holds Notes (object) and Chords (object)
    """

    def __init__(self) -> None:
        self.layers = [[]]
        self.sample_data = []

    def add_layer_to_staff(self):
        """
        Adds an empty list to the called Staff (object) array of piece layers
        """
        self.layers.append([])

    def add_event_to_layer(self, event, layer_num=0, measure=0):
        """
        Adds either Note (object) or Chord (object) as the next sequential event in the specified layer

        Args:
            event (Note) or (Chord): the Note (object) or Chord (object) to be added to the layer
            layer_num (int, optional): the desired layer to be added to. Defaults to 0.
            measure (int, optional): the measure # of the piece. Starts at 1. Defaults to 0.
        """
        curr_layer = self.layers[layer_num]
        event.set_measure(measure)
        curr_layer.append(event)

    def __str__(self) -> str:
        all_layers = []

        for layer in self.layers:
            layer_notes = []
            for note in layer:
                layer_notes.append(str(note))
            all_layers.append(str(layer_notes))

        string = ""
        for num, layer in enumerate(all_layers):
            string += "\n\n\tLayer " + str(num) + "\n"
            string += "\t\t" + layer

        return string


class Score:
    """
    Highest level structure of a music piece
    """

    _sharp_order = ["F", "C", "G", "D", "A", "E", "B"]
    _flat_order = ["B", "E", "A", "D", "G", "C", "F"]

    _major_sharp_key_order = ["G", "D", "A", "E", "B", "F#", "C#"]
    _major_flat_key_order = ["F", "Bb", "Eb", "Ab", "Db", "Gb", "Cb"]

    _minor_sharp_key_order = ["Em", "Bm", "F#m", "C#m", "G#m", "D#m", "A#m"]
    _minor_flat_key_order = ["Dm", "Gm", "Cm", "Fm", "Bbm", "Ebm", "Abm"]

    sample_rate = 0
    bit_depth = 0
    score_num = 0

    def __init__(self) -> None:
        """_summary_
        """
        Score.score_num += 1
        self.set_title()
        self.set_composer()
        self.staves: list[Staff] = []
        self.data_samples = []
        self.set_key()
        self.set_time_sig()
        self.set_tempo()
        self.num_measures = 0
        self.samples_per_beat = int(Score.sample_rate*60/self.tempo)
        self.samples_per_measure = int(
            self.samples_per_beat*int(self.time_sig[0]))

    def __str__(self) -> str:
        string = ""
        string += self.get_score_info() + "\n\n"
        string += self.get_notes()

        return string

    def set_title(self, title="default"):
        """
        Sets the title of Score (object)

        Args:
            title (str, optional): the title name to be used. Defaults to "default".
        """
        self.title = title

    def set_composer(self, name="default"):
        """
        Sets the composer of Score (object)

        Args:
            composer (str, optional): the composer name to be used. Defaults to "default".
        """
        self.composer = name

    def set_key(self, key="C"):
        """
        Sets the key of the Score (object) and the accidentals in that key

        Args:
            key (str, optional): key name. Defaults to "C"

        Examples:
            key = "C" -> key accidentals = []\n
            key = "D" -> key accidentals = [F C]
        """
        if key == "C":
            self.key_accidentals = []
        elif "m" in key:
            if "b" in key or key in ["Dm", "Gm", "Cm", "Fm"]:
                num_flats = Score._minor_flat_key_order.index(key)
                self.key_accidentals = Score._flat_order[:num_flats+1]
            elif "#" in key or key in ["Em", "Bm"]:
                num_sharps = Score._minor_sharp_key_order.index(key)
                self.key_accidentals = Score._sharp_order[:num_sharps+1]
        else:
            if "b" in key or key == "F":
                num_flats = Score._major_flat_key_order.index(key)
                self.key_accidentals = Score._flat_order[:num_flats+1]
            elif "#" in key or key in ["G", "D", "A", "E"]:
                num_sharps = Score._major_sharp_key_order.index(key)
                self.key_accidentals = Score._sharp_order[:num_sharps+1]

        self.key = key

    def set_time_sig(self, beats_per_measure="4", beats_per_note="4"):
        """
        Sets the time signature of the Score (object)

        Args:
            beats_per_measure (str, optional): the number of beats in a measure. Defaults to "4".
            beats_per_note (str, optional): the denominator of the size of note given a single beat.
                Typically a quarter note is given one beat. Defaults to "4".

        """
        self.time_sig = [beats_per_measure, beats_per_note]

    def set_tempo(self, tempo=60.0):
        """
        Sets the tempo of the Score (object)

        Args:
            tempo (float, optional): number of beats per minute. Defaults to 60.0
        """
        if isinstance(tempo, float):
            self.tempo = tempo

    def get_work_info(self):
        """
        Gets the title and composer of the Score (object)

        Returns:
            str: Score (object) information in the form:
                "title" by "composer"
        """
        return str(self.title + " by " + self.composer)

    def get_key(self):
        """_summary_

        Returns:
            _type_: _description_
        """
        string = self.key + " ["
        if len(self.key_accidentals) > 0 and self.key_accidentals[0] == "F":
            string += "Sharps: "
        elif len(self.key_accidentals) > 0 and self.key_accidentals[0] == "B":
            string += "Flats: "

        return string + ", ".join(self.key_accidentals) + "]"

    def get_time_signature(self):
        """_summary_

        Returns:
            _type_: _description_
        """
        return "Time Signature: " + "/".join(self.time_sig)

    def get_score_info(self):
        """_summary_

        Returns:
            _type_: _description_
        """
        info = Score.get_work_info(
            self) + "\n" + Score.get_key(self) + " " + Score.get_time_signature(self)
        return info

    def get_notes(self):
        """_summary_

        Args:
            staff_num (_type_): _description_

        Returns:
            _type_: _description_
        """
        staff_info = ""
        for num, staff in enumerate(self.staves):
            staff_info += "\n\nStaff " + str(num) + str(staff)

        return staff_info

    def get_staff(self, staff_num: int):
        """_summary_

        Args:
            staff_num (int): _description_

        Returns:
            _type_: _description_
        """
        return self.staves[staff_num]

    def add_staff_to_score(self):
        """_summary_
        """
        new_staff = Staff()
        self.staves.append(new_staff)
