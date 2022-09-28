from django.shortcuts import render
from django.http import HttpResponse
from .models import GuessNumbers
from .forms import PostForm
from django.shortcuts import render, redirect

# Create your views here.
def index(request):
    lottos = GuessNumbers.objects.all() # DB에 저장된 GuessNumbers 객체 모두를 가져온다.
    # 브라우저로부터 넘어온 request를 그대로 template('default.html')에게 전달
    # {} 에는 추가로 함께 전달하려는 object들을 dict로 넣어줄 수 있음
    return render(request, 'lotto/default.html', {'lottos':lottos})

def post(request):

    if request.method == "POST":
        form = PostForm(request.POST)


        if form.is_valid():
            lotto = form.save(commit = False)
            lotto.generate()

            return redirect('index')
    else:
        form = PostForm() # empty form
        return render(request, "lotto/form.html", {"form": form})

def hello(request):

    # data = GuessNumbers.objects.all()
    # data = GuessNumbers.objects.get(id=1)

    return HttpResponse("<h1 style='color:red;'>Hello, World!</h1>")

def detail(request, lottokey):
    lotto = GuessNumbers.objects.get(pk = lottokey) # Primary Key
    return render(request, "lotto/detail.html", {"lotto":lotto})




























    # # index.html
    # # <input type='text' name='name'></input> <- 'win the prize!'
    # # <input type='text' name='text'></input>
    # # USER가 값을 입력하고, 전송 버튼을 클릭 -> USER가 입력한 값을 가지고 HTTP POST request
    # user_input_name = request.POST['name'] # HTML에서 name이 'name'인 input tag에 대해 USER가 입력한
    # user_input_text = request.POST['text'] # HTML에서 name이 'name'인 input tag에 대해 USER가 입력한 값
    # new_row = GuessNumbers(name=user_input_name, text=user_input_text, num_lotto=10)
    # print(new_row)
    # "pk 1: win the prize! - updated on 2025.09.12"
    # "pk {} : {} - {}".format(self.pk, self.name, self.text) # pk는 자동생성됨

    # print(new_row.num_lotto) # 5
    # print(new_row.name) # 'win the prize!'
    # new_row.name = new_row.name.upper() # 'WIN THE PRIZE!'
    # new_row.generate()
    # # new_row.lottos = ""
    # # origin = list(range(1,46)) # 1~45의 숫자 리스트 [1, 2, 3, ..., 43, 44, 45]
    # # # 6개 번호 set 갯수만큼 1~46 뒤섞은 후 앞의 6개 골라내어 sorting
    # # for _ in range(0, self.num_lotto):
    # #     random.shuffle(origin) # [10, 21, 36, 2, ... , 1, 11]
    # #     guess = origin[:6] # [10, 21, 36, 2, 15, 23]
    # #     guess.sort() # [2, 10, 15, 21, 23, 36]
    # #     self.lottos += str(guess) +'\n' # 로또 번호 str에 6개 번호 set 추가 -> '[2, 10, 15, 21, 23, 36]\n'
    # # # self.lottos : '[2, 10, 15, 21, 23, 36]\n[1, 15, 21, 27, 30, 41]\n...'
    # #
    # # self.update_date = timezone.now()
    # # self.save() # GuessNumbers object를 DB에 저장

    # new_row.lottos = [ np.randint(1, 50) for i in range(6) ]
    #
    # new_row.save()
