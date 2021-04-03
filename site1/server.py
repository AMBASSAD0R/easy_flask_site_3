import json

from flask import Flask, url_for, request, render_template

app = Flask(__name__)


@app.route('/')
def welcome_page():
    return 'Миссия Колонизация Марса'


@app.route('/index')
def index():
    return 'И на Марсе будут яблони цвести!'


@app.route('/promotion_image')
def promotion_image():
    return f"""<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/file.css')}" />
                    <title>Колонизация!</title>
                    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-BmbxuPwQa2lc/FVzBcNJ7UAyJxM6wuqIj61tLrc4wSX0szH/Ev+nYRRuWlolflfl" crossorigin="anonymous">
                  </head>
                  <body>
                    <h1>Жди нас, Марс!</h1>
                    <img src="{url_for('static', filename='img/MARS.jpg')}"
                        alt="здесь должна была быть картинка, но не нашлась">
                    <p>Вот она какая, красная планета.</p>
                    <div class="alert alert-primary" role="alert">
                      Человечество вырастает из детства.
                    </div>
                    <div class="alert alert-secondary" role="alert">
                      Человечеству мала одна планета.
                    </div>
                    <div class="alert alert-success" role="alert">
                      Мы сделаем обитаемыми безжизненные пока планеты.
                    </div>
                    <div class="alert alert-danger" role="alert">
                      И начнем с Марса!
                    </div>
                    <div class="alert alert-warning" role="alert">
                      Присоединяйся!
                    </div>
                    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta2/dist/js/bootstrap.bundle.min.js" integrity="sha384-b5kHyXgcpbZJO/tY9Ul7kGkf1S0CWuKcCD38l8YkeH8z8QjE0GmW1gYU5S9FOnJ0" crossorigin="anonymous"></script>
                  </body>
                </html>"""


@app.route('/astronaut_selection', methods=['POST', 'GET'])
def astronaut_selection():
    if request.method == 'GET':
        return f'''<!doctype html>
                        <html lang="en">
                          <head>
                            <meta charset="utf-8">
                            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                            <link rel="stylesheet"
                            href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                            integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                            crossorigin="anonymous">
                            <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/file.css')}" />
                            <title>Отбор астронавтов</title>
                          </head>
                          <body>
                            <center>Анкета претендента</center>
                            <center>для участия в миссии</center>
                            <div>
                                <form class="login_form" method="post">
                                    <input type="name" class="form-control" id="name" aria-describedby="emailHelp" placeholder="Введите ваше имя" name="name">
                                    <input type="password" class="form-control" id="password" placeholder="Введите пароль" name="password">
                                    <div class="form-group">
                                        <label for="classSelect">В каком вы классе</label>
                                        <select class="form-control" id="classSelect" name="class">
                                          <option>7</option>
                                          <option>8</option>
                                          <option>9</option>
                                          <option>10</option>
                                          <option>11</option>
                                        </select>
                                     </div>
                                    <div class="form-group">
                                        <label for="about">Немного о себе</label>
                                        <textarea class="form-control" id="about" rows="3" name="about"></textarea>
                                    </div>
                                    <div class="form-group">
                                        <label for="photo">Приложите фотографию</label>
                                        <input type="file" class="form-control-file" id="photo" name="file">
                                    </div>
                                    <div class="form-group">
                                        <label for="form-check">Укажите пол</label>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="sex" id="male" value="male" checked>
                                          <label class="form-check-label" for="male">
                                            Мужской
                                          </label>
                                        </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="sex" id="female" value="female">
                                          <label class="form-check-label" for="female">
                                            Женский
                                          </label>
                                        </div>
                                    </div>
                                    <div class="form-group form-check">
                                        <input type="checkbox" class="form-check-input" id="acceptRules" name="accept">
                                        <label class="form-check-label" for="acceptRules">Готов быть добровольцем</label>
                                    </div>
                                    <button type="submit" class="btn btn-primary">Записаться</button>
                                </form>
                            </div>
                            <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta2/dist/js/bootstrap.bundle.min.js" integrity="sha384-b5kHyXgcpbZJO/tY9Ul7kGkf1S0CWuKcCD38l8YkeH8z8QjE0GmW1gYU5S9FOnJ0" crossorigin="anonymous"></script>
                          </body>
                        </html>'''
    elif request.method == 'POST':
        print(request.form['email'])
        print(request.form['password'])
        print(request.form['class'])
        print(request.form['file'])
        print(request.form['about'])
        print(request.form['accept'])
        print(request.form['sex'])
        return "Форма отправлена"


