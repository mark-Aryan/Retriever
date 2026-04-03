from flask import Flask, render_template, request, redirect, url_for, flash, jsonify, session
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import secure_filename
from PIL import Image
import sqlite3
import os
import uuid
from datetime import datetime
from functools import wraps

app = Flask(__name__)
app.secret_key = os.urandom(24).hex()
app.config['UPLOAD_FOLDER'] = 'static/uploads'
app.config['MAX_CONTENT_LENGTH'] = 10 * 1024 * 1024

login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message = 'Please login to reach out about this item.'

ALLOWED = {'png', 'jpg', 'jpeg', 'gif', 'webp'}

def allowed(fname):
    return '.' in fname and fname.rsplit('.', 1)[1].lower() in ALLOWED

def get_db():
    db = sqlite3.connect('lostfound.db')
    db.row_factory = sqlite3.Row
    db.execute("PRAGMA foreign_keys = ON")
    return db

def init_db():
    db = get_db()
    db.execute('''CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        email TEXT UNIQUE NOT NULL,
        roll TEXT UNIQUE NOT NULL,
        dept TEXT NOT NULL,
        year TEXT NOT NULL,
        phone TEXT NOT NULL,
        password TEXT NOT NULL,
        avatar TEXT DEFAULT NULL,
        created_at TEXT DEFAULT (datetime('now','localtime'))
    )''')
    db.execute('''CREATE TABLE IF NOT EXISTS items (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        uid TEXT UNIQUE NOT NULL,
        user_id INTEGER NOT NULL,
        title TEXT NOT NULL,
        category TEXT NOT NULL,
        location TEXT NOT NULL,
        description TEXT NOT NULL,
        image TEXT NOT NULL,
        status TEXT DEFAULT 'active',
        created_at TEXT DEFAULT (datetime('now','localtime')),
        FOREIGN KEY(user_id) REFERENCES users(id)
    )''')
    db.execute('''CREATE TABLE IF NOT EXISTS reachouts (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        item_id INTEGER NOT NULL,
        user_id INTEGER NOT NULL,
        description TEXT NOT NULL,
        status TEXT DEFAULT 'pending',
        created_at TEXT DEFAULT (datetime('now','localtime')),
        FOREIGN KEY(item_id) REFERENCES items(id),
        FOREIGN KEY(user_id) REFERENCES users(id)
    )''')
    db.commit()
    db.close()

class User(UserMixin):
    def __init__(self, row):
        self.id = row['id']
        self.name = row['name']
        self.email = row['email']
        self.roll = row['roll']
        self.dept = row['dept']
        self.year = row['year']
        self.phone = row['phone']
        self.avatar = row['avatar']

@login_manager.user_loader
def load_user(uid):
    db = get_db()
    row = db.execute('SELECT * FROM users WHERE id=?', (uid,)).fetchone()
    db.close()
    return User(row) if row else None

@app.route('/')
def index():
    db = get_db()
    q = request.args.get('q', '').strip()
    cat = request.args.get('cat', '')
    loc = request.args.get('loc', '')
    query = 'SELECT items.*, users.name as uname, users.roll as uroll, users.dept as udept, users.phone as uphone FROM items JOIN users ON items.user_id=users.id WHERE items.status="active"'
    params = []
    if q:
        query += ' AND (items.title LIKE ? OR items.description LIKE ?)'
        params += [f'%{q}%', f'%{q}%']
    if cat:
        query += ' AND items.category=?'
        params.append(cat)
    if loc:
        query += ' AND items.location LIKE ?'
        params.append(f'%{loc}%')
    query += ' ORDER BY items.created_at DESC'
    items = db.execute(query, params).fetchall()
    cats = db.execute('SELECT DISTINCT category FROM items WHERE status="active"').fetchall()
    db.close()
    return render_template('index.html', items=items, cats=cats, q=q, cat=cat, loc=loc)

