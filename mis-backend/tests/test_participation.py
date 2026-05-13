#test for participation
from app.models.participation import Participation

def test_create_participation(db_session):
    assert db_session is not None
    assert Participation is not None
    