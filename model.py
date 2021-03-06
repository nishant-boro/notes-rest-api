from settings import *
import json
import datetime

db = SQLAlchemy(app)

class Note(db.Model):
    __tablename__ = 'notes'
    id = db.Column(db.Integer, primary_key=True)
    note = db.Column(db.Text, nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.datetime.utcnow)

    def json(self):
        return {'id': self.id, 'note': self.note,
                'timestamp': self.timestamp}

    def add_note(_note):
        new_note = Note(note=_note)
        db.session.add(new_note)
        db.session.commit()

    def get_all_notes():
        return [Note.json(note) for note in Note.query.all()]

    def get_note(_id):
        return [Note.json(Note.query.filter_by(id=_id).first())]

    def update_note(_id, _note):
        note_to_update = Note.query.filter_by(id=_id).first()
        note_to_update.note = _note
        db.session.commit()

    def delete_note(_id):
        Note.query.filter_by(id=_id).delete()
        db.session.commit()