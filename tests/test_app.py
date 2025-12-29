import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest
from app import app, db
from models import Task

@pytest.fixture
def client():
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    
    with app.test_client() as client:
        with app.app_context():
            db.create_all()
        yield client
        with app.app_context():
            db.drop_all()

def test_home_page(client):
    """Test that home page loads"""
    response = client.get('/')
    assert response.status_code == 200
    assert b'Task Manager' in response.data

def test_add_task_page(client):
    """Test that add task page loads"""
    response = client.get('/add')
    assert response.status_code == 200
    assert b'Add New Task' in response.data

def test_add_task(client):
    """Test adding a new task"""
    response = client.post('/add', data={
        'title': 'Test Task',
        'description': 'Test Description'
    }, follow_redirects=True)
    assert response.status_code == 200
    assert b'Test Task' in response.data

def test_add_task_without_title(client):
    """Test that task without title fails"""
    response = client.post('/add', data={
        'title': '',
        'description': 'Test Description'
    }, follow_redirects=True)
    assert response.status_code == 200
    assert b'Title is required' in response.data

def test_toggle_task(client):
    """Test toggling task completion"""
    # First add a task
    with app.app_context():
        task = Task(title='Toggle Test', description='Test')
        db.session.add(task)
        db.session.commit()
        task_id = task.id
    
    # Toggle it
    response = client.get(f'/toggle/{task_id}', follow_redirects=True)
    assert response.status_code == 200

def test_delete_task(client):
    """Test deleting a task"""
    # First add a task
    with app.app_context():
        task = Task(title='Delete Test', description='Test')
        db.session.add(task)
        db.session.commit()
        task_id = task.id
    
    # Delete it
    response = client.get(f'/delete/{task_id}', follow_redirects=True)
    assert response.status_code == 200
    assert b'Task deleted successfully' in response.data