@app.route('/item/<uid>')
def item_detail(uid):
    db = get_db()
    item = db.execute('SELECT items.*, users.name as uname, users.roll as uroll, users.dept as udept, users.phone as uphone, users.email as uemail FROM items JOIN users ON items.user_id=users.id WHERE items.uid=?', (uid,)).fetchone()
    if not item:
        db.close()
        flash('Item not found.')
        return redirect(url_for('index'))
    reachouts = db.execute('SELECT reachouts.*, users.name as rname, users.roll as rroll, users.dept as rdept FROM reachouts JOIN users ON reachouts.user_id=users.id WHERE reachouts.item_id=? ORDER BY reachouts.created_at DESC', (item['id'],)).fetchall()
    user_reached = False
    if current_user.is_authenticated:
        existing = db.execute('SELECT id FROM reachouts WHERE item_id=? AND user_id=?', (item['id'], current_user.id)).fetchone()
        user_reached = existing is not None
    db.close()
    return render_template('item.html', item=item, reachouts=reachouts, user_reached=user_reached)

@app.route('/upload', methods=['GET', 'POST'])
@login_required
def upload():
    if request.method == 'POST':
        title = request.form.get('title', '').strip()
        category = request.form.get('category', '').strip()
        location = request.form.get('location', '').strip()
        description = request.form.get('description', '').strip()
        f = request.files.get('image')
        if not all([title, category, location, description]):
            flash('All fields are required.')
            return redirect(url_for('upload'))
        if not f or not allowed(f.filename):
            flash('Please upload a valid image (jpg, png, gif, webp).')
            return redirect(url_for('upload'))
        ext = f.filename.rsplit('.', 1)[1].lower()
        fname = str(uuid.uuid4()) + '.' + ext
        fpath = os.path.join(app.config['UPLOAD_FOLDER'], fname)
        img = Image.open(f)
        img.thumbnail((1200, 1200))
        img.save(fpath, optimize=True, quality=85)
        uid = str(uuid.uuid4())[:8].upper()
        db = get_db()
        db.execute('INSERT INTO items (uid, user_id, title, category, location, description, image) VALUES (?,?,?,?,?,?,?)',
                   (uid, current_user.id, title, category, location, description, fname))
        db.commit()
        db.close()
        flash('Item posted successfully!')
        return redirect(url_for('item_detail', uid=uid))
    return render_template('upload.html')

@app.route('/reachout/<uid>', methods=['POST'])
@login_required
def reachout(uid):
    db = get_db()
    item = db.execute('SELECT * FROM items WHERE uid=?', (uid,)).fetchone()
    if not item:
        db.close()
        return jsonify({'ok': False, 'msg': 'Item not found'})
    if item['user_id'] == current_user.id:
        db.close()
        return jsonify({'ok': False, 'msg': 'You cannot reach out on your own post.'})
    existing = db.execute('SELECT id FROM reachouts WHERE item_id=? AND user_id=?', (item['id'], current_user.id)).fetchone()
    if existing:
        db.close()
        return jsonify({'ok': False, 'msg': 'You have already submitted a reach-out for this item.'})
    desc = request.form.get('description', '').strip()
    if len(desc) < 30:
        db.close()
        return jsonify({'ok': False, 'msg': 'Please write a more detailed description (min 30 characters).'})
    db.execute('INSERT INTO reachouts (item_id, user_id, description) VALUES (?,?,?)', (item['id'], current_user.id, desc))
    db.commit()
    db.close()
    return jsonify({'ok': True, 'msg': 'Reach-out submitted! The finder will see your request.'})

@app.route('/dashboard')
@login_required
def dashboard():
    db = get_db()
    my_items = db.execute('SELECT items.*, (SELECT COUNT(*) FROM reachouts WHERE item_id=items.id) as reach_count FROM items WHERE user_id=? ORDER BY created_at DESC', (current_user.id,)).fetchall()
    my_reachouts = db.execute('SELECT reachouts.*, items.title as ititle, items.uid as iuid, items.image as iimage FROM reachouts JOIN items ON reachouts.item_id=items.id WHERE reachouts.user_id=? ORDER BY reachouts.created_at DESC', (current_user.id,)).fetchall()
    db.close()
    return render_template('dashboard.html', my_items=my_items, my_reachouts=my_reachouts)