@app.route('/carousel')
def mars_carousel():
    return f"""<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <title>Пейзажи Марса</title>
                    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta3/dist/js/bootstrap.bundle.min.js" integrity="sha384-JEW9xMcG8R+pH31jmWH6WWP0WintQrMb4s7ZOdauHnUtxwoG2vI5DkLtS3qm9Ekf" crossorigin="anonymous"></script>
                    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-eOJMYsd53ii+scO/bJGFsiCZc+5NDVN2yr8+0RDqr0Ql0h+rP48ckxlpbzKgwra6" crossorigin="anonymous">

                </head>
                  <body>
                    <h1>Пейзажи Марса</h1>
                    <div id="carouselExampleSlidesOnly" class="carousel slide" data-bs-ride="carousel">
                      <div class="carousel-inner">
                        <div class="carousel-item active">
                          <img src="{url_for('static', filename='img/mars_1.jpg')}" alt="...">
                        </div>
                        <div class="carousel-item">
                          <img src="{url_for('static', filename='img/mars_2.jpg')}" alt="...">
                        </div>
                        <div class="carousel-item">
                          <img src="{url_for('static', filename='img/mars_3.jpg')}" alt="...">
                        </div>
                      </div>
                    </div>
                  </body>
                </html>"""


@app.route('/choice/<name_planet>')
def choice(name_planet):
    if name_planet == 'Марс':
        return f"""<!doctype html>
                    <html lang="en">
                      <head>
                        <meta charset="utf-8">
                        <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/file.css')}" />
                        <title>Варианты выбора</title>
                        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-BmbxuPwQa2lc/FVzBcNJ7UAyJxM6wuqIj61tLrc4wSX0szH/Ev+nYRRuWlolflfl" crossorigin="anonymous">
                      </head>
                      <body>
                        <h1>Мое предложение: {name_planet}</h1>
                        <img src="{url_for('static', filename='img/MARS.jpg')}"
                            alt="здесь должна была быть картинка, но не нашлась">
                        <h2>Эта планета близка к Земле;</h2>
                        <div class="alert alert-primary" role="alert">
                          На ней много необходимых ресурсов;
                        </div>
                        <div class="alert alert-secondary" role="alert">
                          На ней есть вода и атмосфера;
                        </div>
                        <div class="alert alert-success" role="alert">
                          На ней есть небольшое магнитное поле;
                        </div>
                        <div class="alert alert-danger" role="alert">
                          Наконец, она просто красива!
                        </div>
                        <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta2/dist/js/bootstrap.bundle.min.js" integrity="sha384-b5kHyXgcpbZJO/tY9Ul7kGkf1S0CWuKcCD38l8YkeH8z8QjE0GmW1gYU5S9FOnJ0" crossorigin="anonymous"></script>
                      </body>
                    </html>"""
    elif name_planet == 'Юпитер':
        return f"""<!doctype html>
                            <html lang="en">
                              <head>
                                <meta charset="utf-8">
                                <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/file.css')}" />
                                <title>Варианты выбора</title>
                                <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-BmbxuPwQa2lc/FVzBcNJ7UAyJxM6wuqIj61tLrc4wSX0szH/Ev+nYRRuWlolflfl" crossorigin="anonymous">
                              </head>
                              <body>
                                <h1>Мое предложение: {name_planet}</h1>
                                <img src="{url_for('static', filename='img/JUPITER.jpeg')}"
                                    alt="здесь должна была быть картинка, но не нашлась">
                                <h2>Эта планета далека от Земли;</h2>
                                <div class="alert alert-primary" role="alert">
                                  Самая большая планета солнечной системы;
                                </div>
                                <div class="alert alert-secondary" role="alert">
                                  Планета является газовым гигантом;
                                </div>
                                <div class="alert alert-success" role="alert">
                                  Юпитер имеет магнитное поле в 50 раз сильнее Земного;
                                </div>
                                <div class="alert alert-danger" role="alert">
                                  А здесь могла бы быть ваша реклама :)!
                                </div>
                                <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta2/dist/js/bootstrap.bundle.min.js" integrity="sha384-b5kHyXgcpbZJO/tY9Ul7kGkf1S0CWuKcCD38l8YkeH8z8QjE0GmW1gYU5S9FOnJ0" crossorigin="anonymous"></script>
                              </body>
                            </html>"""


