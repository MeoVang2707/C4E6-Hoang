from flask import *
from mongoengine import *
from os import *
from werkzeug.utils import secure_filename

APP_ROOT = path.dirname(path.abspath(__file__))
UPLOADS_IMAGE = path.join(APP_ROOT, "static/upload")

db_name = "hoang"
host = "ds053126.mlab.com"
port = 53126
user_name = "hoang"
password = "0986369617"

connect(db_name,
        host=host,
        port=port,
        username = user_name,
        password = password)

app = Flask(__name__)
app.config["SECRET_KEY"] = "ahihi. do's ngok's."
app.config["UPLOADS_IMAGE"] = UPLOADS_IMAGE
# @app.route('/index')
# def index():
#     return render_template("index.html")

# Game = [
#     {
#         "Title" : "Dota",
#         "Description": "Là một game khá hay và hot",
#         "Image" : "http://photoservice.gamesao.vn/Resources/Upload/Images/Game/4cf35d11-19cc-43da-a3db-e089c7b787c7.jpg",
#         "Next" : "http://127.0.0.1:5000/fav/1",
#         "link" : "http://playdota.vn/"
#     },
#     {
#         "Title": "LOL",
#         "Description": "Là một game khá hay và hot",
#         "Image": "http://thuonghieuvietnoitieng.vn/images/brand/2015/12/original/lol2.jpg",
#         "Next": "http://127.0.0.1:5000/fav/2",
#         "link" : "https://lienminh.garena.vn/"
#     },
#     {
#         "Title": "Aoe",
#         "Description": "Một game huyền thoại đến tận bây giờ vân chưa hết hot",
#         "Image": "http://i.down.vn/data/image/2014/11/18/aoe-648.jpg",
#         "Next": "http://127.0.0.1:5000/fav/3",
#         "link": "http://aoevietnam.vn/download-game-aoe-1-tai-game-aoe-i/"
#     },
#    ]
#
# Manga = [
#     {
#         "Title": "Dragon_ball",
#         "Description": "Là một bộ truyện tranh huyền thoại gắn với tuổi thơ của các thế hệ 8x,9x ",
#         "Image": "http://www.infographic24h.com/wp-content/uploads/2014/03/Dragon-Ball-SonGoku-Desktop-Wallpaper-full-HD-Infographic-BLOG-93.jpg",
#         "Next": "http://127.0.0.1:5000/fav/4",
#         "link": "https://vi.wikipedia.org/wiki/Dragon_Ball_-_7_vi%C3%AAn_ng%E1%BB%8Dc_r%E1%BB%93ng"
#     },
#     {
#         "Title": "Doremon",
#         "Description": "Là một bộ truyện tranh huyền thoại gắn với tuổi thơ của các thế hệ 9x, 10x",
#         "Image": "https://i.ytimg.com/vi/QVoJk8Hf3sk/maxresdefault.jpg",
#         "Next": "http://127.0.0.1:5000/fav/5",
#         "link": "https://vi.wikipedia.org/wiki/Doraemon"
#     },
#     {
#         "Title": "One Piece",
#         "Description": "là bộ truyện tranh được bình chọn là hot nhất hiện nay",
#         "Image": "http://www.pixelstalk.net/wp-content/uploads/2016/03/One-Piece-Wallpaper-HD-Free-Download-620x422.jpg",
#         "Next": "http://127.0.0.1:5000/fav/6",
#         "link": "https://vi.wikipedia.org/wiki/One_Piece"
#     }
# ]
#
# Novel = [
#     {
#         "Title": "Sherlock Holmes",
#         "Description": "Là một cuốn tiểu thuyết trinh thám rất hay và hot",
#         "Image": "http://audiotruyen.org/wp-content/uploads/2016/02/Sherlock-Holmes.jpg",
#         "Next": "http://127.0.0.1:5000/fav/7",
#         "link": "https://vi.wikipedia.org/wiki/Sherlock_Holmes"
#     },
#     {
#         "Title": "Harry Potter",
#         "Description": "Là một truyện rất hay va hot",
#         "Image": "http://www.daikynguyenvn.com/wp-content/uploads/2015/10/harry-potter324-675x400.jpg",
#         "Next": "http://127.0.0.1:5000/fav/8",
#         "link": "https://vi.wikipedia.org/wiki/Harry_Potter"
#     },
#     {
#         "Title": "The Lord of the Rings",
#         "Description": "Là một truyện rất hay va hot",
#         "Image": "http://lisaebetz.com/wp-content/uploads/2014/09/LOTR_book_covers.jpg",
#         "Next": "http://127.0.0.1:5000/fav/9",
#         "link": "https://vi.wikipedia.org/wiki/Ch%C3%BAa_t%E1%BB%83_nh%E1%BB%AFng_chi%E1%BA%BFc_nh%E1%BA%ABn"
#     },
# ]
# Film = [
#     {
#         "Title": "Terminator",
#         "Description": "Là loạt phim viễn tưởng rất hay",
#         "Image": "http://www.siwallpaperhd.com/wp-content/uploads/2015/09/terminator_genisys_wallpaper.jpg",
#         "Next": "http://127.0.0.1:5000/fav/10",
#         "link": "https://vi.wikipedia.org/wiki/K%E1%BA%BB_h%E1%BB%A7y_di%E1%BB%87t_(1984)"
#     },
#     {
#         "Title": "Fast and furious",
#         "Description": "Là loạt phim hành động rất hay va hot",
#         "Image": "http://cdn.pcwallart.com/images/fast-and-furious-7-poster-wallpaper-1.jpg",
#         "Next": "http://127.0.0.1:5000/fav/11",
#         "link": "https://en.wikipedia.org/wiki/The_Fast_and_the_Furious"
#     },
#     {
#         "Title": "Madagascar",
#         "Description": "Là loạt phim hoạt hình rất hay và hài hước",
#         "Image": "http://vignette4.wikia.nocookie.net/madagascarmerchandise/images/b/b6/Madagascarb3.jpg/revision/latest?cb=20101217230239",
#         "Next": "http://127.0.0.1:5000/fav/12",
#         "link": "http://phim3s.net/phim-le/cuoc-phieu-luu-toi-madagascar_936/"
#     },
# ]

