from IPython.lib.pretty import pprint


class Quote:
    """
    its saved person name and words.

    Methods
    -------
    who()
        return human's name.
    says()
        return human's dialog.
    """

    def __init__(self, person, words):
        """

        Parameters
        ----------
        person : str
            human's name.
        words : str
            human's dialog.
        """
        self.person = person
        self.words = words

    def who(self):
        """

        Returns
        -------
        person : str
            human's name.
        """
        return self.person

    def says(self):
        """

        Returns
        -------
        words + '.' : str
            dialog add '.'.
        """
        return self.words + '.'


class QuestionQuote(Quote):
    def says(self):
        return self.words + '?'


class ExclamationQuote(Quote):
    def says(self):
        return self.words + '!'


class BabblingBrook():

    def who(self):
        return 'Brook'

    def says(self):
        return 'Babble'


brook = BabblingBrook()


def who_says(obj):
    print(obj.who(), 'dialogue', obj.says())


dialogue = 'says:'
hunter = Quote('Elmer Fudd', "I'm hunting wabbits")
print(hunter.who(), dialogue, hunter.says())

hunted1 = QuestionQuote('Bugs Bunny', 'Whats up, doc')
print(hunted1.who(), dialogue, hunted1.says())

hunted2 = ExclamationQuote('Daffy Duck', 'Its rabbit season')
print(hunted2.who(), dialogue, hunted2.says())

who_says(brook)
who_says(hunted1)