@app.route('/results/<nickname>/<int:level>/<float:rating>')
def results(nickname, level, rating):
    if rating > 50.0:
        return f"""<!doctype html>
                        <html lang="en">
                          <head>
                            <meta charset="utf-8">
                            <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/file.css')}" />
                            <title>Результаты</title>
                            <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-BmbxuPwQa2lc/FVzBcNJ7UAyJxM6wuqIj61tLrc4wSX0szH/Ev+nYRRuWlolflfl" crossorigin="anonymous">
                          </head>
                          <body>
                            <h1>Результаты отбора</h1>
                            <h2>Претендента на участие в миссии {nickname}:</h2>
                            <div class="alert alert-success" role="alert">
                              Поздравляем! Ваш рейтинг после {level} этапа отбора составляет {rating}
                            </div>
                            <div class="alert alert-warning role="alert"">
                                Желаем удачи
                            </div>
                            <img src="{url_for('static', filename='img/BELKA_STRELKA.jpg')}"
                                    alt="здесь должна была быть картинка, но не нашлась">
                            <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta2/dist/js/bootstrap.bundle.min.js" integrity="sha384-b5kHyXgcpbZJO/tY9Ul7kGkf1S0CWuKcCD38l8YkeH8z8QjE0GmW1gYU5S9FOnJ0" crossorigin="anonymous"></script>
                          </body>
                        </html>"""
    else:
        return f"""<!doctype html>
                                <html lang="en">
                                  <head>
                                    <meta charset="utf-8">
                                    <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/file.css')}" />
                                    <title>Результаты</title>
                                    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-BmbxuPwQa2lc/FVzBcNJ7UAyJxM6wuqIj61tLrc4wSX0szH/Ev+nYRRuWlolflfl" crossorigin="anonymous">
                                  </head>
                                  <body>
                                    <h1>Результаты отбора</h1>
                                    <h2>Претендента на участие в миссии {nickname}:</h2>
                                    <div class="alert alert-danger" role="alert">
                                      К сожалению ваш рейтинг после {level} этапа отбора составляет {rating}
                                    </div>
                                    <div class="alert alert-info" role="alert">
                                        Приходите в следующий раз!
                                    </div>
                                    <div class="alert alert-warning role="alert"">
                                        Желаем удачи!
                                    </div>
                                    <img src="{url_for('static', filename='img/BELKA_STRELKA.jpg')}"
                                    alt="здесь должна была быть картинка, но не нашлась">
                                    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta2/dist/js/bootstrap.bundle.min.js" integrity="sha384-b5kHyXgcpbZJO/tY9Ul7kGkf1S0CWuKcCD38l8YkeH8z8QjE0GmW1gYU5S9FOnJ0" crossorigin="anonymous"></script>
                                  </body>
                                </html>"""


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1', debug=True)
