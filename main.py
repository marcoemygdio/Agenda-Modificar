from flask import Flask, render_template, request, redirect
app = Flask('app')
contacts = []

@app.route('/')
def index():
  return render_template('index.html', contacts = contacts)

@app.route('/create', methods=['POST'])
def create():
  name = request.form.get('name')
  email = request.form.get('email')
  phone = request.form.get('phone')
  contacts.append({'name': name, 'email': email, 'phone': phone})
  return redirect('/')

@app.route('/update/<int:id>', methods=['POST'])
def update(id):
  name = request.form.get('name')
  email = request.form.get('email')
  phone = request.form.get('phone')
  contacts[id]['name'] = name
  contacts[id]['email'] = email
  contacts[id]['phone'] = phone
  return redirect('/')

@app.route('/delete/<int:id>')
def delete(id):
  contacts.pop(id)
  return redirect('/')


  
if __name__ == '__main__':
  app.run(host='0.0.0.0', port=8080)