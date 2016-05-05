from flask import Flask, jsonify, render_template, request
import datetime
import zapis
app = Flask(__name__)

@app.template_filter()
def datetimefilter(value, format='%Y/%m/%d %H:%M'):
    """convert a datetime to a different format."""
    return value.strftime(format)
id = 0
app.jinja_env.filters['datetimefilter'] = datetimefilter
list = zapis.readfile()
@app.route("/")

def template_test():
    num = 0
    return render_template('template.html', num = num,
        my_list=list, title="Index", current_time=datetime.datetime.now())

@app.route('/', methods = ['POST'])
def contact():
        if request.form['submit'] == 'Add':
            return '''
                <form method='POST'>

                    <p><strong>Как вас зовут?</strong></p>
                    <p><input name='name' maxlength="25" type="text" size="40" value="Вася"></p>

                    <p><strong>Кто вас обидел?</strong></p>
                    <p><input name='comp' maxlength="25" type="text" size="40" value="Евросеть"></p>

                    <p><strong>Чем вас обидел?</strong></p>
                    <p><input name='tema' maxlength="25" type="text" size="40" value="Телефон отжали"></p>

                    <p><b>Оставте коментарий</b></p>
                    <p><textarea name="comment" type="text">Я очень зол!!!!!!</textarea></p>

                    <input type="submit" name="submit" value="Ok">
                    <input type="submit" name="submit" value="Close">

                </form>
            '''
        if request.form['submit'] == 'Ok':
            text = [request.form['name'], request.form['comp'], request.form['tema'], request.form['comment']]
            list.append(text)
            zapis.writefile(list)
            return template_test()
        if request.form['submit'] == 'Delete':
            global id
            id = int(request.form['index'])
            list.pop(id - 1)
            return template_test()
        if request.form['submit'] == 'Refactor':
            global id
            id = int(request.form['index'])
            form = ""
            form += "<form method='POST'>"
            form += "<p><strong>Как вас зовут?</strong></p>"
            form += "<p><input name='name' maxlength='35' type='text' size='40' value=" + list[id-1][0] + "></p>"

            form += "<p><strong>Кто вас обидел?</strong></p>"
            form += "<p><input name='comp' maxlength='35' type='text' size='40' value=" + list[id-1][1] + "></p>"

            form += "<p><strong>Чем вас обидел?</strong></p>"
            form += "<p><input name='tema' maxlength='35' type='text' size='40' value=" + list[id-1][2] + "></p>"

            form += "<p><b>Оставте коментарий</b></p>"
            form += "<p><textarea name='comment' type='text'>" + list[id-1][3] + "</textarea></p>"

            form += "<input type='submit' name='submit' value='Refresh'>"
            form += "<input type='submit' name='submit' value='Censel'>"

            form += "</form>"
            return form
        if request.form['submit'] == 'Refresh':
            list[id - 1][0] = request.form['name']
            list[id - 1][1] = request.form['comp']
            list[id - 1][2] = request.form['tema']
            list[id - 1][3] = request.form['comment']
            zapis.writefile(list)
            return template_test()
        if request.form['submit'] == 'Censel':
            return template_test()
if __name__ == '__main__':
    app.run(debug=True)
