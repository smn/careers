import unittest
from datetime import date, timedelta

"""

JOB OPENING
===========

This is a runnable job description for a position as a software engineer
at Praekelt Digital / Praekelt Foundation.

Run the code, if you understand it and you pass, there's a good chance
we should get in touch.

Good luck!

Praekelt

"""


class FoundationEngineerTestCase(unittest.TestCase):
    """
    If you pass for this test then we're probably looking for you.
    """
    
    def test_experience(self):
        "10 years software development experience."
        assert candidate.results['started_programming'] <= years_ago(10)
    
    def test_python_experience(self):
        "5 years Python experience."
        assert candidate.results['started_python_programming'] <= years_ago(5)
    
    def test_django_experience(self):
        "Rock solid Django experience with highly scalable architecture including server farms and cloud / elastic computing."
        assert candidate.results['django_experience'] >= 6
    
    def test_cloud_experience(self):
        "The word cloud should make you think of computing"
        assert candidate.results['clouds_are_for_rain'] == 'no'
    
    def test_git_experience(self):
        "The word fork should make you think of code and collaboration"
        assert candidate.results['forks_are_for_food'] == 'no'
    
    def test_tdd(self):
        "You should have an appreciation of tests"
        assert candidate.results['appreciates_tests'] == 'yes'
    
    def test_linux(self):
        "You should have experience with Linux"
        assert candidate.results['penguins'] == 'yes'
    
    def test_database(self):
        "You should have experience with OS databases"
        assert candidate.results['databases'] == 'yes'
    
    def test_independent(self):
        "You should be happy to work in an unstructured and not strictly supervised environment."
        assert True # bonus
    
    def test_java_rails_experience(self):
        "Experience with Java / Ruby and Rails is a bonus"
        assert True # bonus
    
    def test_programming_language(self):
        """You shouldn't be bound to a single platform / language"""
        assert True # bonus
    


def prompt(question):
    return raw_input("%s : " % question).strip()

def years_ago(number):
    return date.today() - timedelta(days = number * 365)

class Candidate(object):

    def __init__(self):
        self.results = {}

    def interview(self):
        for attribute in dir(self):
            if attribute.startswith("ask"):
                _, attribute_name = attribute.split("_", 1)
                attribute_function = getattr(self, attribute)
                self.results[attribute_name] = attribute_function()

    def ask_started_programming(self):
        year = prompt("In what year did you start programming? (1980, 1985 etc...)")
        return date(year=int(year), month=1, day=1)

    def ask_started_python_programming(self):
        year = prompt("In what year did you start programming in Python? (1980, 1985 etc...)")
        return date(year=int(year), month=1, day=1)

    def ask_django_experience(self):
        experience = prompt("If on a scale of 1 to 10, 1 equals zero " \
                            "experience and 10 equals very experienced " \
                            "where would you place yourself with regard to " \
                            "Django development?")
        return int(experience)

    def ask_clouds_are_for_rain(self):
        return prompt("Do clouds remind you of rain? (yes or no)")

    def ask_forks_are_for_food(self):
        return prompt("Does the word 'Fork' make you think of eating? (yes or no)")

    def ask_appreciates_tests(self):
        return prompt("Do you like tests? (yes or no)")

    def ask_penguins(self):
        return prompt("Are penguins even remotely related to operating systems? (yes or no)")

    def ask_databases(self):
        return prompt("The following words \"Post Ogres Queue Elle\" are related (yes or no)")

    def ask_independent(self):
        return prompt("Do you enjoy working independently?")



class CandidateTestProgram(unittest.TestProgram):
    def runTests(self):
        self.result = unittest.TextTestRunner().run(self.test)

if __name__ == '__main__':
    candidate = Candidate()
    candidate.interview()
    
    test_program = CandidateTestProgram()
    print "\n\n"
    if not test_program.result.wasSuccessful():
        print "Sorry you didn't pass"
    else:
        print "Hooray, you passed! Now what?"
        print "1. Email your CV to careers+dev@praekelt.com"
        print "2. Fork out this code, suggest improvements and submit those"
        print ""
        print "If we think you're a possible candidate then we'll be in touch."
        print ""
        print "Thanks! Praekelt"
        