# Food = [
#     {
#         "Title": "Phở",
#         "Description": "Là một món ăn rất nổi tiếng của Việt nam trên thế giới",
#         "Image": "http://phoharu.chiliweb.org/wp-content/uploads/2015/10/hinh-mon-pho-bo.jpg",
#         "Next": "http://127.0.0.1:5000/fav/13",
#         "link": "https://vi.wikipedia.org/wiki/Ph%E1%BB%9F"
#     },
#     {
#         "Title": "Bánh mì kẹp thịt",
#         "Description": "Là món ăn nhanh được rất nhiều người Việt Nam và trên thế giới khen ngon",
#         "Image": "http://cms.kienthuc.net.vn/zoom/1000/uploaded/huyenthu/2015_07_21/nhan%20banh%20mi/9-loai-banh-my-sai-gon-kep-nhan-la-ban-chay-quanh-nam-hinh-12.jpg",
#         "Next": "http://127.0.0.1:5000/fav/14",
#         "link": "https://vi.wikipedia.org/wiki/B%C3%A1nh_m%C3%AC_k%E1%BA%B9p_(Vi%E1%BB%87t_Nam)"
#     },
#     {
#         "Title": "Trà đá",
#         "Description": "Là đồ uống phổ biến của sinh viên Việt Nam",
#         "Image": "http://sohanews.sohacdn.com/thumb_w/600/2015/anh1-1-1432174217182-20-0-395-563-crop-1432174245847.jpg",
#         "Next": "http://127.0.0.1:5000/fav/15",
#         "link": "https://vi.wikipedia.org/wiki/Tr%C3%A0_%C4%91%C3%A1"
#     },
# ]
# Travel = [
#     {
#         "Title": "Nha Trang",
#         "Description": "Là nơi có bãi biển rất đẹp và sạch",
#         "Image": "https://upload.wikimedia.org/wikipedia/commons/c/c5/Nhatrang_la_plage.jpg",
#         "Next": "http://127.0.0.1:5000/fav/16",
#         "link": "https://vi.wikipedia.org/wiki/Nha_Trang"
#     },
#     {
#         "Title": "Sapa",
#         "Description": "Là nơi không khí và đồ ăn rất tuyệt vời",
#         "Image": "https://cdn3.ivivu.com/2014/10/du-lich-sa-pa-cam-nang-tu-a-den-z-iVIVU.com-20.jpg",
#         "Next": "http://127.0.0.1:5000/fav/17",
#         "link": "https://vi.wikipedia.org/wiki/Sa_Pa"
#     },
#     {
#         "Title": "Phan Xi Păng",
#         "Description": "Là nóc nhà của Đông Nam Á ",
#         "Image": "http://dulichbui.org/wp-content/uploads/2015/12/leo-nui-fansipan.jpg",
#         "Next": "http://127.0.0.1:5000/fav/18",
#         "link": "https://vi.wikipedia.org/wiki/Phan_Xi_P%C4%83ng"
#     },
# ]
#
# Sport = [
#     {
#         "Title": "Football",
#         "Description": "Là môn thể thao vua trên toàn thế giới",
#         "Image": "http://feelgrafix.com/data_images/out/15/890838-soccer.jpg",
#         "Next": "http://127.0.0.1:5000/fav/19",
#         "link": "https://vi.wikipedia.org/wiki/B%C3%B3ng_%C4%91%C3%A1"
#     },
#     {
#         "Title": "Swim",
#         "Description": "Là môn thể thao giúp hạ nhiệt cơ thể vào mùa hè",
#         "Image": "http://www.wn.com.vn/product_images/uploaded_images/gai-dep-bikini-32838-8-.jpg",
#         "Next": "http://127.0.0.1:5000/fav/20",
#         "link": "https://vi.wikipedia.org/wiki/B%C6%A1i"
#     },
#     {
#         "Title": "Golf",
#         "Description": "Là môn thể thao sang chảnh ở Việt Nam",
#         "Image": "http://www.dundrumhousehotel.com/upload/sequencer_images/stock-golf.jpg",
#         "Next": "http://127.0.0.1:5000/fav/21",
#         "link": "https://vi.wikipedia.org/wiki/Golf"
#     },
# ]