@app.route('/item/close/<uid>', methods=['POST'])
@login_required
def close_item(uid):
    db = get_db()
    item = db.execute('SELECT * FROM items WHERE uid=? AND user_id=?', (uid, current_user.id)).fetchone()
    if not item:
        db.close()
        return jsonify({'ok': False, 'msg': 'Not allowed'})
    db.execute('UPDATE items SET status="closed" WHERE uid=?', (uid,))
    db.commit()
    db.close()
    return jsonify({'ok': True})

@app.route('/item/delete/<uid>', methods=['POST'])
@login_required
def delete_item(uid):
    db = get_db()
    item = db.execute('SELECT * FROM items WHERE uid=? AND user_id=?', (uid, current_user.id)).fetchone()
    if not item:
        db.close()
        return jsonify({'ok': False, 'msg': 'Not allowed'})
    img_path = os.path.join(app.config['UPLOAD_FOLDER'], item['image'])
    if os.path.exists(img_path):
        os.remove(img_path)
    db.execute('DELETE FROM reachouts WHERE item_id=?', (item['id'],))
    db.execute('DELETE FROM items WHERE uid=?', (uid,))
    db.commit()
    db.close()
    return jsonify({'ok': True})

@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    if request.method == 'POST':
        name = request.form.get('name', '').strip()
        email = request.form.get('email', '').strip().lower()
        roll = request.form.get('roll', '').strip().upper()
        dept = request.form.get('dept', '').strip()
        year = request.form.get('year', '').strip()
        phone = request.form.get('phone', '').strip()
        pw = request.form.get('password', '')
        pw2 = request.form.get('confirm', '')
        if not all([name, email, roll, dept, year, phone, pw]):
            flash('All fields are required.')
            return redirect(url_for('register'))
        if pw != pw2:
            flash('Passwords do not match.')
            return redirect(url_for('register'))
        if len(pw) < 6:
            flash('Password must be at least 6 characters.')
            return redirect(url_for('register'))
        db = get_db()
        exists = db.execute('SELECT id FROM users WHERE email=? OR roll=?', (email, roll)).fetchone()
        if exists:
            db.close()
            flash('Email or Roll Number already registered.')
            return redirect(url_for('register'))
        hashed = generate_password_hash(pw)
        db.execute('INSERT INTO users (name, email, roll, dept, year, phone, password) VALUES (?,?,?,?,?,?,?)',
                   (name, email, roll, dept, year, phone, hashed))
        db.commit()
        row = db.execute('SELECT * FROM users WHERE email=?', (email,)).fetchone()
        db.close()
        login_user(User(row))
        flash(f'Welcome, {name}! Your account is ready.')
        return redirect(url_for('index'))
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    if request.method == 'POST':
        identifier = request.form.get('identifier', '').strip()
        pw = request.form.get('password', '')
        db = get_db()
        row = db.execute('SELECT * FROM users WHERE email=? OR roll=?', (identifier.lower(), identifier.upper())).fetchone()
        db.close()
        if row and check_password_hash(row['password'], pw):
            login_user(User(row), remember=True)
            nxt = request.args.get('next')
            return redirect(nxt or url_for('index'))
        flash('Invalid credentials. Please try again.')
    return render_template('login.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Logged out successfully.')
    return redirect(url_for('index'))

@app.route('/api/stats')
def stats():
    db = get_db()
    total = db.execute('SELECT COUNT(*) FROM items WHERE status="active"').fetchone()[0]
    closed = db.execute('SELECT COUNT(*) FROM items WHERE status="closed"').fetchone()[0]
    users = db.execute('SELECT COUNT(*) FROM users').fetchone()[0]
    reachouts = db.execute('SELECT COUNT(*) FROM reachouts').fetchone()[0]
    db.close()
    return jsonify({'active': total, 'closed': closed, 'users': users, 'reachouts': reachouts})

if __name__ == '__main__':
    os.makedirs('static/uploads', exist_ok=True)
    init_db()
    app.run(debug=True, host='0.0.0.0', port=5000)
