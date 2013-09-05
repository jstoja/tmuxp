from tmux import t, Session
from . import TestTmux, TEST_SESSION_PREFIX
from random import randint


class TestSessions(TestTmux):
    def test_has_session(self):
        self.assertTrue(t.has_session(self.TEST_SESSION_NAME))
        self.assertFalse(t.has_session('asdf2314324321'))

    def test_new_session(self):
        new_session_name = TEST_SESSION_PREFIX + str(randint(0, 1337))
        new_session = Session.new_session(session_name=new_session_name)

        self.assertIsInstance(new_session, Session)