# class person:
#     def __init__(self, name, like, list):
#         self.name = name
#         self.like = like
#         self.list = list
#
# Thanh = person("Thành","Game",Game)
# Trong = person("Trọng","Manga", Manga)
# Manh = person("Mạnh","Novel", Novel)
# Nga = person("Nga","Film", Film)
# Hoang = person("Hoàng","Food", Food)
# Phanh = person("Phanh","Travel", Travel)
# Duc = person("Đức","Sport", Sport)
#
# person_list = [Thanh, Trong, Manh, Nga, Hoang, Phanh, Duc]
# like_list = Game + Manga + Novel + Film + Food + Travel + Sport

class Food:
    def __init__(self, Title, Description, Image, Link):
        self.Title = Title
        self.Description = Description
        self.Image = Image
        self.Link = Link

# Pho = Food("Phở", "Là một món ăn rất nổi tiếng của Việt nam trên thế giới",
#            "http://phoharu.chiliweb.org/wp-content/uploads/2015/10/hinh-mon-pho-bo.jpg",
#            "https://vi.wikipedia.org/wiki/Ph%E1%BB%9F")
#
# Banh_mi = Food("Bánh mì kẹp thịt", "Là món ăn nhanh được nhiều người thế giới khen ngon",
#                "http://cms.kienthuc.net.vn/zoom/1000/uploaded/huyenthu/2015_07_21/nhan%20banh%20mi/9-loai-banh-my-sai-gon-kep-nhan-la-ban-chay-quanh-nam-hinh-12.jpg",
#                "https://vi.wikipedia.org/wiki/Ph%E1%BB%9F")
#
# Tra_da = Food("Trà đá","Là đồ uống phổ biến của sinh viên Việt Nam",
#               "http://sohanews.sohacdn.com/thumb_w/600/2015/anh1-1-1432174217182-20-0-395-563-crop-1432174245847.jpg",
#               "https://vi.wikipedia.org/wiki/B%C3%A1nh_m%C3%AC_k%E1%BA%B9p_(Vi%E1%BB%87t_Nam)")
#
# Nem = Food("Nem chua rán", "Món ăn đường phố nổi tiếng ở Việt Nam, rất ngon và rẻ.",
#            "http://vnngon.com/wp-content/uploads/2016/01/pic4900.jpg",
#            "https://vi.wikipedia.org/wiki/Nem_chua_r%C3%A1n")
#
# Bun = Food("Bún bò Huế", "Món ăn đặc trưng ở Huế, ngon ngang ngửa phở.",
#            "http://mixtourist.com.vn/uploads/images/thang%207/15/bun-bo-hue.JPG",
#            "https://vi.wikipedia.org/wiki/B%C3%BAn_b%C3%B2_Hu%E1%BA%BF")

# Hu_tieu = Food("Hủ tiếu", "Đại diện cho khu vực miền Nam, ngon tuyệt vời",
#                "http://img.v3.news.zdn.vn/w660/Uploaded/Ohunoaa/2015_04_02/hutieumytho.jpg",
#                "https://vi.wikipedia.org/wiki/H%E1%BB%A7_ti%E1%BA%BFu")

# Food_list = [Pho, Banh_mi, Tra_da, Nem, Bun]

class Food(Document):
    Title = StringField()
    Description = StringField()
    Image = StringField()
    Link = StringField()

@app.route('/')
def Hoang():
    return render_template("logo.html")

@app.route('/fav')
def fav():
    if "loggedin" in session and session["loggedin"]:
        return render_template("fav.html", Food_list = Food.objects, ask = "http://127.0.0.1:5000/add_fav")
    else:
        return render_template("fav.html", Food_list=Food.objects, ask="http://127.0.0.1:5000/login")

@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")
    elif request.method == "POST":
        username = request.form["usrname"]
        password = request.form["psw"]
        if username == "Hoang" and password == "Hoang":
            session["loggedin"] = True
            return redirect(url_for("add_fav"))
        else:
            return redirect(url_for("login"))

@app.route('/add_fav', methods=["GET", "POST"])
def add_fav():
    if request.method == "GET":
        return render_template("add_fav.html")
    elif request.method == "POST":
        Title = request.form["Title"]
        Description = request.form["Description"]
        Link = request.form["Link"]
        Image = request.files["Image"]
        if Image is not None:
            filename = secure_filename(Image.filename)
            Image_link_real = path.join(app.config["UPLOADS_IMAGE"], filename)
            Image.save(Image_link_real)
            Image_link_fake = "../static/upload/" + filename
        food_add = Food(Title=Title, Description=Description,
                        Image=Image_link_fake, Link=Link)
        food_add.save()
        return redirect(url_for("fav"))

@app.route('/logout')
def logout():
    session["loggedin"] = False
    return redirect(url_for("login"))

@app.route('/video')
def video():
    return render_template("video.html")

if __name__ == '__main__':
    app.run()

